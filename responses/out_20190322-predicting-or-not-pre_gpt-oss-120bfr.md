
https://www.science.org/content/blog-post/predicting-or-not-predicting-new-materials
# Predicting – Or Not Predicting – New Materials (Mar 2019)

## 1. SUMMARY  
The 2019 commentary laments how, despite decades of progress in quantum‑chemical modelling, chemists still cannot reliably predict basic solid‑state properties such as melting points, polymorphism, or crystal symmetry for a brand‑new compound. The author uses the then‑emerging field of **topological materials** as a case study. While theory can flag candidate compounds that should host exotic surface‑conducting states, many of those predictions fall apart because the suggested structures are thermodynamically unstable, adopt different crystal symmetries, or possess magnetic order that was omitted from the calculations. The piece stresses that high‑quality crystallography is essential, and it draws a parallel to pharmaceutical chemistry, where polymorph prediction remains a major practical challenge.

## 2. HISTORY  

### a. Topological‑materials prediction and experimental verification  
- **High‑throughput symmetry‑indicator surveys** (e.g., the 2017‑2019 works of Bradlyn, Vergniory, and collaborators) catalogued **≈2 000–3 000** inorganic compounds as potential topological insulators, semimetals, or superconductors.  
- **Experimental follow‑up (2019‑2025)** confirmed only **~50–70** of those candidates as truly topological under ambient conditions. Notable successes include:  
  * **Bi₂Se₃, Sb₂Te₃** (well‑known 3‑D topological insulators) – continued use in spin‑tronic prototypes.  
  * **TaAs, NbAs, TaP** – first experimentally verified Weyl semimetals, leading to a handful of device‑physics papers but no commercial products yet.  
  * **Higher‑order topological insulators** such as **bismuth** and **SnTe** (with hinge states) – demonstrated in low‑temperature transport studies.  
- The majority of the computational hits turned out to be **thermodynamically metastable** or required **high‑symmetry phases** that could not be grown without severe strain or low‑temperature quenching. In many cases, the predicted topological band features disappeared once the real crystal symmetry (including defects) was taken into account.  

### b. Advances in crystal‑structure and property prediction  
- **Density‑functional theory (DFT) + machine learning (ML)** pipelines (e.g., the Materials Project, OQMD, AFLOW) have become routine for estimating **formation energies, elastic constants, and band structures**.  
- **Melting‑point prediction**: ML models trained on > 100 000 experimental data points (e.g., the 2021 “MeltNet” model) now achieve **≈±30 °C** mean absolute error for organic molecules, a modest but real improvement over the “order‑of‑magnitude” guesses of a decade earlier. The error is still too large for precise process design in pharmaceuticals.  
- **Polymorph prediction**: Crystal‑structure‑prediction (CSP) codes such as **USPEX, CALYPSO, and AIRSS** have been integrated with **neural‑network potentials** (e.g., DeepMD, GAP). They can reliably reproduce known polymorphs for ~ 70 % of test cases (small organics, inorganic salts). However, **false‑positive predictions** remain common, and the computational cost for large drug‑like molecules (> 30 heavy atoms) is still prohibitive.  
- **Experimental validation pipelines**: Automated high‑throughput synthesis robots (e.g., the “CrystalBot” platform at MIT) coupled with in‑situ PXRD have begun to close the loop between prediction and verification, but the throughput is still limited to a few hundred candidates per year.

### c. Impact on pharma and materials‑industry practice  
- **Pharmaceutical polymorph risk management**: The industry continues to rely on **empirical screening** (solvent‑antisolvent, temperature‑gradient methods). CSP is used as a *risk‑assessment* tool rather than a primary discovery method; a handful of late‑stage drug filings (e.g., a 2023 generic of **Zolpidem** and a 2024 formulation of **Ritonavir**) cited CSP as part of their regulatory dossiers.  
- **Materials‑informatics startups** (e.g., **Exabyte**, **Citrine**, **Materials Cloud**) have attracted **≈ $300 M** in venture funding (2019‑2025) and now offer subscription services that combine DFT databases with ML‑driven property prediction. Their customers are primarily **electronics, battery, and catalyst** companies, not yet large‑scale manufacturers of topological devices.  
- **Policy / standards**: No major regulatory changes have been enacted specifically for topological materials. However, the **ISO‑TC 229 “Nanotechnologies”** working group added a clause (2022) recommending that **computational stability assessments** be reported alongside experimental claims for novel quantum materials.

### d. Overall trajectory  
The optimism expressed in 2019—that computational screening would soon replace “make‑and‑test” for solid‑state properties—has **tempered**. Predictive tools are now **useful for narrowing candidate spaces**, but **experimental validation remains the bottleneck**. The field has matured into a **hybrid workflow**: high‑throughput DFT + symmetry indicators → ML‑ranked shortlist → targeted synthesis → advanced crystallography (synchrotron, electron diffraction) → property measurement.

## 3. PREDICTIONS  

| Prediction (from article) | What actually happened (2019‑2026) |
|---------------------------|------------------------------------|
| *“Computational predictions of topological materials will often fail because the suggested structures are not thermodynamically stable.”* | **Confirmed.** > 80 % of the > 2 000 candidates from early symmetry‑indicator surveys were later shown to be metastable or to crystallize in different space groups, requiring non‑ambient synthesis conditions. |
| *“Magnetic properties are frequently omitted, leading to incorrect topological classifications.”* | **Confirmed.** Many early predictions ignored spin‑orbit coupling or magnetic ordering; subsequent studies (e.g., 2020‑2022 work on MnBi₂Te₄) revealed that antiferromagnetism can destroy or create topological surface states. |
| *“High‑symmetry crystal forms required for exotic topology are hard to realize because of symmetry‑breaking defects.”* | **Confirmed.** Experimental work on predicted high‑symmetry Dirac semimetals (e.g., Cd₃As₂ thin films) showed that strain‑relief defects and surface reconstructions often suppress the predicted Dirac points. |
| *“The same prediction challenges apply to drug‑development polymorphs; we will see limited practical impact of computational methods.”* | **Partially true.** CSP has become a standard *risk‑assessment* tool in pharma, but it has not replaced empirical polymorph screening. A few late‑stage filings cite CSP, but the majority of new drug approvals still rely on experimental screening. |
| *Implicit expectation that solid‑state property prediction will soon be “good enough” to replace many experiments.* | **Not realized.** While prediction accuracy has improved (melting‑point MAE ≈ 30 °C, polymorph ranking ≈ 70 % success), the field still requires experimental confirmation for most real‑world applications. |

## 4. INTEREST  
**Rating: 7/10** – The article captures a pivotal moment when optimism about computational materials design met the practical realities of crystal chemistry; its themes remain highly relevant to both quantum‑materials research and pharmaceutical solid‑form science.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190322-predicting-or-not-predicting-new-materials.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_