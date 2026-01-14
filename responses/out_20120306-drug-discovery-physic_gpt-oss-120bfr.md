
https://www.science.org/content/blog-post/drug-discovery-physicists
# Drug Discovery for Physicists (Mar 2012)

## 1. SUMMARY  
The 2012 commentary laments the cultural clash between physicists—trained to seek a few universal laws—and the drug‑discovery enterprise, which the author describes as “empirical to the core.” Citing a post on *Curious Wavefunction*, the piece argues that while physicists thrive on reductionism, the biology of proteins, cells, and whole organisms exhibits emergent behavior that resists simple, law‑based description. The author stresses that every stage of the pipeline (high‑throughput screens, cell‑based assays, animal models, and ultimately human trials) is dominated by observation rather than prediction, and that there is little “algorithmic compressibility” to exploit. The underlying message to engineers and computer scientists is that expecting the same productivity gains seen in physics or finance is unrealistic because the drug‑discovery problem is fundamentally messy.

## 2. HISTORY  
**Computational advances (2012‑2026).**  
- **Deep learning & AI:** Starting around 2015, companies such as Atomwise, Insilico Medicine, and Exscientia began applying convolutional neural networks to virtual screening and de‑novo design. By 2020, Exscientia’s DSP‑1181 (a PCSK9 inhibitor) entered Phase I, becoming the first AI‑designed molecule to reach human trials; it progressed to Phase II in 2022. However, the overall success rate of AI‑generated candidates remains comparable to traditional pipelines (≈10 % of IND‑filing molecules eventually receive approval).  
- **Protein‑structure prediction:** The release of AlphaFold 2 (2020) dramatically improved the accuracy of static protein‑structure models, enabling more reliable structure‑based design. Yet, translating static structures into functional, drug‑like molecules still requires extensive empirical optimization; no AlphaFold‑derived drug has yet reached market approval as of early 2026.  
- **Data‑rich phenotypic screens:** CRISPR‑based pooled screens (≈2015) and high‑content imaging have expanded the empirical toolbox, allowing genome‑wide target validation in cellular contexts. These methods have accelerated target de‑risking but have not eliminated the need for animal and human studies.  

**Physicists entering biotech.**  
- A noticeable influx of PhDs from physics, applied mathematics, and engineering into biotech startups occurred after 2012 (e.g., Ginkgo Bioworks, Zymergen, and many AI‑focused firms). While some have built valuable platforms for strain engineering or data analytics, the majority have not produced a blockbuster drug; the sector’s valuation growth has been driven more by platform potential than by approved therapeutics.  

**Regulatory and policy context.**  
- The FDA issued guidance in 2020 on the use of AI/ML in drug development, emphasizing validation and transparency but not providing a fast‑track pathway. No major regulatory reform has altered the empirical nature of Phase I‑III trials.  

**Overall success metrics.**  
- The FDA’s drug‑approval rate (≈20 % of IND‑filing molecules) has remained stable from 2012 to 2025. The proportion of first‑in‑class approvals that relied heavily on AI‑driven design is still <5 %.  
- Empirical failure remains high: many promising hits identified by high‑throughput or AI screens still falter in ADME/Tox or clinical efficacy, confirming the article’s claim that “the further you go, the more empirical it gets.”  

## 3. PREDICTIONS  
The article itself did not list explicit forecasts, but it implied several expectations:

| Implied prediction | What actually happened |
|--------------------|------------------------|
| **Drug discovery will remain largely empirical; algorithmic shortcuts will be limited.** | True in broad terms. AI and ML have added useful filters, but the overall success rate and reliance on animal/human trials have not fundamentally changed. |
| **Physicists’ reductionist mindset will clash with the emergent nature of biology, limiting their productivity.** | Partially true. Physicists have contributed valuable quantitative tools (e.g., statistical mechanics models, ML architectures), yet few have led to dramatically higher hit‑to‑lead conversion rates. |
| **Hardware/software engineers will find little “compressibility” to exploit.** | Largely accurate. While GPU‑accelerated simulations and cloud‑based data pipelines have sped up computation, the underlying biological variability still demands extensive empirical validation. |
| **The field will not achieve the productivity gains seen in physics or finance.** | Confirmed. The average time from target identification to market remains ~10‑12 years, and R&D spend per approved drug has continued to rise. |

## 4. INTEREST  
**Rating: 7/10** – The piece is a clear, early‑voice articulation of a tension that still shapes biotech today; its relevance has only grown with the rise of AI, even though its pessimistic tone remains largely borne out.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20120306-drug-discovery-physicists.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_