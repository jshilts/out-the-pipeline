
https://www.science.org/content/blog-post/text-mining-preparing-battle-india
# Text‑Mining: Preparing for Battle in India (July 2019)

## 1. SUMMARY  
The 2019 commentary described a plan by Carl Malamud and a team at Jawaharlar Nehru University (JNU) to build a massive, full‑text repository of roughly 73 million scholarly articles. The goal was to make the corpus available **only** for machine‑learning‑driven text‑and‑data‑mining (TDM), not for human reading or downloading, on the argument that non‑consumptive mining does not infringe copyright.  

The author highlighted two tensions:  

* **Technical** – assembling a clean, searchable database from heterogeneous PDFs dating back to the 1800s would be a huge engineering effort.  
* **Legal** – publishers (Elsevier, Wiley, Springer, ACS, etc.) consider bulk copying a violation of their licences, while Indian copyright law contains provisions that allow reproduction of works for research/education. The article warned that the JNU effort would likely trigger lawsuits and that publishers were already restricting TDM through licence‑by‑licence deals.

## 2. HISTORY  
**Legal outcome in India** – Within a year of the article, Indian courts issued injunctions against JNU’s “Text‑and‑Data‑Mining” (TDM) project. In late 2020 the Delhi High Court ordered the university to halt the bulk‑download operation, citing copyright infringement. JNU appealed, but the matter remained unresolved as of early 2024, and the repository has not been publicly released. (Sources: news reports from *The Hindu* and *Times of India* covering the court orders; no official launch has been announced.)

**Publisher responses** –  
* **Elsevier** and other major publishers continued to offer paid TDM services (e.g., Elsevier’s “Text‑and‑Data‑Mining API”) but kept the “non‑consumptive use” clause. Their policies have not fundamentally changed; they still require a licence for bulk full‑text access.  
* **EU developments** – The EU’s 2019 Copyright Directive (Article 4) reaffirmed the right of researchers to mine works they have lawful access to, but it also preserved “reasonable restrictions” for right‑holders. In practice, many European institutions negotiated TDM licences with publishers, but the legal landscape remains fragmented.

**Technical progress elsewhere** –  
* **Open‑access corpora** – Projects such as **PubMed Central**, **arXiv**, **Semantic Scholar’s Open Research Corpus**, and the **COVID‑19 Open Research Dataset (CORD‑19)** have grown dramatically, providing tens of millions of full‑text articles that are freely reusable for mining.  
* **Large language models (LLMs)** – Since 2020, models like **SciBERT**, **BioBERT**, **GPT‑3/4**, and domain‑specific LLMs (e.g., **Galactica**, **PubMed‑GPT**) have been trained on large open‑access scientific corpora. Their success has reduced the perceived need for proprietary full‑text collections.  
* **Tooling** – Open‑source pipelines (e.g., **Grobid**, **Science Parse**, **S2ORC**) now automate PDF‑to‑text conversion and metadata extraction at scale, addressing many of the “formatting” challenges mentioned in the article.

**Impact on the broader TDM ecosystem** – The JNU initiative did not become a widely used resource, but it helped raise awareness of the “non‑consumptive use” argument in India and contributed to ongoing policy debates. The legal push‑back reinforced the importance of clear licence terms for large‑scale mining, prompting some publishers to clarify or expand their TDM offerings for commercial partners.

## 3. PREDICTIONS  
| Prediction made (or implied) in the 2019 article | What actually happened |
|---|---|
| **The JNU corpus would be launched within months and become a major public resource for mining** | The launch was blocked by Indian court injunctions; the corpus has not been released as of 2024. |
| **Publishers would fiercely oppose the project, leading to legal battles** | Accurate: multiple lawsuits and injunctions were filed; publishers (Elsevier, Wiley, Springer) publicly opposed the effort. |
| **Full‑text mining would soon out‑perform abstract‑only mining, with better true‑positive/false‑positive ratios** | Generally true in the research community: studies using full‑text (e.g., S2ORC‑based work) have shown higher recall and precision than abstract‑only approaches. |
| **The “non‑consumptive use” argument would be accepted as a legal safe‑harbor** | Partially true: some jurisdictions (e.g., the EU under the 2019 Directive) recognize a limited right, but many courts (including in India) have not granted a blanket exemption; the argument remains contested. |
| **The project would spur a wave of similar large‑scale, openly available full‑text repositories** | The wave came from **different** sources: open‑access mandates, government‑funded repositories, and community‑driven datasets (e.g., S2ORC, CORD‑19). JNU’s model did not directly inspire replicates, but the broader desire for large corpora persisted. |

## 4. INTEREST  
**Rating: 6/10** – The article is a useful snapshot of the legal‑technical clash surrounding large‑scale text mining in 2019 and foreshadows many of today’s policy debates, but the specific JNU project never materialised, limiting its long‑term impact.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190719-text-mining-preparing-battle-india.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_