
https://www.science.org/content/blog-post/rating-massive-pile-compounds
# Rating A Massive Pile of Compounds (November 2011)

## 1. SUMMARY

The article discusses a Johnson & Johnson study where computational chemists took millions of compounds from the company's files and commercial sources, clustered them into ~20,000 similarity groups, and asked 145 medicinal chemists to vote on whether each cluster represented promising drug candidates. The key finding was that the chemists' subjective preferences closely matched established drug-likeness criteria (Lipinski's rules): compounds in the 300-400 molecular weight range were favored, while those below 250 or above 425 were increasingly rejected, with similar patterns for rotatable bonds, hydrogen bond donors/acceptors, and clogP.

The authors acknowledged this might simply validate existing computational filters rather than break new ground, while highlighting benefits like filling diversity gaps in screening libraries and increasing employee engagement. The blogger expressed skepticism about the practical value, noting that subjective human evaluation ultimately replicated what automated filters could do in seconds, questioning whether this exercise was worth the significant time investment (with only 6 participants completing all 22,015 clusters).

## 2. HISTORY

In the years following this 2011 article, several key developments reshaped compound screening and drug discovery approaches:

**AI/ML Transformation (2012-2024)**: The pharmaceutical industry underwent a fundamental shift away from purely rules-based filtering toward machine learning and artificial intelligence. Companies increasingly adopted AI-driven virtual screening methods that could process billions of compounds rapidly while learning complex structure-activity relationships beyond simple property filters. Deep learning models developed from 2016 onward (particularly graph neural networks) showed superior performance compared to traditional drug-likeness rules.

**Computational Screening Expansion**: By 2020, major pharma companies had largely moved beyond manual curation of screening libraries. J&J itself invested heavily in computational platforms, with their Janssen division launching multiple AI-driven drug discovery initiatives. Virtual compound libraries expanded dramatically, with companies like Schrödinger, Atomwise, and Exscientia offering AI platforms that could screen billions of virtual compounds - making the manual 20,000-cluster evaluation approach obsolete.

**Property Filter Evolution**: While Lipinski's rules remained relevant for oral drugs, the pharmaceutical industry recognized their limitations, particularly for new modalities. The rise of PROTACs, molecular glues, peptide therapeutics, and antibody-drug conjugates (all frequently violating traditional drug-likeness rules) demonstrated that strict adherence to 300-400 molecular weight ranges could miss important therapeutic opportunities. The FDA approved numerous drugs post-2015 with properties that would have been "downvoted" in the 2011 exercise.

**Novel Drug Approvals Defying Traditional Rules**: Several FDA-approved drugs from 2012-2024 violated the 425 molecular weight cutoff favored in the study, including antivirals, cancer drugs, and treatments for rare diseases. This demonstrated that the pharmaceutical industry's actual successful output didn't always align with the preferred taste profiles identified in J&J's study.

**Industrial Automation**: By 2020, most major pharmaceutical companies had automated compound selection workflows using machine learning, with significant reductions in manual curation. The kind of intensive human evaluation described in the article became increasingly rare as computational methods proved faster, more consistent, and better at exploring chemical space diversity.

## 3. PREDICTIONS

**Explicit Predictions by Study Authors:**
- **Prediction**: "Whether the strategy will yield the desired results in the long term with respect to quality, novelty, and number of hits/leads remains to be seen"
- **Outcome**: The strategy of large-scale manual curation did NOT become standard practice. Instead, AI/ML methods proved more effective at generating quality hits while exploring broader chemical diversity. The manual approach was largely abandoned as computational methods advanced.

- **Prediction**: "It is also unclear whether this strategy can lead to sufficient differentiation from a competitive stand-point"
- **Outcome**: The strategy did NOT provide competitive differentiation. Industry moved toward AI-driven approaches instead, with competitive advantage coming from algorithmic sophistication rather than manual curation scale.

**Blogger's Implicit Predictions/Skepticism:**
- **Prediction** (Implicit): Manual curation at this scale might not be worth the effort compared to automated filters
- **Outcome**: **ACCURATE**. The industry largely abandoned this approach in favor of computational methods within 5-10 years.

## 4. INTEREST

**Score: 3/9**

This article captures an interesting historical moment in pharmaceutical research methodology, but represents a transitional approach that was soon superseded by AI/ML methods. Its primary value is documenting how subjective medicinal chemistry intuition aligned with then-current computational filters, but the manual curation approach proved unsustainable and was rapidly replaced by automated systems.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20111107-rating-massive-pile-compounds.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_