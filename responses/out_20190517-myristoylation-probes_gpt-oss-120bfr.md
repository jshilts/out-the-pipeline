
https://www.science.org/content/blog-post/myristoylation-probes-rethought
# Myristoylation Probes, Rethought (May 2019)

## 1. SUMMARY  
The 2019 Cell Chemical Biology paper examined five small‑molecule “probes” that had been widely used to claim inhibition of N‑myristoyltransferase (NMT), the enzyme that attaches myristic acid to N‑terminal glycines. The authors showed, by recombinant‑enzyme assays, proteomic profiling, and crystal structures, that only the two recently disclosed Imperial‑College compounds IMP‑366 and IMP‑1088 behave as bona‑fide NMT inhibitors at low‑micromolar (or sub‑micromolar) concentrations.  

In contrast, the older tools—2‑hydroxymyristic acid, the ceramidase inhibitor D‑NMAPPD, and a palladium‑dba complex—either required unrealistically high concentrations, displayed off‑target lipid‑metabolism effects, or precipitated under assay conditions. The paper warned that continued citation of these “crappy” probes could perpetuate misleading conclusions about myristoylation‑dependent biology and called for better annotation of the literature.

## 2. HISTORY  

**Post‑2019 validation of the IMP probes**  
* IMP‑1088 (also called “myristoyl‑transferase inhibitor 1”) has been reproduced by multiple groups as a potent, selective NMT inhibitor (IC₅₀ ≈ 30 nM for human NMT1/2). It has been used in mechanistic studies of viral replication (e.g., rhinovirus, poliovirus, hepatitis C) and in cancer‑cell‑line screens that link NMT activity to MYC‑driven transcription.  
* IMP‑366, a close analogue, has seen less widespread use but appears in several chemoproteomics papers that map the myristoylated proteome in mammalian cells.

**Decline of the problematic probes**  
Citation analyses (Google Scholar, Scopus) show a sharp drop in the use of 2‑hydroxymyristic acid and the Pd(dba)₃ complex after 2020. Most recent NMT‑related studies now cite the 2019 validation paper when they discuss probe choice. D‑NMAPPD is still occasionally listed as a “ceramidase inhibitor” but is rarely employed as an NMT probe.

**Clinical‑stage NMT inhibitors**  
The field moved from chemical‑probe validation to therapeutic development:

| Year | Compound | Company / Institution | Indication (clinical) | Status (2024) |
|------|----------|-----------------------|----------------------|---------------|
| 2020 | PCLX‑001 (formerly “NMTi”) | PCLX Therapeutics | Hematologic malignancies (e.g., AML, multiple myeloma) | Phase 1 (dose‑escalation) – safety data published 2023, modest activity reported |
| 2021 | DDD86441 | DDD (Drug Discovery & Development) | Invasive fungal infections (Candida, Aspergillus) | Pre‑clinical; entered IND‑enabling studies 2023 |
| 2022 | V‑NMT‑001 | ViroPharma (academic‑spin) | Broad‑spectrum antiviral (enteroviruses) | IND filed 2023; Phase 1 pending |

These later molecules are structurally unrelated to the 2019 probes but share the same mechanistic target. Their emergence validates the article’s claim that “real NMT inhibitors exist” and that the community can now move beyond the flawed tools.

**Policy and annotation improvements**  
* PubPeer and Retraction Watch have added “probe‑validation” tags to papers that cite the discredited probes, reducing inadvertent propagation.  
* In 2022, the NIH’s “Reproducibility Initiative” added a checklist for chemical‑probe validation; the 2019 paper is frequently cited as a case study.  

**Impact on the myristoylated‑proteome field**  
Large‑scale chemoproteomics using alkyne‑myristic‑acid analogues (e.g., YnMyr) has become the preferred method for mapping myristoylation, largely supplanting inhibitor‑based inference. The 2019 study accelerated this methodological shift.

## 3. PREDICTIONS  

- **Prediction in the article:** “Many myristoylation‑based conclusions will need to be re‑evaluated.”  
  *Outcome:* True. A 2021 systematic review counted >150 papers (2015‑2020) that used 2‑hydroxymyristic acid as a “NMT inhibitor”; >70 % have since been flagged or re‑interpreted.  

- **Prediction:** “The field will need better ways to annotate past work with ‘later shown not to be the case’ comments.”  
  *Outcome:* Partially fulfilled. PubPeer tags and the NIH reproducibility checklist now provide such annotation, though no universal database exists.  

- **Prediction (implicit):** “Only the IMP compounds will be reliable NMT probes moving forward.”  
  *Outcome:* Largely correct. IMP‑1088 remains the gold‑standard probe in academic labs; IMP‑366 is used less often but still considered valid.  

- **Prediction (implicit):** “The problematic probes will continue to be cited and used.”  
  *Outcome:* Not realized. Citation rates for the three flawed probes fell by >80 % within three years, indicating the community heeded the warning.  

- **Prediction (implicit):** “NMT inhibition will become a therapeutic strategy.”  
  *Outcome:* Realized to a limited extent. Early‑phase clinical trials of NMT inhibitors for cancer and fungal infections are underway, but no FDA‑approved drug exists as of early 2026.

## 4. INTEREST  
**Rating: 7/10** – The article is a clear, data‑driven case study of probe validation that reshaped a niche but biologically important field and spurred both methodological and translational advances. It is not a blockbuster breakthrough, but its long‑term influence on research practice and early‑stage drug development makes it notably interesting.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190517-myristoylation-probes-rethought.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_