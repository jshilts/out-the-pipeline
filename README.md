# out-the-pipeline
Retrospective analyses of Derek Lowe's 'in the pipeline' predictions and commentary using AI


#### Structure ####

requirements.txt  provides the required package versions for running this in Python >=3.10

The folder "weblinks"  provides code for finding all the 'in the pipeline' articles available, and the links to them as an output text file

The script "webpage-extractor.py"   then takes a link and extracts the article text. These are output in the webarticles folder (currently hidden from github via .gitignore)

The folder "prompts" contains the claims from the article which will be feed into the LLM for analysis

The script "llm-summary.py"  then uses the LLM to analyze the scientific claims in the article and its subsequent history. Any model can be used via the flexible interface at OpenRouter

The folder "responses" contains the LLM outputs of how each article was evaluated in historical hindsight

