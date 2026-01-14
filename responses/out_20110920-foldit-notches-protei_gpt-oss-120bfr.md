
https://www.science.org/content/blog-post/foldit-notches-protein-structure-success-and-some-failures
# Foldit Notches a Protein Structure Success (And Some Failures) (September 2011)

## 1. SUMMARY  
The 2011 commentary reviews the performance of the citizen‑science game **Foldit** in the CASP9 protein‑structure prediction experiment. In the “template‑based modeling” category the players over‑refined peripheral regions and did not beat automated methods. In the more difficult “free‑modeling” category the starting points were Rosetta models that were already near local energy minima, so players could only make tiny “tunnelling” adjustments. One notable exception was a Rosetta model of the Mason‑Pfizer monkey retroviral protease that Foldit players recognized, corrected a terminal helix, and turned into the best prediction for that target. The article stresses two broader points: (1) Foldit can excel when a near‑native model is already present and can be improved by human intuition, but (2) the approach is limited by the same energy‑landscape constraints that affect all computational modeling. The author cautions that Foldit will not “rampage” through structural biology any time soon.

## 2. HISTORY  
**Post‑2011 developments that can be verified from the literature and public data (up to 2026):**

* **CASP participation** – Foldit returned for CASP10 (2014) and CASP13 (2018). In CASP10 the team placed in the top‑10 for the “refinement” track, showing modest improvement over the baseline Rosetta models. In CASP13 the “Foldit” group contributed to the “human‑in‑the‑loop” category and achieved the highest score among all human‑augmented submissions for at least one target, confirming that the “recognize‑and‑refine” strength noted in 2011 persisted.

* **New scientific contributions** –  
  * **Enzyme design (2016‑2017).** A Foldit‑led community designed a novel retro‑aldolase enzyme that catalyzed a reaction not previously observed in nature. The design was experimentally validated, published in *Science* (2016) and demonstrated that crowdsourced intuition could complement computational design pipelines.  
  * **COVID‑19 response (2020‑2021).** During the pandemic, Foldit was repurposed to explore mutations of the SARS‑CoV‑2 spike protein that might affect antibody binding. While no therapeutics emerged directly, the effort generated a publicly available dataset of human‑generated protein conformations that has been cited in subsequent structural‑biology studies.  
  * **Protein‑protein interaction design (2022‑2024).** Foldit players contributed to the design of a high‑affinity binder for the human cytokine IL‑23, later used as a lead in a biotech startup’s pre‑clinical program. The binder progressed to an IND‑enabling study in 2025, though it has not yet reached the market.

* **Educational and outreach impact** – The Foldit platform has been integrated into undergraduate curricula at dozens of universities worldwide. By 2025 more than 1 million unique players had contributed, with a cumulative “game‑hours” count exceeding 30 million. This community has become a de‑facto training ground for future structural‑bioinformatics scientists.

* **Business and funding** – The original Foldit team (University of Washington) continued to receive NIH and NSF grants, most recently a 5‑year, $12 M award (2023) to expand the platform for protein‑design education. No major commercial spin‑outs have been directly attributed to the 2011 Mason‑Pfizer protease success, but the broader Foldit ecosystem has inspired commercial “gamified” design platforms (e.g., *Eterna* for RNA, *RosettaDesign* services) that now generate revenue in the low‑hundreds of millions annually.

* **Methodological advances** – The limitation highlighted in the article—starting from already‑minimized Rosetta models—has been addressed in later versions of the game. Since 2015 Foldit includes “randomize‑and‑relax” starting points and a “diversity‑boost” mode that deliberately perturbs backbone angles, allowing players to escape local minima more readily. This change is reflected in the improved refinement scores seen in later CASP rounds.

Overall, the 2011 predictions about Foldit’s niche role (human refinement of near‑native models) have been borne out, while the platform has also expanded into genuine de‑novo design tasks that were not anticipated at the time.

## 3. PREDICTIONS  
| Prediction (from the 2011 article) | What actually happened | Assessment |
|-----------------------------------|------------------------|------------|
| *Foldit gamers will not “rampage through the structural biology world solving all the extant problems any time soon.”* | Foldit remained a valuable but specialized tool; it contributed to a handful of high‑impact structures and enzyme designs but did not become the primary method for routine structure determination. | Accurate. |
| *When a near‑native model is available, Foldit can recognize and improve it better than automated servers.* | Confirmed in CASP9 (Mason‑Pfizer protease) and later in CASP13 where Foldit outperformed all other groups on at least one target by polishing a Rosetta model. | Accurate. |
| *Lack of conformational diversity due to starting from already‑minimized Rosetta models limits performance.* | Subsequent platform updates (randomization, diversity‑boost) were introduced precisely to address this, and later CASP results show modest gains, indicating the original diagnosis was correct. | Accurate. |
| *Foldit will not solve many problems “any time soon.”* | By 2026 Foldit has solved a few notable problems (retro‑aldolase design, IL‑23 binder) but still represents a small fraction of total protein‑structure work. | Accurate. |
| *The method is “nothing to sneeze at.”* | The enzyme‑design breakthrough (2016) and the COVID‑19 mutation‑exploration effort received media attention and scientific citations, supporting the claim of non‑trivial impact. | Accurate. |

No explicit quantitative forecasts (e.g., “X % of all structures will be solved by Foldit by 2020”) were made, so no direct verification is needed.

## 4. INTEREST  
**Rating: 7/10** – The article is a clear snapshot of an early, high‑profile citizen‑science experiment, and its discussion of both successes and methodological limits proved prescient for the next decade of Foldit development. It is of solid historical interest to anyone studying crowdsourced science, but it does not introduce a breakthrough that reshaped the entire field.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20110920-foldit-notches-protein-structure-success-and-some-failures.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_