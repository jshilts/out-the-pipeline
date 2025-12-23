# -*- coding: utf-8 -*-
# > cd "C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline"
# >  .\.venv\Scripts\activate
# then set  Tools>Preferences>Python Intepreter  to  C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline\.venv\Scripts\python.exe
# restart the kernel (press = button on far right, or just restart spyer)

from openai import OpenAI

with open("openrouter-api-key.shh", "r") as f:
    API_KEY = f.read()

client = OpenAI(
  base_url = "https://openrouter.ai/api/v1",
  api_key = API_KEY,
)


global PROMPT_TEMPLATE # making explicit that is global variable
PROMPT_TEMPLATE = """The following is an article that appeared in Science Magazine many years ago about the biotechnology industry.

Let's use our benefit of hindsight to analyze the article's claims and how they fared up to the present day. Please be thorughtful and deeply critcial, questioning hype and investigating the true real-world impact a technology had.
Write a response following these sections :
    
1. SUMMARY
Give a short summary of 1-2 paragraphs for what the article said.

2. HISTORY
Research what happened subsequent to the article being published and summarize those later developments.

3. PREDICTIONS
Describe what predictions of the article matched the later history, and which predictions were wrong.

4. INTEREST 
Give a score from 0 to 9 on how interesting the article is in hindsight, and the insightfulness of its retrospective analysis.


--- The article ---

"""

article_fulltext = """
Pfizer and Allergan: Here We Go Again
29 Oct 201511:50 AM ET

Last night the Wall Street Journal broke the news that Pfizer and Allergan are considering merging. I'm not a fan of huge pharma mergers, never have been, but this one at least isn't as offensive as some of them. That's partly because, in the words of FierceBiotech's John Carroll (on Twitter) that Allergan at least doesn't have as huge an R&D effort for Pfizer to demolish. And since Allergan is incorporated in Ireland, this is a way for Pfizer to do what it really seems to need to do most - deal with its tax situation, which was the driving force behind their attempt to take over AstraZeneca. Pfizer has gigantic amounts of money piling up in its non-US-based operations, and if they repatriate it, they'll expose themselves to some of the highest corporate tax rates in the industrialized world. (As an aside, does Bernie Sanders want to cut corporate taxes all the way down to Scandanavian levels? Just a thought.)
As the story has it (here's a non-gated summary from Reuters), Pfizer approached Allergan with the idea, who's apparently taking it seriously and not fleeing in terror like AZ did. Earlier rumors has Pfizer going after GSK or Shire (for the same tax reasons), and their shares are actually dropping a bit now that their investors are perhaps missing out on a big Pfizer payday. Allergan's revenues are at least increasing strongly, which is a lot more than you can say for Pfizer's, but this deal would create the biggest behemoth yet in the drug business. And as someone in that Reuters piece says, when you're as big as Pfizer, a deal like this is one of the only things that can really add to the growth of your company - so what situation would they be in afterwards? This whole idea just continues the Pfizer strategy of the last twenty-odd years. It means, I think, that Ian Read may have come into his job as CEO talking about doing things differently, but that now that he's experienced Pfizer's situation from every angle, he's decided that all he can do is more of what got them to this state in the first place. Won't his eventual successor have fun, though!
At any rate, these talks are said to be preliminary. But Pfizer is going to buy someone, and it's going to be someone large and in another country. That much seems clear (as it has been for a while now). It might well be Allergan, but if not, then hey, there are always other drug companies to buy. Gotta buy someone. Can't just sit there. Nothing else left to do.
"""


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

response = client.responses.create( #client.chat.completions.create(
  model = "arcee-ai/trinity-mini:free",
  #messages=[
  #  {
  #    "role": "user",
  #    "content": "What is the meaning of life?"
  #  }]
  input = query_prompt,
  reasoning = {"effort" : "medium"},
  text = {"verbosity": "medium"}
)
response_text = response.output_text
    
print(response_text)
