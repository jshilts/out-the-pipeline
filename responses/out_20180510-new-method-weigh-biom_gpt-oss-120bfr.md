
https://www.science.org/content/blog-post/new-method-weigh-biomolecules
# A New Method to Weigh Biomolecules (May 2018)

## 1. SUMMARY  
The 2018 commentary highlighted a newly reported technique called **iSCAMS** (interferometric scattering mass spectrometry) from a large Oxford‑led team. By measuring the interferometric scattering of visible light from single biomolecules on a surface, the method claims to convert the scattering signal directly into molecular mass with ~1–2 % accuracy, independent of shape. The authors demonstrated the approach on a variety of proteins, lipid nanodiscs, and heavily glycosylated HIV‑Env complexes, and suggested that iSCAMS could become a label‑free alternative to SPR for studying protein‑protein interactions, potentially even reaching single‑molecule kinetic measurements. They noted current limitations: insufficient sensitivity for small‑molecule binding and the likely impossibility of applying the method inside living cells.

## 2. HISTORY  
**Commercialisation and adoption** – Within two years of the paper, the Oxford group spun out a company (Refeyn Ltd.) that marketed the technology under the name **mass photometry**. Commercial instruments (e.g., Refeyn OneMP) have been sold to academic and biopharma labs worldwide. By 2023, dozens of publications reported using mass photometry for:  

* Determining oligomeric states of purified proteins and membrane protein complexes in detergent or nanodiscs.  
* Measuring binding stoichiometries and apparent dissociation constants for antibody‑antigen, protein‑protein, and protein‑nucleic‑acid interactions.  
* Rapid quality‑control of therapeutic antibodies (detecting aggregates, fragments, and heterogeneity).  

**Technical refinements** – Subsequent work improved the scattering model to account for refractive‑index variations of glycans and lipids, extending reliable mass ranges from ~20 kDa up to ~5 MDa. Faster cameras and better vibration isolation have reduced the detection limit to ~10 kDa for some setups, but routine detection of sub‑100 Da small molecules remains out of reach.  

**Kinetic measurements** – Researchers have demonstrated “real‑time” binding assays by monitoring the appearance and disappearance of individual particles on the surface, extracting on‑ and off‑rates for strong (nanomolar) interactions. However, the kinetic precision is still lower than that of SPR or biolayer interferometry, and the method is best suited for interactions that cause a clear mass change (e.g., dimerisation, antibody binding).  

**In‑cell applications** – No published work has achieved true intracellular iSCAMS/mass photometry. The signal‑to‑noise problem in the crowded cytoplasm remains a major barrier, and the technique is still confined to surface‑immobilised, purified samples.  

**Impact on the field** – While iSCAMS has not become a universal replacement for existing biophysical tools, it carved out a niche as a rapid, label‑free “mass ruler” for single molecules. Its influence is evident in the growing number of structural‑biology pipelines that include a mass‑photometry step before cryo‑EM or X‑ray crystallography to assess sample homogeneity. No regulatory or policy changes stemmed directly from the method, and it has not been linked to any approved therapeutics.

## 3. PREDICTIONS  

| Prediction (from the 2018 article) | What actually happened |
|------------------------------------|------------------------|
| **iSCAMS will enable single‑protein kinetic (on/off‑rate) measurements comparable to SPR.** | Partial success: kinetic data can be extracted for strong, high‑mass interactions, but the precision and throughput are still inferior to SPR. The prediction was optimistic. |
| **The technique will eventually detect small‑molecule binding to individual proteins.** | Not realized as of early 2026. Sensitivity improvements have lowered the mass detection limit, but sub‑100 Da ligands remain below reliable detection thresholds. |
| **Application inside living cells will become feasible.** | No credible reports; the method remains limited to surface‑immobilised, purified samples. |
| **iSCAMS will become a widely adopted complement to existing binding assays.** | True to a moderate extent: mass photometry is now a common ancillary tool in many biochemistry labs, especially for assessing oligomeric state and sample heterogeneity, but it has not displaced SPR, ITC, or BLI for routine kinetic work. |
| **The method will work equally well for glycosylated proteins and lipid nanodiscs.** | Confirmed. Subsequent studies validated accurate mass measurements for heavily glycosylated antibodies, viral envelope proteins, and membrane proteins reconstituted in nanodiscs. |

## 4. INTEREST  
**Rating: 7/10** – The article introduced a genuinely novel, label‑free single‑molecule mass measurement that has since matured into a useful commercial technology (mass photometry). Its long‑term relevance is solid for structural biology and biopharma quality control, though the more ambitious predictions (cellular imaging, small‑molecule detection) have not materialised.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180510-new-method-weigh-biomolecules.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_