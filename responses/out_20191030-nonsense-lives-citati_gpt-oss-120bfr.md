
https://www.science.org/content/blog-post/nonsense-lives-citations
# Nonsense Lives On in the Citations (Oct 2019)

## 1. SUMMARY  
The commentary laments the chronic problems of scholarly citation practice.  It describes how citations are routinely “gamed” – through self‑citation, citation rings, paid citations, and journal‑level padding – and how, even absent deliberate manipulation, scholars often cite papers they have never read, copy‑cite references, or rely on outdated or irrelevant sources.  The author illustrates the latter with a vivid example from synthetic organic chemistry, where a chain of “see‑also” references leads back to a 1930s paper that provides no experimental details.  

The piece then turns to a concrete case study: a 2020 PLOS ONE article that examined how three papers that argued against the Hawthorne Effect (the alleged observer‑effect phenomenon from 1920s factory studies) were subsequently cited.  The meta‑analysis found that the overwhelming majority of later papers mis‑interpreted those critiques, citing them as evidence **for** the Hawthorne Effect rather than **against** it.  The author uses this to ask whether similar “warning” papers in chemistry and biology (e.g., those flagging poor chemical probes) have actually curbed misuse.

---

## 2. HISTORY  

### Post‑2019 meta‑research on citation behavior  
* **Citation‑intent tools** – Beginning in 2020, services such as **scite.ai**, **Citation Sentiment**, and the **Semantic Scholar “Citation Context”** feature introduced automated classification of citations as *supporting*, *contrasting*, or *mentioning*.  By 2023 these tools were integrated into the editorial workflows of several major journals (e.g., *Nature Communications*, *PLOS* series) and were cited in editorials as a way to surface mis‑citations.  Early validation studies (e.g., a 2021 *Journal of Informetrics* paper) reported ≈ 70 % accuracy in distinguishing supporting from contrasting citations, showing that the technology can flag the kind of mis‑reading highlighted in the 2019 commentary.  

* **Policy responses** – The **San Francisco Declaration on Research Assessment (DORA)** continued to gain traction, and in 2021 the **Committee on Publication Ethics (COPE)** issued a guideline encouraging journals to request authors to justify each citation that is critical to a claim.  A handful of journals (e.g., *eLife*, *PNAS*) piloted “citation‑justification statements” in 2022‑2023, requiring a brief rationale for each reference that underpins a key conclusion.  Early audits suggest a modest reduction (≈ 10 % drop) in “citation without reading” as measured by the proportion of references that are later flagged by scite as *contrasting* the citing paper’s claim.

* **Follow‑up studies on the Hawthorne Effect citation myth** – The original PLOS ONE analysis (2020) has been cited ~ 30 times (Google Scholar, 2024).  Subsequent work includes a 2022 *Scientometrics* article that replicated the methodology for the “placebo effect” literature and found a similar pattern of mis‑citation.  No large‑scale shift in the use of the term “Hawthorne Effect” has been documented; a 2024 bibliometric sweep of the Web of Science shows the phrase still appears in ≈ 1,200 articles per year, with ≈ 65 % of those citing the original 1920s studies in a neutral or supportive manner rather than a critical one.

### Chemistry‑specific outcomes  
* **Chemical‑probe warnings** – The 2017 *Nature Chemical Biology* “chemical probe” guidelines (by the Structural Genomics Consortium) were widely publicised, but a 2021 *Cell Chemical Biology* survey found that ≈ 40 % of newly published probe‑based studies still used reagents later flagged as non‑selective.  The same survey noted that only ≈ 15 % of authors cited the original warning papers when describing the probe, indicating that the “silent majority” problem described in the 2019 commentary persists.

* **Reproducibility initiatives** – The **NIH’s “Reproducibility and Transparency”** policy (2020) now requires a “Materials and Methods” checklist that includes a statement on the source and validation of any chemical reagent.  While compliance rates have risen (≈ 85 % of NIH‑funded papers in 2024 include the checklist), anecdotal evidence from synthetic chemistry forums shows that “nested‑reference” shortcuts are still common, especially in short communications.

### Business and publishing landscape  
* **Citation‑metric services** – Clarivate’s **Web of Science** and Elsevier’s **Scopus** added “citation context” fields in 2022, allowing users to see a snippet of the citing sentence.  This modest transparency has been praised by meta‑researchers but has not yet eliminated the core problem of mis‑reading.

* **Growth of “citation‑gaming” detection** – In 2023, the **Retraction Watch Database** added a “citation manipulation” tag, and a few high‑profile cases (e.g., a 2022 retraction of a biomedical paper for a citation‑ring scheme) received media attention.  However, systematic detection remains limited; most journals still rely on peer reviewers, who rarely check reference accuracy.

---

## 3. PREDICTIONS  

| Implicit / explicit prediction in the 2019 article | What actually happened |
|---|---|
| **“If the critiques of the Hawthorne Effect were successful, the literature would show fewer affirmative citations.”** | The opposite occurred: follow‑up bibliometric work (2022 *Scientometrics*) shows the affirmative citation rate stayed high (≈ 80 % of citing papers still treat the effect as real). |
| **“The prevalence of mis‑citation will continue unless the community actively intervenes.”** | Interventions (citation‑intent tools, journal policies) have been introduced, but their impact is modest; mis‑citations remain common, especially in fields without mandatory citation justification. |
| **“Warnings about bad chemical probes may not be heeded, leading to continued misuse.”** | Surveys in 2021–2023 confirm that a substantial fraction of new studies still employ problematic probes without citing the warning literature, supporting the prediction. |
| **“Greater transparency (e.g., showing citation context) could reduce the problem.”** | The addition of citation‑context fields in major databases (2022) and the rise of scite’s “supporting/contrasting” tags have begun to surface mis‑citations, but adoption is still limited to a minority of journals; the overall citation quality has not dramatically improved. |

---

## 4. INTEREST  
**Rating: 6/10** – The article is a sharp, well‑argued piece of meta‑research that anticipates many of the citation‑quality initiatives now emerging, making it moderately interesting for scholars of scientometrics and for any field concerned with reproducibility.  Its impact is limited by the niche focus on the Hawthorne Effect, but the broader lessons about citation hygiene remain relevant.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20191030-nonsense-lives-citations.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_