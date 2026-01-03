
https://www.science.org/content/blog-post/new-factor-protein-folding
# A New Factor in Protein Folding (May 2017)

## 1. SUMMARY

The article discusses the discovery of a previously unknown weak intramolecular interaction in proteins: C-H bonds interacting with the pi bonds in carbonyl groups. Researchers detected very small coupling constants in 2D NMR (HMQC) spectra, specifically observing methyl groups in amino acids like valine showing through-space interactions with appropriately positioned backbone carbonyl groups. 

The author notes that protein folding remains a "famously horrendous problem" despite progress in semi-empirical approaches. This newly discovered interaction represents another small but potentially significant factor to consider in protein folding calculations, alongside the many enthalpic and entropic terms that determine protein structure. The discovery required specific isotopic labeling to achieve sufficient signal-to-noise ratios, and researchers suggested that similar interactions likely exist involving OH groups and other moieties, representing a new class of weak hydrogen-bond-like interactions.

## 2. WHAT ACTUALLY HAPPENED

Since the article was published in May 2017, sigma-hole interactions (including C-H···carbonyl contacts) have indeed become recognized as a distinct class of noncovalent interactions in structural biology and protein chemistry.

**Research Development**: These weak interactions are now routinely identified in high-resolution protein structures, particularly as cryo-electron microscopy has advanced to near-atomic resolution. The C-H···O=C contacts fall under the broader category of "sigma-hole" bonding, which includes halogen bonding and chalcogen bonding.

**Practical Impact**: While these interactions individually contribute only 0.5-2 kcal/mol of stabilization energy, their cumulative effect in protein folding and molecular recognition has been validated. However, they have not revolutionized protein structure prediction or drug design in the dramatic way the article tentatively suggested. 

**Methodological Integration**: Such interactions are now incorporated into modern molecular mechanics force fields and structure prediction algorithms, including those used in AlphaFold2 and Rosetta, though primarily as small correction terms rather than major structural determinants.

**Clinical/Drug Development**: This discovery has not led to any FDA-approved drugs or specific therapeutic breakthroughs. While it improved fundamental understanding of molecular recognition, practical drug development continued focusing on stronger, more classical interactions like hydrogen bonds, ionic interactions, and hydrophobic effects.

## 3. HOW THE PREDICTIONS FARED

• **Prediction**: The article suggested this could be "a new way to interrogate protein structures in solution" with broad applicability across different labeling experiments.

**Outcome**: **Partially accurate**. Such NMR-detected weak interactions are now used in specialized structural biology studies, particularly for characterizing intrinsically disordered proteins and protein dynamics. However, this has not become a routine, widely adopted method for general protein structure determination, as X-ray crystallography and cryo-EM remain dominant.

• **Prediction**: Implicit suggestion that this discovery would add significant new considerations to protein folding calculations.

**Outcome**: **Accurate but modest impact**. These interactions are indeed incorporated into modern folding algorithms and force fields, but as minor correction terms rather than transformative additions. They contribute to improved accuracy at the margins but haven't fundamentally changed protein structure prediction, especially given AlphaFold2's revolution starting in 2020.

• **Prediction**: The author wondered about finding more such interactions with OH groups and other moieties.

**Outcome**: **Accurate**. Research has expanded to characterize a broader family of sigma-hole interactions involving various atom types and geometries, including sulfur-mediated contacts and other weak interactions that were previously overlooked.

## 4. INTEREST

Rating: **6/10**

This discovery represents genuine scientific progress in understanding fundamental protein chemistry, but its practical impact has been incremental rather than transformative. The weak nature of these interactions limits their significance compared to stronger forces that dominate protein stability and drug binding.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20170524-new-factor-protein-folding.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_