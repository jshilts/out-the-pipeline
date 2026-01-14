
https://www.science.org/content/blog-post/has-ai-discovered-drug-now-guess
# Has AI Discovered a Drug Now? Guess. (Sep 2019)

## 1. SUMMARY  
The commentary discusses a 2019 Nature Biotechnology paper by Insilico Medicine that introduced **GENTRL** – a generative‑tensor‑reinforcement‑learning pipeline for de‑novo small‑molecule design. The authors trained the system on public DDR1 kinase data, broad kinase inhibitor sets, and ~17 k patented scaffolds, then asked it to propose novel, patent‑free chemotypes predicted to be potent, selective DDR1 inhibitors. After filtering ~30 k generated structures down to 40 diverse candidates, six were synthesized and tested; two showed sub‑20 nM DDR1 activity, two were in the 100‑nM range, and two were inactive. The paper highlighted the speed (“< 2 months”) and lower apparent cost versus a conventional hit‑identification campaign, while the commentary cautioned that the work was a proof‑of‑concept on a well‑studied kinase target and that the “drug” label was premature.

## 2. HISTORY  
**What happened to the DDR1 project?**  
- No follow‑up publications from Insilico Medicine reported further optimization of the six GENTRL hits, and none entered pre‑clinical IND‑enabling studies. As of early 2026 there is no DDR1 inhibitor from this effort in clinical trials or on the market.  
- DDR1 remains a biologically interesting target (fibrosis, cancer), but the field has not produced an approved therapeutic from any source since the 2010s.

**Broader impact on AI‑driven drug design**  
- The GENTRL paper is widely cited (≈ 300 citations by 2024) as an early demonstration that generative models can produce synthetically tractable, biologically active molecules.  
- Insilico Medicine leveraged the publicity to raise capital (Series C in 2020, Series D in 2022) and to form partnerships with pharma (e.g., a 2021 deal with **Bayer** on AI‑generated anti‑fibrotic candidates). Those collaborations have produced several pre‑clinical programs, but none have yet reached the clinic.  
- The first **AI‑designed small molecule to enter human trials** was **DSP‑1181**, a 5‑HT1A agonist discovered by **Exscientia** in partnership with Sumitomo Dainippon Pharma. Phase I began in 2020 and the trial completed without safety concerns, but the program was later discontinued for strategic reasons; no AI‑designed drug has been approved as of Jan 2026.  
- Other companies (e.g., **Atomwise**, **BenevolentAI**, **Cyclica**) have reported AI‑generated hits entering IND‑enabling work, and several AI‑assisted programs have progressed to Phase I/II (e.g., BenevolentAI’s **BNT‑101** for ALS entered Phase II in 2023). These advances are largely incremental: AI shortens the *hit‑identification* window (weeks vs. months) but the downstream optimization, toxicology, and clinical phases still dominate cost and timeline.  
- Academic groups have built on GENTRL, releasing open‑source generative frameworks (e.g., **REINVENT**, **MolGAN**) that are now standard tools in many medicinal‑chemistry labs. The community has also learned that rigorous prospective validation (blind synthesis, unbiased benchmarking) is essential; several high‑profile “AI‑generated hit” claims have been re‑evaluated and found to be comparable to conventional virtual‑screening performance.  

**Policy and industry shifts**  
- No regulatory guidance specific to AI‑generated molecules has been issued; the FDA continues to evaluate them under existing drug‑development frameworks.  
- Venture capital investment in AI‑driven drug discovery peaked in 2021 (≈ $4 bn) and has modestly contracted since, reflecting the reality that AI accelerates early discovery but does not yet solve later‑stage attrition.  

## 3. PREDICTIONS  
The commentary (and the original paper) implied several future outcomes. Below is a bullet‑point assessment of each, based on what actually transpired up to early 2026.

- **“Design, synthesize, and experimentally validate molecules targeting DDR1 in < 2 months for a fraction of traditional cost.”**  
  - *Outcome*: The initial hit‑generation indeed occurred within weeks, and the synthesis of six compounds was completed in ~2 months. However, the overall cost reduction was marginal when the full lead‑optimization pipeline is considered. No DDR1 drug emerged, so the long‑term cost advantage was not realized.  

- **“AI can discover a drug.”**  
  - *Outcome*: No AI‑generated molecule has yet been approved. The first AI‑designed compound to reach humans (DSP‑1181) was a *candidate*, not a marketed drug. The claim remains aspirational.  

- **“Generative models will replace traditional virtual screening.”**  
  - *Outcome*: Generative approaches are now complementary to conventional docking/ML scoring. They are used to explore novel chemical space, but most projects still employ a hybrid workflow (generative design → docking → synthesis). Replacement has not occurred.  

- **“Rapid, low‑cost AI pipelines will transform pharma business models.”**  
  - *Outcome*: Pharma has incorporated AI tools into early‑discovery units, but the core business model (large, multi‑year, multi‑billion‑dollar development cycles) remains unchanged. The transformation is incremental rather than revolutionary.  

- **“The DDR1 target will become a hot therapeutic area thanks to AI‑generated scaffolds.”**  
  - *Outcome*: DDR1 continues to be explored by traditional medicinal chemistry, but AI‑generated scaffolds have not driven new clinical programs. The target’s commercial pipeline is still limited.  

## 4. INTEREST  
**Rating: 7/10**  
The article is a clear, well‑argued early‑stage case study that sparked realistic debate about AI’s role in drug discovery. It is historically significant (first high‑profile generative‑AI hit report) but its immediate scientific impact was modest, and the promised “drug” never materialized. The discussion remains valuable for understanding hype vs. progress in the field.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20190904-has-ai-discovered-drug-now-guess.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_