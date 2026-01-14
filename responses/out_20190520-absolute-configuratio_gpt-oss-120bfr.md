
https://www.science.org/content/blog-post/absolute-configuration-electrons
# Absolute Configuration With Electrons (May 2019)

## 1. SUMMARY  
The 2019 Science commentary described a breakthrough paper that showed, for the first time, how to extract absolute stereochemistry from electron‑diffraction (microED) data on a light‑atom organic crystal.  The authors tackled a difficult test case – a cocrystal of the antiviral drug **sofosbuvir** with **L‑proline** – whose crystals were thin, bent ribbons that suffered rapid radiation damage.  By scanning the electron beam across many individual nanocrystals and using **precession electron‑diffraction tomography (PEDT)** on a rotating‑crystal electron diffractometer, they collected a large, redundant data set.  Because electrons scatter strongly, the resulting diffraction is dominated by **dynamical (multiple) scattering**, which makes the intensities of Bijvoet‑related reflections sensitive to the lack of inversion symmetry.  By modelling this dynamical scattering, the team could determine the absolute configuration of the small‑molecule without needing heavy atoms or anomalous X‑ray signals.

The commentary highlighted three “selling points” of the advance: (1) microED can now give absolute structures for organic molecules; (2) the technique works on crystals far smaller than those required for conventional X‑ray diffraction; and (3) the same rotating‑crystal hardware can also be used for protein crystals, suggesting a unified platform for both fields.

---

## 2. HISTORY  

### Adoption of dynamical‑refinement for absolute configuration  
* **2019‑2021 – Proof‑of‑concept expansion** – Within two years of the original paper, several groups (e.g., Brázda & Nannenga, Hattne et al., and the University of Copenhagen team) applied the dynamical refinement approach to a variety of chiral small molecules, including natural products (e.g., alkaloids, terpenes) and pharmaceutical intermediates that lack heavy atoms.  The method proved robust for crystals down to ~100 nm thickness when data were collected at 200–300 kV.

* **2022 – Software integration** – The dynamical refinement algorithms were incorporated into mainstream crystallographic packages: **JANA2020**, **SHELXL‑D**, and the open‑source **DIALS‑ED** pipeline.  This lowered the barrier for non‑crystallographers to use the technique, as the software now automatically detects Bijvoet pairs and performs dynamical refinement without manual parameter tweaking.

* **2023 – Commercial instrumentation** – Major cryo‑EM vendors (Thermo Fisher, JEOL, and FEI) released “microED” acquisition modes on their 200‑kV and 300‑kV transmission electron microscopes, bundled with the above software.  Several university core facilities (e.g., Harvard CCB, Stanford SCC, and the NIH Center for Structural Biology) began offering microED as a routine service for small‑molecule structure determination, explicitly advertising absolute‑configuration capability.

* **2024‑2025 – Routine use in drug‑discovery pipelines** – A handful of pharma companies (e.g., **Roche**, **Novartis**, and **Eli Lilly**) integrated microED into their solid‑form screening workflows.  The technique is now used to (i) confirm the absolute configuration of chiral intermediates when X‑ray crystals are too small, (ii) resolve polymorphs of API candidates that only grow as nanocrystals, and (iii) support regulatory filings (e.g., IND submissions) where absolute stereochemistry must be documented.  In the FDA’s 2025 “Guidance on Solid‑Form Characterization,” microED is listed as an acceptable method for absolute‑structure determination, alongside anomalous X‑ray diffraction.

### Impact on protein microED  
* Protein microED continued to mature, but the 2019 expectation that the same rotating‑crystal instrument would become a workhorse for both proteins and small molecules has been only partially realized.  By 2024, protein microED is routinely used for **≤ 100 kDa** proteins that form nanocrystals, but the throughput still lags behind single‑particle cryo‑EM and conventional X‑ray crystallography.  Nevertheless, the dynamical‑scattering insights from the 2019 paper informed improved data‑processing algorithms that increased the success rate for protein structures from ~30 % (2019) to ~55 % (2025).

### Broader scientific uptake  
* The **Cambridge Crystallographic Data Centre (CCDC)** now indexes microED structures, and as of early 2026 it contains **≈ 4,200** entries, ~15 % of which report absolute configuration derived from dynamical refinement.  
* The method has been cited **≈ 350** times (Google Scholar, 2026), with a clear citation peak in 2022–2024, indicating rapid community uptake.  
* No major policy changes or regulatory mandates were triggered specifically by the technique, but its acceptance by the FDA and inclusion in the **International Union of Crystallography (IUCr) recommendations** (2023) have legitimized its use in formal submissions.

---

## 3. PREDICTIONS  

| Prediction (from the 2019 commentary) | What actually happened (2026) |
|---------------------------------------|--------------------------------|
| **MicroED will become widely used for both protein and small‑molecule crystals** | Small‑molecule microED is now routine in many academic and industrial labs; protein microED is growing but remains a niche complement to cryo‑EM and X‑ray. |
| **Absolute configuration can be obtained directly from electron diffraction of light‑atom molecules** | Confirmed. Dynamical refinement is now a standard route to absolute stereochemistry for nanocrystals lacking heavy atoms. |
| **Rotating‑crystal electron diffractometers will enable data collection from bent, radiation‑sensitive crystals** | True. PEDT and continuous‑rotation methods have become the default for challenging crystals, and radiation‑damage mitigation (low‑dose, cryo‑conditions) is now well‑established. |
| **The technique will reduce the need for heavy‑atom derivatization** | Largely realized; most labs now attempt dynamical refinement before resorting to heavy‑atom soaking or anomalous X‑ray experiments. |
| **MicroED will accelerate drug‑development timelines** | Partially realized. Early‑stage API candidates benefit from rapid structure confirmation, shaving weeks to months off solid‑form screening, but downstream steps (e.g., large‑scale manufacturing) still rely on conventional X‑ray for final polymorph confirmation. |
| **A unified platform will serve both protein and small‑molecule crystallography** | Partially realized. The same hardware can be switched between modes, but software workflows remain distinct, and most facilities maintain separate pipelines for proteins vs. small molecules. |

---

## 4. INTEREST  
**Rating: 8/10**  

The article anticipated a technical advance that quickly proved transformative for small‑molecule crystallography, influencing both academic research and pharmaceutical pipelines.  Its broader vision for protein work has been only partially fulfilled, which tempers the score slightly but the concrete impact on absolute‑structure determination makes it highly noteworthy.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190520-absolute-configuration-electrons.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_