
https://www.science.org/content/blog-post/theology-ligand-efficiency
# The Theology of Ligand Efficiency (January 2013)

## 1. SUMMARY

The article discusses ligand efficiency—a metric used in drug discovery to assess a compound's binding potency relative to its size. The author describes a debate over how to calculate this metric: one approach divides potency by molecular weight, while another divides by the number of heavy (non-hydrogen) atoms. The author's concern centers on halogen atoms, especially bromine and iodine; because they are heavy, a molecular-weight–based efficiency metric "punishes" them more severely than a heavy-atom–count approach. The author argues that this penalty is justified because large halogens may worsen a drug's pharmacokinetics (PK), stability, and toxicity risk. The piece concludes that, while an iodo or bromo compound should not be ruled out automatically, those atoms must "earn their keep" through measurable benefits (e.g., halogen bonding), and any such candidate should advance quickly into studies that assess real-world liabilities like PK and tox.

## 2. HISTORY

Subsequent to the article's publication, ligand efficiency metrics—especially LE (binding energy per heavy atom), LLE (LipE), LLEAT, and others—became standard tools in medicinal chemistry and fragment-based drug discovery (FBDD). Integrated cheminformatics platforms and corporate workflows now routinely compute and report these metrics to guide lead optimization. Heavy halogen incorporation, particularly for bromine and iodine, remained a niche strategy, typically reserved for cases where halogen bonding provides a clear, measured gain in potency or selectivity.

**No FDA-approved drugs relying prominently on iodine were approved in the decade following the article.** However, halogenated compounds more broadly, including many with chlorine and some with bromine, continued to reach approval. For example:
- Selinexor (Xpovio) and Venetoclax (Venclexta) both include chlorine atoms, but not iodine.
- Tecovirimat (TPOXX), an orthopoxvirus treatment, includes chlorine and fluorine but no iodine.
- The trends in drug approvals over 2013–2023 show an increase in sp$^3$-rich, smaller scaffolds, and fluorine-substitution is routine, whereas heavy-halogen use has remained limited to niche applications.

The iodine stability concerns mentioned by the author proved prescient; **no major drug classes emerged based on primary iodo substituents.** In contrast, heavy-halogen tactics are sometimes used in chemical biology and as transient tools (e.g., radiolabeling precursors in positron emission tomography, or structural probes in crystallography). Policy did not change directly as a result of this debate; instead, industry practice evolved toward multi-parameter optimization, weighing ligand efficiency alongside LipE/LLE, permeability, and off-target screens. Organizations like the European Lead Factory and academic FBDD centers have embedded heavy-atom–based LE thresholds (e.g., Target Fatty Acid Binding Protein, EFABP) while also incorporating LLE to control lipophilicity—which addresses the author's underlying concern about large, lipophilic halogens.

## 3. PREDICTIONS

The article contained several explicit and implicit predictions:
- **Implicit: Iodine substituents are unlikely to yield successful drugs unless they earn their keep through halogen bonding, and they must be scrutinized early for PK, stability, and tox.**  
  - **Outcome: Confirmed.** No blockbuster drugs centered on iodine emerged; heavy-halogen strategies remained niche, with iodine mostly used in specialist applications (e.g., imaging agents like $^{123/131}$I-based radiopharmaceuticals).
- **Implicit: Ligand efficiency metrics will continue to influence decision-making in drug discovery.**  
  - **Outcome: Confirmed.** LE, LLE, and LLEAT became standard guiding metrics, built into commercial and open-source cheminformatics tools and used in hit-to-lead and lead optimization.
- **Explicit: Bromine and iodine should be treated cautiously because of molecular-weight penalties and real-world liabilities (PK/tox).**  
  - **Outcome: Confirmed.** Heavy-halogen compounds remain the exception rather than the rule; lead-optimization campaigns that introduced iodine or bromine typically retained them only where halogen bonding delivered sufficient binding energy to offset the efficiency penalty and where PK/tox liabilities were manageable.

## 4. INTEREST

Rating: **7/10**  

This article captures a specific, technical debate in medicinal chemistry that proved broadly influential across the biopharma industry. While focused on a narrow topic, it correctly anticipated subsequent practice where heavy-halogen tactics remained uncommon and efficiency metrics became standard, making it a historically meaningful commentary on chemists' day-to-day design choices.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20130122-theology-ligand-efficiency.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_