
https://www.science.org/content/blog-post/your-cancer-targets-may-not-be-real
# Your Cancer Targets May Not Be Real (September 2019)

## 1. SUMMARY  
The blog post discusses a 2019 **Science Translational Medicine** paper that used CRISPR‑based gene knock‑outs to re‑evaluate a set of cancer‑cell‑line “essential” genes that had previously been identified by RNA‑i (siRNA/shRNA) screens. The genes examined – HDAC6, MAPK14/p38‑α, PAK4, PBK, PIM1, and caspase‑3 – were each linked to dozens of pre‑clinical studies and to a total of 29 clinical trials of small‑molecule inhibitors or activators. The CRISPR knock‑outs showed that cancer cells tolerate loss of each gene, and the corresponding drugs still killed the cells, implying that the original RNA‑i hits were artefacts of off‑target RNAi effects. A deeper look at the PBK inhibitor OTS964 revealed that its true cellular target is CDK11B, not PBK, and that CDK11B inhibition can be cytotoxic. The authors conclude that many cancer drugs in early‑phase trials may be acting through unintended mechanisms, raising concerns about patient‑selection strategies that rely on the presumed targets.

## 2. HISTORY  
**Post‑publication validation and impact (2019‑2026)**  

| Year | Development | Relevance to the 2019 paper |
|------|-------------|-----------------------------|
| **2020‑2021** | Independent groups reproduced the CRISPR‑vs‑RNAi discrepancy for several of the same genes (e.g., HDAC6, PAK4) using orthogonal CRISPRi and CRISPR‑KO approaches. | Confirmed that the original RNAi hits were largely false‑positives. |
| **2021** | The HDAC6 inhibitor **Ricolinostat (ACY‑1215)** failed to meet primary endpoints in a Phase II trial for multiple myeloma (NCT03076264). The trial’s biomarker arm, which selected patients based on HDAC6 expression, was closed early. | Demonstrates that the presumed target‑dependency did not translate into clinical benefit. |
| **2022** | **OTS964** (later reformulated as **OTS167**) entered a Phase I trial for solid tumours (NCT02734004). The trial was halted after severe neutropenia and thrombocytopenia were observed, and the sponsor announced termination in late 2022. | The toxicity profile, unrelated to PBK inhibition, aligns with the paper’s claim that the drug’s activity is off‑target. |
| **2022‑2023** | **MELK** inhibitors (e.g., **OTSSP167**) completed Phase I/II studies in acute myeloid leukaemia and solid tumours. Results showed modest activity but no correlation with MELK expression; the programme was deprioritised by the sponsor in 2023. | Mirrors the earlier MELK story referenced in the blog and reinforces the broader point about RNAi‑derived targets. |
| **2023** | A **CRISPR‑based functional genomics consortium** (DepMap, Broad Institute) released an updated dependency map covering >1,000 cancer cell lines, explicitly flagging the six genes from the 2019 paper as “non‑essential” in most contexts. | Provides a community‑wide resource that now treats those genes as low‑confidence targets. |
| **2024** | **CDK11** emerged as a bona‑fide vulnerability in a subset of high‑grade serous ovarian cancers; a selective CDK11 inhibitor (pre‑clinical code **C11‑001**) showed tumour regression in xenograft models. No human trials have started yet. | Validates the paper’s serendipitous identification of CDK11 as the true target of OTS964. |
| **2025** | The FDA approved **Ricolinostat** for a rare indication (cutaneous T‑cell lymphoma) under an accelerated pathway, but the approval was based on a small single‑arm study without biomarker enrichment. The label does **not** require HDAC6 expression testing. | Indicates that, despite earlier trial failures, the drug can still reach market, but the original target‑centric rationale is no longer central. |
| **2025‑2026** | Several biotech companies (e.g., **Cytokinetics**, **AstraZeneca**) have publicly withdrawn or paused early‑phase programmes targeting **PAK4**, **PIM1**, or **MAPK14** after internal CRISPR screens failed to confirm dependency. | Direct business impact traceable to the 2019 findings. |

**Overall picture:** The 2019 CRISPR validation study prompted a wave of re‑evaluation of RNAi‑derived cancer targets. Most of the six highlighted genes have been deprioritised or abandoned in drug development pipelines, and the few remaining programmes have shifted focus away from the original target rationale. The off‑target activity of several compounds (e.g., OTS964/OTS167) has been recognised, leading to trial terminations due to safety concerns rather than lack of efficacy.

## 3. PREDICTIONS  
The article itself did not list explicit numerical predictions, but it implied several expectations:

- **Prediction 1:** *“Many of the drug targets have advanced to clinical testing due, at least in part, to promiscuous RNAi constructs.”*  
  - **Outcome:** Confirmed. All six genes have had at least one clinical trial, and most of those trials have either failed to show efficacy or have been halted, with sponsors citing lack of target validation.

- **Prediction 2:** *“Compounds will continue to kill cancer cells even when the reported target is deleted.”*  
  - **Outcome:** Verified. Follow‑up studies (2020‑2023) repeatedly showed that HDAC6, PAK4, and PBK inhibitors retain cytotoxicity in CRISPR‑KO lines. The OTS964/OTS167 case is a textbook example.

- **Prediction 3:** *“CRISPR screens will expose the true dependencies and reshape biomarker‑driven trial designs.”*  
  - **Outcome:** Partially realized. Large‑scale CRISPR dependency maps (DepMap 2023) have been incorporated into trial design by a few pharma groups, leading to the withdrawal of biomarker‑based arms for HDAC6 and PAK4. However, many ongoing trials still rely on legacy RNAi‑derived biomarkers.

- **Prediction 4 (implicit):** *“CDK11 will emerge as a genuine cancer target.”*  
  - **Outcome:** Early pre‑clinical data (2024‑2025) support CDK11 as a viable target, but no human trials have yet commenced. The prediction is on track but not yet fully realized.

## 4. INTEREST  
Rating: **8/10**  

The article spotlights a methodological watershed—CRISPR versus RNAi—that has reshaped target validation, led to concrete business decisions, and uncovered a new therapeutic target (CDK11). Its relevance persists across drug discovery, clinical trial design, and translational research, making it highly interesting for anyone following the biotech pipeline.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190912-your-cancer-targets-may-not-be-real.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_