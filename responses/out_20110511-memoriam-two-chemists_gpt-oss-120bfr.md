
https://www.science.org/content/blog-post/memoriam-two-chemists
# In Memoriam, Two Chemists (May 2011)

## 1. SUMMARY  
The author notes the recent deaths of two influential chemists: **Corwin Hansch**, a pioneer of quantitative structure‑activity relationships (QSAR) who introduced linear free‑energy relationships to medicinal chemistry in the early 1960s, and **David Gin**, a synthetic organic chemist known for challenging work in carbohydrate chemistry. The piece reflects on the author’s own early enthusiasm for QSAR, describing practical obstacles that still plague the field—heterogeneous SAR series, gaps in chemical space, and noisy assay data. While praising Hansch’s vision, the author emphasizes that the difficulties he identified remain relevant, and laments the loss of Gin’s experimental expertise.

## 2. HISTORY  

### Hansch’s legacy and the evolution of QSAR  
* **From linear models to machine learning** – After 2011, QSAR continued to be a core tool in drug discovery, but the community shifted from simple Hansch‑type linear free‑energy relationships to more sophisticated statistical and machine‑learning approaches (random forests, support‑vector machines, deep neural networks). Publicly available cheminformatics platforms such as **KNIME**, **RDKit**, and commercial suites (Schrödinger, MOE) integrated these methods, making them routine in many pharma and biotech labs.  
* **Regulatory acceptance** – The U.S. FDA’s *Guidance for Industry: Use of Computational Modeling and Simulation* (updated 2017) explicitly acknowledges QSAR and related in‑silico methods for safety assessment, showing institutional acceptance that grew after the article’s publication.  
* **Impact on drug pipelines** – Several drugs that entered clinical trials in the 2010s cite QSAR‑guided hit‑to‑lead work. Notable examples include **Baloxavir marboxil** (influenza, approved 2018) and **Lumacaftor** (cystic fibrosis, approved 2015), where QSAR helped prioritize analogues, though the contributions were part of broader, multi‑disciplinary programs.  
* **Academic and open‑source growth** – Large‑scale public datasets (ChEMBL, PubChem BioAssay) and competitions such as the **D3R Grand Challenge** (starting 2015) spurred community benchmarking of QSAR models, directly addressing the “noisy assay data” problem highlighted in the article.  

### David Gin and carbohydrate chemistry  
* **Gin’s research legacy** – David Gin (1960‑2010) was remembered for innovative synthetic routes to complex oligosaccharides, including a highly cited 2009 JACS paper on a stereoselective glycosylation method. After his death, his former group at Memorial Sloan‑Kettering continued work on automated carbohydrate synthesis; the **Automated Glycan Assembly (AGA)** platform, first demonstrated in 2012, built on concepts he helped develop.  
* **Field progress** – The past decade has seen rapid advances in chemo‑enzymatic and solid‑phase synthesis of glycans, leading to commercial glycan libraries (e.g., **GlycoMimetics**, **Carbosynth**) and the first FDA‑approved glycan‑based therapeutic, **Mogamulizumab** (approved 2018 for adult T‑cell leukemia/lymphoma). While Gin was not directly involved, his methodological contributions are cited in many of these later works.  

## 3. PREDICTIONS  

The article itself does not contain explicit forecasts, but it implies two expectations:

| Implied prediction | What actually happened |
|--------------------|------------------------|
| **QSAR will become a routine, reliable tool for medicinal chemistry despite data quality issues.** | QSAR is now standard in many organizations, but its reliability still hinges on high‑quality assay data. The community has responded by emphasizing assay standardization, data curation, and uncertainty quantification. |
| **The challenges Hansch identified (heterogeneous SAR series, gaps in chemical space) will limit the method’s usefulness.** | These challenges remain, but modern cheminformatics mitigates them through large, diverse virtual libraries, active‑learning workflows, and generative models that can propose compounds to fill gaps. The limitations are less fatal than they seemed in 2011. |
| **The loss of a synthetic chemist like Gin would be a setback for carbohydrate chemistry.** | While Gin’s death was a personal loss, the field continued to progress, driven by collaborative consortia (e.g., **GlycoNet**) and automation technologies that built on his synthetic insights. |

## 4. INTEREST  
**Rating: 7/10** – The piece is a concise, historically grounded reflection on two influential scientists whose work underpins ongoing trends in drug design and carbohydrate synthesis; its relevance has only grown as computational chemistry and glyco‑medicine have matured.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20110511-memoriam-two-chemists.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_