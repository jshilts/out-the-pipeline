# -*- coding: utf-8 -*-
# > cd "C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline"
# >  .\.venv\Scripts\activate
# then set  Tools>Preferences>Python Intepreter  to  C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline\.venv\Scripts\python.exe
# restart the kernel (press = button on far right, or just restart spyer)


# to do - 
#   add some simple checks of the LLM's output (e.g. did it follow the structure, and other ideas for checks that come out of manually looking through some examples). If fails the check, then repeats up to 3 times. If a repeat passes, then saves that. If none do, take the last output and give it slightly different filename prefix so can filter out those malformed outputs

import os
import re
from openai import OpenAI   # pip install openai

#### user inputs ####
IF_WEB_SEARCH = False
SELECTED_PROMPT = "prompt-template-2.txt"


#### script ####
with open("openrouter-api-key.shh", "r") as f:
    API_KEY = f.read()

client = OpenAI(
  base_url = "https://openrouter.ai/api/v1",
  api_key = API_KEY,
)


global PROMPT_TEMPLATE # making explicit that is global variable
with open("./prompts/prompt-engineering/" + SELECTED_PROMPT) as f:
    PROMPT_TEMPLATE = f.read()
    

if not IF_WEB_SEARCH: # remove parts of prompt about internet searches
    PROMPT_TEMPLATE = re.sub(r'Use internet searches [^\n]*\n', '', PROMPT_TEMPLATE)
    PROMPT_TEMPLATE = re.sub(r'5\. CITATIONS.*?(?=---|\n\n|$)', '', PROMPT_TEMPLATE, flags=re.DOTALL)
#end

def generate_prompt(article_text: str, 
                    prompt_template = PROMPT_TEMPLATE):
    # produces the prompt for the LLM
    
    if len(article_text) < 10 :
        print("---article not found")  # revise this to give the URL of the missed article in the future
    #end
    
    if article_text[0:4].upper() == "HTTP" :
        article_text.split("\n", maxsplit = 1)[1]  # remove the first line
    #end
    
    lines = [
    prompt_template,
    article_text
    ]
    
    return "\n".join(lines)
#end

# def convert_article_date(article_timestamp: str):
#     # converts dates in the article to the YYYYMMMDD format (in the future can consider using library to do this more robustly)
#     return article_timestamp[7:11] + article_timestamp[3:6] + article_timestamp[0:2]
# #end

model_parameters = {
    "model" :"nex-agi/deepseek-v3.1-nex-n1:free",#"deepseek/deepseek-v3.2",#"arcee-ai/trinity-mini:free",
    "input" : "",
    "reasoning" : {"effort": "high"},
    "text": {"verbosity": "medium"}
    }
if IF_WEB_SEARCH:
    model_parameters["tools"] = [ {
        "type": "web_search",  # warning - this will make 'free' tier models no longer free
        "max_results": 20,
        "include_text": True,
        "include_highlights": True
        } ]
    model_parameters["tool_choice"] = "required"  # cannot attempt to answer without doing some web searching
#end    


article_list = os.listdir("./prompts/")  # by default analyzes everything. If want a subset, put the others not to be processed into the 'storage' folder (since not recursive file finding here)
article_list = [filename for filename in article_list if isinstance(filename, str) and filename.endswith(".txt")]

for i, article_source in enumerate(article_list):
    #article_source = "Valeant-Bound-to-be-a-Good-Explanation-Right.txt"

    with open("./prompts/%s"%article_source, "r", encoding="utf-8", errors="replace") as f_in:
        article_fulltext = f_in.read()
    article_fulltext = article_fulltext.replace("\\'", "'")  # replace escape characters found in apostraphes so tokenizer doesn't see weird things like "I\'m not sure they\'re going"

    query_prompt = generate_prompt(article_fulltext)
    
    model_parameters["input"] = query_prompt
    
    
    response = client.responses.create( 
        **model_parameters)
    
    response_text = response.output_text
    #print(response_text)
    
    simplified_output_name = "out_" + article_source.split(".")[0][:30] + "_" + model_parameters["model"].split("/")[1][:15]   # convert_article_date(article_fulltext.split('\n')[1]) + 
    
    original_url = article_source.split("-", 1)[1]
    original_url = "https://www.science.org/content/blog-post/" + original_url[:-4] if original_url.endswith(".txt") else original_url

    with open("./responses/" + simplified_output_name + ".md", "w", encoding="utf-8") as f:
        params_to_write = dict(model_parameters)
        params_to_write["input"] = article_source
        params_to_write["prompt-template"] = SELECTED_PROMPT.split(".")[0]
        f.write("\n") # start with light gap
        f.write(original_url)
        f.write("\n")
        f.write(response_text)
        f.write("\n\n\n----\n")
        f.write("_model_params = ")
        f.write(repr(params_to_write))
        f.write("_") # end the italic markdown
    #end
    
    print(f"{i+1} out of {len(article_list)} complete ({100.0 * (i+1) / len(article_list):.2f}%) ")
#end


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