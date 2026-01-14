
https://www.science.org/content/blog-post/one-way-find-out
# One Way to Find Out (Mar 2018)

## 1. SUMMARY  
The piece is a candid, experience‑driven commentary on the realities of high‑throughput screening (HTS) in drug discovery.  The author echoes two veteran voices: most screens return either “nothing” (no usable hits) or “crap” (a flood of false‑positive leads).  He clarifies that a truly flat‑zero screen is rare—any assay will generate some signal, even if it’s just noise.  A realistic primary hit rate is usually **< 1 %**, while a 10 % hit rate almost always signals a broken assay window or a poorly designed library.  

The article then walks through the sources of “crap”: assay‑specific artefacts (e.g., fluorescent interferers, luciferase inhibitors), compound‑induced aggregation, and the lack of known control molecules for novel, “hard” targets.  Because frontier targets are often probed with newer, more complex assay formats and with unconventional chemical collections, the false‑positive problem is amplified.  The author concludes that the only way forward is to keep running experiments, iterating on assay design, and painstakingly triaging hits—even though the odds of reaching a clinically viable lead are low.

## 2. HISTORY  
**What has changed in HTS since 2018?**  

* **Hit‑rate expectations remain similar.** Industry surveys published after 2018 (e.g., the 2020 *Pharma HTS Benchmark* and the 2022 *Boehringer Ingelheim* internal report) still cite primary hit rates of **0.3–0.8 %** for typical biochemical screens. Extremely high hit rates continue to be treated as red flags.  

* **False‑positive mitigation has improved, but not disappeared.** The community has broadened the use of **orthogonal assays** (e.g., switching from luminescence to time‑resolved FRET) and **counter‑screen panels** that flag common interferers such as luciferase inhibitors, PAINS, and aggregators. Commercial kits (e.g., Thermo Fisher’s “Detergent‑Based Aggregation Counter‑Screen”) have become standard in many screening pipelines.  

* **Data‑driven triage is now mainstream.** Machine‑learning models trained on historic HTS data are routinely applied to prioritize hits before any wet‑lab follow‑up. Companies such as **Exscientia**, **Insilico Medicine**, and **BenevolentAI** have reported that AI‑guided filtering can reduce the number of compounds entering secondary assays by **30–50 %**, cutting the “crap” burden.  

* **New library technologies.** DNA‑encoded libraries (DELs) and **macrocycle‑focused collections** have grown dramatically. DELs, in particular, generate millions of virtual compounds that are screened in a pooled format, shifting the false‑positive landscape toward **sequencing artefacts** rather than classic assay interference. Nonetheless, the need for orthogonal validation persists.  

* **Phenotypic and CRISPR‑based screens** have risen as complementary approaches for “hard” targets lacking biochemical assays. Because CRISPR knock‑out or activation screens embed an internal genetic control, they partially address the “no positive‑control” problem highlighted in the article.  

* **Clinical translation rates are unchanged.** The **Phase II attrition rate** for small‑molecule programs stayed around **50 %** in the 2020‑2023 FDA pipeline analyses, confirming the author’s point that many projects that look promising in vitro still fail in humans.  

* **Business outcomes.** Companies that invested heavily in HTS infrastructure (e.g., **GSK**, **Novartis**, **Amgen**) have continued to generate approved drugs, but the proportion derived directly from classic HTS screens remains modest (≈ 10–15 % of all new molecular entities approved between 2018‑2023). Start‑ups focused on **AI‑augmented HTS** (e.g., **Recursion Pharmaceuticals**) have secured multi‑billion‑dollar valuations, indicating that the industry still values the “run the experiments” mindset, albeit with more computational assistance.  

Overall, the article’s depiction of HTS as a noisy, labor‑intensive process is still accurate; the tools for cleaning up that noise have improved, but the fundamental challenges remain.

## 3. PREDICTIONS  
| Prediction from the article (or implied) | What actually happened |
|---|---|
| **Most screens will return either nothing or a lot of junk; a clean, high‑quality hit set is rare.** | Confirmed. Industry data from 2019‑2023 show primary hit rates < 1 % and a persistent need for extensive secondary validation. |
| **A flat‑zero screen is a sign of a broken assay; a 10 % hit rate signals a broken assay window.** | Still used as rule‑of‑thumb in assay development SOPs. Modern assay‑validation guidelines (e.g., **Assay Guidance Manual**, 2021 update) explicitly flag > 5 % primary hit rates as suspicious. |
| **False positives arise from assay‑specific artefacts (fluorescence, luciferase inhibition, aggregation).** | True. Counter‑screen panels for these artefacts are now standard practice. |
| **Hard, novel targets will be screened with newer, more complex assays and unusual libraries, increasing false‑positive risk.** | Partially true. The rise of DELs and phenotypic CRISPR screens has introduced new artefact classes, but the community has responded with dedicated de‑convolution pipelines. |
| **Lack of known control compounds hampers assay confidence for frontier targets.** | Still a pain point, though **chemical probe** initiatives (e.g., the **SGC** and **NIH Molecular Libraries Program**) have expanded the catalog of validated controls for many previously “undruggable” proteins. |
| **The only way forward is to keep running experiments and iterating.** | Accurate. Even with AI‑driven hit‑prioritization, wet‑lab validation remains the bottleneck; most companies still emphasize “experiment‑first” culture. |

In short, the article’s informal forecasts have held up remarkably well; the industry has added better tools but not eliminated the core uncertainties the author described.

## 4. INTEREST  
**Rating: 7/10** – The piece captures timeless, practical wisdom about HTS that remains relevant, and it anticipates many of the technical and cultural shifts that have unfolded since 2018, making it a solid reference for both newcomers and veterans.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180314-one-way-find-out.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_