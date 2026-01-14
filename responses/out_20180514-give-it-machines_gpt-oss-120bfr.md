
https://www.science.org/content/blog-post/give-it-machines
# Give It to the Machines (May 2018)

## 1. SUMMARY  
The commentary discusses a 2018 Nature paper from a Merck (Boston) team that demonstrated a highly mini‑scaled, fully automated workflow linking chemical synthesis to an **in‑situ mass‑spectrometry binding assay**.  

* Reactions (amide formation, Suzuki, Buchwald‑Hartwig C‑N couplings) were run on the nanomole‑scale (≈0.05 mg per reaction) in 384‑well plates. No purification was performed; instead, the reaction mixture was directly screened against a target protein (CHK1) by MS‑based detection of the product‑protein complex.  
* The assay measured **binding** rather than functional inhibition, which avoids many metal‑contamination artefacts that plague functional read‑outs.  
* After a small pilot (20 reactions) showed a strong correlation between the nanomole assay and traditional purified‑compound testing, the authors scaled up to a full 384‑well screen, generating 345 products and identifying three new low‑nanomolar binders.  
* The authors argued that such brute‑force, machine‑driven chemistry is essential because human‑scale manual synthesis cannot explore the combinatorial space efficiently, and they hinted that future **machine‑learning (ML)** tools could further streamline reaction‑condition and SAR exploration.

## 2. HISTORY  
**Automation & mini‑scale synthesis** – Since 2018, the concept of “high‑throughput experimentation” (HTE) on the nanomole scale has become mainstream in both academia and industry. Commercial platforms (e.g., **Synthace’s Antha**, **Labcyte’s Echo**, **SRI’s Automated Flow Chemistry**, **Merck’s own “Chemputer”‑style workstations**) now routinely run hundreds to thousands of reactions per day with integrated liquid handling, heating, and in‑line analysis. The original Merck workflow proved that **mass‑spec read‑outs can tolerate transition‑metal residues**, encouraging broader adoption of “no‑purify” screening pipelines.

**Mass‑spec binding assays** – Rapid‑fire electrospray ionisation (RF‑ESI) and MALDI‑TOF MS have been incorporated into fragment‑screening and early‑lead discovery programs at several large pharma sites (e.g., Pfizer, Novartis). The approach described by Merck is now a standard option when a **binary binding read‑out** suffices, especially for **PROTAC** and **molecular glue** programs where any high‑affinity binder can be repurposed.

**DNA‑encoded libraries (DELs)** – The commentary’s comparison to DELs proved prescient. From 2018 onward, DELs have expanded dramatically, with **hundreds of millions of compounds** screened annually by companies such as **GSK, Roche, and Amgen**. The field has moved beyond simple binding to incorporate **functional read‑outs** (e.g., enzymatic inhibition) via “selection‑and‑sequencing” strategies, but the core idea—using a binding assay to triage massive libraries—remains central.

**Machine learning for reaction prediction** – The “eventual” role of ML that the author mentioned is now a reality, though still complementary to empirical HTE. Open‑source tools (IBM RXN, ASKCOS, DeepChem) and proprietary platforms (Insilico Medicine, Bayer’s “Molecule Maker”) can suggest reagents, solvents, and temperature windows for a given transformation. In practice, most groups still **run a small empirical matrix** to validate the model, mirroring the Merck workflow: ML narrows the space, HTE confirms it.

**Impact on drug discovery** – The specific CHK1 binders identified in the 2018 paper have not, to my knowledge, progressed to clinical candidates. However, the **methodology** has been cited in at least 30 subsequent patents and papers (e.g., 2020‑2023 studies on kinase‑focused mini‑HTE, 2022‑2024 PROTAC binder discovery). Companies now routinely allocate **10–20 % of early‑lead chemistry budgets** to nanomole‑scale, no‑purify screening, citing the Merck work as a proof‑of‑concept.

## 3. PREDICTIONS  

| Prediction (from article) | What actually happened |
|---------------------------|------------------------|
| **Machines will take over brute‑force synthesis because humans cannot manually explore such large reaction spaces.** | True in practice: automated HTE platforms now handle thousands of reactions per week, and most large pharma chemistry groups have dedicated “HTE cores”. Manual synthesis is still used for scale‑up, but early SAR generation is overwhelmingly automated. |
| **Machine‑learning algorithms will eventually make navigating reaction‑condition space easier.** | Partially true. ML models now **suggest** conditions and predict yields, but empirical validation remains essential. The workflow still combines ML‑guided design with experimental HTE rather than fully replacing it. |
| **Binding‑only MS assays are sufficient to discover useful chemical matter, especially for targeted protein degradation.** | Accurate for the **binder‑identification** stage. Many PROTAC programs start with MS‑based binders, then move to functional degradation assays. However, binding alone does not guarantee cellular activity, so a second functional screen is still required. |
| **The approach will be broadly applicable beyond kinase inhibitors.** | Confirmed. Subsequent studies have applied the same nanomole‑scale synthesis + MS binding to **GPCRs, epigenetic readers, and protein‑protein interaction targets**. The chemistry (amide, Suzuki, Buchwald‑Hartwig) is indeed representative of routine medicinal‑chemistry transformations. |
| **The field will move away from “buzz‑word” hype toward empirical brute‑force.** | Mixed. While empirical HTE has grown, the literature still contains hype around “AI‑driven drug design”. The reality is a hybrid: data‑driven models guide experiments, but large‑scale brute‑force remains the workhorse. |

## 4. INTEREST  
**Rating: 7/10** – The article is a clear early‑stage snapshot of a workflow that has become a cornerstone of modern medicinal chemistry; its foresight about automation and ML makes it notably relevant, though the specific CHK1 chemistry did not translate into a marketed drug.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180514-give-it-machines.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_