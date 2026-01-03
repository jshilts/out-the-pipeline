
https://www.science.org/content/blog-post/knock-six-years-your-timeline-um
# Knock Six Years Off Your Timeline. Um. (October 2017)

## 1. SUMMARY

This article critiques a consulting presentation that claimed AI could reduce drug discovery timelines by shaving six years off the process through automatic screening. The author argues that this claim is misleading: the bottleneck isn't screening thousands of compounds (which he says can be done in six weeks, not six years), but rather the complex, iterative optimization steps that follow. He acknowledges that AI methods show "real promise" for target identification and drug repurposing, but highlights practical barriers like extreme computational intensity and the labor-intensive need to curate datasets from medical literature.

The article calls out specific companies including Atomwise, BenevolentAI, and twoXAR, suggesting they may be overstating capabilities. The author expresses cautious optimism about AI's long-term potential but pushes back against what he views as premature hype and PowerPoint-driven "revolution" narratives.

## 2. HISTORY

**Computational/AI methods in drug discovery gained significant traction from 2017 onward, but with nuanced outcomes:**

- **Target identification and repurposing** did prove more tractable than de novo design. Katalin Karikó–Drew Weissman's mRNA work, aided by computational approaches, led to COVID vaccines (Pfizer–BioNTech and Moderna), demonstrating speed and precision in designing and optimizing mRNA and lipid nanoparticles.
- **Fragment-based and free-energy perturbation (FEP) methods** matured into routine tools at many pharmas and CROs (e.g., Schrödinger's FEP+, OpenEye tools) for lead optimization, improving affinity predictions and reducing wet-lab cycles.
- **Large-scale virtual screening** became widespread, with cloud platforms (AWS, Azure) enabling millions of compound evaluations, though success still hinged on data quality and target properties.
- **AI-designed drugs entered clinical trials**, but with mixed results. Insilico Medicine progressed AI-designed molecules into Phase I/II (e.g., INS018_055 for fibrosis), and Exscientia advanced several AI-designed oncology/immunology candidates (e.g., EXS-21546, though some trials were terminated); these efforts proved feasibility but have not yet produced broad, approved drug classes.
- **AI platforms became embedded in pharma workflows** (e.g., collaborations with GSK, Sanofi) for hit-finding and optimization, but timelines remained long and costs high, with no wholesale replacement of medicinal chemistry.
- **BenevolentAI** pursued drug repurposing and target discovery (e.g., baricitinib in COVID and other indications) with modest wins, but the "AI-native" drug from scratch remained challenging. Atomwise continued developing AI screening tools, with numerous partnerships but no breakthrough approvals.
- **Regulatory engagement** grew: the FDA and EMA issued guidance on AI/ML in drug development, focusing on data governance, validation, and reproducibility rather than rapid deregulation.

**Impact summary**: AI strengthened certain discovery steps (target ID, virtual screening, lead optimization) and enabled a few clinical candidates, but it did not compress overall discovery-to-approval timelines by years. Validation, translational gaps, and clinical failure rates remained stubborn.

## 3. PREDICTIONS

- **Claim: AI would slash drug discovery timelines by six years ("3–6 years" reduced to "3–6 days")**.
  - **Outcome**: Did not materialize. AI accelerated specific bottlenecks (virtual screening, some lead optimization), but discovery-to-approval timelines remained ~10–15 years in most cases. Early-stage time savings did not cascade into later phases, and clinical failures persisted.

- **Claim: Companies like Atomwise, BenevolentAI, and twoXAR would drive major industry change**.
  - **Outcome**: These firms built credible platforms used in pharma collaborations, but they did not transform the overall productivity or cost structure of drug development. No company delivered a fully AI-designed blockbuster drug validated from de novo design through approval.

- **Implicit prediction: De novo computation of drug properties faced extreme computational barriers**.
  - **Outcome**: Largely correct. High-accuracy quantum-level methods remained computationally prohibitive for routine large-scale screening. Instead, ML models trained on experimental data, hybrid methods, and FEP became the practical path forward.

- **Prediction: Mining existing drugs for repurposing and literature for hidden connections would be AI's nearer-term role**.
  - **Outcome**: Accurate. Drug repurposing (e.g., baricitinib, dexamethasone in COVID) showed success. Knowledge graphs and NLP for target–disease links became standard in pharma R&D, with real but incremental gains.

## 4. INTEREST

Rating: **7/10**

This article was prescient in distinguishing plausible AI applications (repurposing, optimization) from inflated claims (six-year cuts). It accurately anticipated that computational intensity and data curation would remain bottlenecks, and it correctly predicted that progress would be incremental rather than revolutionary. Its concrete critique and references to real tools (FEP) and companies add lasting relevance.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20171003-knock-six-years-your-timeline-um.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_