
https://www.science.org/content/blog-post/predicting-new-targets-another-approach
# Predicting New Targets - Another Approach (June 2014)

## 1. SUMMARY
This 2014 article discusses the challenge of predicting what biological targets a new chemical compound will hit when administered in vivo—a problem where medicinal chemists know prediction is extremely difficult, contrary to public perception. The piece highlights a Novartis approach called HTSFP-TID (High-Throughput Screening FingerPrint - Target ID), which classifies compounds based on biological activity fingerprints across assay suites rather than chemical structure alone. The researchers applied this method to 1,357 natural products and 1,416 experimental drugs/marketed compounds, finding significant differences: natural products predominantly predicted enzyme targets (70%, half kinases) with few GPCR predictions, while drug-like molecules showed more balanced kinase (44%) and GPCR (23%) predictions with fewer protease targets. Experimental validation showed approximately 73% accuracy for predictions overall, with kinase predictions particularly reliable but GPCR calls less so. The article notes that this approach yields hypotheses not obvious from chemical structure alone and suggests combining it with traditional chemical descriptor methods since they produce orthogonal predictions.

## 2. HISTORY
Following the 2014 publication, computational target prediction and polypharmacology profiling became increasingly important in drug discovery, though with mixed real-world success. 

**Academic and Methodology Developments:** The field of chemogenomics and computational target prediction expanded significantly between 2014-2020. Methods combining multiple data types (bioactivity, chemical structure, protein-ligand interaction) became more sophisticated, with several groups publishing improved algorithms for predicting off-target effects and polypharmacology. The strategy of using biological activity fingerprints (like HTSFP-TID) influenced subsequent approaches, though purely structure-based methods using deep learning gained prominence after 2017.

**Industry Impact:** Large pharmaceutical companies continued investing in computational target prediction capabilities, recognizing the importance of understanding polypharmacology early. However, **many predicted targets from these methods failed to translate into clinically relevant effects**. While computational predictions could suggest unexpected targets (as the article noted), the complexity of in vivo pharmacology meant that predictions often didn't correlate with therapeutic outcomes or safety issues in humans.

**Clinical Translation:** The specific compounds and targets mentioned in the Novartis study did not lead to major breakthroughs or new FDA-approved drugs that became widely adopted. The broader challenge remained: **even with improved computational predictions, drug discovery continued to suffer from high failure rates due to unforeseen target interactions, toxicity, or lack of efficacy in clinical trials**. By 2020-2023, the industry increasingly recognized that computational target prediction works best as a hypothesis-generating tool rather than a definitive predictor of clinical success.

**Business and Validation:** The prediction accuracy of ~73% reported in 2014 proved optimistic for real-world drug discovery. Subsequent validation studies showed that while many predicted biochemical interactions could be confirmed in vitro, the **pharmacological and therapeutic relevance of these predicted targets remained questionable**. Pharmaceutical companies found that computational predictions required extensive experimental validation, and many predicted "druggable" targets didn't yield viable drug candidates.

## 3. PREDICTIONS
• **Enthusiasm for fingerprint-based approaches**: The article expressed optimism that HTSFP-TID "provides fresh hypotheses that were previously not pursued because they were not obvious based on the chemical structure." *Outcome*: While biological fingerprint methods remained useful, they didn't fundamentally solve drug discovery prediction challenges. The approach complemented but didn't replace traditional methods.

• **Hope for publication of results from other large collections**: The author expressed desire to "see if that happens or not" regarding whether other large pharmaceutical companies would publish similar analyses using their compound collections. *Outcome*: *Partial* - Some pharmaceutical companies published computational target prediction studies, but comprehensive cross-company analyses remained rare due to proprietary data concerns. Academic groups did more extensive public validation studies.

• **Implicit prediction of utility for "weirdo chemical or biological space"**: The suggestion that such methods would be "particularly useful as you push into weirdo chemical or biological space." *Outcome*: *Mostly accurate* - Computational target prediction has proven valuable when exploring novel chemical matter or unusual biological targets, but still requires experimental validation and hasn't dramatically accelerated discovery timelines.

• **Underlying assumption about importance of understanding polypharmacology**: The entire article assumes that better target prediction will improve drug discovery outcomes. *Outcome*: *Mixed* - While understanding polypharmacology is crucial, computational predictions alone haven't significantly reduced clinical failure rates. The relationship between predicted targets and actual therapeutic/toxicity effects proved more complex than anticipated.

## 4. INTEREST
Rating: **5/10**
This article addresses an important and persistent challenge in drug discovery (target prediction) and highlights a novel methodology, but the approach didn't fundamentally transform the field or lead to major breakthroughs in the following decade. The specific Novartis method influenced academic research but didn't produce notable clinical successes.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20140604-predicting-new-targets-another-approach.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_