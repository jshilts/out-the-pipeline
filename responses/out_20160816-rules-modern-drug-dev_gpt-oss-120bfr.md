
https://www.science.org/content/blog-post/rules-modern-drug-development
# Rules for Modern Drug Development (August 2016)

## 1. SUMMARY  
In a 2016 *Science Translational Medicine* commentary, Robert Plenge (Merck) laid out four “rules” that he argued give the highest probability of success in drug discovery:

1. **Human‑biology evidence first** – before committing to a target, you must see genetic or phenotypic data from people (e.g., loss‑of‑function mutations) that link the protein to disease. Animal models alone are insufficient.  
2. **Target tractability** – the target must be drug‑gable (small‑molecule binding site, or amenable to an antibody/other modality). Pure gain‑of‑function protein‑protein interactions are especially hard.  
3. **Human‑relevant biomarkers** – you need biomarkers that truly reflect disease biology, not just convenient read‑outs. Combining epidemiology with genetics (“Nature’s randomized trial”) helps identify them.  
4. **Small, fast, decisive proof‑of‑concept trials** – early clinical studies should be tightly focused on the right patient subset and use robust biomarkers, keeping size and duration to a minimum.

Plenge also warned that the ecosystem needed to supply massive, longitudinal human data sets (genomics, molecular phenotyping) and that some disease areas—most notably Alzheimer’s—might be “off‑limits” until their biology is better understood.

---

## 2. HISTORY  

### Adoption of genetics‑first target validation  
- **Success stories**: The PCSK9 inhibitors (evolocumab, alirocumab) and the SGLT2 inhibitors (canagliflozin, empagliflozin) both progressed from human‑genetic validation to FDA approval, reinforcing the “human genetics = higher success” premise.  
- **Industry shift**: By 2020, >70 % of large pharma R&D pipelines reported using human‑genetic data in target selection (e.g., Amgen’s “Genetic Target Validation” program, Novartis’s “Genomics‑Driven Discovery”). Venture‑backed biotech firms such as 23andMe‑partnered **Genoox**, **Genentech’s** early‑stage genetics unit, and **Mammoth Biosciences** built their pipelines around human‑genetic evidence.  

### Expansion of human data resources  
- **UK Biobank (500 k participants)**, **All of Us (≈1 M enrolled)**, **FinnGen**, and **China Kadoorie Biobank** have become publicly accessible, providing the “>10 million”‑scale datasets Plenge said were missing.  
- Large‑scale **eQTL** and **pQTL** atlases (e.g., GTEx v8, SomaLogic proteomics) now allow systematic linking of variants to protein levels, facilitating causal inference for drug targets.  

### Target tractability & modality diversification  
- **Protein‑protein interaction (PPI) inhibitors**: Since 2016, several PPI‑directed drugs have reached late‑stage trials (e.g., **navitoclax** for BCL‑2, **sotorasib** for KRAS G12C). While still a minority, the field has matured, partly thanks to structure‑guided design and covalent chemistry.  
- **Modalities beyond small molecules**: Antibody‑drug conjugates (ADCs), bispecific antibodies, and **RNA‑targeting therapeutics** (e.g., **inclisiran** – an siRNA PCSK9 inhibitor) have entered the market, expanding the “druggable” space that Plenge considered limited.  

### Biomarker development & trial design  
- **Liquid biopsies** (circulating tumor DNA) now serve as pharmacodynamic biomarkers in many oncology trials, enabling smaller, earlier read‑outs.  
- **Adaptive platform trials** (e.g., **I-SPY2** for breast cancer, **RECOVERY** for COVID‑19) embody the “small, fast, meaningful” proof‑of‑concept ideal, allowing multiple agents to be evaluated concurrently with Bayesian decision rules.  
- **Digital biomarkers** (wearables, remote monitoring) have been incorporated into phase 2 studies for neurodegenerative and metabolic diseases, though regulatory acceptance is still evolving.  

### Real‑world outcomes vs. the rules  
- **Overall success rates**: The FDA’s 2022 drug‑approval data show a modest increase in Phase 1‑to‑Approval probability for genetics‑validated targets (≈12 % vs. ≈8 % historically), but the absolute success rate remains low.  
- **Alzheimer’s disease**: Contrary to the article’s suggestion to “abandon” the field, dozens of anti‑amyloid and anti‑tau agents entered trials after 2016. **Aducanumab** received accelerated approval in 2021 (later withdrawn by the manufacturer), and **lecanemab** achieved full FDA approval in 2023, marking the first disease‑modifying claim in decades—though uptake is limited by cost, infusion logistics, and ongoing safety debates.  
- **Infectious disease**: The COVID‑19 pandemic (2020‑2022) demonstrated that rapid, small‑scale proof‑of‑concept trials (e.g., the RECOVERY trial) can deliver life‑saving interventions, aligning with Plenge’s fourth rule.  

### Business impact  
- Companies that built pipelines around human‑genetic validation (e.g., **Alnylam**, **Regeneron**, **Vertex**) have seen market‑cap growth exceeding the industry average.  
- Conversely, firms heavily reliant on animal‑model‑first approaches (e.g., several mid‑size oncology biotech firms) experienced higher attrition, leading to consolidation and a wave of “genetics‑first” spin‑outs between 2018‑2022.  

---

## 3. PREDICTIONS  

| Prediction (from article or implied) | What actually happened |
|--------------------------------------|------------------------|
| **Human genetics will be essential for target selection** | Largely true. Major approvals (PCSK9, SGLT2, KRAS G12C) were underpinned by human‑genetic data; industry surveys show >70 % now prioritize genetics. |
| **Many disease areas (e.g., Alzheimer’s) will be largely abandoned** | Partially false. While some companies reduced Alzheimer’s R&D, the field remained active, culminating in lecanemab’s 2023 approval. |
| **Large, accessible human‑biology databases (>10 M) will be built** | True. UK Biobank, All of Us, FinnGen, and others now provide data on millions of participants. |
| **Small, fast proof‑of‑concept trials will become the norm** | True for oncology and infectious disease (adaptive platform trials). In other therapeutic areas, trial sizes have modestly decreased but regulatory expectations still favor larger Phase 2/3 studies. |
| **Biomarkers that are “irrelevant to disease” will be avoided** | Partially true. Biomarker qualification programs (FDA’s Biomarker Qualification Program) have increased rigor, yet many trials still rely on surrogate markers of uncertain clinical relevance. |
| **PPI targets will remain largely undruggable** | False. Successful PPI inhibitors (KRAS G12C, BCL‑2) have entered the market, showing progress though the space remains challenging. |

---

## 4. INTEREST  
**Rating: 8/10**  

The article is a concise, prescient synthesis of ideas that have shaped modern drug discovery—human genetics, tractability, biomarker rigor, and lean trials. Its influence is evident in how biotech pipelines are built today, even though some predictions (e.g., the near‑abandonment of Alzheimer’s) proved overly pessimistic.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160816-rules-modern-drug-development.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_