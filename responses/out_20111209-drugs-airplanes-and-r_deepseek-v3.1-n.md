
https://www.science.org/content/blog-post/drugs-airplanes-and-radios
# Drugs, Airplanes, and Radios (December 2011)

## 1. SUMMARY
This 2011 commentary responds to an article comparing airplane design to drug design. The central argument from the original piece was that if pharmaceutical companies used better computational tools to predict toxicity and other properties early in drug discovery, they could avoid costly clinical trial failures—much like aerospace companies use simulations to test rocket motors before building them. The commentary author remains skeptical, questioning whether existing in silico tools would have actually caught major drug failures like Vioxx or torcetrapib, or whether they might have incorrectly eliminated successful drugs.

The article references biologist Yuri Lazebnik's influential 2002 paper "Can a Biologist Fix a Radio?", which argued that biology needs formal languages and systematic engineering approaches similar to circuit diagrams. The commentator expresses doubt about this analogy, citing algorithmic complexity—biological systems have far more nonlinear interactions and emergent properties than engineered devices like radios. While physics can be elegantly described by compact mathematical formalisms (like Maxwell's equations), biology resists such simplification due to its complexity and context-dependence. The author acknowledges the appeal of engineering approaches but remains unconvinced they're practical for drug discovery at that time.

## 2. HISTORY
In the decade following this article, computational drug discovery made significant advances, though the fundamental challenges the author identified proved persistent. Structure-based drug design and molecular dynamics simulations became more sophisticated and widely adopted across the pharmaceutical industry. However, **the core problems of predicting toxicity and clinical failure remained largely unsolved**. High-profile clinical failures continued, including Alzheimer's disease trials (solanezumab, gantenerumab, crenezumab), which computational approaches did not obviously prevent.

**Regulatory and industry changes** were more incremental than revolutionary. The FDA's adoption of model-informed drug development (MIDD) in the 2010s did promote greater use of computational approaches. Companies like Schrödinger and Atomwise successfully commercialized computational drug discovery platforms, and major pharma companies increasingly integrated AI methods. Yet **the fundamental hit rates in drug discovery remained low**—still around 10% of drugs entering clinical trials reached approval.

**Real-world drug development outcomes** showed mixed success for computational approaches. While some companies achieved notable successes using computational methods (Vertex's CF drugs, various kinase inhibitors), there was no dramatic increase in overall drug approval success rates. The complex, multifactorial nature of drug toxicity that the author identified proved resistant to purely computational solutions. The field moved toward "augmented intelligence" approaches combining computational predictions with experimental validation, rather than pure in silico design. The **Systems Biology Markup Language (SBML)** and other formalisms were developed and adopted in academic research, but did not fundamentally transform industrial drug discovery pipelines as envisioned by the airplane/radio analogies.

## 3. PREDICTIONS
The article contained these predictions or assumptions:

• **"State-of-the-art in silico structure–property prediction tools [would allow] good enough accuracy to eliminate many poor molecules prior to synthesis"** - **Mixed accuracy**. Computational tools did improve and became widely adopted in pharmaceutical workflows, but they **did not achieve the reliable predictive accuracy** needed to prevent major clinical failures. False positives and negatives remained problematic, and the tools were most successful in early-stage screening rather than definitive toxicity prediction.

• **Formal languages and engineering-style formalisms would help systems biology** - **Incomplete realization**. SBML and other formal languages **were developed and gained academic adoption**, but they **did not achieve widespread industrial use** in drug discovery pipelines. The complexity of biological systems proved more resistant to simplification than engineering systems.

• **"Is it even possible?" [to create useful biological formalisms]** - **Answered: partially**. Formalisms were created and proved **valuable for specific applications** (metabolic modeling, some signaling pathways), but they **did not achieve the universal utility** of circuit diagrams in electronics or aerodynamic models in aerospace.

• **"Where to even start?" [with biological formalisms]** - **Multiple starting points emerged**. The field explored various approaches including constraint-based metabolic modeling, Boolean network models, and rule-based systems, but **no single comprehensive formalism** emerged that could handle biological complexity in drug discovery applications.

## 4. INTEREST
**Decile score: 7**

The article was prescient in identifying core challenges that persisted for over a decade in computational drug discovery, with the complexity argument and skepticism about simple engineering analogies proving well-founded. It highlighted fundamental limitations that remained relevant in an increasingly AI-focused pharmaceutical landscape.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20111209-drugs-airplanes-and-radios.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_