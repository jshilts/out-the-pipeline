
https://www.science.org/content/blog-post/modeling-rats-who-model-humans
# Modeling the Rats, Who Model the Humans (August 2015)

## 1. SUMMARY

The article discusses the fundamental challenge in drug discovery that there is often no alternative to expensive, time-consuming in vivo (animal) and clinical (human) studies to determine a drug's efficacy, toxicity, and ADME (absorption, distribution, metabolism, excretion) properties. While in vitro assays and computational models have been attempted, the author notes that none are reliable enough to base real drug discovery decisions on, and project leaders still require animal data before drawing actionable conclusions.

The piece highlights a new paper presenting a computational approach using graph-based signatures to predict ADME and toxicity properties, accessible via a web server. While the authors claim improved performance over existing methods—particularly for rat toxicity, P-glycoprotein inhibition, and CYP enzyme inhibition—the article expresses cautious skepticism, noting that industry researchers would be hesitant to upload proprietary structures to public servers. The author identifies rat toxicity prediction as potentially the most valuable application, as many other ADME parameters can already be assessed through high-throughput assays.

## 2. HISTORY

The period following this 2015 article has seen significant evolution in computational ADME/tox prediction, though many of the fundamental challenges remain.

**Industry Adoption and Limitations**: While computational ADME/tox models have become more sophisticated and widely used in drug discovery pipelines, they have not replaced animal studies as the article hoped might eventually happen. Regulatory requirements still mandate extensive preclinical animal testing before human trials, and computational predictions remain supplementary tools rather than primary decision-making criteria. Pharmaceutical companies now routinely use in silico models for early-stage compound prioritization and risk assessment, but these predictions are always validated with experimental data.

**The PKCSM Tool and Similar Platforms**: The PKCSM web server mentioned in the article is part of a broader ecosystem of computational ADME/tox prediction tools that have continued developing. Similar platforms like SwissADME, admetSAR, and commercial solutions (Schrödinger's QikProp, Simulations Plus' ADMET Predictor) have gained wider acceptance in the pharmaceutical industry. These tools are primarily used for virtual screening and early-stage compound triaging rather than replacing regulatory-required studies.

**Regulatory Landscape**: FDA and EMA have shown increased openness to computational approaches through initiatives like model-informed drug development (MIDD), and there have been discussions about potentially reducing animal testing requirements in certain contexts. However, established regulatory pathways still heavily rely on animal data. Notably, the FDA Modernization Act 2.0 (passed in 2022) removed the mandatory requirement for animal testing before human trials, opening regulatory pathways for alternative approaches, though implementation details and industry adoption patterns are still developing.

**Scientific Advances**: Graph-based deep learning methods, building on the concepts mentioned in the 2015 paper, have shown improved performance for molecular property prediction. However, the fundamental limitation remains: these models are trained on existing data and struggle with compounds that have novel structural features or mechanisms outside the training set distribution.

**Successes and Failures**: While computational models have helped identify problematic compounds earlier in drug discovery, saving some development costs, there have been no dramatic breakthroughs that eliminated the need for animal studies. High-profile drug failures continue to occur due to unforeseen toxicity issues that computational models didn't predict, validating the article's cautious stance.

## 3. PREDICTIONS

The article made several explicit and implicit predictions about the future of computational ADME/tox modeling:

• **"Doesn't happen - no one is going to draw any actionable conclusions until the animal numbers are in"** - This largely remains true. While computational predictions are used for compound prioritization, regulatory submissions and major development decisions still require experimental animal data. Clinical development decisions remain heavily dependent on actual preclinical results.

• **Industry reluctance to use public web servers for proprietary structures** - This prediction proved accurate. Pharmaceutical companies have generally avoided uploading novel structures to public prediction servers, preferring internal computational tools, commercial licensed software, or custom-built models that maintain intellectual property protection.

• **"We'll see how this one performs!" regarding the rat toxicity prediction capability** - Computational rat toxicity prediction has improved but remains imperfect. The field has seen gradual improvements in prediction accuracy, particularly for known toxicophores, but novel mechanisms of toxicity still pose challenges. No computational model has achieved the reliability needed to replace animal testing for regulatory toxicology studies.

• **Implicit prediction that reliable whole-animal tox models could be valuable** - This has proven true in terms of industry interest and research investment, but success has been limited. While there's been progress in specific areas (e.g., hERG cardiotoxicity prediction has become moderately reliable), comprehensive whole-animal toxicity prediction remains elusive.

• **Implicit prediction about reliability of existing computational methods** - The article's skepticism about existing computational methods was warranted. While there have been improvements, pipeline's fundamental limitations remain: models trained on existing data may not generalize to novel chemical space, and the complexity of biological systems makes perfect prediction challenging.

## 4. INTEREST

Rating: **7/10**

The article demonstrates good scientific foresight by identifying the key challenges that would persist in the field. Its cautious assessment of computational methods' limitations proved prescient, and the piece highlights fundamental issues in drug development that remain relevant nearly a decade later.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20150812-modeling-rats-who-model-humans.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_