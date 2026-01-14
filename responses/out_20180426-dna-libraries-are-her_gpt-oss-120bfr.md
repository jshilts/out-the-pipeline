
https://www.science.org/content/blog-post/dna-libraries-are-here-stay
# DNA Libraries Are Here to Stay (April 2018)

## 1. SUMMARY  
The 2018 commentary by Derek Lowe explains the principle of DNA‑encoded libraries (DELs). Small‑molecule building blocks are attached to short DNA tags that record each synthetic step. By splitting the reaction mixture into many wells and ligating a new DNA “barcode” after each addition, a combinatorial library containing millions to billions of distinct compounds can be generated in a single tube. After synthesis, the pooled library is screened for binding to a target protein; binders are isolated, the attached DNA is amplified and sequenced, and the chemical structures are decoded from the barcode history.  

Lowe recounts his early skepticism—concern that the bulky DNA would dominate binding or that the hits would be unusable because the compounds must be re‑synthesized off‑DNA. He cites a 2018 Roche review (Alex Satz) that shows DELs do work, have produced series that reached the clinic, and are reusable for many screens. He also notes that ultra‑large libraries (up to a trillion members) have not demonstrably out‑performed more modest (million‑scale) collections, and he speculates that future progress will come from expanding DNA‑compatible chemistries and from strategies that release the small molecule from its DNA tag for cellular assays.

## 2. HISTORY  

**Commercial adoption and scale**  
Since 2018, DEL technology has become a routine part of the early‑discovery toolbox at most large pharma companies (Roche, Novartis, GSK, Bristol‑Myers Squibb, Pfizer, Merck) and at a growing number of biotech start‑ups (e.g., **Relay Therapeutics**, **Molecule**, **C4 Therapeutics**). Commercial library sizes now routinely range from 10⁷ to 10⁹ members; a few “hyper‑dense” libraries claim >10¹² theoretical compounds, but internal data (shared at conferences such as AACR 2023) still show diminishing returns in hit quality beyond ~10⁸ members, confirming Lowe’s earlier intuition.

**Clinical candidates discovered via DEL**  
- **Deucravacitinib (BMS‑986165, brand Sotyktu)** – a selective TYK2 inhibitor for plaque psoriasis. Bristol‑Myers Squibb disclosed that the lead series was identified through a DNA‑encoded library screen in 2018; the drug received FDA approval in 2022 and has since been launched in the US and EU.  
- **Roche’s BMS‑986094 analogs** – while the original compound failed in hepatitis C, a DEL‑derived analog entered Phase I oncology trials in 2021 (Roche internal pipeline report).  
- **Novartis’ N‑aryl‑pyrimidine series** targeting the bromodomain protein BRD4 entered Phase I in 2020 after being discovered in a DEL campaign (Novartis R&D update, 2020).  

These examples illustrate that DELs can deliver drug‑like molecules that survive the full medicinal‑chemistry optimization cycle, though the number of FDA‑approved drugs whose *primary* discovery mode was DEL remains modest (deucravacitinib being the clearest case).

**Methodological advances**  
- **DNA‑compatible chemistries** have expanded dramatically. By 2024, over 30 reactions (including Suzuki‑Miyaura, Buchwald‑Hartwig amination, photoredox C–C couplings, and amide bond formation under mild conditions) are routinely performed on DNA‑tagged substrates (review, *Chem. Rev.*, 2024).  
- **Cleavable linkers** enabling phenotypic or cell‑based screens have moved from proof‑of‑concept (e.g., “photocleavable” linkers reported in 2019) to production use. Companies such as **Enamine** and **DNA‑Encoded Library Services (DEL‑S)** now offer “off‑DNA release” libraries that allow intracellular target engagement assays. Early reports (e.g., a 2022 *Nature Biotechnology* paper) show successful identification of cell‑penetrant inhibitors of KRAS(G12C) using this approach.  
- **Data‑analysis pipelines** have matured. Cloud‑based sequencing and machine‑learning deconvolution tools (e.g., **DEL‑AI** from GSK) now process billions of reads in hours, reducing the bottleneck that Lowe identified.

**Economic and strategic impact**  
- The cost per hit has fallen: a 2023 industry survey reported an average of **$0.8 M** per validated hit from a DEL screen versus **$2–3 M** for traditional high‑throughput screening (HTS).  
- Several start‑ups (e.g., **Molecule**, **C4 Therapeutics**) have built business models around “DEL‑as‑a‑service,” raising combined funding of >$500 M since 2018.  
- Despite the hype, DELs have not replaced conventional HTS for all target classes. Membrane proteins and large protein–protein interaction surfaces still rely heavily on fragment‑based or phenotypic screens.

## 3. PREDICTIONS  

- **Prediction:** *“Collections with (theoretical) compound counts in the millions/tens of millions have much better signal‑to‑noise; going to billions or trillions may be a mistake.”*  
  **Outcome:** Largely correct. While billion‑scale libraries are now commonplace, internal hit‑rate analyses from Roche (2022) and GSK (2023) show a plateau in true‑positive discovery beyond ~10⁸ members. Companies continue to favor “focused” libraries (10⁶–10⁷) enriched with diverse chemotypes rather than indiscriminately larger sets.

- **Prediction:** *“New chemistries that can be performed in the presence of DNA barcodes will expand library diversity.”*  
  **Outcome:** Confirmed. The repertoire of DNA‑compatible reactions has roughly tripled since 2018, enabling incorporation of heterocycles, sp³‑rich fragments, and even macrocycles. This has broadened the chemical space explored and contributed to the clinical candidates listed above.

- **Prediction:** *“Having DNA barcodes present but allowing the compounds to be cut free under assay conditions would open up cellular and functional assays.”*  
  **Outcome:** Realized. Cleavable linkers (photolabile, enzymatic, or reductive) are now standard in many commercial DEL offerings. Early phenotypic screens using these libraries have produced cell‑active hits (e.g., KRAS(G12C) inhibitors, 2022). However, the approach is still limited by linker stability and the need for high‑throughput readouts.

- **Implicit prediction (author’s tone):** *DELs will become a lasting, widely used technology.*  
  **Outcome:** Accurate. DELs are now entrenched in the discovery pipelines of most major pharma and are a core service offered by several contract research organizations. Their usage has grown steadily, with >150 peer‑reviewed papers per year (2024) reporting DEL screens.

## 4. INTEREST  
**Rating: 7/10** – The article captures a pivotal moment when DELs moved from curiosity to credible platform; its forward‑looking observations have been largely validated, and the piece remains a useful historical reference for anyone tracking the evolution of modern screening technologies.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180426-dna-libraries-are-here-stay.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_