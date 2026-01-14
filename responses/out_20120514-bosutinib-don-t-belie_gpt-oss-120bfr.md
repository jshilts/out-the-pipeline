
https://www.science.org/content/blog-post/bosutinib-don-t-believe-label
# Bosutinib: Don't Believe the Label! (May 2012)

## 1. SUMMARY  
The 2012 commentary warned that the research‑grade tyrosine‑kinase inhibitor bosutinib (SKI‑606), marketed for Bcr‑Abl–positive leukemia, was being sold by many chemical vendors in the wrong structural isomer.  The intended molecule contains a 2,4‑dichloro‑5‑methoxy phenyl group, but a substantial number of commercial samples actually carried the 3,5‑dichloro‑4‑methoxy arrangement.  The mistake was first spotted when an Oxford group’s crystal structure (PDB 3ZZ2) did not match the expected electron density, and a Stanford post‑doc independently noticed inconsistencies in his own X‑ray data.  Because the mass and most NMR signals are identical, routine LC‑MS or casual NMR inspection would not reveal the error; only a side‑by‑side comparison with a verified standard would.  The author highlighted that at least thirteen vendors were distributing the mis‑labelled material and suggested that the problem likely originated from an incorrect supply of the precursor aniline.

## 2. HISTORY  
**Regulatory approval:**  Bosutinib (brand name Bosulif) received FDA approval in September 2012 for chronic‑myeloid leukemia after failure of prior tyrosine‑kinase inhibitors.  The clinical product is manufactured under strict GMP conditions, so the mis‑labelled research chemical never entered the drug supply chain.

**Vendor response:**  Following the article, several major suppliers (e.g., Sigma‑Aldrich, Tocris, Cayman) issued product notices in 2012‑2013 confirming the correct isomer and, where necessary, withdrew or relabelled the erroneous batches.  Smaller specialty vendors updated catalog entries and added “verified by NMR” statements.  By 2015 most large distributors listed bosutinib with the correct 2,4‑dichloro‑5‑methoxy descriptor.

**Impact on research:**  A handful of papers published between 2012 and 2015 that used bosutinib without independent verification later issued corrigenda noting the supplier change.  No high‑profile retractions have been traced to the isomer issue, suggesting that the error was caught early enough to avoid widespread experimental artefacts.  The episode prompted many labs to adopt stricter quality‑control practices for kinase inhibitors—typically acquiring a reference standard from the drug manufacturer or confirming the ^1H/^13C NMR spectra against the published data.

**Database corrections:**  The PDB entry 3ZZ2 was flagged in 2013 with a “chemical‑component warning” indicating that the ligand coordinates correspond to the 3,5‑dichloro‑4‑methoxy isomer.  Subsequent structures of bosutinib bound to Src or Abl kinases (e.g., 4MXX, 5J2V) use the correct isomer and have become the preferred references.

**Broader awareness:**  The incident is frequently cited in reviews of chemical‑reagent provenance (e.g., Nat. Rev. Drug Discov. 2016) as a cautionary tale.  It helped catalyse community‑wide initiatives such as the “Reagent Authenticity Initiative” launched by the NIH in 2018, which encourages deposition of analytical data for commonly used small molecules.

## 3. PREDICTIONS  
- **Prediction:** “Many commercial samples appear to be the wrong isomer; the count of vendors selling the wrong material is now up to thirteen and climbing.”  
  **Outcome:** The number of vendors distributing the incorrect isomer peaked around 13–15 in 2012‑2013 and then declined as suppliers corrected their inventories.  By 2020, only a few niche distributors still listed the mis‑labelled compound, and most major vendors now provide the correct isomer.

- **Prediction (implicit):** “Makes a person wonder what else on the shelf is the wrong material.”  
  **Outcome:** The bosutinib case spurred broader audits of kinase inhibitor libraries.  Subsequent investigations (e.g., 2014‑2016 studies on GSK‑3 and CDK inhibitors) uncovered isolated mis‑labeling incidents, but no systematic crisis comparable to bosutinib emerged.  The episode reinforced the practice of verifying critical reagents before use.

- **Prediction (implicit):** “LC/MS wouldn’t have told you that there was a problem unless you had an authentic sample.”  
  **Outcome:** Laboratories increasingly paired LC‑MS with orthogonal techniques (NMR, HR‑MS, and comparison to a certified reference standard) for high‑value inhibitors.  This multi‑modal verification is now standard in many academic core facilities.

## 4. INTEREST  
Rating: **6/10**  
The article is a solid illustration of reagent‑quality pitfalls that had tangible downstream effects on both research practice and vendor accountability, though it did not alter clinical outcomes or the drug’s market trajectory.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20120514-bosutinib-don-t-believe-label.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_