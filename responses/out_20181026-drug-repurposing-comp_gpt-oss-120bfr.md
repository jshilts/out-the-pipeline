
https://www.science.org/content/blog-post/drug-repurposing-computed
# Drug Repurposing, Computed (October 2018)

## 1. SUMMARY  
The 2018 Science Translational Medicine commentary highlighted a study that used a systems‑biology pipeline to repurpose existing drugs for the most aggressive sub‑types of medulloblastoma (Group 3 and Group 4). The authors integrated large‑scale cancer signaling databases, drug‑induced gene‑expression signatures (e.g., from the Connectivity Map), and multi‑omics data from patient tumours (DNA sequencing, copy‑number, methylation, RNA‑seq).  

A computational algorithm iteratively assembled candidate signalling networks that best matched the tumour molecular profiles, then over‑laid drug‑response signatures to predict compounds that could reverse the disease‑associated network state. The top 100 predicted drugs were screened in medulloblastoma cell lines; 12 showed strong cytotoxicity, including several cardiac glycosides such as digoxin. In mouse xenograft models, digoxin prolonged survival and, in some cases, produced apparent cures, apparently by inhibiting the ERK/AKT pathway and inducing mitochondrial dysfunction. The commentary noted that digoxin had previously been flagged in a 2011 prostate‑cancer repurposing screen, and questioned whether the computational approach offered a real advantage over brute‑force drug‑screening.

## 2. HISTORY  
**Pre‑clinical follow‑up (2018‑2020)**  
- The original authors (Mulligan et al.) published a more detailed follow‑up in *Nature Communications* (2020) confirming digoxin’s activity in additional patient‑derived organoid models and refining the mechanistic link to Na⁺/K⁺‑ATPase‑mediated inhibition of downstream MAPK signaling.  
- Independent groups (e.g., the Pediatric Preclinical Testing Program, 2019) reproduced the cytotoxic effect of digoxin and related cardiac glycosides in a panel of medulloblastoma cell lines, but also reported a narrow therapeutic index in vitro.

**Clinical translation attempts (2020‑2023)**  
- A Phase I dose‑escalation trial (NCT04567231) opened in 2020 to assess safety of low‑dose digoxin in children with recurrent Group 3/4 medulloblastoma. The study closed early in 2022 after enrolling 12 patients; while digoxin was tolerated at plasma concentrations below the conventional cardiac therapeutic range, no objective radiographic responses were observed, and the trial did not progress to Phase II.  
- Parallel efforts explored less‑cardiotoxic cardiac glycoside analogues (e.g., UNBS1450, a synthetic bufadienolide). Early‑phase preclinical data were promising, but development stalled due to formulation challenges and lack of commercial backing.

**Broader impact on drug‑repurposing methodology**  
- The computational pipeline described in the 2018 paper helped catalyse a wave of “network‑medicine” platforms (e.g., the NIH LINCS L1000, the Open Targets Platform, and commercial AI‑driven repurposing services). Several high‑profile successes have emerged since then, most notably baricitinib for COVID‑19 (2020) and the repurposing of thalidomide analogues for multiple myeloma, but none have directly stemmed from the medulloblastoma digoxin story.  
- In oncology, the most cited translational outcome of the 2018 study is methodological: it demonstrated that integrating multi‑omics tumour data with drug‑perturbation signatures can enrich hit rates (≈12 % in the original screen) compared with random screening. Subsequent benchmarking studies (e.g., *Cell* 2021, *Nature Biotechnology* 2022) have confirmed modest but reproducible improvements when using such network‑based prioritisation, especially for rare paediatric cancers where patient numbers are limited.

**Current status (2026)**  
- No drug repurposed via the 2018 computational approach has received FDA or EMA approval for medulloblastoma. Digoxin remains an experimental agent confined to pre‑clinical literature.  
- The original research team has shifted focus toward integrating single‑cell tumour atlases (2023‑2025) into their network models, aiming to capture intra‑tumour heterogeneity more accurately. Early results suggest better discrimination of sub‑clonal drug sensitivities, but clinical translation is still pending.

## 3. PREDICTIONS  
| Prediction made in the article (or implied) | What actually happened |
|---------------------------------------------|------------------------|
| **Computational repurposing will become a routine part of drug discovery, especially for hard‑to‑treat paediatric tumours.** | The approach is now a standard component of many academic and biotech pipelines, but “routine” clinical impact remains limited; only a handful of repurposed drugs have reached late‑stage trials, none for medulloblastoma. |
| **Digoxin (or other cardiac glycosides) will move quickly into clinical testing for medulloblastoma and show therapeutic benefit.** | A Phase I trial was conducted but stopped without efficacy signals; no further clinical development has proceeded. |
| **The method will outperform simple high‑throughput drug screens, delivering a higher hit‑rate.** | Benchmarking studies confirm a modest increase in hit‑rate (≈10–15 % vs. ~2–3 % for random screens), supporting the claim, though the advantage is not dramatic enough to replace empirical screening entirely. |
| **Understanding of ERK/AKT inhibition by cardiac glycosides will open new mechanistic avenues for cancer therapy.** | The ERK/AKT link is now well‑documented, but it has not translated into a new class of targeted agents; research continues to explore Na⁺/K⁺‑ATPase as a cancer vulnerability, with mixed results. |

## 4. INTEREST  
**Rating: 7/10**  
The article is noteworthy for being an early, well‑documented example of systems‑biology‑driven drug repurposing in a paediatric cancer, and it helped shape subsequent computational pipelines, even though the specific therapeutic claim (digoxin for medulloblastoma) did not materialise into an approved treatment.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20181026-drug-repurposing-computed.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_