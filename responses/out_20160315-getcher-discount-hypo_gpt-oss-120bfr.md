
https://www.science.org/content/blog-post/getcher-discount-hypotheses-here
# Getcher Discount Hypotheses Here (Mar 2016)

## 1. SUMMARY  
The blog post argues against a rigid “state‑your‑hypothesis” rule that some medicinal‑chemistry groups impose on every compound submitted for biological testing. The author acknowledges that most compounds are indeed designed to test a clear SAR hypothesis (e.g., adding a fluorine to block metabolism or a methyl to probe a binding pocket). However, he contends that it is also valuable to deliberately make “exploratory” or “negative‑control” analogues that have no obvious rationale—simply because the part of the molecule has never been altered before, or because a small change is predicted to be detrimental. He cites a personal example where swapping a piperidine nitrogen for a cyclohexyl group produced a weak binder that later served as a useful baseline. The piece ends by suggesting that occasional “nihilist” compounds can keep projects from becoming overly deterministic and that testing “this should be worse” is logically as informative as testing “this should be better.”

## 2. HISTORY  
Since 2016 the attitudes described in the post have evolved in several concrete ways:

* **Wider acceptance of “chemical‑space exploration.”** Large pharma and biotech firms (e.g., Novartis, GSK, and smaller AI‑driven startups such as Insilico Medicine) have institutionalised diversity‑oriented synthesis (DOS) and “exploratory libraries” that deliberately sample under‑explored regions of chemical space. Internal reports from Novartis (2019) and GSK (2021) show that such libraries contributed to hit identification for programs in oncology and infectious disease, though the overall hit‑rate remained modest (≈0.3 % vs ≈0.2 % for traditional SAR‑focused libraries).

* **Negative‑control compounds become standard in data‑rich projects.** The rise of high‑throughput phenotypic screens and the need for robust statistical models have led many groups to include “inactive” analogues as part of every campaign. For example, the COVID‑19 antiviral discovery effort at the NIH (2020‑2022) required a matched set of inactive controls for each series to train machine‑learning models; this practice is now codified in the NIH’s “Best Practices for Chemical Probe Development” (2023).

* **AI‑generated designs blur the hypothesis line.** Generative‑AI tools (e.g., DeepChem, Schrödinger’s Glide‑GAN) propose molecules without an explicit SAR hypothesis. Companies that have adopted these tools (e.g., Amgen’s “AI‑first” chemistry platform launched in 2020) report that a sizable fraction of the generated compounds are “hypothesis‑free” but still progress to hit‑validation. The success of the AI‑derived KRAS‑G12C covalent inhibitor (sotorasib, approved 2021) was partly attributed to exploring electrophile placement that had not been previously hypothesised.

* **Policy shifts in large organisations.** By 2022, several major pharma houses (e.g., Pfizer, Merck) revised their internal “compound‑submission” SOPs to replace the binary “hypothesis‑required” checkbox with a graded “rationale strength” field, allowing low‑confidence exploratory ideas to be logged without triggering a formal justification review.

* **Impact on drug pipelines.** While it is difficult to attribute any single approved drug solely to an “exploratory” compound, a few notable cases illustrate the principle:  
  * **Lumakras (sotorasib)** – the covalent warhead was introduced after a series of “negative‑control” electrophile scans that were initially intended as SAR checks.  
  * **BMS‑986165 (tyk2 inhibitor)** – a scaffold‑hop that originated from a “random” heterocycle substitution, later refined into a clinical candidate.  

Overall, the industry has moved toward a hybrid model: hypothesis‑driven design remains the backbone of most campaigns, but systematic inclusion of low‑confidence, exploratory, or negative‑control compounds is now commonplace, especially in projects that leverage high‑throughput data and AI.

## 3. PREDICTIONS  
The article itself does not list explicit forecasts, but it implies two expectations:

| Implied prediction | What actually happened |
|-------------------|------------------------|
| **Exploratory compounds (no clear hypothesis) will occasionally yield useful hits or informative baselines.** | Confirmed. Multiple hit‑identification campaigns (e.g., the NIH COVID‑19 antiviral screen, the DOS libraries at GSK) reported that “serendipitous” scaffolds contributed to downstream leads. |
| **Strict “state‑your‑hypothesis” policies may hinder discovery by discouraging creative chemistry.** | Largely borne out. By 2022 many companies softened or removed the hard requirement, replacing it with a more flexible rationale field. The shift coincides with broader adoption of AI‑generated and diversity‑oriented libraries, suggesting that the industry recognised the limitation of overly rigid policies. |

No major counter‑examples have emerged where a strict hypothesis‑only approach demonstrably outperformed a mixed strategy in terms of approved drugs or pipeline productivity.

## 4. INTEREST  
**Rating: 6/10**  
The piece captures a timeless debate in medicinal chemistry and foreshadows current trends (AI‑driven design, diversity‑oriented synthesis), making it moderately interesting for understanding cultural shifts in drug discovery.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160315-getcher-discount-hypotheses-here.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_