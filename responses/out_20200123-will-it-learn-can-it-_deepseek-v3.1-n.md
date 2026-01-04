
https://www.science.org/content/blog-post/will-it-learn-can-it-learn
# Will It Learn? Can It Learn? (January 2020)

## 1. SUMMARY
This commentary explores the theoretical limits of machine learning through the lens of "learnability"—the question of whether a given ML algorithm can actually extract meaningful rules from a dataset. The author notes that while biopharma companies enthusiastically adopt ML to mine large biological datasets, the approach assumes useful patterns exist and are discoverable. The article centers on a Nature Machine Intelligence paper that mathematically proved certain learning problems are formally undecidable, drawing an explicit connection between ML learnability and Gödel's incompleteness theorems.

The key technical insight involves showing that learnability of a particular ML model (EMX, or "estimating the maximum") is tied to data compressibility, which in turn connects to the continuum hypothesis—the unsolved mathematical question about whether there exist infinite sets between the sizes of rational and real numbers. Since the continuum hypothesis was proven undecidable by Paul Cohen in the 1960s, the learnability question for this ML system is also undecidable: you cannot prove whether the algorithm can or cannot learn certain rules, no matter how sophisticated your analysis. The author acknowledges this may be a contrived theoretical scenario but notes the unnerving implication that undecidability can reach into practical ML applications.

## 2. HISTORY
Since January 2020, machine learning adoption in biotechnology has accelerated dramatically, but with notable shifts in emphasis and outcomes:

**Adoption and Practical Applications:**
- ML/AI became standard in drug discovery pipelines, with major pharmaceutical companies (Pfizer, Novartis, AstraZeneca, GlaxoSmithKline) integrating computational approaches for target identification, lead optimization, and clinical trial design.
- AlphaFold2 (2020) revolutionized protein structure prediction, achieving accuracy previously thought decades away. By 2024, over 200 million protein structure predictions were publicly available, transforming structural biology.
- AI-designed drugs entered clinical trials: Insilico Medicine's AI-discovered drug for idiopathic pulmonary fibrosis reached Phase II trials by 2023, and Exscientia's AI-designed cancer drug entered clinical testing.
- ML models successfully predicted COVID-19 variants, optimized vaccine design, and guided pandemic response strategies.

**Scientific and Methodological Evolution:**
- The field moved toward hybrid approaches combining ML with biophysical knowledge and mechanistic models, recognizing pure data-driven limitations.
- Foundation models like protein language models (ProtTrans, ESM) emerged, trained on billions of protein sequences, demonstrating that scaling dataset size with appropriate architectures achieved previously impossible prediction capabilities.
- Active learning, Bayesian optimization, and uncertainty quantification became standard tools to address the "exploration vs. exploitation" problem inherent in drug discovery.

**Commercial and Regulatory Impact:**
- AI-native biotech companies attracted billions in investment: Recursion Pharmaceuticals, Exscientia, and Schrödinger reached multi-billion dollar valuations.
- The FDA began approving AI/ML-based medical devices and diagnostic tools, establishing regulatory frameworks for algorithm transparency and validation.
- However, most ML applications in drug discovery remained preclinical—very few AI-designed drugs progressed beyond Phase II trials by early 2024, highlighting translational challenges.

**Theoretical Research Evolution:**
- Research on ML theory in biology focused more on practical limitations: data quality, experimental bias, distribution shift, and the "reproducibility crisis" in computational biology.
- Undecidability remained an esoteric topic in mainstream biotech ML applications—the practical challenges of noisy biological data, small sample sizes, and complex causal relationships dominated research directions.

## 3. PREDICTIONS
The article contained no explicit forward-looking predictions, focusing instead on theoretical implications of the undecidability result. However, several implicit assumptions and contextual themes can be evaluated:

**Theme: ML adoption in biopharma will require confronting fundamental limitations**
- **Actual outcome:** The field broadly recognized limitations but focused on practical rather than theoretical undecidability. ML tools were successfully deployed for specific, well-defined tasks (protein structure prediction, molecular property calculation, reaction optimization) while acknowledging that discovering fundamentally new biological mechanisms from data alone remained challenging. The emphasis shifted toward "human-in-the-loop" systems combining ML with domain expertise.

**Theme: The relationship between data compressibility and learnability would have practical implications**
- **Actual outcome:** Compression-based approaches found niche applications (genome compression, protein sequence embeddings that implicitly use compressibility concepts), but the specific EMX model and its undecidability connection remained largely theoretical. Practical ML systems relied on empirical validation rather than theoretical learnability guarantees.

**Theme: ML would become essential for extracting value from large biological datasets**
- **Actual outcome:** **Substantially validated.** ML became indispensable in genomics (variant interpretation, GWAS analysis), proteomics, metabolomics, and clinical data integration. The Human Cell Atlas, single-cell RNA sequencing atlases, and precision medicine initiatives all depended critically on ML methods. However, early hype about "AI discovering drugs autonomously" moderated toward more realistic expectations about ML as a powerful tool augmenting human scientists.

**Not explicitly discussed but relevant: AlphaFold would solve protein folding**
- The article predates AlphaFold2 by 18 months. While not mentioned, the 2020 structural biology revolution dramatically demonstrated that sufficiently large datasets (protein sequences) combined with appropriate architectures (attention-based transformers) could solve problems previously considered intractable, suggesting that learnability limits, while theoretically real, might be pushed very far with enough data and innovation.

## 4. INTEREST
Rating: **8/10**

This article was prescient in highlighting fundamental theoretical limits of machine learning at a time when biopharma enthusiasm was peaking. The undecidability result connects ML to deep mathematics (Gödel, Cohen, Cantor) and anticipates later challenges in ensuring ML reliability. While the specific EMX scenario remained theoretical, the broader caution about assuming learnability proved wise as the field confronted reproducibility issues and the "long tail" problem in deploying ML systems. The piece remains intellectually stimulating for understanding the mathematical foundations of ML limitations.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20200123-will-it-learn-can-it-learn.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_