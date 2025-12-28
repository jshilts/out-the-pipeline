
https://www.science.org/content/blog-post/how-many-good-screening-compounds-are-there
# How Many Good Screening Compounds Are There? (January 2013)

## 1. SUMMARY

This 2013 commentary discusses a paper by Jonathan Baell and colleagues examining the quality and diversity of commercially available screening compounds for drug discovery. The article highlights how applying standard druglikeness filters dramatically reduces compound library sizes—from 400,000 to as few as 6,000-10,000 when accounting for molecular properties, problematic functional groups (PAINS), and structural diversity. The authors found significant issues with vendor collections, including redundant scaffold coverage favoring synthetically accessible series, problematic reactive groups slipping through filters, and reliability problems with compound availability and resupply. The paper estimated that of millions of potentially purchasable compounds, only about 340,000 represented genuinely viable screening candidates covering accessible chemical space. The piece emphasizes the concern that typical vendor libraries are highly imbalanced—containing too many close analogs and singletons—rather than a well-designed collection with multiple representatives of distinct structural classes.

## 2. HISTORY

The 2013 Baell paper and associated commentary significantly influenced the drug discovery field, with lasting impact that has persisted for over a decade.

Baell and colleagues' PAINS (Pan Assay INterference compoundS) critique has been widely adopted across the pharmaceutical industry. Companies and academic groups implemented PAINS filtering as standard practice. The community developed multiple computational tools and databases like FAF-Drugs4, SwissADME, and ZINC15 that incorporate PAINS and SMARTS-based alerts. This has led to validated, higher-quality screening libraries at academic institutions like NIH's Molecular Libraries Program and company collections.

Structural diversity screening approaches have become more systematic. Modern compound libraries now show more balanced representations compared to 2013 vendor collections. The subsequent 2019 publication by Baell (Baell, J.B., Sci. Rep. 2019) confirmed similar PAINS issues with approved drugs, leading to methodological improvements in ADMET prediction and drug-drug interaction prediction.

However, the supply chain reliability issues noted in 2013 have largely persisted. Research published in subsequent years consistently highlights that 5-20% of screening hits from commercial libraries remain unavailable for re-synthesis or repurchase. Vendors have partially addressed this through specialized resupply programs, but many compounds designated as "available" remain synthesis-dependent. Academic screening facilities (such as the University of Pittsburgh, University of Toronto, and Scripps) now maintain internal "cherry-picked" collections specifically designed to mitigate these issues.

Concrete impact: Pharmaceutical companies developed better filtering strategies and internal HTS validations. Published accounts from Novartis, GlaxoSmithKline, Roche, and AstraZeneca document curation of internal screening collections employing Baell's criteria. Such filtering has reduced the frequency of nuisance compounds interfering with high-throughput screens, consequently improving the speed from hit identification to lead optimization and decreasing the risk of investing resources in compounds with reactive groups or assay interference. 

In parallel, DNA-encoded libraries (DELs) and fragment-based drug discovery approaches grew in popularity as complementary discovery methods. Libraries such as GSK's 21,000-compound DNA-encoded library offer screening of vast chemical space with built-in redundancies and takeup over the last decade. Since 2013, DELs have advanced via Encoded Library Technologies (ELT), leading to significant industry adoptions. The approach has helped identify new chemical matter and provide complementary diversity to conventional HTS collections. These developments highlight how mature screening hit identification platforms are altering screening strategies at large pharmaceutical companies.

While no FDA-approved drugs directly trace origins to the 2013 commentary, the methodological improvements it catalyzed are embedded in how pharmaceutical companies construct screening libraries today. In terms of concrete business impact, companies like Enamine, ChemDiv, and WuXi AppTec have expanded their curated compound collections specifically advertising PAINS-filtered, diversity-optimized screening libraries as a competitive differentiator. Most major pharmaceutical companies now curate specialized screening subsets with quality control measures exceeding 2013 standards.

## 3. PREDICTIONS

The 2013 commentary contained several implicit predictions about how screening collections should evolve. Here are the key predictions and their outcomes:

**Prediction:** Vendors with better resupply policies would gain a competitive advantage.
- **Outcome:** Partially validated. Vendors now commonly advertise resupply guarantees (e.g., Enamine's "immediate resupply" policy for prior customers), but many companies still maintain inconsistent or unstandardized resupply practices. The competitive advantage dimension is real but remains limited, as many researchers still report availability issues.

**Prediction:** Reducing Tanimoto similarity cutoffs and balancing structural classes would become standard practice.
- **Outcome:** Validated. Major pharmaceutical companies now routinely apply similarity-based diversity selections and scaffold-balanced libraries. Academic and commercial screening collections are less redundant than they were in 2013. More systematic approaches to library design (e.g., optimizing diversity via MaxMin picking, sphere exclusion clustering) are now common. Curated collections such as the NIH MLSMR and commercial "designer libraries" reflect this shift. 

**Prediction:** PAINS recognition and filtering would gain broader adoption.
- **Outcome:** Strongly validated. PAINS filtering is now standard in virtually all pharmaceutical and academic screening programs. Antechamber tools like RDKit, Pipeline Pilot, and cheminformatic platforms universally incorporate PAINS alerts. The widespread adoption has dramatically reduced problematic compounds in screening collections.

**Prediction:** That singleton compounds would be minimized in well-designed screening collections.
- **Outcome:** Validated. Modern screening libraries prioritize clustered series with SAR insight. Most commercial vendors now offer libraries grouped by scaffold rather than purely singleton-based collections, though singleton compounds still exist (primarily to increase diversity space).

**Prediction:** Functional group filtering would grow more sophisticated.
- **Outcome:** Validated. Sophisticated aggregation-prone, redox-active, and metabolism-unstable group filters are now applied more rigorously than in 2013. Collections are better curated for functional groups liable to cause drug metabolism, toxicology, or assay interference.

## 4. INTEREST

Rating: **8/10**

This article remains highly relevant more than a decade later because it crystallized critical quality control issues in screening collections that continue to shape pharmaceutical R&D practices. The work has had enduring influence on how both academic and industrial researchers select, filter, and evaluate screening compounds, leading to tangible improvements in screening quality and success rates.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20130102-how-many-good-screening-compounds-are-there.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_