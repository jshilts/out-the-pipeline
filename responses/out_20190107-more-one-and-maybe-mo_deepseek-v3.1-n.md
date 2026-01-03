
https://www.science.org/content/blog-post/more-one-and-maybe-more
# More Than One, And Maybe More Than That (January 2019)

## 1. SUMMARY

This article discusses a fundamental limitation in how medicinal chemists interpret X-ray crystallography structures of small-molecule ligands bound to protein targets. The author explains that protein-ligand crystal structures rarely achieve the high resolution that non-crystallographers assume, largely because the electron density for ligands often appears as a "blob" representing an average of multiple possible binding modes rather than a single, well-defined conformation. Traditional presentations of Protein Data Bank (PDB) structures typically model ligands in a single position with measures of atomic displacement, but this simplification masks the reality that ligands can adopt multiple conformations with different occupancies.

The article highlights a new computational tool called qFit-ligand designed to address this problem by systematically identifying alternative ligand conformations through rotational, translational, and conformational searches. The tool was tested on known datasets and shown to detect multiple conformations that were previously unreported, including some with dramatically different binding modes that could be "actionable for drug design." The underlying message is that crystallographic structures should be viewed as models subject to interpretation rather than definitive representations of reality.

## 2. HISTORY

Following the 2019 article, the awareness and tools for analyzing ligand conformational heterogeneity in crystallography have continued to evolve, though progress has been methodologically focused rather than revolutionary in drug discovery outcomes. The qFit-ligand approach represents part of a broader movement toward ensemble-based structure modeling in structural biology, gaining traction among crystallographers but not fundamentally transforming most medicinal chemistry workflows, which still rely heavily on single-conformer models for practical reasons.

However, the documented problem of incomplete annotation of alternate conformations persists in the PDB. Subsequent validation studies and community discussions have reinforced that ligand conformational heterogeneity remains underreported, which can mislead structure-based drug design when key interactions are missed or misinterpreted. The field has seen continued development of computational tools to address uncertainty in experimental structures, with methods like qFit-ligand being part of a toolkit that specialists use but has not seen universal adoption.

The specific examples highlighted in the article (5EZX→6DMI and 5CFW→6DMJ) remain as illustrative cases of how reanalysis can reveal new biology. The bromodomain inhibitor example (BRD4) has particular relevance because bromodomain inhibitors were already under active development around 2019 for oncology applications, with several candidates in clinical trials. Understanding alternative binding modes could theoretically help optimize selectivity or potency, though it is difficult to trace direct impact from a single improved structure to specific drug design decisions or clinical outcomes.

From a broader industry perspective, the limitations of crystallography have become part of routine medicinal chemistry training, but traditional single-conformer interpretations remain dominant in most drug discovery programs due to practical constraints in data analysis and decision-making timelines. The article's emphasis on critical thinking about structural data aligns with ongoing efforts to include uncertainty quantification in structure-based design.

## 3. PREDICTIONS

The article was primarily explanatory rather than predictive, focusing on describing an existing methodological issue and a computational solution. However, it did carry some implicit expectations about the future:

• **Improved recognition of conformational heterogeneity**: The article anticipated that better tools would reveal ligand multiconformers more frequently. **Outcome**: Detection methods have improved, and conformational heterogeneity is more widely acknowledged among structural biologists, but the fundamental issue persists due to the inherent complexity of crystallographic data and publication practices that still favor single-conformer interpretations for clarity.

• **Greater application of alternative-conformation-aware design**: The "actionable for drug design" comment about the BRD4 example suggested that understanding multiple conformations would lead to better inhibitors. **Outcome**: While bromodomain inhibitors continued to advance in clinical development, it is difficult to attribute specific design improvements directly to qFit-ligand-type analyses. Structure-guided optimization remains important, but practical drug discovery often prioritizes simpler interpretable models for decision-making speed.

• **Increased computational scrutiny of PDB entries**: The article implied that routine reanalysis could benefit many existing structures. **Outcome**: Various groups have developed computational pipelines to assess and validate PDB entries, including ligand modeling quality. However, these efforts remain largely specialist tools rather than standard practice for most researchers using structural data, due to the technical complexity and resource requirements.

• **Mindset shift toward viewing structures as models**: The philosophical point that "X-ray crystallographic data really are...models...not messages from the Gods" expected greater appreciation of uncertainty. **Outcome**: This perspective has gained wider acceptance in structural biology, with increased emphasis on validation metrics and uncertainty estimates in structure publications, though the practical impact on how most medicinal chemists use structures remains limited by workflow constraints.

## 4. INTEREST

Rating: **5/10**

This article addresses an important technical issue in structural biology with practical implications for drug design, though its impact has been confined primarily to specialist audiences. While the specific computational tool and examples are noteworthy, the broader topic offers relatively modest long-term importance compared to transformative developments in drug discovery. The rating reflects solid but niche relevance to structural chemists, without broader implications for patient outcomes or major advances in medicine.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20190107-more-one-and-maybe-more.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_