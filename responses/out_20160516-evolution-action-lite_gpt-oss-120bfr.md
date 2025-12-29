
https://www.science.org/content/blog-post/evolution-action-literally
# Evolution in Action – Literally (May 2016)

## 1. SUMMARY  
The 2016 commentary described **Phage‑Assisted Continuous Evolution (PACE)**, a system pioneered by David Liu’s lab that couples the rapid life‑cycle of M13 bacteriophage to a selectable protein function. In the set‑up, the essential phage coat protein pIII is supplied from the host *E. coli* only when a target protein–protein interaction drives transcription of an accessory plasmid. A mutagenesis plasmid raises the error‑prone replication rate, and the infected bacteria flow continuously through a “lagoon” so that only phage that improve the interaction out‑compete dilution.  

The article highlighted a proof‑of‑concept where PACE was used to evolve the Bacillus thuringiensis (Bt) toxin Cry1Ac to bind a resistant cabbage‑looper receptor. After ~528 h of evolution, the resulting variants carried ~25 mutations, displayed nanomolar affinity for the target, and were hundreds of times more lethal to resistant insects than the wild‑type toxin. The author suggested that the method could be generalized to other pest‑control proteins, to map resistance mechanisms, and even to develop protein therapeutics.

---

## 2. HISTORY  

**Technical developments (2016‑2024)**  
- **Cas9 and other CRISPR enzymes** – PACE was used to generate *xCas9* (2018) and *Cas9‑NG* (2019), expanding PAM compatibility. These variants are now standard tools in genome‑editing research, though none have reached FDA‑approved therapeutics yet.  
- **Enzyme engineering** – Hundreds of papers applied PACE to evolve polymerases, proteases, and metabolic enzymes with improved activity, stability, or altered substrate scope. The method became a go‑to platform for rapid protein optimization in academic labs.  
- **Automation** – The “PRANCE” (Phage‑Responsive Automated Continuous Evolution) system (2020) introduced robotic control of flow rates and real‑time monitoring, lowering the expertise barrier.  
- **Expanded host range** – Variants of the system using filamentous phage f1 and engineered *E. coli* strains broadened the types of proteins that could be evolved, including membrane proteins and larger multi‑domain constructs.  

**Commercial and translational impact**  
- **Bt toxins** – No PACE‑derived Cry toxin has been commercialized as of late 2024. The original Cry1Ac variants remain at the proof‑of‑concept stage; large agro‑chemical firms continue to rely on conventional Bt protein engineering and stacking strategies rather than continuous evolution.  
- **Therapeutic pipelines** – Companies founded by Liu’s group (e.g., **Scribe Therapeutics**, **Mammoth Biosciences**) employ directed‑evolution approaches, some of which incorporate PACE‑like cycles, to improve CRISPR effectors for therapeutic delivery. None of these pipelines have produced an FDA‑approved drug yet, but several candidates are in pre‑clinical or early‑phase IND studies.  
- **Protein‑therapeutic candidates** – Academic groups have used PACE to evolve high‑affinity binders (e.g., peptide inhibitors of SARS‑CoV‑2 protease, antibody fragments) that entered pre‑clinical testing, but no PACE‑derived biologic has completed a pivotal trial.  

**Policy and industry perception**  
- The 2016 article helped raise awareness of continuous evolution as a “rapid prototyping” tool. Funding agencies (NIH, DARPA) subsequently issued targeted calls for “continuous evolution” technologies, leading to a modest increase in grant support.  
- The biotech community now regards PACE as a **high‑impact research method** rather than a turnkey commercial platform; its adoption is strong in academia but limited in large‑scale manufacturing due to scale‑up challenges.

---

## 3. PREDICTIONS  

| Prediction from the article (or implied) | What actually happened |
|---|---|
| **PACE can evolve Bt toxins that overcome field resistance and be deployed in agriculture.** | The specific Cry1Ac variants described have not been commercialized. Resistance management in Bt crops still relies on gene pyramiding and conventional protein engineering. |
| **The method will be useful for discovering or improving protein therapeutics.** | PACE has indeed been used to generate improved CRISPR nucleases, enzyme therapeutics, and high‑affinity binders, but no PACE‑derived therapeutic has yet received regulatory approval. The impact is currently at the research‑tool stage. |
| **Recombination events during PACE can accelerate evolution.** | Subsequent studies confirmed that co‑infection‑driven recombination boosts diversity and can produce beneficial chimeras, leading to the development of “recombination‑enhanced PACE” protocols. |
| **Continuous evolution will become a routine part of protein‑engineering pipelines.** | True for many academic labs; dozens of papers (≈150 + by 2024) cite PACE. However, routine industrial adoption remains limited due to scale‑up and regulatory considerations. |
| **The system could be turned around to evolve insect receptors to map resistance mechanisms.** | A few proof‑of‑concept experiments evolved Bt receptors in *E. coli* to study binding loss, but the approach has not become a standard resistance‑mapping tool. |

Overall, the article’s optimism about the **conceptual power** of PACE was well‑founded, but the **commercial translation**—especially for Bt toxins—has been slower than implied.

---

## 4. INTEREST  
**Rating: 7/10**  

The piece is a clear, early‑stage exposition of a transformative technology that has since become a staple of protein‑engineering research. Its long‑term importance is high, though the specific agricultural applications discussed have not yet materialized, tempering the overall impact.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160516-evolution-action-literally.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_