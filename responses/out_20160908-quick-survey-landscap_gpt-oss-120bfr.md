
https://www.science.org/content/blog-post/quick-survey-landscape
# A Quick Survey of the Landscape (September 2016)

## 1. SUMMARY  
The 2016 commentary argued that classic medicinal‑chemistry—designing drug‑like small molecules for well‑defined protein pockets—was reaching the limits of its “low‑hanging fruit.”  The author divided the proteome into three zones:

1. **Traditional, tractable sites** (enzyme active sites, GPCR orthosteric pockets, bromodomains, Hsp90) that have historically yielded many drugs.  
2. **Intermediate, harder‑to‑drug sites** such as shallow protein‑protein interfaces (e.g., Bcl‑Abl groove) and other surface pockets that can be hit with enough screening effort.  
3. **Very challenging territories** (large flat PPIs, intrinsically disordered proteins, protein‑carbohydrate interfaces) that are better served by biologics or emerging hybrid approaches like PROTACs and other small‑molecule‑conjugate technologies.

The piece concluded that the “homeland” of small‑molecule med‑chem was shrinking, but that new, potentially lucrative territories lay beyond—provided chemists could learn to work in them.

---

## 2. HISTORY  

### a. Expansion of “undruggable” targets  
| Target class | Key post‑2016 milestones | Real‑world impact |
|--------------|--------------------------|-------------------|
| **KRAS G12C** | Sotorasib (Lumakras) FDA approval 2021; Adagrasib (Krazati) FDA approval 2022. | First FDA‑approved covalent inhibitors of a classic “undruggable” oncogene; now standard of care for KRAS‑mutant NSCLC. |
| **KRAS G12D/G12V** | Early‑phase trials of G12D covalent inhibitors (e.g., JDQ443) 2023‑24; no approvals yet but robust pipeline. | Demonstrates that the “hard” pocket concept is being breached. |
| **BET bromodomains** | Multiple BET inhibitors entered clinical trials (e.g., birabresib, pelabresib). Most failed to meet efficacy endpoints; pelabresib received FDA **Fast Track** for myelofibrosis (2023) but still not approved. | Shows that even “easier” new pockets can be clinically problematic. |
| **BCL‑2 family** | Venetoclax (already approved 2016) spurred a wave of BCL‑2/BCL‑XL inhibitors; most later candidates (e.g., navitoclax) halted due to thrombocytopenia. | Confirms that some intermediate PPIs are druggable but safety can be limiting. |
| **Protein‑protein interfaces (PPIs)** | Development of *molecular glues* (e.g., lenalidomide analogs) and *PROTACs* accelerated. 2023‑24 saw the first PROTACs (e.g., ARV‑110, ARV‑471) reach Phase III, but **no PROTAC has yet received FDA approval** as of Dec 2025. | The field is maturing; the “conjugate” idea from the article is now a major research area. |
| **Intrinsically disordered proteins (IDPs)** | Small‑molecule binders to MYC (e.g., MYCi975) remain pre‑clinical; no FDA‑approved IDP‑targeted drugs yet. | The hardest zone remains largely out of reach. |

### b. Growth of hybrid modalities  
* **Antibody‑drug conjugates (ADCs)** – FDA approvals rose from 2 in 2016 to >15 by 2024 (e.g., trastuzumab‑deruxtecan, sacituzumab govitecan). While biologic‑centric, the payloads are small‑molecule cytotoxins, validating the “small‑molecule conjugate” concept.  
* **Targeted protein degradation (TPD)** – Beyond PROTACs, *molecular glues* (e.g., lenalidomide, pomalidomide) have become a commercial reality (e.g., iberdomide for SLE, 2022). The field now includes *autophagy‑targeting chimeras* (AUTACs) and *lysosome‑targeting chimeras* (LYTACs) in early trials.  

### c. Technological enablers  
* **AI‑driven structure prediction (AlphaFold, RoseTTAFold)** – Made high‑confidence models of many “undruggable” proteins publicly available, accelerating pocket identification.  
* **Covalent‑warhead libraries & fragment‑based covalent screening** – Enabled rapid discovery of irreversible binders for shallow pockets (e.g., KRAS G12C).  
* **Macrocycle and constrained‑peptide chemistry** – Expanded the chemical space able to engage flat PPIs; several macrocyclic inhibitors entered Phase I/II (e.g., cyclotide‑based BCL‑2 inhibitors).  

### d. Market and business outcomes  
* **Big‑pharma R&D spend** on small‑molecule discovery remained flat (~$30 B / yr) while investment in biologics and TPD rose >50 % from 2016 to 2024.  
* Companies that pivoted early to TPD (e.g., Arvinas, C4 Therapeutics) attracted multi‑hundred‑million‑dollar valuations, whereas firms that stayed solely on traditional enzyme targets saw mixed results.  
* Overall, **small‑molecule approvals continued robustly**: 2020‑2024 saw 45 first‑in‑class NMEs, many in oncology and rare diseases, indicating the “shrinking homeland” narrative was overstated.

---

## 3. PREDICTIONS  

| Prediction (from article) | What actually happened |
|---------------------------|------------------------|
| *“We will eventually come to the end of the list of tractable small‑molecule binding sites.”* | The list has **not** ended; new pockets (KRAS, KRAS‑G12D, KRAS‑G12V, certain PPIs) have been opened, but many classic sites are now saturated. |
| *“The future of small‑molecule medicinal chemistry will be tied to how much of this landscape we can actually manage to work in.”* | Accurate: success of covalent KRAS inhibitors, PROTACs, and macrocycles shows progress is directly linked to expanding the addressable landscape. |
| *“Small‑molecule conjugates with larger biologics (e.g., PROTACs) are a large area with a lot of unexplored territory.”* | Spot‑on. 2020‑2025 saw a surge of PROTAC and molecular‑glue programs; while no FDA approval yet, dozens of candidates are in late‑stage trials, confirming the area’s growth. |
| *“Great big flattish protein‑protein interactions and intrinsically disordered proteins will be the domain of antibodies and biologics.”* | Largely true. 2022‑2025 saw no approved small‑molecule drugs targeting large flat PPIs or IDPs; biologics (e.g., bispecific antibodies) dominate those spaces. |
| *“The traditional homeland of med‑chem is probably shrinking.”* | Partially true: classic enzyme/GPCR space is crowded, but the overall pipeline of small‑molecule NMEs has not declined; new modalities have compensated. |

---

## 4. INTEREST  
**Rating: 7/10**  

The article is a concise, forward‑looking snapshot of a pivotal moment in drug discovery. Its predictions about emerging modalities (PROTACs, conjugates) proved prescient, while its more fatalistic view of a “shrinking” small‑molecule world was only partly correct. The piece remains relevant for understanding how the field’s strategic thinking evolved over the past decade.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160908-quick-survey-landscape.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_