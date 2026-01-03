
https://www.science.org/content/blog-post/machine-learning-be-careful-what-you-ask
# Machine Learning: Be Careful What You Ask For (November 2018)

## 1. SUMMARY

This commentary analyzes a scientific controversy surrounding a 2018 *Science* paper from the Doyle group (Princeton/Merck) that used machine learning to predict success rates of Buchwald-Hartwig coupling reactions, particularly in the presence of isoxazoles that can poison catalytic cycles. The original work appeared promising but was challenged by Chuang and Keiser from UCSF, who argued that the ML algorithms may have exploited patterns in the experimental design rather than meaningful chemical features.

The UCSF response demonstrated that when chemical descriptors were replaced with random numbers, the ML model performed nearly as well as the original—suggesting the algorithm was learning from underlying data structure rather than actual chemistry. Additionally, cross-validation results showed concerning variability (RMSE ranging from 7.8% to 22%), and even with shuffled yield data, the model still "found" isoxazole additives to be the most important features. The Doyle group's response acknowledged insufficient out-of-sample validation but maintained their chemical descriptors contained meaningful information, though the commentary author found this response somewhat missed the core critique about embedded dataset structure being confounded with chemical reality.

## 2. HISTORY

In the years following this 2018 exchange, several important developments occurred:

**Reaction prediction and ML in chemistry became validated and widely adopted.** The challenges raised about proper controls and validation spurred the field to develop more rigorous standards. ML-based reaction prediction moved from experimental curiosity to practical tools. Companies like Merck (continued partner in the original work) and others invested heavily in AI-driven synthesis planning, with platforms like IBM's RXN for Chemistry, DeepMatter's DigitalGlassware, and various startups applying ML to chemical synthesis at scale.

**Buchwald-Hartwig coupling itself saw continued development** with improved catalyst systems and broader substrate scope, becoming a workhorse C-N bond forming reaction in pharmaceutical manufacturing. The reaction's notorious capriciousness that motivated the original ML work remained a practical challenge, driving continued innovation in both computational and experimental approaches.

**Adversarial controls and proper ML validation** became standard practice in chemical ML publications. The UCSF group's critique contributed to raising awareness about validation requirements, influencing how chemometrics and cheminformatics research was conducted and reviewed.

**FDA approval and clinical impact**: The specific application to isoxazole-containing compounds did not immediately translate into FDA-approved drugs specifically tied to this ML work, though isoxazoles continued appearing in drug candidates and approved therapeutics (e.g., various COX-2 inhibitors, antibiotics). The broader impact was methodological—improving how ML is applied to reaction optimization in drug discovery pipelines rather than direct therapeutic breakthroughs.

## 3. PREDICTIONS

The article did not make explicit timeline-based predictions, but implicitly raised several questions about ML's role:

• **"Machine learning is not going away. Nor should it"** ✓ **CORRECT**. ML became increasingly integrated into chemical research, with major pharmaceutical companies establishing AI/ML divisions and routinely using computational approaches for reaction prediction, retrosynthesis, and optimization.

• **The need for adversarial tests and rigorous validation** ✓ **PARTIALLY REALIZED**. While the UCSF group's critique gained attention and influenced best practices, the field continued grappling with validation challenges. High-profile ML failures in drug discovery (e.g., various AI-designed drugs that failed in clinical trials) highlighted persistent validation issues, though practices generally improved.

• **"Our biggest challenge is to avoid covering the landscape with stuff that's plausible-sounding but quite possibly irrelevant"** ✓ **ACCURATE FORESIGHT**. The late 2010s and early 2020s saw numerous ML chemistry papers retracted or questioned, including some high-profile deep learning drug discovery claims. The proliferation of ML hype in chemistry created exactly the concern raised—plausible but unvalidated models that could mislead research direction.

## 4. INTEREST

**Rating: 7/10**

This article captures a pivotal methodological debate at the intersection of ML and chemistry, with enduring relevance for proper ML validation that extends beyond chemistry. While not announcing breakthrough therapeutics, it addressed foundational issues about rigor in computational science that remained critical as ML became ubiquitous.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20181120-machine-learning-be-careful-what-you-ask.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_