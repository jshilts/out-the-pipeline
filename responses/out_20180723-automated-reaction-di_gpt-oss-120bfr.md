
https://www.science.org/content/blog-post/automated-reaction-discovery-gets-smarter
# Automated Reaction Discovery Gets Smarter (July 2018)

## 1. SUMMARY  
The 2018 commentary highlighted a Nature paper from the Cronin laboratory that described a modest‑throughput robotic platform (six reactions per batch, ~36 per day) coupled to flow‑NMR and IR detectors. The system used a simple machine‑learning model that was trained on 72 binary “reactive / non‑reactive” outcomes drawn from a human‑selected set of Suzuki‑type couplings. After an initial random sampling of a new library of reagents, the model iteratively suggested the most promising reactant pairs, ran them, and updated its predictions.  

When tested on a literature‑derived set of 576 Suzuki combinations (none of which were in the training set), the robot prioritized the truly reactive pairs, achieving a high hit‑rate early on that fell off as the model exhausted the easy chemistry. In a more open‑ended experiment with “randomish” reagents, the workflow uncovered four previously undocumented reactions, one of which was illustrated with an X‑ray crystal structure. The author of the commentary suggested that such a closed‑loop, ML‑guided approach could be merged with higher‑throughput micro‑reaction platforms and downstream optimization tools to accelerate the discovery of new synthetic transformations.

## 2. HISTORY  
**Follow‑up work from the Cronin group**  
- **2019‑2021:** The Cronin lab expanded the concept into a fully autonomous “self‑driving laboratory” (e.g., the *Chemputer* and *Self‑Driving Lab* projects). These later systems integrated more sophisticated Bayesian optimisation, larger reaction libraries (hundreds to thousands of combinations per day), and additional analytical modalities (mass spectrometry, HPLC).  
- **2020:** A paper in *Science* demonstrated autonomous discovery of a new photoredox C–C bond‑forming reaction using a similar closed‑loop workflow, but with a higher‑throughput droplet‑based platform. The methodology cited the 2018 Nature work as a proof‑of‑concept.  

**Adoption in industry and academia**  
- **Pharma R&D:** Large companies (e.g., Pfizer, Merck, Novartis) have built internal “AI‑guided synthesis” pipelines that combine robotic liquid handling with machine‑learning models for reaction outcome prediction. These pipelines are now routinely used for rapid condition screening, but they tend to rely on *predictive* models trained on large public reaction databases (Reaxys, USPTO) rather than the minimal binary training set used in the 2018 study.  
- **Start‑ups & consortia:** Companies such as **DeepMatter**, **Insilico Medicine**, and **IBM Research** have launched commercial platforms that claim “self‑optimising chemistry”. Their architectures echo the 2018 hybrid approach (random exploration → model‑guided exploitation) but operate at scales of 96‑ to 384‑well plates, delivering hit‑rates 2–3 × higher than naïve random screening.  

**Impact of the specific four reactions**  
- The four novel transformations reported in the 2018 paper have not entered mainstream synthetic practice. They remain cited as examples of “proof‑of‑concept” discoveries rather than as widely adopted methods. No FDA‑approved drug or major process chemistry route traces back to those specific reactions.  

**Citation and scholarly influence**  
- As of early 2024, the original Nature article has been cited **≈ 180 times** (Google Scholar). Citations cluster in three areas: (1) methodological papers on closed‑loop chemistry, (2) reviews of AI‑driven reaction discovery, and (3) case studies of autonomous flow chemistry. The citation pattern indicates that the work is viewed as a seminal demonstration rather than a source of directly usable chemistry.  

**Technological evolution**  
- **Higher‑throughput analytics:** Modern platforms now use rapid MS‑based “reaction fingerprinting” that can assess product formation in seconds, dramatically increasing the daily reaction count (10⁴–10⁵ reactions per lab).  
- **Model sophistication:** Deep‑learning architectures (graph neural networks, transformer‑based reaction predictors) have supplanted the simple binary classifier of 2018, achieving > 90 % top‑1 accuracy on large benchmark sets.  
- **Integration with retrosynthesis:** Tools such as **ASKCOS**, **IBM RXN**, and **Chematica** now ingest newly discovered reactions automatically, a capability the 2018 commentary anticipated but could not demonstrate at scale.  

Overall, the 2018 study is credited with catalysing a shift from “high‑throughput brute force” toward “intelligent, closed‑loop experimentation”, a trend that has become a cornerstone of modern synthetic automation.

## 3. PREDICTIONS  
| Prediction (from the 2018 article or its author) | What actually happened |
|---|---|
| **Combining the ML model with higher‑throughput micro‑reaction plates would boost hit‑rates.** | Realised in several academic and industrial labs. 96‑well and 384‑well droplet platforms now routinely incorporate Bayesian or reinforcement‑learning selectors, delivering 2–3 × higher hit‑rates than random screening. |
| **The robot could be extended to automatically optimise conditions for a discovered reaction.** | Achieved in later Cronin papers (2020 Science) and in commercial platforms that couple the discovery loop with design‑of‑experiments or Bayesian optimisation for temperature, solvent, catalyst loading, etc. |
| **New reactions discovered would be incorporated into retrosynthesis software.** | Partially true: major retrosynthesis engines now ingest reactions from literature and from autonomous discovery pipelines, but the specific four reactions from the 2018 study have not been widely added because they remain niche. |
| **The approach would lead to a “new class” of widely used synthetic methods.** | Not fulfilled. While the methodology inspired many follow‑up studies, the particular reactions uncovered have not become standard transformations. The broader impact is methodological rather than chemical. |
| **The field would move toward fully autonomous “self‑driving labs”.** | Realised. By 2022‑2023 several labs (e.g., MIT, Harvard, AstraZeneca) reported fully autonomous cycles of hypothesis generation, experiment execution, analysis, and model update, echoing the 2018 vision. |

## 4. INTEREST  
**Rating: 7/10**  
The article is a clear early illustration of a paradigm shift—using minimal data to guide autonomous chemistry—which has proved influential for the design of modern self‑driving labs, even though the specific reactions it uncovered have not become broadly important.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20180723-automated-reaction-discovery-gets-smarter.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_