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



#### define model to use ####
model_parameters = {
    "model": "deepseek/deepseek-r1-0528:free", # "openai/gpt-oss-120b:free",  # "nex-agi/deepseek-v3.1-nex-n1:free", 
    "input": "",
    "reasoning": {"effort": "high"},
    "text": {"verbosity": "medium"}
}
# warning - if use openai model, then on https://openrouter.ai/settings/privacy must permit "enable endpoints that may publish prompts"

if IF_WEB_SEARCH:
    model_parameters["tools"] = [{
        "type": "web_search",
        "max_results": 20,
        "include_text": True,
        "include_highlights": True
    }]
    model_parameters["tool_choice"] = "required"


#### load prompt template ####
with open("./prompts/prompt-engineering/" + SELECTED_PROMPT, "r", encoding="utf-8", errors="replace") as f:
    PROMPT_TEMPLATE = f.read()

if not IF_WEB_SEARCH:
    PROMPT_TEMPLATE = re.sub(r'Use internet searches [^\n]*\n', 
                             'Since you do not have internet access, be careful to avoid hallucination. It would be unlikely you would have memorized exact details about niche topics\n', PROMPT_TEMPLATE)
    PROMPT_TEMPLATE = re.sub(r'5\. CITATIONS.*?(?=---|\n\n|$)', '', PROMPT_TEMPLATE, flags=re.DOTALL)

if model_parameters["model"] == "openai/gpt-oss-120b:free":   # model-specific pathology where uses some absurd tables even when nonsensical
    PROMPT_TEMPLATE = re.sub(r"Markdown format ",
                             "Markdown format (without using any tables) ", PROMPT_TEMPLATE)

def generate_prompt(article_text: str, prompt_template=PROMPT_TEMPLATE):
    if len(article_text) < 10:
        print("---article not found")
    if article_text[0:4].upper() == "HTTP":
        article_text = article_text.split("\n", maxsplit=1)[1] if "\n" in article_text else ""
    return "\n".join([prompt_template, article_text])




#### script ####

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
            print('--not finding response text')
            # fallback if output_text not present
            # try to reconstruct if the SDK returns structured output
            try:
                response_text = "\n".join([m.get("content", "") for m in response.output or []])
            except Exception:
                response_text = str(response)
    
        response_text = re.sub("/n• ", "/n- " response_text)  # fix common bug in markdown files (may be should make whole script for cleaning post-generation)

        simplified_output_name = "out_" + article_source.split(".")[0][:30] + "_" + params["model"].split("/")[1][:15] + f"{'-web' if IF_WEB_SEARCH else ''}"
        simplified_output_name = re.sub(r'[^A-Za-z0-9._-]', '', simplified_output_name)  # must sanitize name otherwise will get no output if contains something like a colon
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
    
deepseek 3.2
    - takes around 20 seconds with web search and high reasoning effort
    - good quality outputs. Not as nice as ChatGPT thinking model, partly because was more terse (e.g. didn't mention the CEO change that came alongside the shift toward more R&D). Citations are real though not diverse
    - costs around 0.025 per prompt

deepseek R1
    - not able to do web searches, but tried it since thought it may be better for free offline articles than next ai's deepseek 3.1 variant below
    - outputs were more terse and not really better quality. Made same errors as other models on the 'nativis' and 'vanderbilt' benchmarks
    - least favorite model so far. Mediocre accuracy, mediocre analysis. Not terrible on either, but alternatives are better in all dimensions
    
next ai deepseek 3.1 free
    - also slower of around 20 seconds even without web search
    - unliked 'deepseq R1', this one is able to use web search tools. However, lacks the 'reasoning' parameter
    - surprisingly gave almost just as good output as deepseq 3.2 despite all citations being hallucinations and having no website access. However this may be partly luck since started 'yes merger happend but'... then corrected itself
    - costs 0 though risky that makes plausible-sounding text that may not be real    
    - when added web access, surprisingly did not do any better on the 'vanderbilt-heads' or 'nativis-lives' challenging benchmark examples. Still missed Nativis rename, and the Vanderbilt article just became bland and had almost non meaningful content anymore

openai/gpt-oss-120b:free
    - compared to deepseq 3.1, gives fewer hallucinations. Deepseq 3.1 rate is not terrible, but it will overconfidently make up extremely price details that aren't true when given a very niche subject (e.g. about Vanderbilt's VU319 fairly obscure drug). Thought deepseq does very well on anything at least semi-famous (i.e. company mergers, mainstream pharma's drug pipelines)
    - over-uses tables to a damaging degree. Even when remake prompt to get this model to stop, it still will use tables very frequently even when makes text very hard to read and follow
    - compared to deepseq 3.1, gives somewhat less interesting responses. Look into more examples, but so far on ones like Vanderbilt article, the openAI model just commented narrowly about their specific drug, while Deepseek also addressed the broader question of others who tried the same drug target. 
    - both deepseq and gpt-oss miss some important details, like neither finding Nativis renamed (which admitedly is a niche fact, so at least neither hallucinated there)

'''