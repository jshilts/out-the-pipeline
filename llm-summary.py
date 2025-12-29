# -*- coding: utf-8 -*-
# > cd "C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline"
# >  .\.venv\Scripts\activate
# then set  Tools>Preferences>Python Intepreter  to  C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline\.venv\Scripts\python.exe
# restart the kernel (press = button on far right, or just restart spyer)


# to do - 
#   add some simple checks of the LLM's output (e.g. did it follow the structure, and other ideas for checks that come out of manually looking through some examples). If fails the check, then repeats up to 3 times. If a repeat passes, then saves that. If none do, take the last output and give it slightly different filename prefix so can filter out those malformed outputs
#    also eventually re-run all the articles since first-pass run with Nov+Dec of 2010 - 2015 had some periodic bugs


import os
import re
from copy import deepcopy
from openai import OpenAI   # pip install openai
import concurrent.futures
import traceback

#### user inputs ####
IF_WEB_SEARCH = False
SELECTED_PROMPT = "prompt-template-2.txt"
MAX_WORKERS = 8  # adjust this to control concurrency

#### script ####
with open("openrouter-api-key.shh", "r") as f:
    API_KEY = f.read().strip()

BASE_URL = "https://openrouter.ai/api/v1"

# load prompt template
with open("./prompts/prompt-engineering/" + SELECTED_PROMPT, "r", encoding="utf-8", errors="replace") as f:
    PROMPT_TEMPLATE = f.read()

if not IF_WEB_SEARCH:
    PROMPT_TEMPLATE = re.sub(r'Use internet searches [^\n]*\n', '', PROMPT_TEMPLATE)
    PROMPT_TEMPLATE = re.sub(r'5\. CITATIONS.*?(?=---|\n\n|$)', '', PROMPT_TEMPLATE, flags=re.DOTALL)


def generate_prompt(article_text: str, prompt_template=PROMPT_TEMPLATE):
    if len(article_text) < 10:
        print("---article not found")
    if article_text[0:4].upper() == "HTTP":
        article_text = article_text.split("\n", maxsplit=1)[1] if "\n" in article_text else ""
    return "\n".join([prompt_template, article_text])


model_parameters = {
    "model": "nex-agi/deepseek-v3.1-nex-n1:free",
    "input": "",
    "reasoning": {"effort": "high"},
    "text": {"verbosity": "medium"}
}
if IF_WEB_SEARCH:
    model_parameters["tools"] = [{
        "type": "web_search",
        "max_results": 20,
        "include_text": True,
        "include_highlights": True
    }]
    model_parameters["tool_choice"] = "required"


article_list = os.listdir("./prompts/")
article_list = [filename for filename in article_list if isinstance(filename, str) and filename.endswith(".txt")]

# prepare tasks (read files first to minimise I/O contention during concurrent requests)
tasks = []
for article_source in article_list:
    with open("./prompts/%s" % article_source, "r", encoding="utf-8", errors="replace") as f_in:
        article_fulltext = f_in.read()
    article_fulltext = article_fulltext.replace("\\'", "'")
    query_prompt = generate_prompt(article_fulltext)
    tasks.append((article_source, article_fulltext, query_prompt))

def worker_task(task_tuple):
    """
    Each worker:
      - creates its own OpenAI client (avoids client thread-safety issues)
      - deepcopies model params and sets input
      - calls responses.create
      - returns (article_source, response_text) or raises
    """
    article_source, article_fulltext, query_prompt = task_tuple
    try:
        # create a fresh client per worker
        local_client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

        params = deepcopy(model_parameters)
        params["input"] = query_prompt

        response = local_client.responses.create(**params)
        response_text = getattr(response, "output_text", None)
        if response_text is None:
            # fallback if output_text not present
            # try to reconstruct if the SDK returns structured output
            try:
                response_text = "\n".join([m.get("content", "") for m in response.output or []])
            except Exception:
                response_text = str(response)

        simplified_output_name = "out_" + article_source.split(".")[0][:30] + "_" + params["model"].split("/")[1][:15]
        original_url = article_source.split("-", 1)[1] if "-" in article_source else article_source
        original_url = ("https://www.science.org/content/blog-post/" + original_url[:-4]) if original_url.endswith(".txt") else original_url

        # write result file
        out_path = os.path.join("./responses", simplified_output_name + ".md")
        os.makedirs("./responses", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            params_to_write = dict(params)
            params_to_write["input"] = article_source
            params_to_write["prompt-template"] = SELECTED_PROMPT.split(".")[0]
            f.write("\n")
            f.write(original_url + "\n")
            f.write(response_text + "\n\n\n----\n")
            f.write("_model_params = ")
            f.write(repr(params_to_write))
            f.write("_")  # end of the italic markdown for the params
        return (article_source, None)  # None indicates success, we already wrote file
    except Exception as e:
        tb = traceback.format_exc()
        # write an error file for later inspection
        err_name = "err_" + article_source.split(".")[0][:30]
        err_path = os.path.join("./responses", err_name + ".err.txt")
        with open(err_path, "w", encoding="utf-8") as ef:
            ef.write("Error processing: %s\n\n" % article_source)
            ef.write(str(e) + "\n\n")
            ef.write(tb)
        return (article_source, e)

# run concurrently
total = len(tasks)
completed = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    future_to_task = {executor.submit(worker_task, t): t for t in tasks}
    for fut in concurrent.futures.as_completed(future_to_task):
        article_source, error = fut.result()
        completed += 1
        if error is None:
            print(f"{completed} out of {total} complete ({100.0 * completed / total:.2f}%) - {article_source} succeeded")
        else:
            print(f"{completed} out of {total} complete ({100.0 * completed / total:.2f}%) - {article_source} failed: {error}")

print("All done.")

#### pipeline could be quick calls via a free model to gauge which articles of interest to analyze (outputing just a few tokens of the interest score) then thinking LLM analyzes those texts in the second pass



'''  how to figure out what parameters each model supports :
import requests
url = "https://openrouter.ai/api/v1/parameters/arcee-ai/trinity-mini%3Afree"
headers = {"Authorization": "Bearer %s"%API_KEY}
response = requests.get(url, headers=headers)
print(response.json())
'''


''' notes

arcee-ai/trinity-mini:free
    - very fast, within a few seconds even if include web search
    - lots of hallucinations even though web search tool helps a bit
    - costs around $0.02 per prompt
    
deepseq 3.2
    - takes around 20 seconds with web search and high reasoning effort
    - good quality outputs. Not as nice as ChatGPT thinking model, partly because was more terse (e.g. didn't mention the CEO change that came alongside the shift toward more R&D). Citations are real though not diverse
    - costs around 0.025 per prompt
    
deepseq 3.1 free
    - also slower of around 20 seconds even without web search
    - surprisingly gave almost just as good output as deepseq 3.2 despite all citations being hallucinations and having no website access. However this may be partly luck since started 'yes merger happend but'... then corrected itself
    - costs 0 though risky that makes plausible-sounding text that may not be real    

'''