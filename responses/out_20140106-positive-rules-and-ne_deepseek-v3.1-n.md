
https://www.science.org/content/blog-post/positive-rules-and-negative-ones
# Positive Rules and Negative Ones (January 2014)

## 1. SUMMARY

The article discusses the practical reality of medicinal chemistry guidelines, distinguishing between "negative rules" (what to avoid) and "positive rules" (what to try). The author observes that negative rules—such as Lipinski's Rule of Five and other structural alerts—are "moderately reliable" at predicting failure and should generally be heeded. In contrast, positive rules, which suggest specific structural modifications to address problems like hERG liability, poor BBB penetration, or metabolic stability, have "very very low" positive predictive power but must still be attempted routinely before moving to more exotic solutions.

The piece acknowledges numerous exceptions to these guidelines, citing examples like fosfomycin, nitroglycerin, and suramin as "ugly" drug structures that nevertheless work. The inherent uncertainty—negative rules aren't absolute, and positive rules often fail—creates persistent debate among medicinal chemists, where individual experiences with the same strategy can yield opposite outcomes. Ultimately, the article concludes that current guidelines primarily serve to narrow options "from an impossible number to a highly improbable number," and until better predictive tools emerge, medicinal chemistry will remain largely empirical.

## 2. HISTORY

Since 2014, the tension between empirical medicinal chemistry rules and data-driven approaches has evolved significantly, though the fundamental challenges remain recognizable:

- **Computational and AI-driven drug discovery growth**: The period saw major expansion of machine learning in medicinal chemistry, with companies like Atomwise, Exscientia, BenevolentAI, Recursion Pharmaceuticals, and Insilico Medicine developing AI platforms for target identification, hit-to-lead optimization, and de novo design. While these tools increasingly incorporate both positive and negative design signals, they still struggle with the "ugly drug" exceptions and low positive predictive value noted in 2014.
- **Approved drugs defying traditional rules**: The trend of "beyond Rule of Five" (bRo5) drugs accelerated, with approved therapeutics increasingly violating multiple Lipinski rules. Notable examples include anticancer agents (e.g., venetoclax), antivirals (e.g., glecaprevir/pibrentasvir), and cyclic peptides. Systematic analyses (e.g., Doak et al., 2014; DeGoey et al., 2018) quantified that ~10–20% of oral drugs now lie in bRo5 space, validating that "ugly" structures can indeed succeed.
- **Continued relevance and refinement of rules**: Guidelines like the Rule of Five still influence early-stage design, but have been supplemented by more nuanced frameworks (e.g., CNS MPO for brain penetration, ligand efficiency metrics, and QED for drug-likeness). However, these remain probabilistic, not deterministic—consistent with the 2014 observation that rules narrow options rather than guaranteeing success.
- **Clinical attrition persists**: Despite computational advances, drug discovery attrition rates remain high (often >90% from Phase I to approval), with poor pharmacokinetics, toxicity, and lack of efficacy still major drivers. This underscores that positive design rules have not dramatically improved success probabilities, though AI-guided programs increasingly enter clinical trials (e.g., Exscientia's DSP-1181, Insilico Medicine's USP1 inhibitor).
- **Structural diversification of drug targets**: The rise of protein-protein interaction (PPI) inhibitors, molecular glues, targeted protein degraders (PROTACs), and covalent inhibitors further challenged classical rules, as these modalities often require larger, more lipophilic, or "non-traditional" structures to engage challenging targets.
- **Business and policy developments**: AI-native biotechs attracted substantial investment (e.g., Exscientia's IPO in 2021, Recursion's IPO in 2021), and regulatory agencies began engaging with AI/ML in drug development (FDA's 2021 discussion paper on AI/ML submissions). Public initiatives like the Accelerating Medicines Partnership (AMP) aimed to systematize target validation, though concrete policy mandates remained limited.

The article's core insight—that negative rules are more reliable than positive ones, and that medicinal chemistry remains a balance of probabilities—has largely held true, even as computational tools have scaled.

## 3. PREDICTIONS

The article did not make explicit timeline-based predictions, but embedded several implicit expectations about how medicinal chemistry might evolve:

- **"When (or if) we can do better, medicinal chemistry will change a great deal"**  
  ✓ This has partly materialized: Machine learning and AI have become deeply integrated into drug design workflows (e.g., generative models for molecules, scoring functions, and ADMET prediction). However, the change has been more incremental than transformative—medicinal chemistry still relies heavily on empirical screening, rules of thumb, and iterative optimization. No paradigm shift has eliminated the need for large experimental datasets or rendered human medicinal chemists obsolete.

- **Implication that positive rules will remain weakly predictive**  
  ✓ This has largely held: While computational tools now suggest structures with higher predicted success rates, real-world validation remains challenging. Clinical translation of AI-designed molecules is still early-stage, and positive predictive power remains low for many optimization strategies (e.g., changing a single substituent to improve potency or selectivity).

- **Implication that negative rules will persist but accumulate exceptions**  
  ✓ This is accurate: Lipinski-style guidelines remain widely taught and referenced, but the pharmaceutical industry increasingly accepts bRo5 chemical space, particularly for difficult targets. The "ugly drugs" cited (fosfomycin, nitroglycerin, suramin) were precursors to a much larger set of approved non-compliant therapeutics.

- **Implication that debate and anecdotal evidence will continue**  
  ✓ Confirmed: Medicinal chemistry discourse still features competing experiences with specific strategies, and many design decisions rely on institutional knowledge, structural precedents, and case-by-case judgment rather than universal laws.

## 4. INTEREST

Rating: **7/10**  

The article captures a durable, practitioner-level truth in medicinal chemistry—the asymmetry between negative and positive design rules—and remains broadly relevant to today's drug discovery landscape. Its insights anticipate the continued relevance of empirical guidelines even amid computational advances, and the proliferation of "beyond Rule of Five" drugs validates its caution about over-relying on exclusionary rules. The core tension remains central to AI-driven drug design, where models still grapple with low positive predictive value and exceptions to learned patterns.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20140106-positive-rules-and-negative-ones.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_