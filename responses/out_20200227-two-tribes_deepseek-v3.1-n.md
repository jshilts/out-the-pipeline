
https://www.science.org/content/blog-post/two-tribes
# Two Tribes (February 2020)

## 1. SUMMARY

This commentary reflects on a persistent cultural and skills gap in biopharma between two communities: medicinal chemists (wet-lab practitioners focused on organic synthesis, biochemistry, and bench-level drug discovery) and computational/ML specialists (who work in modeling, programming, algorithm optimization, and data science). The author observes from an MIT AI-in-drug-discovery conference that while calls for "bilingual" talent are common, true convergence remains limited. The divide stems partly from different personal interests and toolkits, and partly from a pragmatic lack of need—neither group has historically found deep knowledge of the other domain essential to their work. Medicinal chemists, the author notes, would engage more with computation if it reliably produced actionable guidance and had not disappointed in the past; computational scientists might engage more with bench realities if that knowledge improved their own workflows. The piece closes by positioning machine learning/AI as a potential "attention-getting" catalyst that could finally make the "Why should I?" hurdle worth clearing—if it delivers actionable predictions and insights.

## 2. HISTORY

Since February 2020, several developments both validated and challenged the article's "two tribes" premise.

In late 2020, DeepMind's AlphaFold2 produced high-accuracy protein structure predictions, followed by the public AlphaFold Protein Structure Database rollout in 2021. This spurred widespread adoption by experimental biologists and medicinal chemists and coincided with expanded investment in computational structure-based drug design. Evidence includes broad database usage by academic groups and pharmaceutical companies, inclusion of AlphaFold2 structures in drug-discovery pipelines, and follow-on advances in docking and functional annotation. Nonetheless, adoption remains stronger for rapidly generating initial hypotheses than for prospective clinical decision-making.

Generative models have matured significantly. Examples include transformer-based protein language models used to design functional proteins; small-molecule generative models (including diffusion and flow-matching methods) that can propose synthesizable structures; and de novo antibody design pipelines. While these tools have entered preclinical workflows at several pharmaceutical and biotech companies, they have not yet become standard universally, and many labs continue to rely on more traditional medicinal chemistry and SAR exploration.

AI-driven target identification and repositioning gained visibility during the pandemic, where computational pipelines were used to prioritize repurposing candidates for COVID-19. However, in many cases these prioritized candidates did not translate into widely adopted, effective therapies, and clinical validation remains the primary driver of uptake. In parallel, AI-driven pathology (digital pathology analysis) and AI-assisted clinical trial design have expanded, with some tools receiving regulatory clearance, although broad clinical adoption varies by market and institution.

On the drug pipeline front, several AI-native biotechs advanced programs into clinical trials (e.g., Exscientia, Recursion, Insilico Medicine, Schrödinger), with early clinical readouts emerging in oncology, immunology, and rare diseases. As of late 2024/early 2025, many of these are still in Phase 1/2 with limited efficacy data, and none has yet produced an AI-discovered-and-developed blockbuster approval that reshapes standard of care. Failures and pipeline adjustments have occurred as well. The overall takeaway is that while AI can accelerate preclinical design, clinical success rates have not dramatically shifted, and the value of these approaches still turns on empirical validation and clinical outcomes, not just computational predictions.

Translational gaps persist. A 2022–2024 theme in industry conferences and publications is that AI-hypothesized targets and molecules still face long odds in synthesis, ADME/Tox, and clinical validation. While generative models can propose novel compounds, experimental hit rates, synthetic accessibility, and pharmacologic fit remain limiting for many programs. Consequently, hybrid workflows blending AI suggestions with medicinal-chemistry triage and optimization are more common than pure end-to-end AI-driven pipelines.

Workforce and training have evolved moderately. Universities and pharmaceutical companies have increased "bilingual" hiring (data science plus therapeutic-area expertise), but the culture gap persists. Computational platforms are more widely used by medicinal chemists for tasks like virtual screening and QSAR, yet deep methodological fluency remains concentrated in specialized teams. Bench chemists often behave as sophisticated end-users rather than developers of ML methods. The "two tribes" have not fully merged, but collaboration interfaces and better tooling have lowered friction in many settings.

Policy and investment saw tangible shifts. AI in drug discovery attracted billions in venture funding, and regulatory agencies issued frameworks and guidance for AI/ML-based submissions. The FDA created initiatives around digital health and AI, with some drug and device approvals incorporating AI evidence. Adoption is growing in targeted applications (e.g., patient stratification, endpoints derived from digital biomarkers), though broad, across-the-board policy reform is still in progress.

## 3. PREDICTIONS

- **Prediction: ML/AI might start producing attention-getting, actionable insights that convince skeptical medicinal chemists.** 
  - **Outcome:** Partially borne out. Generative models and structure prediction are now routinely used for target and lead generation in many organizations, and experimentalists increasingly use AI outputs as hypotheses for validation. However, many AI-proposed targets and compounds fail at the synthesis or validation stage. High-profile successes (e.g., COVID repurposing candidates) often did not translate into clinical impact. Convincing the skeptical chemist still depends less on ML novelty and more on demonstrated SAR improvements, synthetic accessibility, and eventual clinical efficacy.

- **Prediction: The "two tribes" distinction would fade as "bilingual" talent becomes common.** 
  - **Outcome:** Only partially realized. Integrated roles and better interfaces exist, but deep dual expertise remains rare. Teams are more collaborative, yet medicinal chemists and computational experts continue to co-exist as distinct skill populations. Many chemists are sophisticated consumers of computational tools rather than developers, and computational experts often rely on chemists for experimental validation and SAR refinement.

- **Prediction (explicit skepticism): Significant convergence hasn't happened yet, and may not unless the value proposition improves for both sides.** 
  - **Outcome:** Broadly consistent with what followed. Value has improved in specific areas (e.g., structure prediction, generative ideas), but cross-training incentives remain modest. Hybrid workflows are more common than wholesale role consolidation, and the "Why should I?" barrier persists in domains where AI outputs prove unreliable or difficult to synthesize and test.

## 4. INTEREST

Rating: **8/10**

This article remains highly relevant because it diagnosed a durable cultural and technical divide that still shapes drug-discovery workflows. The subsequent arrival of high-impact tools like AlphaFold and generative models sharpened—rather than erased—this dynamic, making the piece a durable lens for understanding adoption and collaboration in computational biology.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20200227-two-tribes.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_