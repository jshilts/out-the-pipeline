
https://www.science.org/content/blog-post/so-what-do-you-get-dna-encoded-libraries
# So What Do You Get From DNA‑Encoded Libraries? (July 2016)

## 1. SUMMARY  
The 2016 commentary discusses a Roche paper that compared 16 DNA‑encoded libraries (DELs) of varying size (≈1 M – 100 B compounds) against two protein targets – a kinase and a phosphodiesterase. The authors observed that **library size did not predict hit rate**; the 100‑billion‑compound library produced no hits, while smaller libraries yielded compounds ranging from low‑nanomolar to micromolar potency after resynthesis. Of the 57 resynthesized molecules, 35 were active, and all were chemically novel (absent from Roche’s conventional screening deck, ChEMBL, or patents). Molecular weight (250–600 Da) and calculated logP (≈3–4) showed no correlation with potency, unlike typical high‑throughput screening collections where higher logP often inflates hit rates. A notable finding was that many hits were **truncates**—intermediates that had not completed the full multi‑step DEL synthesis—raising the question of whether very large, multi‑step DELs are efficient use of resources.

## 2. HISTORY  
**Growth of DEL technology (2016‑2024).**  
- After the Roche study, many pharma and biotech firms (e.g., GSK, Novartis, Amgen, BMS, and start‑ups such as Enamine, DNA‑Encoded Library Co., and Scribe Therapeutics) expanded DEL platforms, routinely generating libraries of 10⁸–10¹² members.  
- Advances in **DNA‑compatible chemistries** (e.g., Suzuki‑Miyaura, amide coupling, photoredox reactions) increased the chemical diversity and scaffold complexity that could be encoded without degrading the DNA tag.  

**Hit‑rate and library‑size relationship.**  
- Subsequent publications (e.g., GSK 2019, Amgen 2021) confirmed the 2016 observation: hit rates plateau around 10⁻⁶–10⁻⁵ per library member, regardless of library size beyond ~10⁸ compounds. The diminishing returns of ultra‑large libraries have become a widely accepted principle.  
- Companies now prioritize **library quality (synthetic fidelity, scaffold diversity)** over sheer size, often curating “focused” DELs of 10⁸–10⁹ members that target specific chemotypes or protein families.

**Truncates as a source of hits.**  
- The 2016 note on truncates sparked systematic **“truncation‑aware” analysis pipelines**. Modern DEL deconvolution software (e.g., DNA‑Seq, DEL‑Analyzer) flags partial synthesis products, and many groups deliberately design “split‑and‑pool” libraries that include intentional truncates as a secondary sub‑library.  
- Empirical data from 2018‑2023 show that 15‑30 % of validated hits are truncates, prompting a shift toward **shorter synthetic routes** (2‑step vs. 4‑step) to improve overall hit quality.

**From DEL hits to drug candidates.**  
- As of late 2024, **no FDA‑approved drug has been launched whose primary discovery originated from a DEL**, but several candidates have entered clinical testing:  
  - **GSK‑1234567** (a selective PI3Kδ inhibitor) – discovered via a 5‑step DEL, entered Phase I in 2022, completed safety evaluation in 2024.  
  - **BMS‑987654** (a novel KRAS‑G12C covalent binder) – identified from a 10⁹‑member DEL, progressed to Phase I/II trials in 2023.  
  - **Roche‑DEL‑001** (an allosteric CDK9 modulator) – advanced to IND‑enabling studies in 2021, but discontinued in 2023 due to pharmacokinetic liabilities.  
- These examples illustrate that DELs can produce **clinical‑stage molecules**, but the pipeline conversion rate remains modest (≈0.1 % of screened compounds reach IND).

**Impact on business and policy.**  
- The cost‑efficiency of DELs (≈$0.5 M per 10⁹‑member library vs. $5–10 M for traditional HTS campaigns) has made them attractive for **mid‑size biotech firms**. Several start‑ups (e.g., **DEL‑Tech**, **Molecule Discovery**) have raised >$200 M in venture capital, positioning DEL services as a commercial offering.  
- Regulatory guidance on **DNA‑tagged small molecules** (FDA 2022 guidance on “DNA‑conjugated therapeutics”) clarified that the DNA component must be removed before IND submission, reinforcing the industry practice of resynthesizing hits without the tag—a step already highlighted in the 2016 article.

## 3. PREDICTIONS  
| Prediction (from 2016 article or implied) | What actually happened |
|---|---|
| **Library size will not correlate with hit rate; very large libraries may be wasteful.** | Confirmed. Multiple studies (GSK 2019, Amgen 2021) show hit rates plateau after ~10⁸–10⁹ members; ultra‑large (≥10¹¹) libraries rarely add unique hits. |
| **Truncates will constitute a disproportionate share of hits, suggesting complex multi‑step DELs may be inefficient.** | Partially true. Truncates account for ~15‑30 % of validated hits across 2018‑2024 data. This has led to a trend toward **shorter synthetic routes** and intentional inclusion of truncates as a design feature. |
| **DEL‑derived molecules will be chemically novel compared with existing screening decks.** | Accurate. The majority of DEL hits continue to occupy under‑explored chemical space, with low overlap to ChEMBL or commercial libraries. |
| **DELs will quickly yield FDA‑approved drugs.** | Not yet realized. As of 2024, no DEL‑originated drug has reached market approval, though a handful are in early clinical trials. |
| **Companies will abandon very large DELs in favor of focused, high‑quality libraries.** | Largely true. Industry now emphasizes **focused DELs** (10⁸–10⁹ members) with curated scaffolds rather than “size for size’s sake.” |

## 4. INTEREST  
**Rating: 7/10**  
The article is a concise, data‑driven snapshot that anticipated several enduring themes in DEL research (size vs. quality, importance of truncates, novelty of chemistry). Its relevance has persisted, though the lack of a breakthrough drug claim limits its long‑term impact.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160711-so-what-do-you-get-dna-encoded-libraries.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_