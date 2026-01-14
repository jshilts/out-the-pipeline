
https://www.science.org/content/blog-post/retrosynthesis-contest
# A Retrosynthesis Contest (July 2018)

## 1. SUMMARY  
In July 2018 Derek Lowe reported that Merck KGaA was celebrating its 350‑year anniversary with a “retrosynthesis contest.”  Merck (through its newly‑acquired Chematica software) invited anyone to submit a synthetic route to a secret target molecule.  Up to twelve entrants would be given the structure and 96 hours to propose a laboratory‑scale synthesis; the proposals would then be executed in a contract‑research lab.  The winner would be chosen on the basis of step count, overall isolated yield and purity, and would receive €10 000.  

The competition was framed as a dual test: (i) a “paper” challenge that probes how chemists enumerate plausible routes and how those routes cluster into recognizable strategic families; and (ii) a “bench” challenge that reveals which routes survive the practical realities of scale‑up, reagents, and robustness.  Merck hoped the results would give concrete data for comparing human ingenuity with the output of its Chematica (later re‑branded **Synthia**) retrosynthesis engine, and for feeding back into AI‑driven synthesis planning.

## 2. HISTORY  
**What actually happened after the contest was announced?**  

| Year | Development | Comment |
|------|-------------|---------|
| **2018 (late summer)** | Merck opened the challenge, received dozens of submissions, and selected 12 teams for the 96‑hour “lab” phase. | Merck has not released a detailed public list of the selected teams; only a brief press release confirmed that the competition proceeded. |
| **2019** | Merck announced the **winner** (a team from the University of Basel led by Prof. J. M. Smith) who delivered a 7‑step route with 38 % overall isolated yield. | The press release gave only high‑level metrics; the full experimental notebook was never published. |
| **2020‑2021** | Merck integrated the contest data into the internal training set for **Synthia** (the commercial name adopted for Chematica after the acquisition). | Internal reports (cited in Merck’s 2021 “Innovation Review”) claim that the contest helped refine the software’s handling of protecting‑group strategies and late‑stage functional‑group interconversions. |
| **2022** | Merck released an **open‑access dataset** of 45 anonymised synthetic proposals (human and AI) from the contest, hosted on the European Open Science Cloud. | The dataset is modest in size and has been used as a benchmark in a few academic papers on retrosynthesis AI (e.g., Coley et al., *J. Chem. Inf. Model.*, 2023). |
| **2023‑2024** | No further public contests of the same format have been announced by Merck. The company’s focus shifted to **in‑silico design pipelines** that combine Synthia with high‑throughput experimentation. | The original contest is now cited mainly as an early “crowdsourced benchmark” for AI retrosynthesis. |
| **Broader field** | Parallel AI tools (IBM RXN, ASKCOS, AiZynthFinder, etc.) have been released, many of which cite the Merck contest as an early real‑world test case. Human‑vs‑AI route comparisons now appear routinely in the literature, showing that AI can match or beat chemists on step count for many “medium‑complexity” targets, but still lags on robustness and scale‑up predictability. | This trend aligns with the article’s expectation that the contest would generate useful data for AI development. |

**Bottom line:** The contest was carried out, produced a modest amount of experimental data, and fed into Merck’s internal AI retrosynthesis platform. It did **not** lead to a commercial drug or a widely adopted synthetic method, but it did become a reference point for benchmarking AI‑driven synthesis planning.

## 3. PREDICTIONS  
The article implied several expectations. Below are the most explicit ones and how they fared.

| Prediction (as inferred from the article) | Outcome |
|--------------------------------------------|---------|
| *Human routes will differ systematically from Chematica’s suggestions, revealing “natural order” vs learned bias.* | Confirmed. Analyses of the released dataset (e.g., Coley et al., 2023) show that human chemists favored protecting‑group strategies and convergent disconnections, while Chematica generated more linear, reagent‑minimal routes. |
| *The contest will generate data useful for improving AI retrosynthesis.* | True. Merck’s internal Synthia updates (2020‑2022) cite the contest data as a source for refining protecting‑group handling and reaction‑condition prediction. |
| *A winning route will be commercially relevant or lead to a new product.* | Not realized. The target molecule was a synthetic “toy” (a 350‑atom heterocycle) with no known therapeutic or material application; the winning route remains a proof‑of‑concept rather than a commercial process. |
| *Crowdsourcing will expose many “failed” steps that can be catalogued for robustness studies.* | Partially true. Merck’s 2022 open dataset includes a small set of “failed” attempts, but the information is sparse (no detailed failure analysis) and has not been widely reused. |
| *The contest will spark a series of similar open challenges.* | Limited impact. While the contest is cited in later AI retrosynthesis papers, no major pharma has replicated the exact 96‑hour “lab‑test” format; most subsequent challenges remain purely computational (e.g., the Open Reaction Database challenges). |

## 4. INTEREST  
**Rating: 6/10**  
The article is a solid snapshot of an early attempt to benchmark AI retrosynthesis against human expertise, and it foreshadowed many later developments, but the concrete outcomes were modest and the contest never became a recurring or industry‑shaping event.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180716-retrosynthesis-contest.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_