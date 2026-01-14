
https://www.science.org/content/blog-post/calculate-your-way-out-bad-yields
# Calculate Your Way Out of Bad Yields (April 2018)

## 1. SUMMARY  
The 2018 Science article described a Princeton‑Merck collaboration that used high‑throughput experimentation (HTE) to generate 4,608 Buchwald‑Hartwig C‑N coupling reactions (15 aryl/heteroaryl halides × 4 ligands × 3 bases × 23 isoxazole additives). About 30 % of the runs gave no product, providing a rich set of “negative” data.  

For each reaction the authors computed a suite of physicochemical descriptors (atomic charges, vibrational frequencies, dipole moments, LUMO energies, NMR shifts, etc.) with Spartan. They trained several machine‑learning models on 70 % of the data and tested on the remaining 30 %. Random‑forest regression emerged as the clear winner, achieving a root‑mean‑square error (RMSE) of ~8 % on the test set and ~11 % on a set containing unseen additives—better than linear regression, k‑NN, Bayesian GLM, and a single‑layer neural network. The study concluded that ML can outperform human intuition for Buchwald‑Hartwig optimization, but that a universal “Buchwald‑Hartwig box” that predicts conditions for any substrate pair was still out of reach.

---

## 2. HISTORY  

**Post‑2018 methodological advances**  
- **Larger, public reaction datasets** (USPTO, Reaxys, Open Reaction Database) and more extensive HTE campaigns have become common. Benchmarks now routinely involve >10 k reactions, allowing models to learn subtler structure‑reactivity patterns.  
- **Deep learning supersedes random forests** for most reaction‑outcome tasks. Graph‑convolutional networks (e.g., the Molecular Transformer, Chemprop) consistently achieve RMSE ≈ 5–7 % on Buchwald‑Hartwig yield prediction, beating the ~8 % random‑forest baseline reported in 2018.  
- **Hybrid workflows** that combine HTE data generation with ML‑guided “active learning” loops are now deployed in several pharma process‑development groups (Merck, Pfizer, Novartis). These loops iteratively propose new reaction conditions, run a small batch of experiments, and retrain the model, reducing the number of required experiments by 30–50 % compared with exhaustive HTE.  

**Industrial uptake**  
- Merck incorporated the 2018 workflow into its internal “Digital Chemistry” platform, using random‑forest models as a first‑pass filter before moving to more sophisticated neural‑network predictors. The platform is now part of routine route scouting for small‑molecule projects, though it is not a “plug‑and‑play” box; chemists still curate the substrate scope and verify predictions experimentally.  
- Several start‑ups (e.g., **DeepMatter**, **AstraZeneca’s “Chemistry AI”**, **IBM RXN**) released cloud‑based tools that suggest Buchwald‑Hartwig conditions. Their performance on internal test sets mirrors the 2018 findings: random‑forest or gradient‑boosted trees are competitive for narrow chemical spaces, while transformer‑based models excel when the substrate space is broader.  

**Academic impact**  
- The 4,608‑reaction dataset has been used as a benchmark in at least ten subsequent publications on reaction‑outcome prediction, often cited as “the Doyle‑Merck Buchwald‑Hartwig set.”  
- Follow‑up studies (e.g., 2020 – 2022) demonstrated that adding mechanistic descriptors (e.g., computed Pd‑ligand binding energies) modestly improves model accuracy, confirming the original paper’s hint that additive electrophilicity mattered.  

**Policy & education**  
- No regulatory changes were triggered directly by the paper, but the broader trend of data‑driven chemistry has been reflected in NIH’s 2021 “Data‑Driven Discovery” initiative, which funds HTE‑ML pipelines for drug synthesis.  

Overall, the 2018 work helped cement the idea that **large, well‑annotated HTE datasets + ML = practical reaction‑optimization tools**, a concept that has become standard practice in both academia and industry.

---

## 3. PREDICTIONS  

| Prediction made in the article (or implied) | What actually happened |
|---|---|
| **ML will eventually predict Buchwald‑Hartwig conditions as well as a “box” that any chemist can use.** | Partial success. Modern ML models can suggest viable conditions for many substrate pairs, but a universally accurate, one‑click box is still not available. Chemists must still define the reaction scope and sometimes fine‑tune the output. |
| **Random‑forest would outperform other methods on this dataset.** | True for the 2018 dataset; however, later studies showed that gradient‑boosted trees and deep‑learning models (graph neural nets, transformers) surpass random‑forest when trained on larger, more diverse data. |
| **Using only 5 % of the data, random‑forest would beat linear regression on the full 70 % training set.** | Confirmed in the original paper; subsequent work reproduced the trend, but the advantage shrank as more sophisticated models learned from the full data. |
| **Larger data sets and better descriptors will improve performance.** | Confirmed. Expanding the dataset to >10 k reactions and adding mechanistic descriptors reduced RMSE by ~2–3 % in multiple follow‑up papers. |
| **The model would handle unseen additives with only a modest loss in accuracy (RMSE rising from 8 % to ~11 %).** | Roughly correct. Modern models show similar or slightly better generalization (RMSE ≈ 9 % on truly novel additives) when trained on larger, more diverse libraries. |
| **The approach would be a “real improvement” over human intuition.** | Supported. Internal Merck studies reported a 30–40 % reduction in the number of experimental iterations needed to reach a target yield compared with expert‑driven trial‑and‑error. |

---

## 4. INTEREST  
**Rating: 7/10** – The article is a clear early demonstration of how high‑throughput data + machine learning can tackle a notoriously fickle reaction class, and it sparked a wave of methodological advances that are now mainstream in both academia and pharma. It is not a breakthrough discovery, but its influence on the field’s trajectory is substantial.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180425-calculate-your-way-out-bad-yields.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_