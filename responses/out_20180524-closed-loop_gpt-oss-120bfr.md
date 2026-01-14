
https://www.science.org/content/blog-post/closed-loop
# A Closed Loop (May 2018)

## 1. SUMMARY  
The commentary discusses a 2017 J. Med. Chem. paper describing a “closed‑loop” workflow for medicinal‑chemistry optimisation of hepsin inhibitors.  A team from the University of Helsinki, LifeArc and the startup Cyclofluidic built a flow‑reactor platform that could (i) synthesize amide‑ and sulfonamide‑containing analogues on‑demand, (ii) purify them inline, (iii) assay the compounds against hepsin (and a counter‑screen on urokinase), and (iv) feed the assay data back into software that suggested the next set of building blocks.  In practice the system generated 142 compounds over several days, culminating in a 22 nM hepsin inhibitor that was ~200‑fold selective versus urokinase.  The author, Derek Lowe, stresses that human chemists still guided the SAR space and interpreted the data, but the routine “boring” chemistry was delegated to the automated loop.

## 2. HISTORY  

### Automated “self‑driving” labs  
* **Cyclofluidic** was acquired by **Evotec** in 2020 (announced Oct 2020).  Evotec integrated Cyclofluidic’s flow‑automation and AI‑driven design into its broader drug‑discovery platform, branding it “Evotec Self‑Driving Lab”.  The acquisition confirmed commercial interest but the technology has remained a niche capability rather than a universal replacement for human‑led synthesis.  
* Since 2018, several other companies (e.g., **DeepMatter**, **Synthace**, **IBM RXN**, **Insilico Medicine**) have launched or expanded self‑driving laboratory services.  Academic consortia (e.g., the **DARPA Accelerated Molecular Discovery** program, launched 2020) have funded prototype labs that couple rapid flow synthesis, high‑throughput assays and machine‑learning‑guided design.  These efforts have demonstrated the feasibility of sub‑hour design‑make‑test cycles for simple chemotypes, but scaling to complex, multi‑step routes remains a bottleneck.  

### Hepsin as a therapeutic target  
* No hepsin‑targeting drug has entered Phase III trials or received regulatory approval as of early 2026.  The 22 nM inhibitor described in the 2017 paper has not progressed beyond early‑stage preclinical evaluation; public disclosures from LifeArc and the University of Helsinki show that the series was discontinued around 2020 due to modest in‑vivo efficacy and pharmacokinetic liabilities.  
* Hepsin continues to be investigated as a biomarker and a potential target in prostate and pancreatic cancers, but the field has shifted toward broader protease‑focused programs (e.g., matriptase, TMPRSS2) and toward antibody‑drug conjugates rather than small‑molecule inhibitors.  

### Impact on medicinal‑chemistry practice  
* The “closed‑loop” concept has become a reference point in the literature and is frequently cited in reviews of autonomous chemistry (e.g., Nature Chemistry 2021, Science 2022).  However, most large pharma labs still rely on human‑directed design combined with parallel automated synthesis (e.g., Chemspeed, Synthace).  Full end‑to‑end automation of SAR cycles is still limited to well‑defined chemistry (amide couplings, Suzuki couplings) and to projects where rapid assay read‑outs are available.  
* The workflow highlighted the importance of robust, inline assays.  Since 2018, advances in microfluidic bioassays (e.g., label‑free SPR, real‑time enzymatic read‑outs) have broadened the range of targets that can be screened in a closed loop, but integration remains project‑specific.  

## 3. PREDICTIONS  

| Prediction (from the article or implied) | What actually happened |
|---|---|
| **Automated flow synthesis + AI will replace “boring” amide chemistry, freeing chemists for higher‑level work.** | Partially true.  Flow‑based amide coupling is now routine in many discovery labs, and AI‑suggested building blocks are used to prioritize libraries.  Human chemists still design the overall SAR strategy and intervene when synthesis becomes non‑trivial. |
| **The closed‑loop system could generate a lead series in ~90 min per cycle, accelerating drug discovery timelines.** | Demonstrated in proof‑of‑concept studies (sub‑hour cycles for simple chemotypes).  For more complex series, cycle times are still measured in days because of purification, solubility, and assay setup constraints. |
| **Hepsin inhibitors will move toward clinical development.** | Not realized.  The lead series was discontinued before animal‑model validation; no hepsin‑targeted drug has reached clinical trials as of 2026. |
| **The approach will become widely adopted across the industry.** | Adoption is growing but remains limited to niche projects.  Large pharma has invested in self‑driving labs, yet most discovery programs still use hybrid human‑machine workflows rather than fully autonomous loops. |
| **Machines will “steal” routine chemistry jobs from human chemists.** | The labor market has shifted: routine batch synthesis roles have declined, while demand for chemists who can program, troubleshoot flow systems and interpret AI outputs has increased.  No large‑scale displacement has occurred. |

## 4. INTEREST  
**Rating: 7/10** – The article is a clear early illustration of autonomous medicinal‑chemistry workflows, a theme that has grown into a major research and commercial focus, even though the specific hepsin project did not translate into a drug.  Its relevance to the evolution of self‑driving labs makes it notably interesting.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180524-closed-loop.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_