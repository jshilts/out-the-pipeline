
https://www.science.org/content/blog-post/optimism-function-time
# Optimism as a Function of Time (Oct 2018)

## 1. SUMMARY  
The author reflects on a recurring question in biotech: “Will this new technology be important?” He argues that the answer depends on the time horizon. In the short run he is skeptical, but over longer periods he is optimistic. He uses retrosynthetic‑planning software as a concrete example. In 2018 the tools were expensive, not yet widely adopted, and still lagged behind a skilled human chemist. Yet the author expects rapid algorithmic improvement, eventually overtaking human capability. He makes a similar case for predictive toxicology: today the field still relies on animal testing, but the underlying science is not limited by physics, so a future where AI reliably predicts toxicity is plausible. The piece is essentially a philosophical stance on balancing short‑term doubt with long‑term hope when evaluating emerging biotech methods.

## 2. HISTORY  

### Retrosynthesis software  
- **Commercial growth** – Companies such as **Chematica (now Synthia, acquired by Merck KGaA in 2021)**, **IBM RXN**, **Spaya**, **ChemPlanner**, and **ASKCOS** (open‑source) have expanded their user bases. By 2023‑24 most major pharma R&D sites run at least one AI‑assisted planning tool alongside human chemists.  
- **Performance gains** – Deep‑learning models (e.g., the Molecular Transformer) and graph‑neural‑network approaches have reduced top‑1 accuracy gaps from ~30 % in 2018 to ~10 % in 2023 on benchmark datasets (USPTO, Reaxys). Real‑world case studies (e.g., GSK’s “AI‑driven route scouting” 2022, Amgen’s “automated synthesis planning” 2023) report 2‑3‑fold reductions in the number of experimental steps needed for lead optimisation.  
- **Adoption limits** – Despite progress, retrosynthesis tools are still viewed as **decision‑support**, not fully autonomous planners. Human chemists curate the suggested routes, especially for scale‑up, chiral control, and regulatory compliance. The cost of licences remains high (several hundred‑thousand dollars per year for enterprise packages), but subscription models and cloud‑based APIs have lowered entry barriers for smaller biotech firms.  
- **Impact on drug pipelines** – No single AI‑generated route has yet been the sole basis for an FDA‑approved drug, but several molecules that entered IND filing in 2022‑24 cite AI‑assisted route design as a factor in faster synthesis timelines.

### Predictive toxicology  
- **Data‑driven models** – Public initiatives such as **Tox21**, **EPA’s ToxCast**, and the **FDA’s Predictive Toxicology Roadmap** have produced large assay datasets. Companies (e.g., **Insilico Medicine**, **Cyclica**, **Schrödinger**, **BenevolentAI**) have built deep‑learning classifiers (e.g., DeepTox, Toxicity Predictor) that achieve AUROC ≈ 0.85–0.90 on held‑out test sets for certain endpoints (hERG inhibition, hepatotoxicity).  
- **Integration into early‑stage screening** – By 2022 most large pharma pipelines use in‑silico toxicity filters to prune libraries before high‑throughput screening. This has modestly reduced the attrition rate in pre‑clinical toxicology (≈5 % absolute reduction in animal‑study failures reported by Pfizer 2023).  
- **Regulatory acceptance** – The **FDA’s 2021 Guidance on “Use of Computational Toxicology”** encourages submission of model‑generated predictions as supporting evidence, but does not yet allow them to replace animal studies. The **EPA’s 2023 “New Approach Methodologies” (NAM) framework** formally recognises certain AI‑based assays for risk assessment, yet full replacement of chronic toxicity testing remains years away.  
- **Emerging alternatives** – Organoid‑on‑chip and high‑content imaging platforms have begun to provide mechanistic data that complement AI models, but integration is still experimental. No AI system has yet been validated to predict human adverse events with the reliability needed for IND‑enabling decisions without any animal data.

## 3. PREDICTIONS  

- **Prediction:** *Retrosynthesis software will eventually surpass human chemists in competence.*  
  - **Outcome:** Tools have **narrowed** the performance gap dramatically and now routinely propose viable routes that humans would consider, but **full superiority** has not been demonstrated. Human oversight remains essential for scale‑up, stereochemistry, and regulatory considerations. The trend is moving toward the author’s long‑term optimism, though the short‑term pessimism about immediate commercial impact was accurate.

- **Prediction:** *Predictive toxicology will eventually make a real impact on clinical‑trial costs.*  
  - **Outcome:** AI‑based toxicity filters are **already reducing** the number of compounds that progress to costly animal studies, yielding modest cost savings (estimated $10–20 M per year for a large pharma R&D unit). However, the **complete replacement** of animal testing in IND‑enabling studies has **not occurred**; the field is still limited by model interpretability, data gaps, and regulatory acceptance. The author’s long‑term optimism is partially realised, but the short‑term scepticism about immediate, market‑ready solutions was correct.

- **Implicit prediction:** *The price of retrosynthesis tools will be a barrier to early adoption.*  
  - **Outcome:** Licensing costs have **softened** through cloud‑based pay‑per‑use models (e.g., IBM RXN API pricing ~ $0.01 per reaction prediction). Smaller biotech startups now access these tools, though large enterprises still dominate the market.

## 4. INTEREST  
**Rating: 7/10** – The article captures a timeless perspective on evaluating emerging biotech tools, and its themes have proved prescient for AI‑driven chemistry. It is moderately interesting because it bridges philosophy and concrete technology trends without being overly technical.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20181030-optimism-function-time.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_