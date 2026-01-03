
https://www.science.org/content/blog-post/not-even-wrong
# Not Even Wrong (March 2015)

## 1. SUMMARY
This article critiques computational chemistry's ability to accurately model the mechanism of the Morita-Bayliss-Hillman (MBH) reaction. The author discusses a JACS paper by Singleton and Plata at Texas A&M that examined 11 prior computational studies of this reaction. These computational approaches failed to meaningfully predict the actual mechanism—predictions for the proton-shuttle process varied by 35 orders of magnitude, effectively making them "not even wrong" (per Pauli's famous phrase). The real mechanism involved proton transfer to solvent molecules, but computational methods had consistently favored proton-shuttle mechanisms simply because those were computationally tractable. The piece notes that solvation effects and polar interactions remain significant challenges for computational chemistry, which has implications for related fields like molecular docking.

## 2. HISTORY
In the years following this article, the "reproducibility crisis" in computational chemistry and drug discovery gained broader recognition. A 2016 review highlighted that inadequate treatment of conformational sampling and solvent effects remained major sources of error. Research into more reliable solvent models advanced, including improvements in continuum solvent models and explicit solvent simulations. Several pharmaceutical companies publicly discussed challenges with binding affinity predictions and the need for better validation of computational methods. Academic groups published retrospective studies showing that computational predictions for reaction mechanisms still required careful experimental validation.

Does the MBH reaction itself have translational significance? While important among synthetic chemists for C−C bond formation under mild conditions, MBH chemistry has not become a major route in pharmaceutical manufacturing or drug discovery; rather, it remains primarily an academic tool. No notable FDA-approved drugs using MBH chemistry are prominent. Generally, method development continued an upward trend, but adoption hinges on robustness and predictability, which remains imperfect.

## 3. PREDICTIONS

- **Article's implicit prediction**: That computational studies of complex multimolecular polar reactions in solution require extreme care and their predictions shouldn't be trusted without validation.
  - That prediction largely holds today: It is widely accepted in both academia and industry that computational results require experimental validation for complex, multi-step, polar reactions in solution.


## 4. INTEREST
Rating: **7/10**
This article ranks in the 70th percentile of interest due to its clear exposition of hard limitations in predictive computational chemistry at the time and its broader resonance with reproducibility and transparency issues in computational modeling.

## 5. NOTES
- The author is Derek Lowe, whose "In the Pipeline" blog is known for frank commentary on pharmaceutical and computational chemistry.
- No specific companies are discussed; the focus is on the academic literature and the methodology's limitations.
- The MBH reaction remains a niche tool in synthetic organic chemistry, not a mainstay in pharmaceutical manufacturing.
- While no direct policy changes are cited, principles of careful interpretation of computational modeling and independent validation have become more commonplace in peer review and research guidance (for example, in journals).


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20150306-not-even-wrong.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_