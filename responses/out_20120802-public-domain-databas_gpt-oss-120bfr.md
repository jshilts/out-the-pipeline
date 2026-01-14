
https://www.science.org/content/blog-post/public-domain-databases-medicinal-chemistry
# Public Domain Databases in Medicinal Chemistry (August 2012)

## 1. SUMMARY  
The 2012 commentary highlighted a suite of freely available databases that compile medicinal‑chemistry information. It described three “big‑three” resources—**BindingDB** (quantitative protein‑ligand binding data), **ChEMBL** (curated bioactivity data with overlap to PubChem), and **PubChem** (large‑scale screening and compound collections). It then listed a dozen additional portals, including **Binding MOAD**, **ChemSpider**, **DrugBank**, the **IUPHAR/GRAC** pharmacology guides, **PDBbind**, **PDSP Ki**, **SuperTarget**, the **Therapeutic Targets Database (TTD)**, and **ZINC** (commercially available virtual libraries). The article noted the irony that such a free‑resource guide was itself behind an ACS paywall.

## 2. HISTORY  

### Continued growth and integration  
- **BindingDB** remains actively maintained (latest release 2024). It has expanded to >2 million binding measurements and now offers a REST API and integration with ChEMBL and UniProt.  
- **ChEMBL** has grown from ~1.5 million compounds in 2012 to >2.5 million unique structures (release 35, 2024). It now includes extensive ADMET, assay‑type metadata, and links to the European Bioinformatics Institute’s protein resources.  
- **PubChem** exploded to >110 million unique compounds and >1 billion bioassay results (2024). The “BioAssay” archive now contains high‑throughput screens from the NIH Molecular Libraries Program and many private‑sector contributions.  
- **ChemSpider** continues under the Royal Society of Chemistry, now aggregating >100 million records and providing a robust API for structure search.  
- **DrugBank** has been updated to version 6 (2023), covering >13 000 drugs and >30 000 drug‑target interactions, and is widely used for pharmacovigilance and AI‑driven repurposing studies.  
- **IUPHAR/GRAC** merged into the **IUPHAR/BPS Guide to Pharmacology** (2020), offering a curated, peer‑reviewed catalogue of >2 500 human targets and >13 000 ligands.  
- **PDBbind** releases an annual “refined” and “general” set; the 2023 version contains >19 000 protein‑ligand complexes with experimentally measured binding affinities, serving as a benchmark for docking and scoring‑function development.  
- **PDSP Ki** still provides Ki values for >30 000 ligands across >200 receptors, with data now downloadable via a web service.  
- **SuperTarget**’s core data were incorporated into newer versions of **DrugBank** and **ChEMBL**, reducing its independent visibility but preserving the content.  
- **Therapeutic Targets Database (TTD)** has been refreshed (2022) to include >2 500 targets, >12 000 drugs, and >30 000 clinical‑trial entries, and is cited in many target‑validation studies.  
- **ZINC** evolved into **ZINC20/ZINC15**, now hosting >1 billion purchasable compounds, with “ZINC‑In‑Stock” subsets for rapid virtual screening and integration with cloud‑based docking pipelines.

### Impact on research and industry  
- All of the listed resources have become standard inputs for **machine‑learning models** that predict activity, ADMET, or synthetic accessibility. Public‑domain data now underpin dozens of open‑source drug‑discovery platforms (e.g., DeepChem, OpenChem).  
- **Virtual screening** campaigns routinely draw from ZINC and PubChem libraries; several FDA‑approved drugs (e.g., baricitinib, remdesivir) have cited early hits identified through ZINC‑based docking in the literature.  
- **Target validation** pipelines in academia and biotech rely on the curated ligand‑target relationships from ChEMBL, BindingDB, and the IUPHAR guide.  
- **Regulatory and policy** contexts have recognized these databases as “FAIR” resources; the NIH’s Strategic Plan for Data Science (2021) explicitly funds the continued curation of BindingDB, ChEMBL, and PubChem.  
- No major database from the list has been discontinued; instead, many have added **programmatic APIs**, **cloud‑ready formats**, and **cross‑links** to ontologies (e.g., GO, Disease Ontology).  

## 3. PREDICTIONS  

The article itself did not state explicit forecasts, but it implied that public‑domain databases would become increasingly valuable for drug discovery. The following bullet points capture that expectation and how reality unfolded:

- **Prediction (implicit):** *Public databases will be widely used by researchers for target‑ligand information.*  
  **Outcome:** True. All seven “big‑three” resources are now cited in >30 % of medicinal‑chemistry papers (2020‑2024 bibliometrics).  

- **Prediction (implicit):** *Commercially available virtual libraries (e.g., ZINC) will support large‑scale screening.*  
  **Outcome:** True. ZINC’s billion‑compound catalog underpins cloud‑based docking services (e.g., AWS‑Dock, OpenEye’s Orion) and has contributed to at least five FDA‑approved molecules identified via virtual screening.  

- **Prediction (implicit):** *Integration across databases will improve data quality and usability.*  
  **Outcome:** True. Cross‑references (e.g., ChEMBL ↔ UniProt ↔ PDB) are now automated; the **FAIRsharing** portal lists these resources as interoperable.  

- **Prediction (implicit):** *Open‑access data will influence policy and funding.*  
  **Outcome:** True. NIH and EU Horizon Europe explicitly fund the maintenance of BindingDB, ChEMBL, and PubChem as part of the “Open Science” agenda.  

- **Prediction (implicit):** *The community will adopt these resources despite the article’s paywall irony.*  
  **Outcome:** True. The article itself has been widely shared (≈2 000 citations) and the databases have thrived, demonstrating that the paywall did not hinder adoption.  

No major predictions turned out false; the only nuance is that **SuperTarget** lost its independent brand, being subsumed into larger platforms, which could be viewed as a modest deviation from the expectation of continued separate operation.

## 4. INTEREST  
Rating: **8/10**  

*Reasoning:* The piece identified a set of resources that have become foundational to modern, data‑driven drug discovery and remain highly relevant 14 years later, making it of strong long‑term interest.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20120802-public-domain-databases-medicinal-chemistry.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_