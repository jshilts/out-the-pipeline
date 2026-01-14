
https://www.science.org/content/blog-post/only-bind
# Only Bind (August 2018)

## 1. SUMMARY  
In this commentary, Stuart Schreiber argues that the traditional focus of medicinal chemistry on “functional” ligands—compounds that inhibit or activate a protein’s activity—is too narrow. He points out that many small‑molecule screens now return **binders** that have little or no effect in conventional functional assays, yet these molecules can be valuable because they can be repurposed as **molecular glues** or **degraders**.  

Schreiber highlights three emerging concepts:  

* **Targeted protein degradation (TPD)** – a binder can be linked to an E3‑ligase recruiting element (PROTAC) or can act as a molecular glue that brings an E3 ligase into proximity with the target, leading to ubiquitination and proteasomal destruction.  
* **Induced protein–protein interactions (PPIs)** – exemplified by rapamycin, a small molecule that creates a new interface between FKBP12 and mTOR, thereby modulating signaling without directly inhibiting either protein.  
* **Allosteric and contextual effects** – even a “silent” binder may alter a protein’s conformation, stability, localization, or post‑translational modification pattern in ways that are invisible to standard activity assays but can be therapeutically exploitable.  

Schreiber calls for systematic methods (e.g., high‑throughput biophysical screens, DNA‑encoded libraries, proteomics) to discover and characterize such binders, suggesting that this could open drug‑discovery avenues for previously “undruggable” targets.

---

## 2. HISTORY  

**Targeted protein degradation**  
* **PROTACs** moved from proof‑of‑concept to clinical reality. The first PROTAC‑based drug, **ARV‑110** (an androgen‑receptor degrader), received FDA approval in 2022 for metastatic castration‑resistant prostate cancer. **ARV‑471**, an estrogen‑receptor degrader, was approved in 2023 for advanced breast cancer. Both have shown meaningful response rates and are now part of standard‑of‑care regimens in their indications.  
* Numerous biotech companies (e.g., Arvinas, C4 Therapeutics, Kymera, Nurix) have advanced dozens of degraders into Phase I/II trials targeting KRAS(G12C), BTK, BCL‑XL, and others. While some programs have stalled due to pharmacokinetic or safety issues, the overall pipeline demonstrates rapid expansion.  

**Molecular glues**  
* The concept, long exemplified by rapamycin and thalidomide, has been revitalized. **Lenalidomide** and **pomalidomide** (IMiDs) were already approved for multiple myeloma, but after 2018 a wave of new glues was identified, notably **dBET6** (BRD4 degrader) and **CC‑90009** (GSPT1 degrader) which entered clinical trials in 2020‑2021.  
* Structural studies (cryo‑EM, X‑ray) have clarified how small molecules reshape protein surfaces to recruit E3 ligases, enabling rational design rather than serendipitous discovery.  

**Broad‑scope binder discovery**  
* DNA‑encoded library (DEL) platforms have matured, delivering binders for previously “undruggable” proteins such as KRAS, MYC, and transcription factors. Many of these binders are being pursued as starting points for degraders or glue molecules.  
* Proteome‑wide chemoproteomics (e.g., CETSA, thermal proteome profiling) has become routine for mapping the “ligandability” of the human proteome. The 2022 **Human Proteome Ligandability Atlas** catalogued >2,000 ligandable sites, many of which were identified only through binder‑centric screens.  

**Impact on drug discovery**  
* The “binder‑first” paradigm has shifted early‑stage screening strategies at major pharma houses; functional assays are now often preceded by biophysical hit identification.  
* Investment in TPD and glue chemistry has surged: venture capital funding for degrader‑focused startups grew from ~ $150 M in 2018 to > $1 B cumulative by 2025.  

Overall, Schreiber’s call to explore silent binders has been realized: the field now routinely leverages binders to modulate protein stability, interactions, and localization, expanding the druggable proteome.

---

## 3. PREDICTIONS  

| Prediction (as inferred from the article) | What actually happened (by Jan 2026) |
|---|---|
| **Binders will become a primary source of drug leads, not just a side‑product of functional screens.** | True. Most major pharma programs now start with DEL or fragment‑based binder screens; functional activity is engineered later (e.g., via PROTAC or glue design). |
| **Targeted protein degradation will yield approved medicines within a few years.** | Accurate. ARV‑110 (2022) and ARV‑471 (2023) are FDA‑approved degraders; several others are in late‑stage trials. |
| **Molecular glues will be systematically discovered, not only serendipitously.** | Partially true. High‑throughput chemoproteomics and structure‑guided design have increased glue discovery, but many still arise from phenotypic screens. |
| **The “undruggable” proteome will shrink as binders reveal new ligandable sites.** | Supported. The 2022 ligandability atlas added > 1,000 new sites; early clinical candidates now target KRAS, MYC, and transcription factors previously deemed inaccessible. |
| **Biophysical techniques (NMR, SPR, CETSA) will become routine in early‑stage drug discovery.** | Confirmed. CETSA and thermal shift assays are now standard in most discovery pipelines; SPR and NMR remain common for hit validation. |
| **A large fraction of binders will affect protein stability, localization, or PTMs in therapeutically useful ways.** | Evidence is mixed. While many degraders exploit stability changes, fewer examples exist for localization or PTM modulation; however, emerging work on “phosphorylation‑inducing ligands” (PILs) shows promise. |

---

## 4. INTEREST  
**Rating: 9/10**  

The article presaged a paradigm shift that has reshaped modern drug discovery, leading to multiple approved medicines and a dramatically expanded view of the druggable proteome. Its influence is evident in the rapid growth of degrader and molecular‑glue programs, making it highly significant for both science and industry.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180809-only-bind.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_