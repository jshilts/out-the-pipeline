
https://www.science.org/content/blog-post/ligands-nothing
# Ligands From Nothing (September 2013)

## 1. SUMMARY

The article describes a fragment-based drug discovery technique developed by the Ernst lab at the University of Basel that combines spin-label NMR screening with in situ click chemistry to generate high-affinity ligands from very weak starting fragments. The method uses SLAPSTIC (Spin Labels Attached to Protein Side chains as a Tool to identify Interacting Compounds), where a spin label is attached to a weak-affinity ligand (such as a sialic acid with only 137 micromolar affinity for myelin-associated glycoprotein), then uses NMR to detect nearby binding fragments. When a suitable second-site binder is identified, the fragments are linked using azide-acetylene click chemistry, sometimes with the protein itself catalyzing the reaction.

The technique was demonstrated on two targets: MAG (myelin-associated glycoprotein) and E-selectin. For MAG, they started with a 137 micromolar fragment and ended with a 190 nanomolar linked compound. For E-selectin, they started with a 1 micromolar trisaccharide derivative and achieved 20-50x improvements in affinity. Notably, 5-nitroindole repeatedly emerged as the second-site binder, raising concerns about the generality of the approach. The method is structure-agnostic (doesn't require knowing the protein structure or labeling the protein) and represents a clever revival of fragment-linking strategies, though the author notes practical challenges with earlier SAR-by-NMR approaches from the 1990s that consumed significant resources with limited success.

## 2. HISTORY

Fragment-based drug discovery (FBDD) has evolved significantly since 2013, though the specific spin-labeling technique described here has not become a mainstream industrial approach. Fragment-based methods more broadly have demonstrated continued success in drug discovery, with multiple FDA-approved drugs originating from fragment screens and many more in clinical development.

The most notable success story validating fragment-based approaches is **venetoclax (Venclexta)**, a BCL-2 inhibitor for chronic lymphocytic leukemia that originated from fragment screening and was FDA-approved in 2016. However, this came from more conventional FBDD rather than the spin-label/click chemistry approach described in the article. Other fragment-derived drugs include vemurafenib and erdafitinib.

The **NMR-based screening market** has remained a niche but valuable tool, with companies like Novartis (where Jahnke's original SLAPSTIC work was done) continuing to use various NMR techniques for fragment screening, though primarily through protein-observed methods rather than spin-labeling approaches. Bruker and other NMR manufacturers maintain dedicated fragment-screening workflows.

**Click chemistry** has found broader adoption in drug discovery, particularly for PROTAC development and bioconjugation, but the specific in situ "protein-templated" click approach described here has not become standard practice. The concern about **5-nitroindole** being problematic for drug development due to potential toxicity/metabolic issues remains valid - functional groups like nitro groups are generally avoided in screening libraries due to potential for off-target effects and metabolic liabilities.

The **academic trajectory** of this specific technique appears limited. A search of subsequent literature shows the Ernst lab continued publishing in NMR methodology, but the spin-label click-linking approach did not spawn widespread adoption or commercialization. The technique remains an elegant academic demonstration rather than a transformative industrial technology.

## 3. PREDICTIONS

The article contained several explicit and implicit predictions that can be evaluated:

• **Fragment linking would continue to be challenging**: ✓ **CORRECT**. While fragment-based drug discovery has succeeded (venetoclax, etc.), fragment *linking* specifically remains difficult and has lower success rates than fragment-to-lead optimization. The "brutal" nature of getting linking to work, as the author noted, matches post-2013 experience.

• **The nitro group concern would cause problems**: ✓ **CORRECT**. The author's worry about nitro groups being "an invitation to trouble" has been validated by subsequent drug development experience. Nitroaromatics are known for potential mutagenicity, metabolic reduction to toxic anilines, and other liabilities. Modern fragment libraries typically exclude such functionalities.

• **The technique might only work with 5-nitroindole**: **PARTIALLY VALIDATED**. The limited subsequent adoption of this exact approach suggests it may indeed have narrow applicability. However, this specific concern wasn't definitively resolved in published literature.

• **Structure-agnostic methods would be valuable**: **MIXED**. While desirable in theory, most successful FBDD programs still benefit from structural information (X-ray crystallography, cryo-EM). The author's enthusiasm for methods not requiring protein structure was understandable, but subsequent experience shows structural information generally accelerates optimization.

• **The technique would be worth taking seriously as a practical tool**: ✗ **NOT BORN OUT**. Despite elegant demonstrations on MAG and E-selectin, this specific spin-label/click approach has not become widely adopted in pharmaceutical discovery, suggesting practical limitations not evident in the proof-of-concept papers. Most industrial FBDD now uses SPR, thermal shift, or NMR with direct protein observation rather than spin-labeled ligands.

## 4. INTEREST 

Rating: **4/10**

The article covers an intellectually clever but ultimately niche technique that did not substantially impact drug discovery practice, though it intersects with broader trends (FBDD, click chemistry) that have shown clinical success through other implementations.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20130912-ligands-nothing.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_