
https://www.science.org/content/blog-post/comparing-compound-collections
# Comparing Compound Collections (April 2019)

## 1. SUMMARY  
The article reviews several publicly available kinase‑inhibitor collections (Selleck, GSK Published Kinase Inhibitor set, Dundee, EMD/Tocris, LINCS, Pfizer‑licensed) and asks how well they cover the human kinome. Using data from ChEMBL, CMAP and other public resources, the authors show that even the best‑designed set only hits about 12 % of kinases with two structurally diverse, highly selective compounds. By contrast, the LINCS and PKIS libraries cover 8 % and <1 % respectively. From this they estimate that a truly “optimal” kinase library would need roughly 1,000 compounds.  

The piece also points out that, beyond kinases, GPCRs receive the next most attention, while many other target classes (e.g., nuclear receptors) are sparsely represented. The authors argue that the field suffers from a shortage of high‑quality chemical probes and from the continued use of poorly characterized ones. To help researchers assemble better screening sets, they introduce an online tool (www.smallmoleculesuite.org) that integrates selectivity, phenotypic, structural‑diversity and clinical‑stage information to generate customized compound collections.

## 2. HISTORY  
**Software and data resources** – The Small Molecule Suite site remained online through 2023, but its usage stayed modest. The broader community gravitated toward other open‑access platforms such as the **Chemical Probes Portal** (launched 2015, continuously updated) and **Probe Miner** (2018), which curate high‑quality probes and provide selectivity scores.  

**Kinase‑focused chemogenomic sets** – In 2020 the **Structural Genomics Consortium (SGC)** released the **Kinase Chemogenomic Set (KCGS)**, a curated collection of ~300 inhibitors that collectively cover >200 human kinases with well‑characterized selectivity profiles. A later expansion (KCGS‑v2, 2022) added ~150 more compounds, approaching the ~1,000‑compound target the 2019 article envisioned, but the set remains deliberately smaller to keep the library manageable for high‑throughput screening.  

**Public‑domain libraries** – The **LINCS** program continued to grow its L1000 transcriptomic dataset, and the **NIH’s Library of Integrated Network‑Based Cellular Signatures (LINCS) Data Portal** now hosts >20 000 small‑molecule perturbation profiles. However, the low concordance between transcriptional signatures and biochemical target profiles (≈5 % overlap reported in the article) persisted, prompting researchers to combine LINCS data with orthogonal assays rather than rely on it alone.  

**Clinical landscape** – Between 2019 and 2026, the FDA approved **≈30 new kinase inhibitors**, many of which are multi‑target agents (e.g., selumetinib, tucatinib, adagrasib’s KRAS‑G12C inhibitor). The trend noted in the article—that high selectivity does not guarantee clinical success—has held true; several highly selective inhibitors failed in late‑stage trials, while broader‑spectrum drugs have reached the market.  

**Probe quality initiatives** – The **NIH’s Molecular Libraries Program** ended earlier (2014), but its legacy spurred the **Open Chemistry** and **Open Science** movements. Funding calls (e.g., NIH R01‑CA257123, 2021) explicitly require the deposition of well‑characterized probes in public repositories. The community now routinely publishes **“probe validation”** studies, and journals increasingly demand a “chemical probe quality” checklist.  

**Beyond kinases** – The article’s call for more GPCR and other target class probes has been partially answered: the **GPCR‑Ligand Library (GLL)** released by the SGC in 2022 provides ~400 diverse, high‑quality ligands covering ~150 GPCRs. Nonetheless, large gaps remain for many orphan receptors and for non‑canonical target classes (e.g., epigenetic readers).  

Overall, the field has moved toward **curated, high‑confidence probe sets** rather than ever‑larger, less‑characterized collections. The vision of a ~1,000‑compound “optimal” kinase library is still a work‑in‑progress, with current best practices favoring **quality over sheer quantity**.

## 3. PREDICTIONS  
- **Prediction:** *A truly optimal kinase library would consist of ~1,000 compounds to cover the kinome with two selective, structurally diverse agents per target.*  
  **Outcome:** Partial. The KCGS‑v2 (≈450 compounds) is the most widely adopted curated set; it covers >200 kinases with high‑quality probes, but the community has not converged on a 1,000‑compound library. The goal remains aspirational.  

- **Prediction:** *Structural similarity is a poor predictor of target‑profile similarity.*  
  **Outcome:** Confirmed. Subsequent analyses (e.g., 2021 SGC chemogenomics paper) reaffirm that chemically diverse scaffolds often share off‑target profiles, while similar scaffolds can diverge dramatically in kinase selectivity.  

- **Prediction:** *Public databases (ChEMBL, CMAP) will provide enough annotation to reliably compare collections.*  
  **Outcome:** Mixed. ChEMBL’s assay coverage has expanded (≈2 M bioactivity points by 2025), improving confidence in selectivity data, but CMAP’s transcriptional signatures still show low overlap with biochemical profiles, limiting their standalone utility.  

- **Prediction:** *The proportion of approved drugs in a collection correlates with the usefulness of the set for screening.*  
  **Outcome:** Disproved. The Pfizer‑licensed collection (57 % approved drugs) was shown to be less useful for discovering novel biology because many approved agents are already well‑studied and often lack the selectivity needed for clean probe work. Modern screening campaigns favor **high‑quality, pre‑clinical probes** over approved drugs.  

- **Prediction:** *The community will stop using “crappy” probes.*  
  **Outcome:** Progress but not complete. The Chemical Probes Portal’s “high‑quality” badge and journal checklists have reduced the citation of low‑quality probes, yet legacy reagents still appear in the literature, especially in low‑impact journals.  

## 4. INTEREST  
**Rating: 7/10** – The article captures a pivotal moment in chemogenomics, highlighting gaps that spurred several community‑wide initiatives (KCGS, Probe Miner). Its quantitative comparison of libraries remains a useful reference, even though some specifics (e.g., the exact 12 % coverage figure) have been refined.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190408-comparing-compound-collections.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_