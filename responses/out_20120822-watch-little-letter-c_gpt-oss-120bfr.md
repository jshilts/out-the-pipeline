
https://www.science.org/content/blog-post/watch-little-letter-c
# Watch that Little Letter (August 2012)

## 1. SUMMARY  
The author, a medicinal chemist, critiques the ubiquitous reliance on **cLogP** (calculated octanol‑water partition coefficient) in early‑stage drug discovery.  
*LogP* measures a compound’s “greasiness” by the ratio of its concentration in octanol versus water; high values (≥ 3) often predict poor solubility, membrane permeability problems, extensive metabolism, and non‑specific protein binding. The author points out two practical issues:  

1. **Experimental logP (shake‑flask) is rarely performed** because it is labor‑intensive; most teams never generate a single measured value.  
2. **Calculated logP (cLogP) is taken as fact** despite being derived from fragment‑based lookup tables or simple algorithms that may be inaccurate for heterocycles, charged species, or novel scaffolds. The author worries that decisions are being made on numbers that lack error estimates or experimental validation.

## 2. HISTORY  
Since 2012 the landscape around logP/logD estimation and usage has evolved, but the core concerns remain relevant.

| Development | What happened | Impact / relevance to the article |
|-------------|---------------|-----------------------------------|
| **Improved fragment‑based calculators** | Newer versions of **ChemAxon LogP**, **ACD/LogP**, **Schrödinger’s QikProp**, and **Molinspiration** incorporated larger training sets, better treatment of hetero‑atoms, and optional **confidence scores**. | Reduces, but does not eliminate, the “black‑box” problem highlighted by the author. |
| **Machine‑learning (ML) models** | Open‑source tools (e.g., **DeepChem**, **MoleculeNet**, **OPERA**) and commercial platforms (e.g., **Insilico Medicine**, **Schrödinger’s Jaguar‑ML**) began delivering **data‑driven logP predictions** with reported RMSE ≈ 0.5 logP units on external test sets. | Provides alternatives to fragment methods and often includes uncertainty estimates, directly addressing the author’s call for “range on it”. |
| **Experimental high‑throughput (HT) shake‑flask** | Miniaturized shake‑flask assays (10 µL scale) coupled to LC‑MS became commercially available (e.g., **Eurofins**, **Cerep**). 96‑well plate formats allow measurement of dozens of compounds per week. | Makes real logP/logD data more accessible, though still not routine for every hit. |
| **Shift toward logD₇.₄ and multiparameter optimization (MPO)** | The community increasingly reports **logD at pH 7.4** (or 6.5) alongside cLogP, especially for ionizable molecules.  MPO scores (e.g., **Lipinski‑Veber**, **CNS‑MPO**) weight logD, solubility, and clearance together. | Aligns with the author’s emphasis on physiological relevance; the “logD” term is now standard in project meetings. |
| **Regulatory and project‑level guidelines** | Many pharma SOPs now require **experimental verification of at least one physicochemical property** (solubility, logD, permeability) before advancing a series, and they explicitly note the **uncertainty of calculated values**. | Institutionalizes the caution the author advocated. |
| **Adoption in AI‑driven design** | Generative models (e.g., **Reinforcement Learning**, **GANs**) treat logP as a “soft constraint” but typically penalize values outside a target window (≈ 1–3).  Some pipelines incorporate **uncertainty‑aware predictions** to avoid over‑optimizing on noisy cLogP. | Shows that the community still leans on logP, but now with more nuanced handling of its limitations. |

Overall, **cLogP remains a staple descriptor**, but the field has added **better calculators, uncertainty metrics, and more routine experimental checks**. The author’s warning about blind trust has been heeded in many organizations, though the “calculated number is taken as reality” still occurs, especially in early‑stage virtual screens.

## 3. PREDICTIONS  
The article itself does not list explicit forecasts, but it implies several expectations:

| Implied prediction | What actually happened |
|--------------------|------------------------|
| *“Calculated logP values will continue to be used without error estimates.”* | **Partially true.** Most commercial calculators still output a single number, but many now provide **confidence intervals** or **applicability domain warnings**. |
| *“Experimental logP measurements will remain rare because the assay is tedious.”* | **True for most early‑discovery labs.** High‑throughput shake‑flask methods have lowered the barrier, yet most projects still rely on calculations for the bulk of compounds. |
| *“Heterocyclic fragments will be poorly represented, leading to misleading cLogP values.”* | **Confirmed.** Early fragment libraries struggled with saturated heterocycles; newer calculators have expanded coverage, but edge‑case scaffolds (e.g., sp³‑rich bicyclic heterocycles) still show larger prediction errors. |
| *“Reliance on cLogP could drive poor decision‑making in drug projects.”* | **Observed.** Several public case studies (e.g., early‑phase failures of high‑logP kinase inhibitors) cite over‑optimistic ADME predictions as a factor, prompting tighter experimental checkpoints. |
| *Implicit: “The community will eventually adopt better, more realistic metrics.”* | **Realized.** The shift toward **logD₇.₄**, **solubility**, and **permeability** measurements, plus the rise of ML‑based predictions with uncertainty, reflects this trend. |

## 4. INTEREST  
**Rating: 7/10**  
The piece is a concise, still‑relevant critique of a foundational metric in medicinal chemistry; it sparked broader discussion about data quality and uncertainty, though it does not introduce novel science. It scores high for practical impact but modest for novelty.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20120822-watch-little-letter-c.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_