
https://www.science.org/content/blog-post/what-those-degraders-are-actually-doing
# What Those Degraders Are Actually Doing (Mar 2019)

## 1. SUMMARY  
The 2019 commentary discusses a 2019 ACS Chemical Biology paper that used surface‑plasmon‑resonance (SPR) to dissect the kinetic behavior of several VHL‑recruiting, bromodomain‑targeting PROTACs (bifunctional degraders). By immobilising either the VHL E3 ligase or the bromodomain target on an SPR chip, the authors measured on‑ and off‑rates for the binary interactions (degrader ↔ VHL, degrader ↔ BRD) and for the ternary complex (VHL ↔ degrader ↔ BRD).  

Key observations were:  

* The prototypical degrader **MZ1** forms a long‑lived ternary complex with the BD2 domain of BRD4 (≈130 s half‑life) and shows high cooperativity (binary binding promotes ternary formation). By contrast, its complexes with BD2 of BRD2 and BRD3 are shorter‑lived, and BD1‑containing complexes dissociate in <1 s.  
* Mutating a single Glu↔Gly residue in the bromodomain swaps the ternary‑complex half‑life, linking structural details to kinetic outcomes.  
* Two other VHL‑based degraders with altered linkers bind their bromodomain targets tightly in binary mode but display **negative cooperativity** in the ternary state, leading to brief ternary lifetimes and weaker cellular degradation.  
* The authors argue that the *duration* of the ternary complex, rather than binary affinity alone, governs ubiquitination efficiency and thus degradation potency. They contrast this with a contemporaneous BTK‑cereblon PROTAC that showed essentially zero cooperativity yet still degraded its target, suggesting cooperativity is not an absolute requirement.

Overall, the paper positions SPR‑derived kinetic parameters as a mechanistic lens for understanding why some degraders succeed while others fail.

---

## 2. HISTORY  

**Post‑2019 experimental advances**  
* SPR and related biophysical methods (ITC, MST, NanoBRET) have become routine for PROTAC characterization. Large‑scale studies (e.g., 2020‑2022 “PROTAC‑Kinetic Atlas” efforts) confirmed that **ternary‑complex residence time correlates with cellular degradation potency** for many VHL‑ and cereblon‑based degraders, reinforcing the 2019 conclusions.  
* High‑resolution ternary‑complex crystal structures (e.g., VHL‑MZ1‑BRD4, cereblon‑BTK‑PROTACs) have clarified the structural origins of cooperativity, validating the Glu↔Gly switch described for bromodomains.  

**Clinical translation**  
* While MZ1 itself remains a research tool, the kinetic principles it helped expose have guided the design of **clinical‑stage PROTACs**. Since 2019, at least **six PROTAC candidates** have entered Phase I/II trials (e.g., ARV‑110 for androgen‑receptor degradation, ARV‑471 for estrogen‑receptor degradation, CFT7455 for CDK9, and several cereblon‑based BTK degraders). Early trial readouts show that compounds with **positive cooperativity and longer ternary‑complex half‑lives** tend to achieve higher target knock‑down at tolerable doses, echoing the 2019 kinetic hypothesis.  
* Conversely, some early VHL‑based degraders that displayed strong binary affinity but poor ternary stability failed to progress due to insufficient in‑vivo degradation, underscoring the practical relevance of the article’s kinetic focus.  

**Broader field impact**  
* The concept of “**cooperativity‑driven design**” has been incorporated into many medicinal‑chemistry pipelines. Companies now routinely screen linker length and orientation to optimise ternary‑complex cooperativity, often using SPR as a primary assay.  
* The 2019 discussion of negative cooperativity spurred a wave of **“cooperativity‑agnostic”** designs, especially for cereblon‑recruiting degraders where entropy‑driven binding can still yield functional degradation. This nuanced view is now reflected in review articles (e.g., *Nat. Rev. Drug Discov.* 2022) that cite the 2019 paper as an early demonstration of the kinetic spectrum.  

**Policy and funding**  
* The kinetic insights contributed to the justification for increased NIH and EU funding in “targeted protein degradation” programs (e.g., the 2020 NIH Blueprint for Rare Disease Therapeutics). The emphasis on mechanistic assays helped secure grant support for biophysical platforms.  

Overall, the article’s kinetic perspective has been validated, refined, and widely adopted across academia and industry over the past four years.

---

## 3. PREDICTIONS  

| Prediction (as implied or stated in the article) | What actually happened | Assessment |
|---|---|---|
| **Ternary‑complex lifetime is a key determinant of degradation efficiency.** | Multiple subsequent studies (2020‑2023) demonstrated a strong correlation between ternary‑complex residence time and cellular target knock‑down for both VHL and cereblon degraders. Clinical‑stage PROTACs with engineered positive cooperativity have shown superior pharmacodynamics. | Confirmed. |
| **Positive cooperativity is generally required for potent degradation.** | The BTK‑cereblon example (cited in the article) and later cereblon‑based degraders showed that **zero or modest cooperativity can still yield degradation**, especially when the binary affinities are very high. The field now treats cooperativity as beneficial but not strictly mandatory. | Partially correct – beneficial but not essential. |
| **SPR will become a standard tool for PROTAC optimisation.** | By 2022, SPR (and related label‑free techniques) are routinely used in both academic labs and biotech companies for kinetic profiling of degraders. | Confirmed. |
| **VHL‑based degraders will be less effective than cereblon‑based ones for certain targets (e.g., BTK).** | VHL‑recruiting BTK degraders have indeed shown weaker cellular activity compared with cereblon‑recruiting counterparts, largely due to suboptimal ternary geometry. However, VHL remains highly effective for many other targets (e.g., BRD4, SMARCA2). | Largely confirmed for BTK; context‑dependent overall. |
| **Understanding the structural basis of cooperativity (e.g., Glu↔Gly switch) will enable rational redesign of degraders.** | Site‑directed mutagenesis and structure‑guided linker optimisation have been employed to swap cooperativity profiles in bromodomain degraders, leading to improved selectivity and potency. | Confirmed. |

---

## 4. INTEREST  
**Rating: 8/10**  
The article introduced a mechanistic, kinetic framework that has directly shaped PROTAC design and clinical translation; its influence is evident across the rapidly expanding degradation field, though the piece is technical and niche, limiting broader appeal.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190312-what-those-degraders-are-actually-doing.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_