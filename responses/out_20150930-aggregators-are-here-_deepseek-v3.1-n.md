
https://www.science.org/content/blog-post/aggregators-are-here-stay-unfortunately
# Aggregators Are Here to Stay, Unfortunately (September 2015)

## 1. SUMMARY

The article discusses the persistent problem of colloidal aggregation in drug discovery screening—a major source of false positives where compounds clump together in solution and sequester protein targets, appearing as hits when they're actually artifacts. The phenomenon was brought to wider attention largely through Brian Shoichet's group at UCSF. Detection methods include adding detergents to assays or using dynamic light scattering, but predicting aggregators upfront remains difficult because behavior varies with assay conditions and concentration.

A key finding from a new Journal of Medicinal Chemistry paper by Shoichet's group reveals problematic trends: over 7% of compounds in the medicinal chemistry literature (ChEMBL) are predicted aggregators, compared to just 0.73% of purchasable molecules, and the prevalence of plausible aggregators increased more than 8-fold between 1995 and 2015. The authors launched a freely available aggregator database (advisor.bkslab.org) with similarity searching capabilities to help identify these problematic compounds.

The article speculates on why aggregators are being enriched in the literature—either because false positives get pursued as leads, or because structural features causing aggregation may overlap with features that protein binding sites naturally select for, making them fundamentally hard to avoid.

## 2. HISTORY

The aggregator problem persisted and became more systematically addressed after 2015:

**Aggregator Database and Tools Evolution**: The advisor.bkslab.org database (BKS Aggregator Advisor) referenced in the article continued to be maintained and expanded. Subsequent research refined understanding of aggregator mechanisms and improved prediction tools. The aggregator detection workflow—using detergent addition, dynamic light scattering, and computational filters—became standard practice in high-throughput screening facilities.

**Industry Adoption**: Major pharmaceutical companies and academic screening centers widely adopted systematic aggregator detection protocols. Many organizations started including detergent controls (typically Triton X-100 or Tween) as standard in primary screening assays. The "aggregator flag" became a routine step in hit validation workflows.

**Impact on Drug Discovery Pipelines**: The recognition of aggregation artifacts led to more rigorous hit validation processes. False positive rates in screening campaigns decreased as aggregator detection became earlier and more systematic. However, aggregators remained a significant challenge, particularly in certain target classes and with specific chemical scaffolds.

**Research Developments**: Subsequent studies explored the structural features promoting aggregation and refined computational prediction methods. Work continued on understanding why some aggregators still showed activity even when aggregation was prevented, suggesting some might have genuine binding modes. The field moved toward distinguishing "pure" aggregators from compounds that had dual mechanisms.

The fundamental challenge remained: certain privileged scaffolds in medicinal chemistry continued to have aggregation tendencies, making complete avoidance difficult while maintaining chemical diversity.

## 3. PREDICTIONS

**Prediction: Aggregators will remain a persistent problem because they share structural features with desirable drug-like compounds**

- **Outcome**: This proved largely accurate. Aggregators remained a significant issue in drug discovery throughout the late 2010s and beyond. However, systematic detection and filtering improved significantly, reducing (but not eliminating) their impact on false leads in drug discovery pipelines.
- **Specifics**: The fundamental tension identified—that aggregation-prone features can overlap with protein-binding features—continued to be validated. Subsequent research on privileged scaffolds and PAINS (pan-assay interference compounds) confirmed that many useful pharmacophores also had aggregation potential.

**Implicit prediction: The 8-fold increase in aggregators in the literature would continue or accelerate**

- **Outcome**: The growth rate likely stabilized or slowed as awareness increased. By the late 2010s, most major journals and pharmaceutical companies had implemented stricter hit validation criteria that would have reduced the publication of unrecognized aggregator false positives.

**Implicit prediction: The free aggregator database would become a valuable community resource**

- **Outcome**: The BKS Aggregator Advisor and similar tools became widely used in the field. Computational aggregation prediction tools became integrated into cheminformatics workflows, though with the caveats about false positives/negatives noted in the original article.

## 4. INTEREST

**Rating: 8/10**

The article addresses a persistent, practical problem in drug discovery with concrete data showing how bad the aggregator problem had become. It captures a moment when systematic approaches to this issue were just becoming widespread, and its analysis of why aggregators get enriched in the literature remains relevant. The topic has ongoing importance as high-throughput screening continues to be a primary drug discovery method.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20150930-aggregators-are-here-stay-unfortunately.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_