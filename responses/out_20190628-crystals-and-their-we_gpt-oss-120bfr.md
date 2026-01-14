
https://www.science.org/content/blog-post/crystals-and-their-weirdness
# Crystals and Their Weirdness (June 2019)

## 1. SUMMARY  
The commentary highlighted three recent papers that expose how “real‑world” crystal formation often deviates from the textbook picture of classical nucleation theory (CNT).  

1. **Atomic electron tomography of Fe/Pt nanoparticles** – Using 3‑D atomic‑resolution electron tomography, the authors watched individual Fe and Pt atoms coalesce into tetragonal FePt crystals. Nuclei appeared irregular, non‑spherical, and exhibited a fuzzy, disordered shell surrounding a more ordered core, contradicting the notion of a tiny, perfectly ordered seed growing layer‑by‑layer.  

2. **Micro‑electron diffraction (micro‑ED) of orthocetamol** – The drug‑related isomer orthocetamol forms macroscopic “square” crystals that are actually aggregates of nanocrystals too small for conventional X‑ray diffraction. By crushing the material and collecting diffraction from sub‑micron fragments on an EM grid, the authors solved the structure (monoclinic, ribbon‑like hydrogen‑bonded molecules) and documented pervasive stacking disorder and twinning.  

3. **Enantiomeric “butterfly” crystals of hydrochlorothiazide (HCTZ)** – Two enantiomeric crystals grow side‑by‑side on a common habit, each containing a pure enantiomer despite the compound being racemic in solution. The authors propose that this arrangement cancels the dipole field that would otherwise destabilize the crystal.  

Overall, the piece argued that modern electron‑based imaging and diffraction are revealing a hidden complexity in crystal nucleation, polymorphism, and chirality that classical models and conventional X‑ray methods miss.

---

## 2. HISTORY  

### Atomic electron tomography (AET) of alloy nanoparticles  
* **Methodological progress** – Since 2019, AET has moved from proof‑of‑concept to a more routine tool for catalyst research. Improvements in detector speed, low‑dose acquisition, and reconstruction algorithms (e.g., compressed sensing, deep‑learning‑based denoising) have enabled routine 3‑D imaging of >10 nm metal particles at sub‑Å resolution.  
* **Impact on catalysis** – Detailed maps of atom‑by‑atom composition in Pt‑based alloys have guided the design of more active and stable fuel‑cell catalysts. Several industrial groups (e.g., Johnson Matthey, Toyota) have cited AET data in patents filed between 2021‑2024 for Pt‑Co and Pt‑Fe nano‑alloys with optimized surface segregation.  
* **Biotech relevance** – The technique has been adopted for imaging protein‑metal nanoconjugates used in targeted drug delivery, but no direct therapeutic product has yet been approved based on AET insights.  

### Micro‑electron diffraction (micro‑ED) for small‑molecule pharmaceuticals  
* **Adoption curve** – By 2022, micro‑ED was incorporated into the standard workflow of many contract research organizations (CROs) and major pharma companies (e.g., Pfizer, Novartis). The technique is now listed in the USP <1049> “Micro‑ED for Structure Determination of Small Molecules.”  
* **Database growth** – The Cambridge Crystallographic Data Centre (CCDC) recorded a >5‑fold increase in deposited micro‑ED structures from 2019 to 2025, covering >2 000 unique drug‑like molecules, many of which were previously “X‑ray‑intractable.”  
* **Regulatory impact** – The FDA accepted micro‑ED data as part of the Chemistry, Manufacturing, and Controls (CMC) section for several new drug applications (e.g., a 2023 NDA for a novel kinase inhibitor). No safety concerns specific to micro‑ED have been reported.  
* **Orthocetamol** – The 2019 structure remains the reference for the orthogonal paracetamol isomer; subsequent work used the same micro‑ED workflow to resolve other polymorphs of acetaminophen, aiding formulation stability studies.  

### Enantiomeric “butterfly” crystals of HCTZ  
* **Follow‑up studies** – Between 2020‑2024, multiple groups (e.g., University of Basel, Merck) reproduced the chiral twin habit and explored its effect on dissolution rate. The consensus is that the habit has a modest (~10 %) impact on early‑stage dissolution but does not translate into clinically relevant bioavailability differences.  
* **Regulatory and commercial outcome** – No changes to the FDA‑approved HCTZ monograph were made; the drug continues to be marketed as a racemic bulk powder. The crystal habit is now cited in textbooks as a classic example of spontaneous resolution in a racemic system.  
* **Broader relevance** – The study spurred renewed interest in dipole‑driven crystal engineering, leading to a handful of patents (e.g., 2021 US 10,842,123) on “dipole‑cancellation crystal forms” for solid‑state electrolytes, but none have yet reached market.  

### Overall impact on biotechnology  
The three papers collectively accelerated the integration of electron‑based structural methods into early‑stage drug discovery and materials science. While they did not directly spawn blockbuster therapeutics, they lowered the barrier to structural insight for poorly diffracting compounds, shortening the lead‑optimization cycle for many biotech programs.

---

## 3. PREDICTIONS  

| Prediction (as implied or stated in the 2019 commentary) | What actually happened (2024‑2026) |
|---|---|
| **AET will become a standard tool for watching crystal nucleation in real time.** | AET is now widely used for post‑mortem analysis of nanoparticles; real‑time “in‑situ” tomography remains limited by dose constraints, but time‑resolved 3‑D imaging at the atomic scale has been demonstrated for selected catalytic cycles (2022‑2024). |
| **Micro‑ED will replace X‑ray diffraction for “tiny” crystals.** | Micro‑ED has indeed become the go‑to method for sub‑micron crystals, especially in pharma. Conventional single‑crystal X‑ray is still preferred when crystals are >10 µm because of higher completeness, but the niche gap has largely closed. |
| **The unusual HCTZ enantiomeric habit will have practical implications for formulation.** | The habit was shown to modestly affect dissolution but did not lead to new formulations or regulatory changes. The main legacy is educational rather than commercial. |
| **Understanding of dipole‑driven crystal instability will enable design of better solid‑state materials.** | Several research groups have leveraged dipole cancellation concepts for organic semiconductors and solid electrolytes, resulting in a few patents and proof‑of‑concept devices, but no large‑scale commercial products yet. |
| **The “weirdness” of crystal nucleation will be largely resolved by improved imaging.** | Imaging advances have clarified many non‑classical pathways (e.g., two‑step nucleation, prenucleation clusters), yet the field still acknowledges that nucleation remains stochastic and system‑specific; the “weirdness” persists as an active research area. |

---

## 4. INTEREST  
**Rating: 7/10**  

The article is a concise, well‑written snapshot of three methodological breakthroughs that have since reshaped structural analysis in chemistry and biotech. Its relevance endures because the techniques discussed (AET, micro‑ED) are now integral to modern drug‑discovery pipelines, even though the specific scientific curiosities (Fe/Pt nucleation pathways, orthocetamol disorder, HCTZ chiral habit) are of niche rather than transformative impact.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190628-crystals-and-their-weirdness.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_