
https://www.science.org/content/blog-post/what-s-crucial-and-what-isn-t
# What’s Crucial And What Isn’t (September 2019)

## 1. SUMMARY  
The author argues that the hype around big‑tech AI efforts to predict protein structures (e.g., the claim that “Amazon, Google, and Facebook are using AI to find protein structures, a crucial step in drug discovery”) overstates the importance of structure prediction for actually delivering new medicines. He points out that many successful drug‑discovery programs have proceeded without high‑resolution target structures, relying instead on robust phenotypic assays, translatable animal models, and clean toxicology data. While acknowledging that AI‑driven structure prediction is a useful tool, he predicts it will not, by itself, produce a “big leap” in drug‑development efficiency. The real bottlenecks, in his view, are target validation, predictive disease models, and early safety assays.

## 2. HISTORY  
**Breakthroughs in structure prediction (2020‑2024)**  
* **AlphaFold 2** (DeepMind, July 2021) achieved near‑experimental accuracy on the CASP14 benchmark, dramatically raising confidence in AI‑predicted structures.  
* **AlphaFold Protein Structure Database** (released July 2021, expanded to >200 million predicted structures by 2023) made high‑confidence models freely available to the scientific community.  
* **RoseTTAFold** (University of Washington, 2021) provided an open‑source alternative that quickly gained traction.  

**Adoption in biotech and pharma**  
* Academic labs now routinely retrieve AlphaFold models for target inspection, mutagenesis planning, and hypothesis generation.  
* Several biotech companies (e.g., **Exscientia**, **Insilico Medicine**, **Schrödinger**) incorporated AlphaFold predictions into their computational pipelines, mainly for **binding‑site annotation** and **homology‑model improvement**.  
* Large‑pharma collaborations (e.g., **Pfizer‑DeepMind** on SARS‑CoV‑2 main‑protease) used AI‑predicted structures to accelerate early‑stage design, but the final drug candidates still relied on experimentally determined structures or extensive SAR work.  

**Impact on drug approvals**  
* As of early 2024, **no FDA‑approved small‑molecule drug** has been publicly credited as being discovered *solely* from an AlphaFold‑derived structure.  
* The most cited success stories involve **target validation** and **mechanistic insight** (e.g., identification of a cryptic pocket in the LRRK2 kinase for Parkinson’s research, or guidance for antibody epitope mapping against SARS‑CoV‑2). These contributions shortened research timelines but did not directly translate into a marketed product.  

**Big‑tech involvement**  
* **Google/DeepMind** remains the primary AI‑structure player; **Amazon Web Services** provides the compute backbone for many users, but Amazon itself has not launched a drug‑discovery product based on its AI models.  
* **Meta (Facebook) AI Research** contributed early work on protein‑folding networks but has not maintained a high‑profile public program in this space.  

**Overall effect on the drug‑discovery ecosystem**  
* The AI‑predicted structures are now considered **standard background data**—similar to a “digital atlas” that researchers consult before committing to experimental work.  
* They have **reduced the need for de‑novo crystallography** for many targets, especially those that are difficult to express, but they have **not eliminated the experimental validation step** (e.g., confirming ligand binding, assessing dynamics).  
* The **primary bottlenecks** identified in the article—predictive disease models, translatable animal systems, and early safety assays—remain largely unchanged; progress in those areas has been incremental (e.g., organ‑on‑chip platforms, improved in‑silico toxicology) rather than revolutionary.  

## 3. PREDICTIONS  
| Prediction made (or implied) in the 2019 article | What actually happened |
|---|---|
| **Protein‑structure prediction will *not* become a rate‑limiting step in drug discovery** | Largely true. AI models now supply structures quickly, removing a bottleneck for many targets. |
| **AI‑predicted structures will *not* on their own drive a major efficiency leap** | Accurate. No clear, quantifiable jump in overall pipeline speed or cost has been demonstrated; gains are modest and context‑dependent. |
| **The “real killers” are target validation, predictive models, and early safety data** | Still correct. Advances in organoid models, CRISPR screens, and in‑silico ADMET have been the main drivers of efficiency gains, not structure prediction. |
| **Big‑tech claims that AI will revolutionize drug discovery are overblown** | The hype has been tempered. While DeepMind’s AlphaFold is celebrated, most companies treat it as a complementary tool rather than a replacement for traditional R&D. |
| **Widespread adoption of AI‑driven virtual screening will soon replace experimental screening** | Not realized. Virtual screening using predicted structures is used, but experimental high‑throughput screening remains essential for hit identification. |

## 4. INTEREST  
**Rating: 7/10**  
The article is a thoughtful, skeptical counter‑point to the 2019 hype wave and remains relevant because it correctly anticipated the limited, incremental impact of AI structure prediction on drug pipelines, even after the AlphaFold breakthrough. Its relevance to ongoing discussions about AI’s role in biotech gives it solid, though not groundbreaking, interest.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190925-what-s-crucial-and-what-isn-t.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_