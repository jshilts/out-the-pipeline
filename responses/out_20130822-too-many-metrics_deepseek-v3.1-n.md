
https://www.science.org/content/blog-post/too-many-metrics
# Too Many Metrics (August 2013)

## 1. SUMMARY

The article discusses a paper by Michael Shultz of Novartis that critically evaluates the proliferation of molecular optimization metrics in drug discovery. Since Lipinski's "Rule of Five" was introduced around 1998, the field had seen an explosion of parameters, composite indices, and visualization methods for assessing drug candidates—including ligand efficiency (LE), lipophilic ligand efficiency (LipE/LLE), and numerous other calculated properties.

Shultz argues that this abundance creates "analysis fatigue" and confusion rather than clarity. Many popular metrics, particularly those dividing logarithmic potency by heavy atom count, violate mathematical principles (specifically the quotient rule of logarithms). Through systematic analysis, Shultz finds that most efficiency metrics don't correlate well with successful drug optimization in practice. However, he identifies lipophilic ligand efficiency (LipE = pIC50 - logP) as mathematically sound and validated in real drug discovery campaigns. The article includes an analysis showing how different chemical substituents affect binding potency when maintaining constant LipE values, providing practical guidance for medicinal chemists.

## 2. HISTORY

The 2013 article anticipated a needed consolidation in medicinal chemistry metrics, and subsequent developments largely validated Shultz's concerns and recommendations:

**LipE/LLE became a standard metric**: Following this publication, LipE (Lipophilic Ligand Efficiency) became widely adopted across the pharmaceutical industry as a primary optimization metric. Major drug companies incorporated it into their standard compound profiling workflows, and it remains a core metric in drug discovery today.

**Continued metric proliferation with increased discrimination**: While new metrics continued to emerge, the field became more discerning. Publications after 2013 showed increased emphasis on metrics with solid theoretical foundations and practical validation. Many of the mathematically problematic metrics criticized by Shultz fell out of common use.

**Practical industry adoption**: Pharmaceutical companies increasingly focused on a smaller set of validated metrics including LipE, lipophilicity (logP/logD), and basic physicochemical properties. Decision-making moved away from complex multi-metric dashboards toward simpler, more interpretable parameter sets.

**Integration with AI/machine learning**: As drug discovery incorporated more computational approaches, LipE and related efficiency metrics became standard features in machine learning models for compound prioritization and optimization.

**No major regulatory changes**: FDA and EMA guidance documents didn't substantially change based on these metric discussions, as regulators focus more on clinical safety and efficacy data than preclinical optimization metrics.

The practical impact was that drug discovery programs became more disciplined in their use of metrics, leading to more rational optimization strategies rather than metric-driven "gaming" that had been problematic with some earlier approaches.

## 3. PREDICTIONS

**Shultz's implicit prediction that LipE would prove more useful than other efficiency metrics**: **✓ CORRECT**  
LipE became a widely adopted standard metric in pharmaceutical industry workflows, with numerous subsequent publications validating its utility in drug optimization campaigns. It remains a core metric today.

**Shultz's suggestion that mathematically invalid metrics would fall out of favor**: **✓ LARGELY CORRECT**  
Many of the mathematically problematic metrics (particularly those violating the quotient rule for logarithms) did decrease in prominence. However, some imperfect metrics continued to be used pragmatically in specific contexts.

**The article's implication that rationalizing metrics would improve drug discovery outcomes**: **✓ PARTIALLY CORRECT**  
Better discrimination among metrics did lead to more rational optimization strategies. However, drug discovery success rates remained challenging with many other factors (target selection, clinical translation, regulatory pathways) being more determinative than choice of preclinical metrics.

**The idea that too many metrics impede decision-making**: **✓ CORRECT**  
Recognition of "analysis fatigue" and metric overload led to industry practices focusing on a smaller set of well-validated parameters, improving decision-making clarity in drug optimization.

## 4. INTEREST

Rating: **8/10**

This article addressed a critical issue in drug discovery methodology that had broad practical implications across the pharmaceutical industry. It contributed to the rationalization and standardization of efficiency metrics that enabled more effective optimization of drug candidates.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20130822-too-many-metrics.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_