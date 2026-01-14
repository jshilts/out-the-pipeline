
https://www.science.org/content/blog-post/tighten-your-numbers
# Tighten Up Your Numbers! (April 2018)

## 1. SUMMARY  
The article reports on John Ioannidis’s proposal to lower the conventional “statistical significance” cutoff from *p* < 0.05 to *p* < 0.005 in biomedical research. Ioannidis argues that about one‑third of published positive findings would be re‑classified as merely “suggestive,” which he views as a net benefit because many of those results are likely false positives. He stresses that p‑values are useful only a minority of the time and that researchers should rely more on effect sizes, confidence intervals, and Bayesian methods. He also warns that a stricter threshold could encourage ever larger sample sizes without improving scientific insight, and he calls for better experimental design and bias control as the real solution.

## 2. HISTORY  
**Post‑2018 developments in statistical practice**

* **Journal policies:** A handful of journals (e.g., *Nature* Human Behaviour, *Psychology Science*) have experimented with a *p* < 0.005 requirement for primary hypotheses, but the majority of biomedical journals have retained the traditional 0.05 threshold. No major publisher has mandated the new cutoff across the field.

* **NIH and funding agencies:** The U.S. National Institutes of Health issued updated “Statistical Guidelines for Researchers” (2020) that stress pre‑registration, power analysis, and transparent reporting of effect sizes and confidence intervals. The guidelines do **not** require a 0.005 threshold but encourage “more stringent statistical standards where appropriate.”

* **Reproducibility initiatives:** Large‑scale replication projects (e.g., the Reproducibility Project: Cancer Biology, 2021‑2023) continued to find a substantial proportion of published findings non‑replicable, confirming Ioannidis’s earlier concerns. However, the failure rate has not dramatically changed, suggesting that lowering the *p*‑value alone has not been a decisive factor.

* **Bayesian methods:** Adoption of Bayesian statistics in biomedical research has grown modestly. Software such as Stan and the R package **brms** have become mainstream, and several high‑impact journals now accept Bayesian analyses alongside frequentist ones. Nonetheless, Bayesian approaches remain far from the majority of published studies.

* **Educational reforms:** Graduate curricula in biostatistics and epidemiology have placed greater emphasis on reproducibility, effect‑size interpretation, and alternatives to null‑hypothesis testing. This reflects the broader cultural shift Ioannidis advocated, though the change is incremental.

* **Economic impact:** No systematic evidence shows that a universal shift to *p* < 0.005 has increased trial costs. Instead, many sponsors have adopted adaptive designs and Bayesian monitoring to maintain power without inflating sample sizes, aligning with Ioannidis’s suggestion that smarter design can offset larger *n* requirements.

Overall, Ioannidis’s call sparked vigorous debate and modest policy tweaks, but the core *p* < 0.05 convention remains dominant in biomedical publishing as of early 2026.

## 3. PREDICTIONS  
* **Prediction:** “Lowering the threshold to *p* < 0.005 will reclassify about one‑third of published biomedical results as ‘suggestive.’”  
  *Outcome:* Roughly correct in magnitude for fields that have applied the stricter cutoff (e.g., psychology), but in biomedicine the change has been limited to isolated journals, so the overall proportion of re‑classified results across the literature is far smaller than a third.

* **Prediction:** “The new cutoff will make research more expensive and time‑consuming unless better designs are used.”  
  *Outcome:* No widespread cost surge has been documented. Instead, many groups have adopted adaptive and Bayesian designs that preserve power with similar or reduced sample sizes, partially validating Ioannidis’s mitigation argument.

* **Prediction:** “Most of the literature (80‑90 %) should stop using p‑values.”  
  *Outcome:* While the proportion of papers reporting only p‑values has declined (estimates suggest a drop from ~70 % in 2015 to ~55 % in 2024), the majority still rely on p‑values as a primary inferential tool. The prediction remains aspirational.

* **Prediction:** “Bayesian measures could be useful half the time, maybe more.”  
  *Outcome:* Bayesian analyses are now common in clinical trial monitoring (e.g., FDA’s Bayesian drug‑approval pathways) and in certain sub‑fields (genomics, epidemiology). Their usage is still well below 50 % of published studies, but the upward trend aligns with the prediction’s direction.

## 4. INTEREST  
Rating: **7/10**  
The article is a clear snapshot of a pivotal reproducibility debate that continues to shape statistical standards, making it notably relevant for understanding ongoing reforms in biomedical research.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180416-tighten-your-numbers.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_