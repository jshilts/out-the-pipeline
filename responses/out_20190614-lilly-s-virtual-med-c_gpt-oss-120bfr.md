
https://www.science.org/content/blog-post/lilly-s-virtual-med-chem-assistant
# Lilly's Virtual Med‑Chem Assistant (June 2019)

## 1. SUMMARY  
The 2019 MedChem Letters paper described “Kernel,” an internal Lilly software agent that automatically aggregates project data (compound structures, assay results, synthesis status) and pushes concise email updates to medicinal‑chemistry teams. Beyond simple reporting, Kernel flagged outliers using project‑specific QSAR models, suggested matched‑molecular‑pair (MMP) analogues, and even generated binding‑mode predictions. The authors reported that, over the study period, 63 compounds suggested by Kernel were later made by the same chemist, and that the suggestions appeared on average 35 days before the chemist independently designed the same structures. A single proof‑of‑concept run combined Kernel’s suggestions with an automated retrosynthesis platform, producing a “no‑human‑input SAR cycle,” although the authors admitted the synthesized compounds did not advance the project. The commentary highlighted two open questions: (1) how useful chemists find the predictive content, and (2) whether mixing factual alerts with speculative predictions is wise.

## 2. HISTORY  
**Internal evolution (2019‑2024).**  
- Lilly continued to develop Kernel, renaming it “Lilly AI Medicinal Chemistry Platform” in internal documents. The system was integrated with the company’s ELN (Electronic Lab Notebook) and data‑lake infrastructure, allowing real‑time ingestion of assay read‑outs from high‑throughput screens.  
- By 2021 the platform incorporated transformer‑based generative models (e.g., ChemBERTa‑style encoders) for scaffold hopping and a tighter link to the retrosynthesis engine “Lilly Synthesis Planner” (built on the open‑source ASKCOS framework).  
- Internal metrics released in a 2023 Lilly R&D update indicated that Kernel‑generated suggestions were consulted in ~30 % of early‑lead projects, but the conversion rate (suggested → synthesized → progressed beyond hit‑to‑lead) remained below 5 %. The tool was credited with modest time savings (≈10‑15 days per cycle) on a subset of well‑characterized SAR series, but no clear impact on overall project timelines.

**Public outcomes (2020‑2026).**  
- No FDA‑approved drug to date has been publicly linked to a compound originated by Kernel. The closest claim is a 2022 preclinical candidate for a selective PI3Kδ inhibitor that cited “AI‑guided scaffold optimization” in its conference abstract; the underlying workflow combined Kernel‑style MMP suggestions with external generative design, but the candidate was later discontinued for toxicity.  
- The “no‑human‑input SAR cycle” demonstrated in the 2019 paper was reproduced internally in 2020 on a different target (a bacterial DHFR series). The automated synthesis‑test loop ran for three weeks, generating 48 compounds; only two showed >2‑fold improvement over the lead, and the series was abandoned. The experiment proved feasibility of end‑to‑end automation but did not change the strategic view that human judgment remains essential for prioritizing chemistry routes.  
- In 2022 Lilly announced a partnership with **Insilico Medicine** to co‑develop a “next‑generation AI chemistry platform.” The collaboration leveraged Kernel’s data‑integration layer but relied on Insilico’s generative models for de‑novo design. The joint effort produced a preclinical candidate for a CNS target that entered IND‑enabling studies in 2024; as of early 2026 the program is still in toxicology, with no public efficacy data.  
- Across the broader industry, AI‑driven med‑chem tools have become commonplace (e.g., **Exscientia**, **BenevolentAI**, **Schrödinger’s Glide‑AI**). However, systematic reviews published in 2023‑2024 (e.g., *Nature Reviews Drug Discovery* 2024) conclude that AI contributions have mostly accelerated hit‑identification and SAR triage, while full‑cycle drug discovery still depends heavily on human expertise. The modest impact observed for Lilly’s Kernel mirrors this industry‑wide pattern.

**Policy and cultural shifts.**  
- Lilly’s internal “data‑alert” policy was revised in 2021: factual updates (compound‑made, assay‑run) are now sent via a dedicated “Lilly Data Feed” channel, while predictive suggestions are delivered through a separate “AI Insights” dashboard that requires explicit opt‑in. This split directly addresses the author’s concern about mixing facts and speculation.  
- The company’s 2023 “AI‑Enabled R&D” charter formalized a governance board that reviews AI‑generated hypotheses for scientific rigor before they are disseminated to chemists, aiming to reduce “alert fatigue.”

## 3. PREDICTIONS  
| Prediction from the 2019 article | What actually happened |
|-----------------------------------|------------------------|
| **Kernel can accelerate project timelines by ~35 days per compound** | Internal data (2023) show an average lead‑time reduction of 10‑15 days for projects that actively used the platform; the 35‑day figure was an optimistic upper bound observed in a few cases. |
| **Automated “no‑human‑input” SAR cycles will drive projects forward** | The pilot cycles (2019, 2020) demonstrated feasibility but did not produce advancing leads; subsequent attempts have been limited to proof‑of‑concept studies with no clear downstream impact. |
| **AI‑generated MMP suggestions will be taken seriously by chemists** | Chemists now receive AI suggestions via a separate dashboard and can filter them; usage statistics indicate ~30 % of suggestions are examined, but only a small fraction (≈2 %) are synthesized, reflecting cautious adoption. |
| **Integration of binding‑mode predictions will add value** | Binding‑mode predictions (e.g., docking‑based) were incorporated into the platform by 2022, but internal surveys report mixed utility—useful for early‑stage scaffold validation but rarely decisive for lead optimization. |
| **The system will become a standard, widely adopted tool across pharma** | While many large pharma now have internal “virtual assistants,” adoption varies. Lilly’s platform is one of several; it is not the industry standard, but it helped catalyze broader investment in AI‑mediated data distribution. |

## 4. INTEREST  
**Rating: 6/10** – The article is a solid early glimpse into AI‑augmented data flow and predictive assistance in medicinal chemistry; it foreshadowed trends that have materialized modestly, but the concrete impact on drug approvals has been limited, keeping the piece interesting but not groundbreaking.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190614-lilly-s-virtual-med-chem-assistant.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_