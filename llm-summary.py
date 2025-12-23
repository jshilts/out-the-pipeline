# -*- coding: utf-8 -*-
# > cd "C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline"
# >  .\.venv\Scripts\activate
# then set  Tools>Preferences>Python Intepreter  to  C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline\.venv\Scripts\python.exe
# restart the kernel (press = button on far right, or just restart spyer)

from openai import OpenAI   # pip install openai

with open("openrouter-api-key.shh", "r") as f:
    API_KEY = f.read()

client = OpenAI(
  base_url = "https://openrouter.ai/api/v1",
  api_key = API_KEY,
)


global PROMPT_TEMPLATE # making explicit that is global variable
PROMPT_TEMPLATE = """The following is an article that appeared in Science Magazine many years ago about the biotechnology industry.

Let's use our benefit of hindsight to analyze the article's claims and how they fared up to the present day. Please be thorughtful and deeply critcial, questioning hype and investigating the true real-world impact a technology had. 
Use internet searches to follow the facts precisely and include a citation reference after every fact you mention. When looking up sources, look up articles from different time periods and avoid looking up too many similar articles.
Write a response following these sections :
    
1. SUMMARY
Give a short summary of 1-2 paragraphs for what the article said.

2. HISTORY
Research what happened subsequent to the article being published and summarize those later developments.

3. PREDICTIONS
Describe what predictions of the article matched the later history, and which predictions were wrong.

4. INTEREST 
Give a score from 0 to 9 on how interesting the article is in hindsight, and the insightfulness of its retrospective analysis. Do not simply give all articles a medium score, please be thoughtful about long-term impact.

5. CITATIONS
Here cite the URLs of the websites you used as sources of information. Remember to search across multiple timeframes, not just one time period

--- The article ---

"""

article_source = "Valeant-Bound-to-be-a-Good-Explanation-Right.txt"

with open("./prompts/%s"%article_source, "r") as f_in:
    article_fulltext = f_in.read()


def generate_prompt(article_text: str, 
                    prompt_template = PROMPT_TEMPLATE):
    if len(article_text) < 100 :
        print("---article not found")  # revise this to give the URL of the missed article in the future
    #end
    
    lines = [
    prompt_template,
    article_text
    ]
    
    return "\n".join(lines)
#end
    
query_prompt = generate_prompt(article_fulltext)

model_parameters = {
    "model" :"nex-agi/deepseek-v3.1-nex-n1:free",#"deepseek/deepseek-v3.2",#"arcee-ai/trinity-mini:free",
    "input" : query_prompt,
    # "tools" : [ {
    #     "type": "web_search",  # warning - this will make 'free' tier models no longer free
    #     "max_results": 20,
    #     "include_text": True,
    #     "include_highlights": True
    #     } ],
    "tool_choice" : "required",  # cannot attempt to answer without doing some web searching
    "reasoning" : {"effort": "high"},
    "text": {"verbosity": "medium"}
    }

response = client.responses.create( 
    **model_parameters)

response_text = response.output_text



with open("./responses/output-test.md", "w", encoding="utf-8") as f:
    params_to_write = dict(model_parameters)
    params_to_write["input"] = article_source
    f.write("model_params = ")
    f.write(repr(params_to_write))
    f.write("\n\n") # two newlines separating
    f.write(response_text)
#end


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