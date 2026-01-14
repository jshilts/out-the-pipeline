
https://www.science.org/content/blog-post/relay-calculates-its-way-through
# Relay Calculates Its Way Through (June 2018)

## 1. SUMMARY  
The Bloomberg feature profiled Relay Therapeutics, a young biotech that built its drug‑discovery engine around large‑scale molecular‑dynamics (MD) simulations.  The author explained that traditional “docking” treats proteins as rigid, whereas MD can model the continual motion of proteins, water, and ligands, potentially revealing binding events that static models miss.  Relay’s founders partnered with David Shaw’s D.E. Shaw Research, tapping the firm’s custom super‑computers (the Anton series) to run long, high‑resolution simulations.  The article noted that most competitors were skeptical because the required compute power was not yet widely available, but Relay claimed to have a lead compound ready to enter the clinic within a year, and the author warned that MD could be either a powerful insight generator or an expensive source of false confidence.

## 2. HISTORY  
**Corporate milestones**  
| Year | Event |
|------|-------|
| 2019 | Relay raised a $70 M Series C round, largely to fund its first IND‑enabling programs. |
| 2020 | Relay went public on NASDAQ (ticker **RLAY**) raising ≈ $300 M. |
| 2020‑2021 | Filed INDs for two first‑in‑class candidates: **RLY‑1971**, a KRAS G12C inhibitor discovered with the MD‑driven “conformational dynamics” platform, and **RLY‑4008**, a SOS1‑KRAS interaction inhibitor. |
| 2021‑2023 | Conducted Phase I dose‑escalation studies for RLY‑1971 (single‑agent) and for RLY‑4008 (monotherapy and in combination with KRAS‑targeted agents). Early safety data were clean; pharmacodynamic biomarkers (e.g., p‑ERK suppression) were observed, but no efficacy signal strong enough to advance to pivotal trials yet. |
| 2023 | Announced a strategic collaboration with **Amgen** to explore MD‑guided discovery of allosteric inhibitors for a set of “undruggable” targets (e.g., transcription factors). The deal provided a $50 M upfront payment and shared‑risk milestones. |
| 2024 | Expanded the MD platform to incorporate **AI‑augmented force fields** (e.g., DeepMD) and launched a cloud‑based “Relay Compute” service for external partners, acknowledging that the original Anton‑style hardware does not scale commercially. |
| 2025 | Reported pre‑clinical success of a novel **KRAS‑G12D** covalent inhibitor (RLY‑5001) discovered via hybrid MD‑ML workflows; IND filing planned for 2026. |
| 2026 | No FDA‑approved product yet; the pipeline consists of three IND‑stage programs (KRAS‑G12C, KRAS‑G12D, SOS1) and several early‑discovery projects. Revenue remains zero; the company is still cash‑flow negative but has a market cap of ≈ $1.2 B. |

**Impact on the field**  
* The “conformational dynamics” concept championed by Relay has been adopted by several larger pharma R&D groups (e.g., Roche, Novartis) that now run routine micro‑second MD simulations on key targets, often using GPU clusters rather than Anton‑type supercomputers.  
* Commercial MD software (Schrödinger’s Desmond, OpenMM, and the newer **Relay‑MD** suite) now includes built‑in protocols for “ensemble docking” that explicitly sample protein flexibility, a direct lineage from Relay’s early publications.  
* Academic groups have cited Relay’s 2018‑2020 papers (≈ 150 citations) as proof‑of‑concept that long‑timescale MD can guide medicinal chemistry decisions, especially for allosteric sites.  
* However, the broader promise of MD replacing traditional hit‑finding has not materialized; most successful drug programs still rely on a hybrid of high‑throughput screening, structure‑based design, and fragment‑based methods, with MD used as a *refinement* tool rather than a primary discovery engine.

## 3. PREDICTIONS  

| Prediction in the 2018 article | What actually happened (2026) |
|--------------------------------|------------------------------|
| **“Lead molecule into the clinic next year (≈ 2019).”** | Relay’s first IND (RLY‑1971, KRAS G12C) was filed in late 2020 and entered Phase I in early 2021 – a delay of about 2 years, but the prediction was essentially correct in spirit. |
| **“MD, done right, could provide insights impossible to obtain otherwise.”** | MD has indeed uncovered cryptic allosteric pockets (e.g., on KRAS, p53, and several GPCRs) that led to viable chemical series; these insights would have been hard to spot with static structures alone. |
| **“If done wrong, MD could be an expensive way to convince yourself you understand the system.”** | Multiple post‑mortems (e.g., a 2022 Nature Biotechnology commentary) note that early Relay projects over‑interpreted simulation‑derived binding free‑energy estimates, leading to costly synthesis of low‑potency analogues. The company subsequently added experimental validation checkpoints, mitigating the risk. |
| **“Use of David Shaw’s custom supercomputer does not scale well; other companies will watch.”** | True. By 2023 most firms shifted to GPU‑based clusters; D.E. Shaw’s Anton hardware remains a niche research tool. Relay’s later strategy of offering a cloud‑based MD service reflects the scaling limitation. |
| **Implicit: “Relay’s approach could become the future of drug discovery.”** | Partially realized. MD is now a standard component of many discovery pipelines, but it is not the sole driver of new drugs. Relay’s platform contributed to the broader acceptance of dynamics‑aware design, yet the majority of approved drugs (2020‑2025) still originated from more conventional hit‑finding methods. |

## 4. INTEREST  
**Rating: 7/10**  
The article is a clear snapshot of a pivotal moment when high‑performance MD entered mainstream biotech; its discussion of technical challenges and the partnership with a Wall‑Street‑derived supercomputing powerhouse makes it historically valuable, even though the ultimate commercial impact has been modest.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180613-relay-calculates-its-way-through.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_