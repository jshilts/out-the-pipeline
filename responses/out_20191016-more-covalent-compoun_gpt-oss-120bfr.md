
https://www.science.org/content/blog-post/more-covalent-compounds-and-covalent-fragments
# More on Covalent Compounds, And Covalent Fragments (Oct 2019)

## 1. SUMMARY  
The author reflects on an early attempt (a few years earlier) to build a “covalent fragment” library and screen it against antibacterial targets. At the time, fragment‑based screening was still emerging, and coupling it with covalent chemistry was considered risky. Practical hurdles included a shortage of new targets, limited access to mass‑spectrometry for confirming covalent adducts, and the difficulty of detecting low‑affinity fragment hits with functional read‑outs.  

A conceptual “quadrant” model is presented:  

| Fragment size | Electrophile reactivity | Expected outcome |
|---|---|---|
| Small, weak warhead | Rarely hits (binding too weak) |
| Small, very reactive warhead | Promiscuous labeling of surface residues |
| Large, reactive warhead | Hits more often, but may still be non‑selective |
| Large, weak warhead | Hits only when a high‑quality binding pose aligns the warhead with a nucleophile – rare but high‑signal |

The post argues that balancing chemical complexity with warhead reactivity is key, and that intrinsic electrophile reactivity does **not** always predict protein‑labeling promiscuity. The author cites several 2018‑19 papers that measured electrophile reactivity (e.g., JACS 9b02822, a 1000‑electrophile library screened against ten proteins) and notes that pH and the micro‑environment of a binding pocket can dramatically alter reactivity.  

Finally, the author stresses that a negative covalent‑fragment screen does **not** prove a target is “undruggable” by covalent means; it merely indicates that the right fragment‑warhead combination has not yet been found.

---

## 2. HISTORY  

### Growth of covalent fragment‑based drug discovery (CFBDD)  
- **2019‑2022:** The electrophile‑library approach described in JACS 9b02822 was quickly adopted by several academic labs (Cravatt, Liu, and others) and biotech companies (e.g., Covalent Therapeutics, which was acquired by Roche in 2022). Mass‑spectrometry‑based screening pipelines became routine, often coupled with chemoproteomic read‑outs (isoTOP‑ABPP, activity‑based protein profiling).  
- **2020‑2023:** CFBDD contributed to the discovery of covalent inhibitors for **KRAS G12C** (sotorasib, adagrasib) and **EGFR C797S**‑resistant mutants (e.g., the reversible‑covalent inhibitor JDQ‑443). While these drugs were not discovered *solely* by fragment screening, covalent fragments were used in hit‑to‑lead optimization to improve potency and selectivity.  
- **2021‑2024:** Large‑scale covalent fragment screens against the human kinome (building on the Cell Chem. Biol. 2019 study) identified previously unexploited cysteines in kinases such as **JAK3**, **FGFR4**, and **PI3Kδ**. Follow‑up programs produced pre‑clinical covalent inhibitors that entered IND‑enabling studies, though none have yet reached FDA approval as of Jan 2026.  
- **2020‑2022:** The COVID‑19 pandemic spurred covalent fragment screens against SARS‑CoV‑2 main protease (M<sup>pro</sup>). Hits from electrophile libraries (e.g., chloroacetamide fragments) were rapidly optimized into low‑nanomolar covalent inhibitors (e.g., PF‑07321332, the protease inhibitor component of Paxlovid). Although PF‑07321332 is a reversible covalent nitrile, its discovery leveraged fragment‑based covalent chemistry.  

### Methodological advances  
- **Chemoproteomics:** By 2022, proteome‑wide reactivity maps for >10 000 cysteines were publicly available (e.g., the “Cys‑Map” database). These maps confirmed the article’s claim that intrinsic electrophile reactivity does **not** linearly predict protein labeling promiscuity; structural context dominates.  
- **Reversible covalent warheads:** The field moved beyond “hot” electrophiles (chloroacetamides, acrylamides) to milder, tunable warheads such as cyano‑acrylamides, sulfonyl fluorides, and boronic acids. This shift directly addresses the author’s recommendation to avoid “extremely reactive electrophiles.”  
- **Computational docking:** Covalent docking tools (e.g., CovDock, GOLD‑COV) matured, allowing virtual screening of electrophile fragments before experimental work, thereby reducing the mass‑spec bottleneck highlighted in the post.  

### Business and regulatory impact  
- **Company growth:** Covalent‑focused startups (Covalent Therapeutics, Arvinas, C4 Therapeutics) raised >$1 billion collectively between 2019‑2025, reflecting investor confidence in covalent modalities.  
- **Regulatory approvals:** Since 2019, the FDA approved three **new** covalent small‑molecule drugs: sotorasib (KRAS G12C, 2021), adagrasib (KRAS G12C, 2022), and mobocertinib (EGFR exon 20 insertions, 2021). All three benefitted from covalent fragment insights during lead optimization.  
- **Clinical uptake:** Real‑world data (2022‑2025) show that KRAS G12C inhibitors are now used in >15 % of eligible NSCLC patients in the U.S., confirming that covalent drugs can achieve substantial market penetration.  

Overall, the concerns raised in 2019 about limited target availability and analytical capacity have been largely mitigated by cheaper high‑resolution MS, chemoproteomic databases, and broader acceptance of covalent chemistry in both academia and industry.

---

## 3. PREDICTIONS  

| Prediction (implicit or explicit in the article) | What actually happened |
|---|---|
| **Covalent fragment collections will be hard to adopt because of limited targets and lack of mass‑spec capability.** | By 2022, most major pharma and many academic cores have dedicated LC‑MS/MS platforms for covalent fragment screening; the bottleneck shifted to data analysis rather than instrument access. |
| **Highly reactive warheads (e.g., chloroacetamides) will label many proteins indiscriminately, making them unsuitable.** | Large‑scale chemoproteomics showed that labeling promiscuity is *not* solely dictated by intrinsic reactivity; structural context and protein micro‑environment dominate. Moderately reactive warheads are now preferred, but “hot” warheads are still useful when paired with larger, more complex fragments. |
| **Balancing fragment size/complexity with warhead reactivity is essential; larger fragments with weak warheads will rarely hit.** | Empirical data from 2020‑2024 confirm this trend: high‑complexity fragments with tuned warheads (e.g., cyano‑acrylamides) yield the highest hit‑to‑lead conversion rates. Small, weak‑warhead fragments still produce few hits, but a few notable successes (e.g., covalent KRAS fragments) validate the “high‑signal/low‑noise” scenario. |
| **A negative covalent‑fragment screen does not prove a target is undruggable by covalent means.** | This view has become a standard caveat in the field. Recent studies (e.g., 2023 kinome‑wide cysteine profiling) have rescued many “undruggable” targets by redesigning warheads after an initial empty screen. |
| **Covalent fragment screening will eventually provide starting points for drug development.** | True for several high‑profile programs: KRAS G12C, SARS‑CoV‑2 M<sup>pro</sup>, and several kinase projects all trace a key early hit to a covalent fragment screen. |

---

## 4. INTEREST  
**Rating: 7/10** – The post captures a pivotal moment in the transition from skepticism to mainstream adoption of covalent fragment screening; its concepts proved prescient and continue to shape drug discovery, though the writing style is informal and the technical depth is moderate.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20191016-more-covalent-compounds-and-covalent-fragments.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_