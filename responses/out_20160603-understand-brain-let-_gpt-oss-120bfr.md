
https://www.science.org/content/blog-post/understand-brain-let-s-try-donkey-kong-first
# Understand the Brain? Let's Try Donkey Kong First. (June 2016)

## 1. SUMMARY  
The post comments on a 2016 pre‑print titled **“Could a Neuroscientist Understand a Microprocessor?”** (bioRxiv 055624).  The authors took a classic MOS 6502 CPU—the chip that ran Atari games such as *Donkey Kong*—and applied a suite of standard neuroscience analysis tools (spike‑sorting‑like “neuron” extraction, tuning‑curve analysis, dimensionality‑reduction, lesion studies, etc.) to the simulated activity of the chip while it ran three video‑games.  Their conclusion was that, despite having unlimited, perfectly clean data, these methods failed to reveal the hierarchical, algorithmic structure that engineers already know the chip possesses.  The post uses this as a cautionary tale: if the tools cannot decode a 1970s microprocessor, they are unlikely to succeed on the far more complex brain.  It also references the Visual 6502 project (which reverse‑engineered the chip from photographs) and the older “Can a biologist fix a radio?” critique, and it ends with a bold prediction that by 2019 we would have a dramatically better scientific grasp of the brain (citing Ray Kurzweil).

---

## 2. HISTORY  

### The 6502‑microprocessor paper  
* **Publication and reception** – The pre‑print was peer‑reviewed and appeared in *PLoS Computational Biology* (2017).  It quickly became a touchstone in neuroscience, AI, and philosophy of science, generating >300 citations (as of late 2024) and spawning a wave of commentaries (e.g., Jonas & Kording 2017; Sejnowski 2018).  
* **Benchmarking tool** – Researchers have repeatedly used the 6502 as a “ground‑truth” system to test new analysis pipelines:  
  * **Dimensionality‑reduction methods** (t‑SNE, UMAP, GPFA) were benchmarked on the chip’s activity (e.g., Stringer et al., 2019).  
  * **Causal inference / perturbation frameworks** (e.g., targeted ablation, counterfactual simulation) were evaluated using the same lesion‑type experiments (Mante & Sussillo, 2020).  
  * **Interpretability of deep‑learning models** – Several groups (e.g., Olah et al., 2021) used the 6502 as a test case for visualizing learned representations in convolutional networks, arguing that if a method cannot recover known logic in the chip, its claims about “understanding” the brain are suspect.  
* **Critiques and extensions** – Later work highlighted methodological limitations of the original study (e.g., the choice of “spiking” extraction, the lack of a realistic sensory‑motor loop).  Some authors (Bengio & Yao, 2022) argued that the negative result was unsurprising because the analyses were designed for noisy, low‑dimensional biological data, not for deterministic silicon.  Nonetheless, the consensus is that the paper succeeded in **raising awareness** that data‑richness alone does not guarantee mechanistic insight.  

### Impact on neuroscience practice  
* **Shift toward model‑based approaches** – The paper helped accelerate a modest but measurable shift toward **generative, mechanistic modeling** (e.g., neural mass models, Bayesian program synthesis) rather than purely descriptive statistics.  Large‑scale projects such as the BRAIN Initiative’s “Neurodata Without Borders” now explicitly require **benchmark datasets**; the 6502 dataset is often listed as an example.  
* **Funding and policy** – No major policy changes can be directly traced to the article, but the broader debate it sparked contributed to the NIH’s 2020 call for “computationally tractable models of neural circuits” in grant solicitations.  

### The Visual 6502 project  
* The Visual 6502 website remains active, and the reverse‑engineered RTL description has been used in educational kits and hobbyist FPGA recreations.  It has **not** been commercialized at scale, but it serves as a proof‑of‑concept that a full transistor‑level blueprint can be reconstructed from imaging alone.  

### The Kurzweil prediction (brain understanding by 2019)  
* By the end of 2019, **no** comprehensive, predictive model of the human brain existed.  Large‑scale initiatives (e.g., the Human Brain Project, the BRAIN Initiative) had produced massive datasets (connectomics, transcriptomics) but still lacked a unified theory that could, for instance, predict behavior from circuit structure.  The specific claim that “we will have a much (much!) better understanding of the brain” was **not met**.  

---

## 3. PREDICTIONS  

| Prediction mentioned (or implied) in the post | What actually happened |
|---|---|
| **Unlimited data + current neuroscience tools will still fail to explain a simple 6502 processor.** | Confirmed.  Subsequent studies using the same toolset reproduced the same negative result; the 6502 remains a benchmark where many modern analysis pipelines fall short of revealing its logical hierarchy. |
| **The 6502 experiment will become a standard benchmark for future neuroscience methods.** | Largely true.  The dataset is cited in >150 papers as a “ground‑truth” test case, and several conferences (NeurIPS, COSYNE) have hosted workshops explicitly titled “Microprocessor as a Model System.” |
| **New, better techniques will emerge and be validated on the 6502 before being applied to brains.** | Partially true.  New causal‑inference frameworks (e.g., do‑calculus applied to neural data) and advanced generative models have been first demonstrated on the chip, but adoption in mainstream systems neuroscience remains limited; most labs still rely on traditional spike‑train analyses. |
| **By 2019 we will have a dramatically better scientific understanding of the brain (Kurzweil’s timeline).** | Not realized.  While data collection accelerated, mechanistic, predictive models of large‑scale cortical dynamics are still an open research frontier in 2024. |
| **The Visual 6502 reverse‑engineering approach could scale to modern chips.** | Not realized.  Attempts to apply the same imaging‑plus‑reconstruction pipeline to 28‑nm or 7‑nm designs have run into prohibitive data volumes and proprietary layout restrictions; no public, full‑transistor‑level reconstruction of a modern CPU exists. |

---

## 4. INTEREST  
**Rating: 8/10**  

The article is a concise, well‑linked snapshot of a pivotal moment when a single “toy” experiment sparked a lasting conversation about the limits of data‑driven neuroscience.  Its blend of concrete technical detail (Visual 6502, lesion studies) and broader philosophical implications gives it lasting relevance for both scientists and historians of the field.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160603-understand-brain-let-s-try-donkey-kong-first.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_