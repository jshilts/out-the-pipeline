
https://www.science.org/content/blog-post/virtual-compound-screening-state-art
# Virtual Compound Screening: The State of the Art (September 2018)

## 1. SUMMARY  
The 2018 commentary by Pat Walters (and reposted here) surveys the problem of “chemical space”: the gap between the few million compounds that can be physically screened in a laboratory and the astronomically larger set of molecules that could, in principle, be evaluated in silico.  Walters reviews estimates of the total number of drug‑like molecules—typically 10²⁰–10³⁰ depending on the definition of “drug‑like”—and describes how researchers have tried to generate massive virtual libraries (e.g., the GDB‑17 enumeration of 166 billion molecules, commercial‑starting‑material libraries that quickly reach quadrillions).  

He points out that existing clustering and similarity‑search tools break down beyond the low‑million‑compound range, and that even fast 2‑D screens become unwieldy when one attempts to dock billions of 3‑D conformers against realistic protein pockets.  The article stresses two practical bottlenecks: (1) computational scaling limits on both library handling and docking, and (2) high false‑positive rates of current scoring functions.  As a possible way forward, Walters suggests “generative” approaches that build libraries on‑the‑fly guided by activity predictions, but notes that such methods were still experimental in 2018 and would likely need new machine‑learning algorithms to reach their promise.

## 2. HISTORY  
**Growth of ultra‑large docking campaigns** – After 2018 several groups demonstrated that billions of compounds could be docked on modern GPU clusters or cloud platforms.  Notable examples include the 2020 “1.4‑billion‑compound” screen against the SARS‑CoV‑2 main protease (Lyu et al., *Nature*), which yielded low‑micromolar inhibitors that progressed to animal studies.  Similar billion‑scale screens have been reported for KRAS G12C, the estrogen receptor, and various kinases, showing that the hardware bottleneck has been largely overcome by GPU‑accelerated docking engines (e.g., *AutoDock‑GPU*, *Vina‑GPU*, *Gnina*).

**Generative chemistry becomes mainstream** – Deep learning‑driven molecule generators (variational autoencoders, reinforcement‑learning agents, diffusion models) have moved from proof‑of‑concept to production pipelines.  Companies such as Insilico Medicine, Exscientia, and Relay Therapeutics have reported AI‑designed candidates entering IND‑enabling studies.  The most publicized case is DSP‑1181, an AI‑designed melatonin‑receptor antagonist that entered a Phase I trial in 2021 and completed dosing without safety concerns.  By 2024, dozens of AI‑generated molecules have reached preclinical or early clinical stages, confirming that generative approaches can produce chemically tractable, synthetically accessible hits.

**Improved scoring and false‑positive mitigation** – The community has introduced several strategies to curb the high false‑positive rates that Walters warned about: (i) consensus docking (multiple scoring functions), (ii) rescoring with physics‑based methods such as MM‑GBSA or free‑energy perturbation on a narrowed set, and (iii) integration of structure‑based deep‑learning scoring (e.g., *DeepDock*, *EquiBind*).  Retrospective analyses of ultra‑large screens show enrichment factors that are modest but reproducible, and the overall hit‑to‑lead conversion has improved from ~0.001 % to ~0.01 % in the best cases.

**Database handling advances** – Modern cheminformatics platforms (e.g., *FAIR*Chem, *MolPort*, *OpenEye*’s *Omega* with cloud‑native indexing) now support indexing and similarity search over tens of billions of molecules using locality‑sensitive hashing and GPU‑accelerated clustering.  While true “all‑of‑chemical‑space” indexing remains infeasible, the practical limit for routine similarity search has moved from ~10 M to >10 B compounds.

**Policy and industry impact** – The rise of AI‑driven virtual screening has spurred increased investment: venture capital funding in AI‑chemistry startups grew from ≈ $200 M in 2018 to > $2 B in 2025.  Regulatory agencies have begun to issue guidance on the use of AI‑generated structures in IND submissions (FDA 2023 draft guidance).  However, the “big‑data” hype has not translated into a wholesale replacement of wet‑lab HTS; most pharma programs now use a hybrid model—small focused libraries for primary screens, complemented by AI‑guided virtual enrichment.

## 3. PREDICTIONS  

- **Prediction:** *Current hardware will soon hit scaling limits for brute‑force virtual screens; generative methods will be needed.*  
  **Outcome:** Largely correct.  By 2022 GPU clusters and cloud services allowed docking of >10⁹ compounds, but further scaling (10¹²‑10¹³) remains impractical.  Generative models are now routinely used to propose focused libraries of 10⁴‑10⁶ candidates, sidestepping exhaustive enumeration.

- **Prediction:** *New machine‑learning algorithms will be required to unlock the full potential of on‑the‑fly library generation.*  
  **Outcome:** Accurate.  Diffusion‑based molecule generators (2023‑2025) and transformer‑based retrosynthesis planners have become the de‑facto standard for on‑demand library creation, delivering chemically realistic, synthetically tractable molecules.

- **Prediction:** *False‑positive rates must be dramatically reduced for big‑drug‑like space navigation to be useful.*  
  **Outcome:** Partially fulfilled.  Consensus docking and ML rescoring have lowered false‑positive rates by roughly an order of magnitude, but they remain a major source of attrition; experimental validation is still essential.

- **Prediction:** *Clustering algorithms will not handle >10 M compounds efficiently.*  
  **Outcome:** Confirmed.  Traditional hierarchical clustering still fails beyond ~10⁸ items.  New approximate nearest‑neighbor methods (e.g., HNSW, FAISS) now handle billions, but they trade exactness for speed and are used mainly for similarity search, not full clustering.

- **Prediction:** *Generative techniques “barely tested” in 2018 will soon be proven.*  
  **Outcome:** True.  Within five years (by 2023) several AI‑generated molecules entered IND‑enabling studies, and by 2025 dozens of such candidates were in preclinical pipelines.

## 4. INTEREST  
**Rating: 7/10** – The article captures a pivotal moment when the community recognized the limits of brute‑force virtual screening and anticipated the AI‑driven shift that has since reshaped drug discovery.  Its blend of realistic constraints and forward‑looking suggestions makes it still relevant, though many specifics have been superseded by rapid methodological advances.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180906-virtual-compound-screening-state-art.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_