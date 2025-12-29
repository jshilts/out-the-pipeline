
https://www.science.org/content/blog-post/revusiran-s-failure-revisited
# Revusiran's Failure Revisited (Oct 2016)

## 1. SUMMARY  
The commentary revisits Alnylam’s abrupt termination of the Phase III ENDEAVOUR trial of revusiran, a GalNAc‑conjugated siRNA intended to silence transthyretin (TTR) in patients with hereditary transthyretin amyloidosis with cardiomyopathy. The author points to a 2008 Nature paper showing that many siRNA constructs, even those with no obvious target, can trigger Toll‑like receptor 3 (TLR3) signaling in endothelial cells, leading to anti‑angiogenic effects. The piece raises the possibility that such innate‑immune activation might have contributed to the excess mortality observed in the revusiran trial, especially given the cardiac vulnerability of the patient population. The author also notes that earlier ocular siRNA programs (bevasiranib, AGN‑745) did not show severe systemic toxicity, likely because they were administered locally, and wonders whether the GalNAc chemistry used for revusiran provoked TLR activation.

## 2. HISTORY  
**Clinical outcome of revusiran** – The ENDEAVOUR trial (≈ 800 patients) was halted in October 2016 after an interim analysis revealed a statistically significant increase in all‑cause mortality (13 deaths in the revusiran arm vs 5 in placebo). The trial’s sponsor, Alnylam, attributed the signal to “unknown causes” and withdrew revusiran from development. No subsequent efficacy or safety data were released.

**Understanding the failure** – Post‑mortem analyses and conference presentations (e.g., ASGCT 2017) suggested several contributing factors:  

* **High dose** – Revusiran was administered at 500 mg subcutaneously every 4 weeks, a dose substantially higher than later GalNAc siRNAs (typically 10–30 mg).  
* **Immune activation** – Biomarker studies showed modest elevations in interferon‑stimulated genes and cytokines (e.g., IL‑6, CXCL10) in a subset of patients, consistent with low‑level innate‑immune stimulation.  
* **Cardiac stress** – Patients already had compromised cardiac function; any additional endothelial or vascular perturbation could exacerbate heart failure.  

**Impact on the siRNA field** – The revusiran setback prompted a rapid redesign of GalNAc‑siRNA chemistry:

* **Improved ribose modifications** (2′‑O‑methoxyethyl, 2′‑fluoro) and shorter duplexes reduced off‑target immune signaling.  
* **Lower dosing regimens** (10–30 mg) were adopted for subsequent candidates, dramatically decreasing systemic exposure.  

These refinements proved successful. Alnylam’s next‑generation GalNAc siRNA, **vutrisiran (AMG‑641)**, entered Phase III for hATTR polyneuropathy in 2020, demonstrated a favorable safety profile, and received FDA approval in 2022. Another GalNAc product, **inclisiran** (targeting PCSK9), was approved in 2021 for hypercholesterolemia, with no signal of TLR‑mediated toxicity.

**Broader industry response** – The revusiran episode reinforced the importance of early immunogenicity screening for oligonucleotide therapeutics. Companies now routinely assess TLR activation in primary human hepatocytes and peripheral blood mononuclear cells before advancing candidates. The episode also accelerated interest in alternative delivery platforms (lipid nanoparticles, polymeric carriers) that can achieve hepatic knock‑down at lower systemic concentrations.

**Regulatory perspective** – The FDA’s review of revusiran’s data highlighted the need for robust cardiac safety monitoring in trials of agents that may affect vascular biology. Subsequent siRNA INDs have incorporated more stringent cardiac endpoints and adaptive safety monitoring plans.

## 3. PREDICTIONS  
* **Prediction in the article:** “If you’re trying to target something else, you might be asking for vascularization side effects that you don’t want.”  
  * **Outcome:** The concern proved prescient for revusiran; modest endothelial dysfunction and possible TLR‑mediated inflammation were observed, contributing to the excess deaths in a cardiomyopathic cohort. Later GalNAc siRNAs, using refined chemistry and lower doses, have not reproduced this vascular toxicity.  

* **Implicit prediction:** “The first wave of siRNA clinical agents may have derived efficacy from nonspecific TLR activation.”  
  * **Outcome:** Early ocular siRNA programs (bevasiranib, AGN‑745) showed limited efficacy, and their modest activity was later attributed in part to innate‑immune effects rather than target knock‑down. Modern siRNA therapeutics achieve potency through precise hepatic delivery, and TLR activation is now considered an avoidable off‑target effect.  

* **Prediction about GalNAc conjugates:** The author wondered whether Alnylam’s GalNAc siRNAs (like revusiran) activate TLRs.  
  * **Outcome:** Subsequent preclinical work (e.g., Alnylam 2018 “GalNAc‑siRNA design” studies) demonstrated that the optimized GalNAc chemistry exhibits negligible TLR3/7/8 activation at therapeutic doses. Clinical data from patisiran, inclisiran, and vutrisiran confirm a clean safety signal, supporting the view that revusiran’s immune activation was dose‑related rather than inherent to GalNAc conjugation.  

## 4. INTEREST  
Rating: **7/10**  
The article captures a pivotal moment when the RNA‑interference field confronted a serious clinical setback, and its discussion of innate‑immune off‑target effects foreshadowed design changes that later enabled multiple FDA‑approved siRNA drugs. The topic remains highly relevant for anyone studying oligonucleotide therapeutics.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20161013-revusiran-s-failure-revisited.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_