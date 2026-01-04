# out-the-pipeline
Retrospective analyses of Derek Lowe's "In the Pipeline" predictions and commentary using AI

  
#### Summary ####
  
For the past quarter-century, Derk Lowe has been publishing a daily column in the journal _Science_ describing events in the  history of biopharma and perspectives on drug discovery.  (https://www.science.org/blogs/pipeline)

These articles give us a unique kind of 'time capsule' to read and look back on, to see what scientific discoveries may have gotten attention but ended up being more hype than revolutionary, and how predictions about new medicines compare to what we now know later happened. 

This project produces a free website to explore that history. When you open it, it defaults to showing what was written this day 10 years ago. With the help of a large language model (LLM), it summarizes what was said back then, and compares the predictions in the article to what subsequently took place. Please note that LLMs are not perfect, and so factual mistakes will sometimes occur (mostly on articles about niche topics, where the model could not find the relevant facts and so may have invented its own)

You can browse any othe year available for the articles written. As a guide, there is color-coded score from 0 to 10 to highlight more interesting articles with higher scores. If there is enough interest on this version of the site, I will keep adding more years of reviews and run this on more powerful LLMs to get better quality analyses!

https://jshilts.github.io/out-the-pipeline/
  
  
#### Structure ####

requirements.txt  provides the required package versions for running this in Python >=3.10

The folder "weblinks"  provides code for finding all the 'in the pipeline' articles available, and the links to them as an output text file

The script "webpage-extractor.py"   then takes a link and extracts the article text. These are output in the webarticles folder (currently hidden from github via .gitignore)

The folder "prompts" contains the claims from the article which will be feed into the LLM for analysis. In that folder is also 'prompt-cleaning.py' as a short script to fix the formatting of a few of the web files.

The script "llm-summary.py"  then uses the LLM to analyze the scientific claims in the article and its subsequent history. Any model can be used via the flexible interface at OpenRouter

The folder "responses" contains the LLM outputs of how each article was evaluated in historical hindsight.

The script "index-json-maker.py" then prepares all those outputs so they can be interactively viewed on the public site (https://jshilts.github.io/out-the-pipeline/)


#### Usage ####

All the outputs are available at the site https://jshilts.github.io/out-the-pipeline/

If you'd like to play around with the LLM, you can customize your files in the 'prompts' folder and re-rerun the "llm-summary.py" script.

On the site there are links to all the original articles for you to read if you want to learn more. You can subscribe to the "In the Pipeline" blog for future articles at https://www.science.org/blogs/pipeline
