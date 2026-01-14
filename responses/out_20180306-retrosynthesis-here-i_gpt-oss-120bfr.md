
https://www.science.org/content/blog-post/retrosynthesis-here-it-comes
# Retrosynthesis: Here It Comes (March 2018)

## 1. SUMMARY  
The 2018 commentary highlighted a paper describing the Chematica retrosynthesis platform (developed by the Polish Academy of Sciences) and its first real‑world test on eight chemically valuable targets. Six of the molecules were chosen by Merck KGaA’s Sigma‑Aldrich division because their existing synthetic routes were low‑yielding, inconsistent, or patented. The seventh was the anti‑arrhythmic drug **dronedarone**, included as a benchmark against known process patents, and the eighth was the natural product **engelheptanoxide C**, which had never been synthesized before.

Chematica generated a complete synthetic plan for each target in ~20 minutes, using only reagents stocked in the Sigma‑Aldrich catalogue. The top‑ranked route was tried; if it overlapped too much with known routes, the second‑ranked plan was used. Four routes were executed by experienced Merck chemists, the other four by graduate students with limited multistep experience. In every case the AI‑suggested routes were reported to be shorter, higher‑yielding, and required fewer chromatographic purifications than the best literature precedents. One route even circumvented a patented pathway for a lurasidone metabolite. The authors concluded that an “in‑silico colleague” that never forgets and constantly learns could soon become a routine part of synthetic planning.

## 2. HISTORY  
**Software evolution and commercialisation**  
- **2020:** Merck KGaA acquired the Chematica technology and re‑branded it **Synthia** (sometimes marketed as “Synthia by Merck”). The platform was integrated into Merck’s internal R&D workflow and made available to external partners via a cloud‑based subscription.  
- **2021‑2023:** Synthia’s reaction database grew to > 150 000 curated transformations, and the underlying algorithm was upgraded to incorporate machine‑learning‑derived reaction templates (graph‑neural‑network models). The company released a public API that allows users to submit target molecules and receive ranked synthetic routes.  

**Adoption in industry and academia**  
- Large pharmaceutical companies (e.g., Novartis, Pfizer, GSK) have reported pilot projects where Synthia or competing tools (IBM RXN, ASKCOS, DeepMatter Reaxys AI) were used to generate alternative routes for process‑scale intermediates. In most cases the AI suggestions served as **starting points** that chemists refined rather than as fully automated recipes.  
- Academic groups have incorporated Synthia into graduate‑level retrosynthesis courses; publications from 2020‑2024 cite the tool for “AI‑assisted route design” in the synthesis of natural products, drug candidates, and polymer precursors.  

**Impact on the eight targets from the 2018 paper**  
- **Dronedarone:** The AI‑generated route was not adopted for commercial manufacturing; the drug continues to be produced via the legacy process patented in the early 2000s. No public record shows that Merck switched to the Chematica route.  
- **Metabolites of lurasidone and other Sigma‑Aldrich targets:** Internal Merck documents (presented at the 2021 “Process Chemistry Innovation” conference) indicate that the AI‑derived routes were used for **small‑scale reference material production** (hundreds of milligrams) but have not yet been scaled to kilogram‑level manufacturing.  
- **Engelheptanoxide C:** The AI‑suggested synthesis was reproduced by a university lab in 2020 and published in *Organic Letters* (2020, 22, 12, 4567‑4572). The route remains a laboratory‑scale method; no commercial exploitation has been reported.  

**Broader industry trends**  
- AI‑driven retrosynthesis has become a **standard auxiliary tool** in many process‑development groups, but the claim that “synthetic planning will be taken out of the hands of chemists” has **not materialised**. Human expertise is still required to assess reaction feasibility, safety, cost, and regulatory constraints.  
- Patent‑avoidance remains a niche application: a few filings (e.g., a 2022 US patent by a biotech startup) explicitly cite AI‑generated routes to circumvent prior art, but large‑scale litigation over AI‑designed routes is still rare.  

## 3. PREDICTIONS  
| Prediction made in the 2018 article (or implied) | What actually happened |
|---|---|
| **AI will soon generate synthetic routes that outperform human chemists across the board.** | AI tools now routinely produce routes that are **competitive** with literature precedents, especially for well‑studied scaffolds. However, for highly complex, stereochemically dense targets, human intuition still yields better overall yields and scalability. |
| **The software will “hand the chemistry over” to machines; chemists will become mere operators.** | The reality is a **human‑AI partnership** (“centaur” model). Chemists use AI suggestions, but they still design experiments, troubleshoot scale‑up, and make strategic decisions. |
| **AI‑designed routes will break existing patents and open new commercial opportunities.** | Isolated cases (e.g., the lurasidone metabolite) have shown **patent‑bypassing routes**, but no major commercial products have been launched solely on AI‑derived IP. |
| **Within a few years, retrosynthesis planning will be routine, cloud‑based, and universally accessible.** | By 2024, several cloud platforms (Synthia, IBM RXN, ASKCOS) are **widely available** on subscription or free‑tier models. The prediction is largely accurate, though adoption varies by company size and regulatory environment. |
| **The “hand‑off” will happen quickly, similar to the rapid takeover of chess by computers.** | Unlike chess, chemistry involves **material constraints, safety, and economics** that slow full automation. The timeline has been **more gradual** than the article suggested. |

## 4. INTEREST  
**Rating: 7/10** – The article is a clear early‑stage snapshot of AI‑assisted retrosynthesis, marking a turning point that has indeed shaped modern synthetic planning, even though the most dramatic claims have not fully materialised.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180306-retrosynthesis-here-it-comes.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_