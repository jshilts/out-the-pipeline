
https://www.science.org/content/blog-post/compound-properties-starting-renunciation
# Compound Properties: Starting a Renunciation (October 2014)

## 1. SUMMARY

This commentary challenges the over-reliance on simple compound property metrics (such as cLogP, polar surface area, aromatic ring count) in drug discovery as a way to predict and avoid toxicology-driven failures. The author argues that while such metrics may offer broad, fuzzy guidance on pharmacokinetics, treating rule-of-five-type cutoffs as rigid, electrified fences is counterproductive. He contends that predicting PK is already relatively low-value because PK data are easy to obtain experimentally, whereas predicting toxicology—the real bottleneck—is far more complex and not meaningfully captured by these simple metrics. The piece cites an AstraZeneca paper that failed to reproduce Pfizer's earlier trends on property influences as evidence that these approaches lack robustness. The author concludes that he is "losing faith" in property-space policing for toxicology, maintaining only a handful of structure-based red flags (e.g., quinones, rhodanines) while acknowledging that most medicinal chemists already avoid such obvious risks, limiting the practical impact of property-based rules.

## 2. HISTORY

In the years following this article, the pharmaceutical industry's relationship with molecular property metrics evolved in several concrete directions. Lipinski's Rule of Five (Ro5), introduced in 1997 and previously treated as near-dogma, saw its limitations openly debated and its rigid application softened. Research increasingly focused on understanding promiscuity, aggregation, and frequent-hitter behavior, exemplified by the community's adoption and refinement of PAINS (Pan-Assay Interference Compounds) filters, which flagged problematic substructures (e.g., rhodanines, certain quinones) rather than relying on gross property cutoffs. The rise of targeted protein degraders (PROTACs), macrocycles, and antibody-drug conjugates in the late 2010s and early 2020s produced clinically successful drug candidates with molecular weights and properties that clearly violate Ro5, demonstrating the need for mechanism- and modality-aware rules rather than universal cutoffs. Big Pharma began shifting from simple rule enforcement to predictive computational toxicology, leveraging machine learning, transcriptomics, and proteomics to build mechanism-based toxicity models. Public portals such as ChEMBL and PubChem enabled broader analyses of structure-property relationships, often revealing complex, non-linear dependencies that challenge simple cutoff thinking. The AstraZeneca perspective that skeptical, data-driven interrogation is healthy gained traction, while the overall approach matured into one of using property profiles for risk awareness rather than hard go/no-go decisions.

## 3. PREDICTIONS

- **Prediction (implicit): The industry would continue over-relying on simple property metrics and Ro5 zealotry, driven by management's appetite for easy, cheap, quantitative measures.**
  - **Outcome:** Partially accurate. Ro5 and property cutoffs remain widely used in early-stage screening and design, often out of risk aversion and for ease of communication. However, by the mid-to-late 2010s, major companies increasingly adopted nuanced policies—e.g., "property-based guidelines" rather than rigid rules—and invested in computational toxicology platforms. The rise of "beyond-Ro5" modalities forced explicit policy adjustments, and the trend moved toward multiparameter optimization, machine-learning models, and mechanistic risk assessment rather than simple score cutoffs.
  
- **Prediction (implicit): Property-space metrics would remain poor tools for addressing toxicology, because toxicology is too complex and the proposed correlations are too weak and irreproducible.**
  - **Outcome:** Broadly accurate. Simple property-based cutoffs have not become a robust or standard basis for predicting in vivo toxicity outcomes in drug pipelines. Instead, the industry adopted mechanism-based screens (e.g., hERG, CYP inhibition/induction, reactive metabolite traps, cytotoxicity panels, genetic toxicity assays). Successes in predictive toxicology now rely on QSAR/machine-learning models trained on specific mechanisms, human cell-based assays, and multi-omics signatures rather than global property rules.
  
- **Prediction (explicit): Quinones, rhodanines, and other "PAINS" substructures would continue to be broadly avoided due to tox/liability concerns, but this alone would not meaningfully improve overall success rates.**
  - **Outcome:** Accurate. PAINS-aware filtering became standard practice in virtual screening and library design by the mid-2010s and remains so today. However, avoiding these egregious liabilities has not dramatically improved clinical success rates; the broader challenge of unexpected toxicity and lack of efficacy has persisted. The author's nuance regarding cytotoxics and anti-infectives—where quinone-like scaffolds are sometimes tolerated due to selective mechanisms—was also consistent with later practice (e.g., certain kinase inhibitors and redox-active agents).

- **Prediction (implicit): The alternative to property policing would be a less satisfying, empirical, case-by-case approach to compound evaluation.**
  - **Outcome:** Largely accurate. While in vitro and in vivo experimentation remain the bedrock of safety assessment, the post-2014 era saw growth in high-throughput phenotypic screens, humanized organoid/3D culture models, and model-informed drug development (MIDD). These are more empirical than rule-based cutoffs but are more systematic than a purely "wait and see" approach.

## 4. INTEREST

Rating: **7/10**

This article was an influential articulation of growing skepticism toward simple molecular property rules in drug discovery. It correctly diagnosed over-reliance on metrics like Ro5 and appropriately separated PK from toxicology, a distinction that became central to subsequent policy shifts across the industry and the rise of mechanism-based approaches to safety.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20141020-compound-properties-starting-renunciation.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_