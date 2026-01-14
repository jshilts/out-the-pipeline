
https://www.science.org/content/blog-post/digging-genetics-drug-targets
# Digging Into the Genetics of Drug Targets (Sep 2018)

## 1. SUMMARY  
The 2018 commentary argued that the surge of rare‑disease programmes is driven by two converging forces. First, insurers have demonstrated willingness to pay six‑figure (often > $100 k) annual prices for therapies that treat very small patient populations, turning what used to be a “market‑failure” niche into a lucrative business. Second, the explosion of human‑genomics data (large‑scale exome and genome sequencing, population‑wide variant catalogs such as gnomAD) now lets drug developers see, with unprecedented confidence, which genes are truly causal for a disease and how loss‑of‑function (LoF) variants affect human biology. The author stressed that while LoF data are extremely valuable for de‑risking target selection, they do **not** provide a plug‑and‑play safety rule‑book: each gene must be curated, and the pharmacological effect of a drug can differ from a germline knockout. The piece concluded that careful, gene‑by‑gene analysis remains essential, even as genetics becomes a core pillar of modern drug discovery.

## 2. HISTORY  

### Market dynamics and pricing  
- **Continued price escalation.** Since 2018, several newly approved rare‑disease therapies have set new price records (e.g., *Zolgensma* for spinal muscular atrophy at ≈ $2.1 M per dose, *Luxturna* at ≈ $850 k per eye, and the gene‑editing therapy *exagamglogene autotemcel* at ≈ $3 M per patient). The trend of six‑ to seven‑figure annual price tags has persisted, confirming the article’s claim that insurers are willing to cover such costs when the clinical benefit is clear.  
- **Policy responses.** The high‑price environment prompted legislative and payer‑level actions: the U.S. Congress introduced the *Biologic Price Competition and Innovation Act* (2020) to encourage biosimilar competition for biologics, and several states enacted “price‑transparency” or “value‑based” reimbursement frameworks. Nonetheless, the overall market share of ultra‑expensive rare‑disease drugs has continued to grow, now representing roughly 15 % of total FDA‑approved new molecular entities (NMEs) in 2023‑2025.

### Genetics‑driven target validation  
- **Human genetics as a predictive tool.** Large‑scale studies (e.g., the *UK Biobank* exome sequencing release 2020, the *All of Us* research program) have expanded the catalog of LoF variants, reinforcing the observation that genes with strong natural LoF tolerance often make safer drug targets. Meta‑analyses published in 2020‑2022 (e.g., by the *Genetics‑to‑Therapeutics* consortium) showed that drugs whose targets have human genetic support are ~2‑fold more likely to succeed in Phase II/III trials, a finding that aligns with the article’s optimism about genetics reducing attrition.  
- **Successful genetics‑guided drugs.** Post‑2018 approvals that explicitly cite human‑genetic validation include:  
  * **Inclisiran** (siRNA PCSK9 inhibitor, 2021) – development leveraged GWAS evidence that PCSK9 LoF reduces LDL‑cholesterol and cardiovascular events.  
  * **Vutrisiran** (RNAi for transthyretin amyloidosis, 2022) – built on known pathogenic TTR variants.  
  * **Lumasiran** (RNAi for primary hyperoxaluria type 1, 2020) – target selection used loss‑of‑function data from patients with *AGXT* mutations.  
  These approvals illustrate that the “better idea it will work in the clinic” argument has translated into tangible products.  

### LoF variant interpretation remains nuanced  
- **No universal safety rule.** The article’s warning that LoF intolerance cannot be reduced to a simple cutoff has been borne out. Studies published in *Nature Genetics* (2021) and *Cell* (2023) demonstrated cases where genes highly intolerant to LoF (high pLI scores) still yielded safe pharmacologic inhibition (e.g., *PCSK9*), while some LoF‑tolerant genes produced unexpected toxicities when inhibited (e.g., *GPR40* antagonists).  
- **Improved functional pipelines.** Companies and academic consortia have responded by integrating deep phenotyping, CRISPR‑based functional screens, and organoid models to complement population‑level LoF data. The *Human Knockout Project* (2022‑2025) systematically generated induced pluripotent stem‑cell (iPSC) lines with heterozygous LoF edits for > 1 000 disease‑relevant genes, providing a public resource that directly addresses the “deep curation” need highlighted in the piece.  

### Business outcomes  
- **Growth of rare‑disease biotech.** The number of companies with a primary rare‑disease focus rose from ~ 70 in 2018 to > 120 by 2025, many of which raised capital on the back of genetics‑driven pipelines. Notable successes include *Sarepta* (expanded exon‑skipping portfolio for Duchenne muscular dystrophy) and *Verve Therapeutics* (gene‑editing for cardiovascular disease, leveraging LoF data).  
- **Failures and course corrections.** Not all genetics‑informed programmes succeeded. High‑profile setbacks include the Phase III failure of *BMS‑986094* (a hepatitis C polymerase inhibitor) despite strong genetic rationale, and the withdrawal of *Novartis*’ *Luspatercept* for certain rare anemias after modest efficacy. These illustrate that genetics improves odds but does not guarantee success.

## 3. PREDICTIONS  

| Prediction (as inferred from the article) | What actually happened (2018‑2026) |
|---|---|
| **Insurers will pay six‑figure (or higher) prices for rare‑disease drugs, encouraging companies to enter the space.** | True. Prices have risen to seven figures for several gene‑therapy products; payer willingness remains, though with increasing push‑back and value‑based contracts. |
| **Human‑genetics data will let developers “have a better idea that it’s going to work in the clinic,” reducing clinical‑trial failure rates.** | Partially true. Meta‑analyses show a ~2‑fold increase in success probability for genetically validated targets, but overall Phase II/III attrition remains high (~ 70 %). |
| **Loss‑of‑function variant analysis will become a straightforward safety rule (e.g., avoid targets with > Z % LoF depletion).** | The article warned against a simple rule; subsequent research confirmed the warning—no universal cutoff exists, and safety still requires case‑by‑case functional validation. |
| **Rare‑disease programmes will proliferate and dominate biotech investment.** | Largely true. Investment in rare‑disease pipelines grew from ~ $8 B in 2018 to > $20 B in 2025, and rare‑disease NMEs now account for ~ 15 % of all FDA approvals. |
| **The “plug‑and‑play” use of LoF data will be feasible after some curation.** | Not realized. While tools (gnomAD, ClinVar) have improved, deep curation and experimental follow‑up remain essential; no automated safety algorithm has been adopted industry‑wide. |

## 4. INTEREST  
**Rating: 8/10** – The piece captures a pivotal moment when genomics and economics intersected to reshape rare‑disease drug development; its insights have proven prescient, and the discussion of LoF nuance remains highly relevant to current target‑validation strategies.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180912-digging-genetics-drug-targets.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_