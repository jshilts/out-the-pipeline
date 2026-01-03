
https://www.science.org/content/blog-post/adverse-events-look-under-hood
# Adverse Events: A Look Under the Hood (August 2017)

## 1. SUMMARY
This commentary reviews a 2017 eLife paper by the Shoichet group (UCSF), Novartis, and Oracle Health Sciences examining the FDA's Adverse Event Reporting System (FAERS). The article describes FAERS as a massive but flawed database containing over 9 million reports by 2017, with inconsistent reporting quality and significant data curation challenges. Key problems identified include duplicate reports (1% duplicates), variable reporting rates across sources (50% healthcare professionals, 33% patients, 3% lawyers), reporting biases favoring serious events over minor ones (15% death reports despite drugs not killing 15% of users), and a critical drug synonym problem (378 synonyms for fluoxetine alone).

The paper highlights how external events dramatically affect reporting patterns, using Vioxx as an example where physician reports stayed constant but lawyer reports dramatically increased after 2000 when MI risks were publicized. For rosiglitazone versus pioglitazone, both PPAR ligands for Type II diabetes, the data shows rosiglitazone associated with more cardiovascular events (particularly after 2002 publicity) while pioglitazone showed more bladder cancer reports (especially after 2009, possibly lawyer-driven). The authors recommend improved drug synonym standardization, better correlation with pharmacokinetics data, and more automated/interactive reporting to make FAERS more scientifically useful.

## 2. HISTORY
Following the 2017 critique, several developments occurred in pharmacovigilance and adverse event monitoring:

**Regulatory Changes:** The FDA continued enhancing FAERS but fundamental structural issues persisted. In 2018, the FDA launched the FDA Adverse Event Reporting System (FAERS) Quarterly Data Files in more accessible formats, improving data transparency. However, the core synonym and duplication problems remained largely unaddressed systematically.

**Rosiglitazone and Pioglitazone Outcomes:** The cardiovascular risks of rosiglitazone became more firmly established. The FDA significantly restricted rosiglitazone in 2010 and completely removed restrictions only after legal challenges. By contrast, pioglitazone maintained broader market access but continued accumulating bladder cancer safety signals. Both drugs saw declining use in clinical practice due to these safety concerns and the emergence of newer diabetes medications.

**Real-World Evidence Integration:** Post-2017, there was growing recognition that spontaneous reporting systems like FAERS, while valuable for signal detection, required integration with more systematic real-world evidence. This led to increased emphasis on active surveillance systems, systematic registries, and retrospective database mining using electronic health records and insurance claims data to complement FAERS data.

**Vioxx Legacy:** Merck's Vioxx remained a landmark case in pharmacovigilance history. The $4.85 billion settlement in 2007 resolved most litigation, but sporadic cases continued. The episode fundamentally shaped how pharmaceutical companies approached pre-market cardiovascular safety assessment for new drugs.

**Technology Improvements:** Oracle Health Sciences and other technology partners continued working on improving pharmacovigilance data management. Companies increasingly adopted more sophisticated natural language processing and machine learning approaches to clean and standardize adverse event data, addressing some synonym and duplication problems identified in the original paper.

## 3. PREDICTIONS
**Prediction:** The authors suggested FAERS needed "a more rational approach to drug synonyms" and that their work "clearing up the tangle" could serve as a starting point.

**Outcome:** Limited progress occurred. While individual companies and research groups developed better drug normalization databases, the fundamental synonym problem in FAERS persisted. No comprehensive federal initiative systematically addressed the issue across all historical data.

**Prediction:** The authors proposed "a more interactive and automated form of reporting would also be useful, to reduce reporting errors."

**Outcome:** Some progress was made, with the FDA implementing online reporting portals and encouraging structured electronic submissions. However, significant error rates and reporting biases remained. The basic structure of voluntary reporting with its inherent biases did not fundamentally change.

**Prediction:** The article implied that better correlation of FAERS data with pharmacokinetics could improve signal detection.

**Outcome:** Academic researchers and pharmaceutical companies increasingly adopted these approaches, with published studies correlating adverse events with PK parameters, dosing, and drug formulations. However, regulatory decision-making still often relied on simpler aggregate statistics rather than sophisticated population PK-PD modeling of adverse events.

**Overall Assessment:** The fundamental limitations identified in 2017—reporting biases, data quality issues, and poor standardization—persisted, though incremental improvements in data accessibility and analytical methods occurred.

## 4. INTEREST
Rating: **6/10**
While the article identified important limitations in drug safety surveillance, it covered well-established concerns rather than introducing novel insights or solutions. The critique was accurate but didn't drive major systemic changes in pharmacovigilance practice or policy.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20170829-adverse-events-look-under-hood.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_