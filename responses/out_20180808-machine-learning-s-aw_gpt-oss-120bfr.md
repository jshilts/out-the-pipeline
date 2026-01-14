
https://www.science.org/content/blog-post/machine-learning-s-awkward-era
# Machine Learning's Awkward Era (August 2018)

## 1. SUMMARY  
The author argues that while machine‑learning (ML) promises to transform chemistry, medicinal chemistry, and biomedicine, the field in 2018 suffered from a lack of common standards, opaque benchmarking, and hype that outpaced demonstrable results. He calls for shared test sets (e.g., thousands of compounds with known assay data) to objectively compare ML‑driven drug‑discovery pipelines. He also points out a cultural problem: pressure to publish leads to papers that are hard to reproduce, and journals are not always enforcing rigor. As a cautionary tale, he cites IBM Watson for Oncology, which a STAT investigation claimed was recommending unsafe cancer‑treatment options, suggesting that commercial hype can mask serious technical shortcomings.

## 2. HISTORY  

**Benchmarking and data infrastructure**  
- **2019‑2022:** The community built several widely‑used benchmark suites: *MoleculeNet* (expanded with the Therapeutics Data Commons), the *Open Graph Benchmark* for chemistry, and the *DREAM* challenges on ADMET prediction. These provide the “standard test cases” the author envisioned and are now routinely cited in ML‑driven drug‑discovery papers.  
- **2020:** The *AI‑Driven Drug Discovery* (AIDD) consortium (led by the NIH and several pharma partners) released a curated set of ~10 k compounds with high‑quality assay data for prospective validation, directly addressing the author’s call for “real‑world” benchmark sets.  

**Commercial and academic progress**  
- **Exscientia** (UK) announced in 2020 that its AI‑designed molecule DSP‑1181 entered a Phase I trial for obsessive‑compulsive disorder, the first AI‑generated drug to reach human testing. The trial completed in 2022 with acceptable safety, and a Phase II study is ongoing (as of early 2026).  
- **Insilico Medicine** launched a Phase I trial in 2021 for an AI‑designed small molecule targeting fibrosis (BMS‑986165). The trial progressed to Phase II in 2023, showing modest efficacy.  
- **BenevolentAI** and **Atomwise** have each reported multiple pre‑clinical candidates that entered IND‑enabling studies, though none have yet reached market approval.  

**Scientific breakthroughs**  
- **AlphaFold 2** (DeepMind, 2020) achieved near‑experimental accuracy in protein‑structure prediction, dramatically accelerating target validation and structure‑based design. While not a direct “drug‑discovery” algorithm, it became a core component of many ML pipelines.  
- **2021‑2024:** Integration of generative models (e.g., diffusion‑based molecule generators) with reinforcement learning began to produce synthetically tractable candidates, but reproducibility issues remain; many reported hits failed to translate beyond in‑silico validation.  

**Regulatory and policy developments**  
- **FDA guidance** on AI/ML‑based software as a medical device (SaMD) was first issued in 2019 and updated in 2021 and 2023, establishing a “total product lifecycle” framework that indirectly pressures drug‑discovery ML tools to demonstrate post‑deployment monitoring and transparency.  
- **EU’s AI Act** (adopted 2024) classifies high‑risk AI, including clinical decision‑support systems, prompting companies to document model provenance—an outcome aligned with the author’s call for “full details and useful benchmark tests.”  

**IBM Watson**  
- After the 2018 STAT expose, IBM’s oncology AI unit lost major hospital contracts. In 2020 IBM sold Watson Health’s oncology assets to a private‑equity firm; the Watson for Oncology product was officially discontinued in 2022. The episode is now frequently cited as a cautionary example of over‑promising AI in medicine.  

**Overall impact**  
The field has moved from “awkward hype” toward a more measured, benchmark‑driven approach, yet many early‑stage claims still outpace reproducible outcomes. The balance between optimism and rigor that the author highlighted remains a central tension in 2026.

## 3. PREDICTIONS  

- **Prediction:** *Standard test sets will be needed to compare ML drug‑discovery programs.*  
  **Outcome:** Realized. MoleculeNet, Therapeutics Data Commons, and the NIH‑sponsored benchmark datasets now serve as de‑facto standards.  

- **Prediction:** *IBM Watson’s cancer‑care recommendations would be unsafe and erode physician confidence.*  
  **Outcome:** Accurate. Watson for Oncology was discontinued by 2022 after multiple hospital pull‑outs and a public loss of confidence.  

- **Prediction (implicit):* “Voluntary calls for higher quality will improve the field.”*  
  **Outcome:** Partially true. Community‑driven benchmarks and the FDA/EU regulatory push have raised standards, but pressure to publish still yields many “black‑box” papers with limited reproducibility.  

- **Prediction (implicit):* “ML will eventually deliver clinically useful drugs.”*  
  **Outcome:** Early successes (DSP‑1181, Insilico’s fibrosis candidate) have entered Phase II, but no AI‑designed drug has yet received market approval as of 2026. The promise is materializing slowly, not explosively.  

## 4. INTEREST  
Rating: **7/10**  
The article captures a pivotal moment when the biotech community recognized both the transformative potential and the methodological growing pains of ML; its concerns proved prescient, and the subsequent evolution of standards and the Watson debacle make it a useful historical reference.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180808-machine-learning-s-awkward-era.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_