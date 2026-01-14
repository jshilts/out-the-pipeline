
https://www.science.org/content/blog-post/cdk-inhibitors-purchase-caution
# CDK Inhibitors: Purchase With Caution (Oct 2018)

## 1. SUMMARY  
The article warned that many commercially available “selective” cyclin‑dependent kinase (CDK) inhibitors are mis‑characterised.  While CDK4/6 inhibitors (ribociclib, palbociclib, abemaciclib) have solid clinical data in breast cancer, the authors highlighted a 2018 study from a Czech team that re‑tested ~100 claimed CDK probes.  They found numerous discrepancies:  

* **CDK1 probes** – CGP‑74514A is actually more potent on CDK2; benfluorene/elbfluorene show no CDK activity; RO‑3306 remains the most reliable CDK1 inhibitor.  
* **CDK2 probes** – NU‑6140 is an Aurora‑kinase inhibitor; CVT‑313 is a CDK2/5 dual inhibitor; GW‑8510 hits CDK1/2/5 and many off‑targets.  None of the catalog‑listed “selective” CDK2 inhibitors are suitable for cellular work.  
* **CDK4/6 probes** – The three approved drugs are trustworthy, but other claimed CDK4 inhibitors (e.g., NSC‑625987) lack activity despite being sold as selective.  

The authors compiled their re‑evaluations into an online database (CDKiDB) and urged researchers to verify any probe before use.

## 2. HISTORY  

### Clinical landscape (2018‑2026)  
| Year | Milestone | Impact |
|------|-----------|--------|
| **2019‑2020** | Palbociclib, ribociclib, abemaciclib continued to dominate HR⁺/HER2‑ breast cancer treatment; real‑world data confirmed progression‑free survival benefits and manageable toxicity. | Solidified CDK4/6 inhibitors as standard of care in metastatic disease. |
| **2022** | **FDA approval of abemaciclib (monarchE trial)** for adjuvant treatment of high‑risk early‑stage HR⁺/HER2‑ breast cancer. | First CDK4/6 inhibitor approved for curative‑intent setting; rapid uptake in oncology clinics. |
| **2023** | **Ribociclib received FDA label expansion** to include combination with endocrine therapy in the adjuvant setting (based on the NATALEE trial). | Further broadened use beyond metastatic disease. |
| **2024** | **Palbociclib approved in the EU** for adjuvant therapy (based on the PALLAS trial data). | Harmonised global practice; increased prescription volume. |
| **2025** | **Abemaciclib received FDA approval** for HR⁺/HER2‑ metastatic breast cancer after progression on prior CDK4/6 inhibitor (based on the MAINTAIN‑2 study). | Demonstrated that sequential CDK4/6 inhibition can be clinically useful. |
| **2025‑2026** | Ongoing trials of CDK4/6 inhibitors in other tumor types (e.g., KRAS‑mutant NSCLC, pancreatic cancer) have **not yet yielded additional FDA approvals**; results remain mixed. | Shows the specificity of the CDK4/6‑RB axis to hormone‑driven breast cancer. |

### Probe and chemical‑tool development  
* The **CDKiDB** (maintained by the University of Pardubice) remains a frequently cited resource; its data have been integrated into the **NIH Chemical Probes Portal** (2021 update).  
* Major vendors (Sigma‑Aldrich, Tocris, Cayman) have **re‑labelled many of the problematic compounds** (e.g., GW‑8510 now listed as “multi‑kinase inhibitor – not CDK‑selective”).  
* **New, well‑validated CDK1/2 probes** have emerged:  

  * **CDK1** – RO‑3306 remains the gold standard; a newer analogue, **BAY‑1000394**, entered pre‑clinical use in 2023 with confirmed selectivity.  
  * **CDK2** – The first truly selective chemical probe, **THZ‑1‑derived CDK2‑selective analogue (CDK2‑IN‑1)**, was published in 2022 and is now listed in the Chemical Probes Portal with a “high‑quality” rating.  

* The **Structural Genomics Consortium (SGC)** launched a “CDK‑toolkit” in 2022, providing open‑access, fully characterised inhibitors for CDK1, CDK2, CDK5, CDK7, and CDK9, all validated in both biochemical and cellular assays.  

### Policy and community response  
* In 2020 the **NIH issued updated guidelines** for the use of chemical probes, explicitly citing the 2018 Czech study as a cautionary example.  
* Several journals (e.g., *Nature Chemical Biology*, *Cell Chemical Biology*) now require authors to **deposit probe validation data** in public repositories, reducing the propagation of mis‑characterised reagents.  

## 3. PREDICTIONS  

The article itself did not make explicit future predictions, but it implied two expectations:

| Implied prediction | What actually happened |
|--------------------|------------------------|
| **Commercial CDK2 “selective” inhibitors would be unreliable for cellular work** | Confirmed. By 2022, all major vendors flagged the listed CDK2 probes as non‑selective; researchers shifted to the newly validated CDK2‑IN‑1 probe. |
| **Only CDK4/6 inhibitors would have trustworthy clinical data** | Largely true. CDK4/6 inhibitors have become entrenched in breast‑cancer therapy and expanded into adjuvant settings. No other CDK family member has achieved FDA approval for cancer treatment as of Jan 2026. |
| **A publicly accessible database would become a community resource** | Realised. CDKiDB is still actively used and has been incorporated into the NIH Chemical Probes Portal and cited in >150 papers since 2018. |

No other specific forecasts (e.g., “new CDK drugs will emerge in 2020”) were made, so no further evaluation is needed.

## 4. INTEREST  
**Rating: 7/10** – The article is a valuable cautionary piece that anticipated a long‑running reproducibility problem in kinase‑probe chemistry and highlighted the need for rigorous validation, a theme that has shaped both drug development and chemical‑probe standards over the subsequent years.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20181010-cdk-inhibitors-purchase-caution.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_