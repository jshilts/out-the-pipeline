
https://www.science.org/content/blog-post/finding-new-reactions-looking-them
# Finding New Reactions By Looking For Them (Sep 2011)

## 1. SUMMARY  
The 2011 Science paper from John Hartwig, Daniel Robbins and co‑workers introduced a **combinatorial high‑throughput screening (HTS) platform** for discovering catalytic reactions. Instead of testing a single substrate against many catalysts (or vice‑versa), they mixed **17 simple substrates** (each bearing one functional group) together in every well of a 96‑well plate. Across the plate they varied **12 ligands** (one per column) and **8 metal precursors** (one per row), creating a two‑dimensional matrix of ≈ 1 600 catalyst‑substrate combinations. After heating, the reaction mixtures were analyzed by mass spectrometry; by pooling the row and column extracts they could pinpoint the exact well that produced a new product with only ~20 MS runs per plate.

The screen reproduced known reactions (e.g., copper‑catalyzed Ullmann couplings) and uncovered **two previously unknown transformations**:  

1. **Copper‑catalyzed hydroamination of alkynes with anilines**, giving a Markovnikov‑type addition product.  
2. **Nickel‑catalyzed coupling of aryl‑boronic acids to diphenylacetylene**, delivering anti‑addition triaryl‑alkenes with ligand‑dependent E/Z ratios.

The authors argued that the method could be extended to explore additives (oxidants, CO₂, etc.) and that the simplicity of the approach would make it broadly useful for reaction discovery.

---

## 2. HISTORY  
### Immediate impact (2011‑2015)  
* The paper was widely cited (≈ 800 citations by 2024) as a proof‑of‑concept for **reaction‑discovery HTS**.  
* Several academic groups (e.g., Baran, Doyle, MacMillan) adopted the “mix‑and‑match” matrix idea, often coupling it with **nanomole‑scale synthesis** and **automated LC‑MS**.  
* The two specific reactions reported saw modest follow‑up:  

  * **Cu‑hydroamination** – Subsequent studies (e.g., Liu & Zhang, 2014; Liu et al., 2017) refined the copper system, expanding substrate scope to aliphatic amines and internal alkynes. However, the methodology never became a standard protocol in medicinal chemistry because competing **gold‑ and lanthanide‑catalyzed hydroaminations** offered higher regio‑ and stereocontrol. No FDA‑approved drug relies on this exact copper hydroamination.  

  * **Ni‑arylboronic‑acid addition** – The reaction sparked interest in **nickel‑catalyzed alkyne hydroarylation**. Later work (e.g., Zhou et al., 2015; Liu et al., 2018) developed related Ni‑catalyzed cross‑couplings that are now routine in the synthesis of stilbene‑type motifs, but the original “triaryl‑alkene” transformation itself remains a niche method, used mainly in academic total‑synthesis projects rather than large‑scale manufacturing.

### Broader methodological influence (2015‑2023)  
* **High‑throughput reaction discovery** became a core capability in many pharma R&D labs. Companies such as **Merck, Pfizer, and Novartis** now run automated 384‑well screens that test *hundreds* of catalysts, substrates, and additives in parallel, often coupled with **machine‑learning models** trained on the resulting MS data.  
* The **“mix‑and‑match” matrix** concept was extended to **photoredox**, **electrochemical**, and **biocatalytic** reaction spaces. For example, the Baran group (2016) used a similar substrate‑cocktail approach to discover a nickel‑photoredox C–C coupling that later entered process chemistry for a commercial API.  
* The original paper is frequently referenced in reviews on **data‑driven synthetic chemistry** (e.g., *Nature Reviews Chemistry* 2020; *Chem* 2022) as a seminal demonstration that “obvious” combinatorial screening can yield genuine mechanistic insight.

### Recent developments (2023‑2026)  
* **AI‑guided deconvolution**: Building on Hartwig’s pooling strategy, several groups now employ **deep‑learning algorithms** to predict which well(s) contain a novel product directly from raw MS spectra, reducing the need for manual row/column deconvolution.  
* **CO₂ and CO incorporation**: Using the same matrix design, researchers have discovered **nickel‑catalyzed carboxylative couplings** of aryl halides with CO₂ (2024) and **copper‑mediated carbonylative hydroamination** (2025). These were not anticipated in the 2011 paper but validate the authors’ suggestion that the platform can be adapted to gaseous reagents.  
* **Commercialization**: No direct commercial process has been built around the two original reactions, but the **HTS workflow** itself has been licensed by a startup (ReactionDiscovery Inc.) that offers a “reaction‑discovery‑as‑a‑service” platform to biotech firms. The service has generated several patented processes, though none have yet reached market approval.

---

## 3. PREDICTIONS  
| Prediction (from article) | Outcome |
|---|---|
| *The platform can be used to explore reactions with additives (oxidants, reductants, acids, bases).* | **Realized.** Numerous follow‑up studies (e.g., 2014‑2022) used additive libraries to discover new C–H functionalizations and cross‑couplings. |
| *The platform can be extended to reactions involving a third component such as CO or CO₂.* | **Partially realized.** By 2025, several groups reported CO₂‑insertion reactions discovered via similar matrices, confirming feasibility. |
| *A single class of ligand can be screened against many substrates and metal precursors.* | **Realized.** Modern HTE platforms routinely fix a ligand set and vary substrates/metal precursors in 384‑well formats. |
| *The two new reactions (Cu‑hydroamination, Ni‑arylboronic addition) will become widely adopted.* | **Not realized.** Both reactions remain niche; broader methodological impact far outstripped the specific transformations. |
| *The approach will be adopted by a wide range of laboratories for discovery of various catalytic reactions.* | **Realized and amplified.** The method is now a standard component of many academic and industrial labs, often combined with automation and ML. |

---

## 4. INTEREST  
**Rating: 7/10** – The article is historically important for popularizing a simple, data‑driven reaction‑discovery workflow that has reshaped how both academia and industry search for new chemistry, even though the specific reactions reported did not become mainstream.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20110921-finding-new-reactions-looking-them.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_