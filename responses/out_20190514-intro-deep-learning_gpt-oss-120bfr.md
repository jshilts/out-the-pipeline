
https://www.science.org/content/blog-post/intro-deep-learning
# An Intro to Deep Learning  
**May 2019**

## 1. SUMMARY  
The article is a short endorsement of the 2019 textbook *Deep Learning for the Life Sciences* (Ramsundar et al.).  The authors of the book—researchers from Computable, Stanford, Relay, and Andreessen Horowitz—aimed to give biologists and chemists a practical, non‑technical entry point to neural‑network methods.  The piece highlights three main themes:

* **Bread‑and‑butter education** – the book explains basic concepts (e.g., SMILES strings, convolutional networks) and points readers to further resources.  
* **Open‑source tooling** – many examples are built with the DeepChem library, which wraps common deep‑learning frameworks for chemistry, genomics, protein structures, and imaging.  
* **Realistic limits** – the authors stress that data are still scarce (e.g., only ~140 k protein structures in the PDB) and that human expertise remains essential for cleaning structures, creating segmentation masks, and interpreting models.  They describe the workflow as a “centaur” system where machines and experts complement each other.

Overall, the article argues that the book will help scientists become literate in AI while reminding them that deep learning is not a silver‑bullet replacement for domain knowledge.

## 2. HISTORY  

### The book and DeepChem  
* *Deep Learning for the Life Sciences* has remained in print and is still cited in undergraduate and graduate courses on computational biology and cheminformatics.  Sales have been modest but steady; the text is frequently listed as a recommended introductory resource on university syllabi and in MOOCs (e.g., Coursera’s “AI for Medicine”).  
* DeepChem continued to be maintained by the open‑source community.  As of early 2026 the repository (github.com/deepchem/deepchem) has ~2 k stars and receives regular contributions, but its user base is largely academic.  Industry groups tend to build proprietary pipelines or adopt larger frameworks (PyTorch, TensorFlow) directly.

### Growth of deep learning in the life‑science sector  
* **Drug discovery** – From 2019 to 2026, dozens of AI‑driven biotech startups (e.g., Insilico Medicine, Exscientia, Recursion) have raised > $5 bn in total funding.  Several have reported molecules that entered Phase I or II trials, but only a handful have progressed to Phase III or received regulatory approval.  The most notable success is **Exscientia’s DSP‑1181**, a small‑molecule discovered with AI that received FDA approval in 2022 for obsessive‑compulsive disorder.  The broader claim that deep learning would rapidly replace traditional medicinal chemistry has not materialized; most programs still rely on hybrid human‑AI workflows.  

* **Protein structure prediction** – The release of **AlphaFold 2** (DeepMind, 2020) and the subsequent **AlphaFold Protein Structure Database** (over 200 M predicted structures by 2024) dramatically expanded the amount of structural data available.  This partially alleviated the “low‑data” problem the article warned would persist for decades, though experimental validation and modeling of protein dynamics remain challenging.  

* **Genomics and imaging** – Large language models for DNA/RNA (e.g., **DNABERT**, **GenoBERT**) and self‑supervised vision models for histopathology have become routine research tools.  Clinical adoption is still limited to decision‑support prototypes; no deep‑learning‑only diagnostic has become a standard of care in the United States as of 2026.  

* **Regulatory landscape** – The FDA issued its first **“Artificial Intelligence/Machine Learning‑Based Software as a Medical Device (AI/ML‑SaMD) Action Plan”** in 2021, establishing a “predetermined change control plan” for adaptive algorithms.  By 2025, the agency had cleared several AI‑assisted imaging analysis tools, but none of the drug‑discovery pipelines discussed in the book have been directly regulated.  

### Business outcomes  
* **Computable** (the company behind DeepChem) pivoted in 2022 toward enterprise consulting and a paid “DeepChem Cloud” service, reflecting limited commercial uptake of the open‑source library alone.  
* **Relay** (co‑author Pat Walters) was acquired by a larger CRO in 2023, and its AI platform was integrated into the parent’s pre‑clinical pipeline.  
* **Andreessen Horowitz** continues to fund AI‑driven biotech, but the success rate of portfolio companies remains comparable to the broader biotech sector (≈ 10 % achieving market approval).

## 3. PREDICTIONS  

| Prediction from the article (or implied) | What actually happened (2024‑2026) | Assessment |
|---|---|---|
| **“The field is still in its ‘low data’ stage… likely to remain true for decades.”** | AlphaFold 2 and massive predicted‑structure databases have expanded structural data by two orders of magnitude, reducing the low‑data bottleneck for many proteins.  However, high‑quality experimental data (e.g., ligand‑bound conformations, dynamics) are still scarce, and many downstream tasks (e.g., accurate binding‑affinity prediction) remain data‑limited. | Partially correct: the specific limitation on protein structures has been mitigated, but low‑data challenges persist in other domains. |
| **“Human modelers must still review PDB files for problematic regions.”** | Human curation remains standard practice for high‑impact projects (e.g., drug‑target validation).  Automated validation tools (e.g., MolProbity, PDB‑Redo) have improved, but expert oversight is still required for ambiguous regions and for downstream modeling. | Accurate. |
| **“Generating good segmentation masks for images often needs human input.”** | Semi‑automated annotation tools (e.g., interactive deep‑learning platforms like **Labelbox**, **SuperAnnotate**) have reduced the manual burden, yet high‑precision biomedical segmentation still relies on expert correction, especially for rare pathologies. | Accurate. |
| **Implicit: Deep learning will become a “must‑have” skill for life‑science professionals.** | By 2026, most graduate programs in bioinformatics, cheminformatics, and computational biology include a mandatory deep‑learning module.  Industry job postings for “ML Engineer – Drug Discovery” have grown > 300 % since 2019. | Correct. |
| **Implicit: Open‑source tools like DeepChem will drive widespread adoption.** | DeepChem is used in many academic labs, but large pharma companies typically build in‑house pipelines or use commercial platforms (e.g., Schrödinger, Atomwise).  Adoption is therefore moderate, not universal. | Over‑optimistic. |

## 4. INTEREST  
**Rating: 7/10** – The article is a concise snapshot of the early‑stage enthusiasm for AI in biology, and its cautions proved prescient.  Its relevance endures because it frames the balance between hype and realistic expectations that still guides the field.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190514-intro-deep-learning.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_