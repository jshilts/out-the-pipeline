
https://www.science.org/content/blog-post/putting-number-chemical-beauty
# Putting a Number on Chemical Beauty (January 2012)

## 1. SUMMARY

The article discusses a 2012 *Nature Chemistry* paper titled "Quantifying the Chemical Beauty of Drugs," which proposed a new "desirability score" for evaluating chemical structures in drug discovery. The authors developed this metric by analyzing eight physical and structural properties across 770 well-known oral drugs, using Shannon entropy to determine optimal weighting for each property. Notably, hydrogen-bond acceptors and polar surface area received zero weight, suggesting these measures were already captured by other factors.

The paper included an experiment where AstraZeneca chemists evaluated 17,000 compounds, with only about 30% receiving approval for further chemistry work—most rejections were due to structures being either "too complex" or "too simple." The authors' model showed a modest difference between accepted (mean score 0.67) and rejected compounds (mean score 0.49), with statistically significant but not particularly strong correlation to medicinal chemists' preferences. The authors also attempted to extend their model to assess target druggability, finding slightly higher scores for approved oral drugs (0.539) compared to all database targets (0.478).

The article's author takes a skeptical but fair view, seeing the work as refining existing approaches like Lipinski's Rule of 5 into a more continuous scale rather than offering a revolutionary breakthrough.

## 2. HISTORY

The 2012 paper by Bickerton et al. introduced what became known as the "Quantitative Estimate of Drug-likeness" (QED) score, which gained significant traction in drug discovery despite the initial lukewarm reception. The QED framework addressed a genuine need in the field for more nuanced, quantitative metrics beyond simple rule-based approaches like Lipinski's Rule of 5.

In the years following publication, **QED became widely adopted** across pharmaceutical companies and academic labs. The method proved particularly valuable for prioritizing compound libraries and guiding medicinal chemistry optimization. Numerous studies validated and extended the approach, with Google Scholar showing over 1,800 citations by 2024. The QED concept influenced subsequent development of more sophisticated AI-driven drug design tools, including machine learning models that built upon its framework.

However, **clinical success rates remained largely unchanged** by these computational advances. The fundamental challenges in drug discovery—high attrition rates, unexpected toxicity, and inadequate efficacy—persisted despite better compound prioritization tools. FDA drug approvals didn't significantly increase in the decade following QED's introduction, with approval rates hovering around 10-15% for drugs entering clinical trials.

The **skepticism expressed in the original article proved partly justified**: while QED was useful, it wasn't transformative. Pharmaceutical R&D continued facing the same systemic challenges, with most drug candidates still failing in expensive late-stage trials. The modest correlation between QED scores and chemists' preferences (evidenced by the 0.67 vs 0.49 score difference) reflected real-world complexity that couldn't be captured by simple numerical scores.

Practical implementation showed that **QED worked best as one of many filters** rather than a standalone decision tool. Companies integrated it into multi-parameter scoring systems alongside other metrics like ligand efficiency, ADMET predictions, and synthetic accessibility. The method's greatest value was in early-stage hit triaging and library design rather than predicting clinical success.

## 3. PREDICTIONS

The 2012 article made several implicit predictions and assessments:

• **"What does it give us that we haven't had before?"** - The author questioned whether QED offered substantial advantages over existing methods like Lipinski's Rule of 5.  
**OUTCOME**: QED did provide value by offering a continuous, weighted scoring system rather than binary pass/fail rules, leading to widespread adoption. However, it complemented rather than replaced existing approaches.

• **"Will people be willing to make decisions based on this method?"** - The author expressed uncertainty about practical adoption.  
**OUTCOME**: Yes, the method was widely adopted across the industry, becoming a standard tool in computational drug discovery workflows.

• **"The two ends of the scale are hard to argue with, but there's a great mass of compounds in the middle"** - The author noted that QED would be most useful for extreme cases.  
**OUTCOME**: This proved accurate—QED was most reliable for clearly drug-like or clearly problematic structures, while mid-range compounds still required expert judgment.

• **The overall assessment was that the paper offered "nothing spectacularly right"** - A prediction that this wouldn't revolutionize the field.  
**OUTCOME**: This was largely accurate. QED became a useful but incremental advance rather than a paradigm shift. Drug discovery success rates didn't dramatically improve, and fundamental challenges remained.

• **Implicit in the druggability assessment was that this could help prioritize targets** - The authors claimed their method could rank target druggability.  
**OUTCOME**: Target druggability prediction remained challenging, and QED-based approaches had limited impact on actual target selection decisions in pharmaceutical companies.

## 4. INTEREST

**Rating: 6/10**

The article covers an important but incremental methodological advance in drug discovery—the QED score proved broadly useful but didn't fundamentally change the field's trajectory or solve core challenges.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20120126-putting-number-chemical-beauty.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_