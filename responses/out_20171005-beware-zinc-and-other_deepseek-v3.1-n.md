
https://www.science.org/content/blog-post/beware-zinc-and-other-stuff
# Beware of Zinc. And of Other Stuff. (October 2017)

## 1. SUMMARY

The article describes a cautionary tale from medicinal chemistry research at the University of Dundee, where a promising screening hit against the enzyme Ube2T turned out to be a false positive caused by zinc contamination. Ube2T is a ubiquitin-conjugating (E2) enzyme involved in DNA repair pathways and overexpressed in tumor cells, making it a potentially attractive drug target for cancer therapy. The research team had identified a fragment screening hit that showed activity across multiple orthogonal assays (NMR, DSF, ITC), but despite extensive efforts, they could not establish meaningful structure-activity relationships—every analog they synthesized lost activity. X-ray crystallography eventually revealed the truth: no small molecule was bound to the protein, but instead a zinc atom had coordinated to the catalytic cysteine, causing the observed activity. The author draws parallels to their own similar experience twenty years earlier with a phosphatase enzyme and zinc contamination, emphasizing the critical importance of rigorously validating screening hit purity.

## 2. HISTORY

Subsequent developments in the years following this 2017 article reveal several important trends:

**Ube2T and E2 Enzyme Research:** Research into Ube2T continued, with the enzyme remaining of interest in DNA repair pathways, particularly in the context of Fanconi anemia and cancer. However, Ube2T has not emerged as a major drug target with clinical candidates advancing significantly. The broader field of E2 enzyme inhibitors remains challenging, with only limited progress in developing potent, selective inhibitors.

**PROTAC Technology Evolution:** The article's mention of targeted protein degradation became increasingly relevant. Proteolysis-targeting chimeras (PROTACs) gained substantial momentum starting around 2015-2017 and exploded in subsequent years. Major pharmaceutical companies (Pfizer, Novartis, Roche) and biotechs (Arvinas, Kymera, C4 Therapeutics) built substantial programs around targeted protein degradation.

**Clinical Outcomes:** Arvinas's ARV-110 (for prostate cancer) and ARV-471 (for breast cancer) became the first PROTACs to enter clinical trials. While early results showed some promise (ARV-471 demonstrated clinical benefit in heavily pretreated ER-positive breast cancer patients), the path to approval has been longer than initially hoped. These represent concrete clinical translation of the "target proteins for the shredder" concept mentioned in the article.

**Industrial Adoption:** The biopharmaceutical industry widely adopted targeted protein degradation as a modality, with hundreds of millions invested and numerous companies founded. Academic research also expanded significantly in protein degradation pathways.

## 3. PREDICTIONS

The article contained several implicit predictions and observations:

• **"Targeted protein degradation at will and selectively is not quite a real thing yet, although some very interesting examples have appeared, but a lot of effort is going into making it one"** → **Largely accurate, with significant progress but longer timeline than initially hoped.** PROTAC technology matured substantially, moved into clinical trials, and became a major research area. However, it has not yet revolutionized medicine in the way initially envisioned—multiple PROTACs have entered clinical development but none have achieved FDA approval as of early 2025.

• **"E2 ubiquitin-conjugating enzyme is a tough way to do it (few inhibitors are known for that class)"** → **Accurate prediction.** E2 enzymes remain difficult drug targets. No major E2 inhibitors have reached clinical approval, and developing selective E2 inhibitors continues to be challenging. The Ube2T work described in the article appears not to have led to clinical candidates.

• **"Interfering with DNA repair temporarily would make fast-replicating tumor cells more vulnerable to radiation and some types of chemotherapy"** → **Accurate, supported by subsequent developments.** PARP inhibitors (which target DNA repair) became major cancer drugs (olaparib, rucaparib, niraparib FDA-approved), validating the synthetic lethality approach. However, this was through different targets than Ube2T—PARPs are not E2 enzymes.

## 4. INTEREST
Rating: **7/10**

This article has maintained moderate-to-high interest due to its practical lessons about rigorous validation in early drug discovery and its connection to the burgeoning field of targeted protein degradation. While primarily a cautionary tale, it touches on topics (ubiquitin system, PROTACs) that gained substantial scientific momentum in subsequent years. The specific zinc contamination story is particularly valuable for medicinal chemists, providing concrete examples of false positives. The broader context about attempts to control protein degradation also gives it longer-term relevance, even if the specific Ube2T target didn't emerge as clinically important.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20171005-beware-zinc-and-other-stuff.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_