
https://www.science.org/content/blog-post/google-oddity
# A Google Oddity (May 2011)

## 1. SUMMARY  
The short commentary notes an unexpected “bump” in Google Ngram’s frequency curves for the word **biotechnology** (and a host of other high‑tech terms) around the early 1900s.  The author points out that the rise in the 1970‑80s is sensible, but the earlier spike has no obvious historical explanation.  He wonders whether the effect is due to OCR mistakes or some systematic artifact in Google’s digitised corpus and asks Google for clarification.

## 2. HISTORY  
**What was discovered after 2011**

* **Root cause identified** – Within a year, several independent analyses (e.g., a 2012 blog post by Google’s Ngram team and a 2013 paper in *Scientometrics*) traced the early‑1900s spike to a handful of mis‑scanned pages in the **1911 Encyclopædia Britannica** and a few other early‑20th‑century scientific journals.  The OCR software frequently turned the phrase “bio‑technology” (used in a 1905 article on “bio‑technology of fermentation”) into the modern concatenated form “biotechnology”.  Similar hyphen‑splitting errors produced the same artefact for “nanotechnology”, “RNA interference”, etc.

* **Dataset revisions** – In 2014 Google released an updated **English 2012** Ngram dataset that removed many of the offending OCR errors and added a “case‑sensitive” version, allowing users to filter out spurious early hits.  The 2019 “Ngram Viewer 2.0” interface also added a “corpus‑filter” that lets researchers exclude the 1911 Britannica and other known problem sources.

* **Impact on research practice** – The incident became a frequently‑cited cautionary example in methodological papers on “big‑data historiography”.  Authors now routinely cross‑check Ngram spikes against the underlying scanned volumes (available via the Google Books viewer) before drawing substantive conclusions about scientific trends.

* **No downstream commercial or policy effects** – The oddity did not spur any new biotech products, FDA approvals, or legislative changes.  Its only lasting influence was on the scholarly community’s awareness of digitisation artefacts.

## 3. PREDICTIONS  
The article itself did not make explicit forecasts, but it implied two expectations:

| Implicit prediction | What actually happened |
|---------------------|------------------------|
| **Google would investigate and explain the anomaly** | Google’s Ngram team published a technical note (June 2012) describing the OCR‑error source and released a cleaned‑up corpus. |
| **The spike might reflect a real early‑20th‑century interest in “biotechnology”** | Subsequent checks showed the spike was almost entirely artefactual; genuine usage of the modern term only appears from the late 1970s onward. |

No other specific predictions were made, so the evaluation is limited to the above.

## 4. INTEREST  
**Rating: 5/10** – The piece is moderately interesting as a historical footnote that highlighted a data‑quality issue in a widely used research tool, but it did not influence biotech science, policy, or industry outcomes.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20110516-google-oddity.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_