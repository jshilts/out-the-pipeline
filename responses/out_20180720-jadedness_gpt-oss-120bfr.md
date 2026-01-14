
https://www.science.org/content/blog-post/jadedness
# On Jadedness (July 2018)

## 1. SUMMARY  
The author reflects on the emotional toll of working in drug discovery, contrasting “experienced” with “jaded.” Because most projects fail, they argue that scientists must stay open‑minded about any hit while avoiding the low‑energy cynicism that leads to premature dismissal. The piece uses “ugly” chemical matter—particularly PAINS (pan‑assay interference compounds) such as rhodanines—as a case study. The author’s policy is to test such structures rigorously (both the target‑specific assays and the standard PAINS counterscreens) before deciding they are junk. Their personal record shows that most of these suspicious compounds turn out to be false positives, but they acknowledge that occasional genuine hits can emerge from unlikely chemotypes. The discussion then widens to the broader culture of drug‑discovery teams, noting that repeated exposure to negative data can breed pessimism, and that large HR‑driven initiatives rarely change day‑to‑day scientific practice.

## 2. HISTORY  
**PAINS and “ugly” chemotypes** – Since 2018 the community has continued to refine PAINS filters. Open‑source libraries (e.g., the FAF‑Drugs4, the PAINS‑A and PAINS‑B sub‑sets) have been updated, and many high‑throughput screening (HTS) facilities now run orthogonal counterscreens automatically. At the same time, a modest but growing body of literature has demonstrated that a small fraction of rhodanine‑derived molecules can be optimized into bona‑fide leads (e.g., certain kinase inhibitors and antibacterial agents). The consensus remains that PAINS should be treated as red flags, not absolute disqualifiers, echoing the author’s “cautious but open” stance.

**Cultural shifts in biotech** – The past few years have seen a measurable increase in attention to employee well‑being in pharma and biotech. Companies have introduced structured mental‑health programs, flexible‑working policies, and “science‑first” culture statements. While these HR initiatives differ from the “huge HR initiatives” the author dismissed, surveys (e.g., the 2022 Biotech Workforce Survey) report modest improvements in reported burnout levels, suggesting that some organizational changes do have impact, albeit incremental rather than revolutionary.

**Assay and data‑analysis practices** – Advances in machine‑learning‑driven hit‑triage have reduced the reliance on manual visual inspection of structures. Platforms such as Atomwise, Insilico Medicine, and open‑source tools like DeepChem now flag likely aggregators or redox‑cyclers early in the pipeline. Nonetheless, the core principle of confirming hits with orthogonal assays remains unchanged, confirming the author’s recommendation to “run the warning‑this‑is‑junk assays as soon as possible.”

**Overall drug‑discovery productivity** – The number of FDA‑approved small‑molecule drugs has remained roughly steady (≈40–50 per year) with a slight uptick in first‑in‑class approvals from 2019‑2023. The proportion of drugs emerging from phenotypic screens versus target‑based screens has shifted modestly toward phenotypic approaches, partly because they are less vulnerable to PAINS‑type artefacts. No major “paradigm shift” in how organizations run discovery projects has occurred; most changes are incremental (e.g., adoption of cloud‑based LIMS, more collaborative data‑sharing).

## 3. PREDICTIONS  
- **Prediction:** “Compounds like rhodanines and other PAINs have a poor track record and need to be approached with caution; most will fail.”  
  **Outcome:** Largely correct. Systematic PAINS filtering continues to be standard practice, and the majority of such hits still prove non‑viable. A few exceptions have been reported, but they remain the minority.

- **Prediction:** “Huge HR initiatives will not change the way we do business.”  
  **Outcome:** Partially correct. Large‑scale, top‑down HR programs have had limited disruptive effect on day‑to‑day discovery work. However, incremental HR measures (flexible hours, mental‑health resources) have modestly improved employee satisfaction, indicating some impact, though not the sweeping transformation the author doubted.

- **Implicit prediction:** “Running both project‑specific and junk‑screen assays early will allow a quick call on the viability of ugly hits.”  
  **Outcome:** Confirmed. Modern HTS pipelines now embed orthogonal counterscreens (e.g., detergent‑based aggregation tests, redox‑cycling assays) early, and this practice has become a de‑facto standard, aligning with the author’s recommendation.

## 4. INTEREST  
Rating: **6/10**  
The article offers a candid, experience‑based view of drug‑discovery culture and the practical handling of PAINS, topics that remain relevant, but it lacks concrete data or novel predictions, limiting its broader impact.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180720-jadedness.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_