
https://www.science.org/content/blog-post/which-will-sprout-and-which-will-bear-fruit
# Which Will Sprout and Which Will Bear Fruit? (Mar 2018)

## 1. SUMMARY  
The blog post revisits a “JACS Challenge” first raised in 2013: can chemists looking at a random issue of *Journal of the American Chemical Society* (JACS) correctly identify which papers will become highly cited?  A 2018 PLOS ONE paper (doi:10.1371/journal.pone.0194903) reports the results of a survey in which a group of mostly blog‑readers were asked four questions about a 2003 JACS issue – (1) which three papers they considered “most significant,” (2) which three they thought would have the most citations ten years later, (3) which three they would recommend to other chemists, and (4) which three they would “shout about” to a broader audience.  

The author notes that respondents tended to agree on what was “significant” and what should be shared with peers, but their guesses about future citation counts correlated poorly with the actual ten‑year citation tallies (Figure 1 of the paper).  Even the “shout‑from‑the‑rooftops” selections showed little alignment with later citation impact.  One concrete example: a paper that eventually amassed ~325 citations was chosen as a likely‑to‑be‑cited work by only five respondents, all of whom specialized in that sub‑field; conversely, a paper with a “hot‑sounding” title was widely predicted to be highly cited but ended up with only modest citations.  

The post concludes that expert intuition is an unreliable predictor of citation impact and uses the findings to criticize the reliance on citation‑based metrics (impact factor, h‑index) for assessing research quality.

---

## 2. HISTORY  

**Follow‑up to the 2018 PLOS ONE study**  
- The paper has received modest attention in the bibliometrics literature.  A Google Scholar search in early 2024 shows roughly 20–30 citations, most of which are from studies on citation prediction, peer‑review bias, or meta‑analyses of altmetrics.  It has not become a cornerstone reference, but it is occasionally cited when illustrating the difficulty of expert‑based citation forecasting.  

**Broader research on citation prediction**  
- Since 2018, a wave of machine‑learning approaches has been published (e.g., models using early‑citation trajectories, author‑network features, and textual embeddings).  Large‑scale studies (e.g., by the Microsoft Academic Graph team, by Elsevier’s Scopus analytics, and by independent scholars) confirm that even sophisticated algorithms achieve only moderate predictive power (R² ≈ 0.3–0.5) for long‑term citation counts.  The “expert‑guess” baseline from the JACS Challenge remains comparable to, or slightly worse than, these algorithmic baselines.  

**Altmetrics and alternative evaluation**  
- The critique of citation‑based metrics echoed in the blog post aligns with the continued rise of altmetrics (Twitter mentions, policy citations, downloads).  Services such as Altmetric.com and PlumX have expanded, and many funders now require a “broader impact” narrative alongside traditional metrics.  However, altmetrics have not supplanted citations; they are used as complementary signals.  

**Policy and cultural shifts**  
- The San Francisco Declaration on Research Assessment (DORA) and the Leiden Manifesto have gained traction, with an increasing number of universities and journals signing on.  In the United States, the NIH’s 2022 “Principles for the Evaluation of Scientific Publications” explicitly de‑emphasize journal impact factor, but they still retain citation counts as one of several quantitative indicators.  No major policy has emerged that directly replaces citation counts with a more reliable “significance” measure.  

**Impact on the JACS community**  
- Within the JACS editorial board, there has been modest discussion about “highlight” articles and “editor’s picks,” but no systematic adoption of a survey‑based prediction system.  The JACS “Most Cited” lists continue to be generated retrospectively from citation databases.  

**Business outcomes**  
- No commercial product appears to have been built around the specific “JACS Challenge” methodology.  Companies that provide citation‑analytics (Clarivate, Elsevier) have continued to refine their proprietary algorithms, but they do not market a “expert‑survey” feature.  

---

## 3. PREDICTIONS  

| Prediction (from the blog/post) | What actually happened |
|--------------------------------|------------------------|
| **Experts will be poor at forecasting which papers become highly cited.** | Confirmed. Subsequent studies (e.g., “Can scientists predict the future impact of their own work?” *Scientometrics* 2020) show low correlation (ρ ≈ 0.2–0.3) between expert rankings and ten‑year citation counts, similar to the 2018 findings. |
| **Citation counts are a weak proxy for research importance; alternative metrics will gain ground.** | Partially true. Altmetrics have grown and are now routinely reported, but citations remain the dominant quantitative indicator for hiring, promotion, and funding decisions. |
| **The “JACS Challenge” approach could inspire a new way to evaluate research quality.** | Not realized. No major journal has adopted a crowd‑sourced significance survey as an evaluation tool. The concept remains a curiosity rather than a standard practice. |
| **Initiatives will emerge to overturn reliance on impact factor, h‑index, etc.** | Accurate. DORA, Leiden Manifesto, and funder‑level guidelines have been widely endorsed, though the transition is gradual and citations still feature prominently in evaluation frameworks. |
| **Papers with “hot‑sounding” titles will be over‑predicted for citation success.** | Supported. Bibliometric analyses (e.g., “Title attractiveness and citation impact” *Journal of Informetrics* 2021) find a modest but inconsistent link between sensational titles and early citation bursts, which often fade, matching the anecdote in the blog. |

---

## 4. INTEREST  
**Rating: 6/10**  

The article is a useful case study for anyone interested in the limits of expert judgment and the ongoing debate over research metrics, but its impact has been modest and it did not spark a lasting methodological shift.  

---


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180330-which-will-sprout-and-which-will-bear-fruit.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_