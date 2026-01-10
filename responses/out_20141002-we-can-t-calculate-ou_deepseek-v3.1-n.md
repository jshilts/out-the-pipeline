
https://www.science.org/content/blog-post/we-can-t-calculate-our-way-out-one
# We Can't Calculate Our Way Out of This One (October 2014)

## 1. SUMMARY
This 2014 commentary addresses the pharmaceutical industry's persistent problem of high clinical trial failure rates, particularly those attributed to unexpected toxicity and safety issues. The author examines various molecular property "rules" that had been proposed to predict and avoid problematic compounds—notably a 2008 Pfizer rule suggesting that compounds with calculated lipophilicity (clogP) > 3 and total polar surface area (TPSA) < 75 Ų are 2.5 times more likely to encounter safety problems, as well as the "Escape from Flatland" concept linking more three-dimensional, sp³-rich structures to better safety profiles.

The central focus is a critical research paper from AstraZeneca scientists who analyzed 130 of their own development compounds and found that these proposed rules did not hold up. The Pfizer rule was actually **inverted** in their dataset, and sp³ fraction showed no correlation with toxicity. Even more telling, when applied to drugs actually approved between 2009-2012, these filters would have rejected many successful medicines, with approved drugs actually clustering in the supposedly "bad" high clogP/high TPSA quadrant. The article argues that simple physicochemical metrics lack sufficient validity to guide drug discovery decisions, and that reliance on such heuristics may cause companies to discard potentially valuable drugs.

## 2. HISTORY
In the decade following this article's publication, the pharmaceutical industry's relationship with predictive metrics evolved significantly, though clinical attrition remained stubbornly high:

**Continued Failures Despite Better Tools:** Clinical trial failure rates remained elevated through the 2010s and into the 2020s, with oncology drugs still failing at 85-90% rates and other therapeutic areas at 80% or higher. While computational methods improved, they did not eliminate the fundamental uncertainty facing drug development.

**Machine Learning Integration:** Rather than abandoning computational approaches, the industry increasingly embraced more sophisticated machine learning and AI-driven methods. Companies applied neural networks, deep learning, and ensemble models to ADMET (absorption, distribution, metabolism, excretion, toxicity) prediction, though these systems required large, high-quality datasets and often struggled with generalization across therapeutic areas.

**Expanded Property Spaces:** Paradoxically, many successful drugs continued to possess "rule-breaking" properties. The rise of targeted protein degraders (PROTACs) and covalent inhibitors created entirely new classes of compounds with molecular weights and properties far exceeding traditional limits. The success of drugs like sotorasib (KRAS inhibitor) and various kinase inhibitors demonstrated that "undesirable" properties could be tolerated when targeting specific mechanisms.

**Real-World Evidence Integration:** By the late 2010s, pharmaceutical companies increasingly incorporated real-world evidence, pharmacogenomics, and patient stratification to reduce trial failures rather than relying solely on compound property predictions. Success rates improved modestly in specific targeted therapies, particularly in oncology.

**Quantitative Impact:** Post-2014 literature suggested that simple cutoff-based approaches continued to be used cautiously, often as prescreening tools rather than definitive decision criteria. The field moved toward probabilistic risk assessment rather than binary pass/fail thresholds, acknowledging the complexity the AstraZeneca study highlighted.

## 3. PREDICTIONS
Several implicit and explicit predictions appear in the article:

• **"We'd be better off if we just admitted it"** - The author predicted that acknowledging the limitations of simple metrics would improve drug discovery decision-making.
  * **Outcome**: **Partially correct but complex.** The industry did become more sophisticated in its use of computational tools, incorporating AI/ML approaches and understanding context-dependence of properties, while still struggling with high attrition rates. Many organizations abandoned hard cutoffs in favor of risk scoring systems, though regulatory pressures sometimes reinforced the use of simple heuristics for early screening.

• **Implicit prediction that rejecting simple metrics wouldn't solve the fundamental problem** - The article argued that even without these flawed filters, distinguishing good from bad compounds would remain difficult.
  * **Outcome**: **Confirmed.** Despite abandoning strict adherence to rules like the Pfizer 3/75 metric, clinical failure rates remained high throughout the 2010s and early 2020s, demonstrating that the underlying prediction challenge persisted.

• **That compounds with "bad" properties according to the rules would continue to succeed** - The study of 2009-2012 approved drugs showed they clustered in supposedly problematic property space.
  * **Outcome**: **Largely confirmed.** Many important drugs approved post-2014 (including kinase inhibitors, PROTACs, covalent inhibitors) continued to possess properties that would have failed simple cutoff criteria, reinforcing that target engagement, mechanism, and clinical context often override simple physicochemical concerns.

• **Implicit prediction that the specific Pfizer 3/75 rule wouldn't become standard practice** - The article strongly suggested the rule lacked general validity.
  * **Outcome**: **Confirmed.** The 3/75 rule did not become an industry standard or regulatory requirement, and subsequent literature generally treated it as one of many historical attempts rather than an established guideline.

## 4. INTEREST
Rating: **7/10**

This article captured an important moment in computational drug discovery's evolution—the realization that simplistic heuristics often fail despite appealing correlations. It highlighted the critical difference between retrospective pattern-matching and prospective prediction, a tension that remained central to pharmaceutical AI through 2024. The AstraZeneca study's findings continued to inform how researchers approached molecular property analysis, making this a prescient piece about the limits of reductionist approaches to complex biological problems.

The analysis maintained lasting relevance, as the fundamental challenge of predicting clinical outcomes from molecular structure persisted, even as computational methods became more sophisticated.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20141002-we-can-t-calculate-our-way-out-one.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_