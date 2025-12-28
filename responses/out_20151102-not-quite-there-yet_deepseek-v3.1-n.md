
https://www.science.org/content/blog-post/not-quite-there-yet
# Not Quite There Yet (November 2015)

## 1. SUMMARY

This 2015 blog post critiques a paper claiming breakthrough validation of computational de novo design for drug discovery. The paper described using machine learning software (DOGS - Design of Genuine Structures) to generate fragment-sized kinase inhibitors targeting DAPK3, identifying a 3-(tetrazoyl) phenylsulfonamide compound. The authors also discovered that azosemide, an existing marketed diuretic drug with similar structure, showed activity on DAPK3 - which they presented as validation of their computational approach.

The blogger (Derek Lowe) expressed significant skepticism, noting that kinase ATP-binding sites are relatively easy to find fragment hits for anyway, that the prediction of carbonic anhydrase activity for arylsulfonamides is pharmacologically obvious, and that the paper lacked important controls: no information on hit rates for the machine learning predictions, no data on how other top-ranked compounds performed, and no comparison to standard fragment library screening. The overall assessment was that while the approach might have merit, this particular paper didn't provide convincing evidence.

## 2. HISTORY

In the years since 2015, computational drug design has indeed advanced significantly, but in ways that largely validate the blogger's cautious skepticism about this specific paper.

**DOGS Software and De Novo Design:** The DOGS software mentioned in the paper did not become widely adopted in pharmaceutical drug discovery. Most major pharmaceutical companies have moved toward more integrated computational platforms (like Schrödinger's suite, MOE, or OpenEye tools) rather than standalone "de novo design" packages. Fragment-based drug discovery remains important, but the emphasis has shifted toward empirical screening followed by structure-guided optimization.

**DAPK3 as a Drug Target:** DAPK3 has not emerged as a major validated drug target. As of 2024, there are no FDA-approved drugs targeting DAPK3, and the kinase has not become a major focus of pharmaceutical R&D pipelines. This reflects the broader challenge in kinase drug discovery - of the hundreds of kinases in the human genome, only a small fraction have proven to be clinically actionable targets.

**Azosemide:** The discovery that azosemide inhibits DAPK3 had no clinical impact. Azosemide remains a niche diuretic with limited use, and its DAPK3 activity has not led to new therapeutic indications or repurposing efforts.

**Machine Learning in Drug Discovery:** Interestingly, the broader field of machine learning for drug discovery has exploded since 2015, but through different approaches than those described in the criticized paper. Deep learning models (like AlphaFold for protein structure, or graph neural networks for molecular property prediction) have become influential, and companies like Exscientia, Insilico Medicine, and Atomwise have built substantial businesses around AI-driven drug discovery. However, these successful applications have generally focused on predicting ADMET properties, molecular optimization, or target identification at much larger scale - not the specific de novo fragment design approach described in the 2015 paper.

## 3. PREDICTIONS

The blogger did not make explicit long-term predictions, but the implicit predictions in his analysis were:

• **That computational drug design would need more rigorous validation before gaining widespread adoption** - **LARGELY VINDICATED**: While computational methods are now ubiquitous in drug discovery, they're used as decision-support tools rather than standalone discovery engines, with continued emphasis on empirical validation

• **That DAPK3 activity might not translate to clinical importance** - **VINDICATED**: No DAPK3-targeted drugs have reached the market

• **That fragment screening for kinases should not be difficult** - **CONFIRMED**: Fragment-based approaches are now standard for kinase drug discovery at major pharmaceutical companies

• **That azosemide's DAPK3 activity was a curiosity rather than a therapeutic breakthrough** - **VINDICATED**: This finding had no clinical impact

• **That machine learning approaches would need better validation** - **MIXED**: ML is now widely used but in different forms than proposed in 2015, and the field remains appropriately skeptical of overclaimed computational approaches

## 4. INTEREST

**Score: 3/10**

This was a routine critique of an overhyped academic paper. While it displayed appropriate scientific skepticism, the particular paper being critiqued was not historically significant, and DAPK3 has not emerged as an important drug target. The blogger's skepticism was well-founded but the episode was not a major moment in drug discovery history.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20151102-not-quite-there-yet.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_