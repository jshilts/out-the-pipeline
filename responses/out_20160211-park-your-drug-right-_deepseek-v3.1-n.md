
https://www.science.org/content/blog-post/park-your-drug-right-here-while
# Park Your Drug Right Here For a While (February 2016)

## 1. SUMMARY
This is a commentary reviewing a *Nature Reviews Drug Discovery* retrospective by Bob Copeland on the concept of drug-target residence time in drug discovery. The article notes that Copeland was a key developer of the concept and that it had gained traction in how medicinal chemists think about compound optimization. The piece explains that residence time is governed by on-rates and off-rates of binding, with off-rates showing wider variation. It connects the growth of this approach to the broader adoption of surface plasmon resonance (SPR) assays, which provide direct measurements of both kinetic steps.

The article contrasts the classic "lock and key" model with an "induced fit" picture, where both compound and binding site rearrange in multiple steps. Because reversing those steps takes time, longer residence times often correlate with higher potency—offering a way to optimize both potency and pharmacokinetics together rather than independently. It observes that residence times can exceed a drug's pharmacokinetic half-life, yielding sustained pharmacodynamic effects even after the drug has cleared from circulation. Finally, it places covalent inhibitors (irreversible binders) as the far end of the residence-time continuum rather than a separate category, citing Bruton's tyrosine kinase (BTK) inhibitors as a case where noncovalent compounds can achieve very long residence times similar to covalent ones.

## 2. HISTORY

**Method adoption and instrumentation.** After 2016, SPR and related biophysical methods (bio-layer interferometry, nanoBRET, ITC) became standard tools in drug discovery. Biacore SPR systems are now widespread in most pharmaceutical and biotech R&D labs, and kinetic characterization ($k_{on}$, $k_{off}$, residence time) is routinely captured for hit-to-lead and lead optimization.

**BTK inhibitors (the article's example) demonstrated real-world impact:**
- Ibrutinib (approved pre-2016) is covalent and supported durable efficacy in B-cell malignancies; it saw broad uptake and became a blockbuster (~$6–7B peak revenue).
- Post-2016, acalabrutinib (2017, covalent) and zanubrutinib (2019, covalent) gained FDA approval, reaffirming the value of long target residence in this kinase class.
- Noncovalent BTK inhibitors progressed through trials: vecabrutinib was tested but discontinued (NCT03037645), while pirtobrutinib (noncovalent, FDA-approved 2023) demonstrated durable responses in patients with acquired resistance to prior covalent BTK inhibitors. Pirtobrutinib exemplifies the article’s thesis that noncovalent compounds can achieve long residence times and durable coverage, though its $k_{off}$-driven duration can still differ from covalent agents.

**Approved drugs leveraging residence-time concepts:**
- Kinase inhibitors where long residence time couples potency to durable target coverage: palbociclib, ribociclib, abemaciclib (CDK4/6), osimertinib (EGFR), lorlatinib (ALK), among others—many with PK half-lives of a few hours but PD effects lasting days.
- Long residence time helped address key liabilities in HIV therapy. Doravirine (approved 2018) was rationally optimized to combine high residence time at the viral target with minimal off-target CNS/EHBR binding, reducing side effects despite high potency.
- BCR-ABL (chronic myeloid leukemia): asciminib (2021) exploits residence time on the myristoyl pocket to drive selectivity and overcome resistance to earlier ATP-competitive inhibitors.

**Failures and limitations.**
- Prolonged on-target pharmacology can increase toxicity (e.g., SGLT2 occupancy beyond a threshold duration can elevate genitourinary infection risk; hyper-long residence times on kinases may accentuate on-target toxicities).
- Many oncology drugs with long PD tails still exhibit acquired resistance despite long residence times, showing that optimization involves trade-offs among residence time, selectivity, and tolerability.

**Public and regulatory policy.**
- FDA guidance now generally incorporates kinetic and mechanistic measures (e.g., guidance around covalent inhibitors and requirements for data to support dose selection for irreversible agents). Labeling increasingly reflects PK/PD relationships that depend on residence time (e.g., once-daily dosing for compounds with short PK half-lives but long target coverage).
- Pharmacodynamic biomarkers (target occupancy or pathway inhibition readouts) are routinely used to justify dose and schedule when residence time greatly exceeds PK half-life.

**Business developments.**
- Epizyme (where Copeland previously worked) continued to pursue lysine methyltransferase inhibitors leveraging kinetic principles; its lead drug tazemetostat gained accelerated approval (2020) for certain sarcomas and follicular lymphoma.
- SPR consumables and instruments now represent a substantial market, with vendors like Cytiva (Biacore), Sartorius (Octet), and Nicoya Lifesciences offering workflow-integrated platforms.

## 3. PREDICTIONS
- **Prediction (implicit):** Maximizing residence time would become a routine optimization axis to unify potency and pharmacokinetics. 
  - **Outcome:** Correct. Modern lead optimization often uses SPR early to triage and optimize compounds by residence time. The strategy is now standard in kinase, protease, and epigenetic-target programs.
- **Prediction (implicit):** Noncovalent compounds could achieve extremely long residence times comparable to covalent inhibitors, making reversibility a continuum rather than a binary property. 
  - **Outcome:** Largely correct. BTK inhibitor development showed that potent noncovalent agents can deliver long duration of action (e.g., pirtobrutinib in relapsed/refractory settings). Kinases, phosphatases, and GPCRs have all yielded noncovalent compounds with residence times exceeding PK half-life.
- **Prediction (implicit):** Induced-fit binding would be better described as multi-step docking of compliant partners, displacing “lock and key.”
  - **Outcome:** Supported. Biophysical and structural methods routinely reveal complex binding pathways, conformational selection, and multi-state mechanisms (e.g., RAS-binding inhibitors, KRAS-G12C tools like sotorasib that exploit induced pockets). “Squishy lock and key” remains a useful mental model.
- **Prediction (implicit):** SPR would continue to enable kinetic profiling across compound libraries.
  - **Outcome:** Correct. SPR throughput, sensitivity, and robustness improved, and biophysical fragment screening on Biacore persists as a staple of fragment-based drug discovery.

## 4. INTEREST

Rating: **8/10**

This article captures a durable, practical idea that reshaped lead optimization across the industry and helped explain clinical success—especially for kinase and antiviral drugs—where long residence time decouples efficacy from systemic exposure.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20160211-park-your-drug-right-here-while.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_