
https://www.science.org/content/blog-post/lipinski-s-anchor
# Lipinski's Anchor (November 2013)

## 1. SUMMARY
This commentary analyzes Michael Shultz's critique of how medicinal chemists use metrics in drug discovery. The article focuses on Shultz's concept of "Lipinski's Anchor" - the idea that Christopher Lipinski's "Rule of Five" (MW ≤ 500, LogP ≤ 5, H-bond donors ≤ 5, H-bond acceptors ≤ 10) has become a cognitive anchor that overly influences how researchers evaluate drug candidates, beyond what the original intent of the rule supported.

The piece discusses two cognitive biases from Daniel Kahneman's work: "attribute substitution" (replacing complex problems with simpler proxies) and "anchoring" (over-reliance on initial numerical benchmarks). Shultz argues that drug hunters have misinterpreted the Rule of Five as defining "drug-likeness" when the original 1997 paper studied only Phase II+ drugs and aimed to flag poor oral bioavailability risks. The commentary notes that the average molecular weight of approved oral drugs has been increasing over time, while pharmacokinetic failure rates have been decreasing - potentially contradicting the assumption that MW 500 is a critical cutoff. The author expresses willingness to maintain some bias toward Rule-of-Five compliant compounds but acknowledges molecular weight may not be a reliable proxy for the ADME properties researchers actually need to optimize.

## 2. HISTORY
Debate around drug-likeness metrics has continued evolving since 2013, with several important developments. Research into RO5 exceptions has expanded with multiple groups analyzing drugs outside these cutoffs. The success of orally bioavailable drugs with MW > 500 has become much more clear over the past decade, including examples like cyclosporine (1202 Da), voclosporin (~866 Da), and several kinase inhibitors in the 500-650 Da range that achieved oral bioavailability through structure-guided design.

Post-2013, the pharmaceutical industry has increasingly moved toward more nuanced, data-driven ADME property assessment rather than rigid cutoffs. Tools like DMPK informatics platforms now combine multiple parameters (lipophilicity, molecular flexibility, polar surface area) with predictive models rather than relying solely on RO5 compliance. Lipinski himself co-authored papers around 2016-2017 emphasizing that the rules were guidelines for early-stage screening library design, not drug development constraints. Research has shown that apparent "convergence" on RO5 properties in the 2010s was influenced by target class selection and screening cascade design.

However, metrics like Ligand Efficiency and LLE (Lipophilic Ligand Efficiency) remain widely used in medicinal chemistry optimization, often for practical rather than scientific reasons - they provide simple communication tools for cross-disciplinary teams.

## 3. PREDICTIONS
- **Prediction**: Molecular weight cutoffs would be reconsidered because the average MW of approved oral drugs was increasing while PK/ bioavailability failure rates were decreasing
- **Outcome**: This trend continued, with more large oral drugs approved (e.g., selinexor, pacritinib). However, apparent success doesn't prove MW 500 isn't a useful compromise between permeability, solubility, and target binding - the causal question remains debated

- **Prediction**: The industry would increasingly recognize that RO5 was overly simplistic as a definition of "drug-likeness"
- **Outcome**: Mixed. RO5 remains widely taught and used in drug discovery, but with explicit caveats about exceptions and context-dependence

- **Prediction**: More sophisticated, multivariate analyses would replace simple anchor metrics
- **Outcome**: This has occurred to some degree with AI-driven ADME prediction tools, but simple metrics persist for heuristic decision-making

## 4. INTEREST 
**8/10** - This article connects important cognitive science principles to practical drug discovery behavior, focusing on observed perceptual rigidities rather than drug development outcomes. While the specific argument relies on retrospective data that was already available in 2013, its reframing around systematic bias has lasting influence on how medicinal chemists approach property optimization.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20131125-lipinski-s-anchor.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_