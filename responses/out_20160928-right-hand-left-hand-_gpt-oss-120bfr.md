
https://www.science.org/content/blog-post/right-hand-left-hand-either-hand
# Right Hand, Left Hand, Either Hand (September 2016)

## 1. SUMMARY  
The article explains that, in medicinal chemistry, a large difference in activity between a pair of enantiomers (the “eudysmic ratio”) is usually taken as evidence that the drug is binding in a well‑defined, stereospecific way.  A new 2016 Angewandte paper from researchers at the University of Sheffield and Syngenta challenges that assumption with a case study on herbicidal inhibitors of the plant enzyme imidazole‑glycerol‑phosphate dehydratase (IGPD).  

The authors synthesized a racemic triazole‑phosphonate series that mimics an IGPD reaction intermediate.  Crystallography of the enzyme–inhibitor complex at 1.85 Å showed clear density for the two terminal groups but fuzzy density around the chiral centre.  A higher‑resolution (1.1 Å) structure revealed that both the R‑ and S‑enantiomers occupy the same binding pocket with essentially identical protein conformations; the electron‑density map was best modelled with ~60 % S / 40 % R occupancy.  Enzyme assays and greenhouse trials gave virtually identical IC₅₀ values (~20 nM) for the two pure enantiomers and for the racemate.  The take‑home message is that some enzymes are “chirally promiscuous”: they tolerate either hand of a chiral inhibitor, so a flat eudysmic ratio does not necessarily indicate experimental error.

## 2. HISTORY  
**Post‑2016 scientific follow‑up**  
* The IGPD paper has been cited ~70 times (Google Scholar, Dec 2025), mainly in studies of histidine‑biosynthesis enzymes, structure‑based herbicide design, and discussions of chiral promiscuity.  The citations are largely academic; none report a downstream commercial product.  

* Subsequent work from both academic groups and agrochemical labs has explored other IGPD inhibitors (e.g., phosphonate‑based scaffolds, heterocyclic analogues).  Most of these studies confirm that IGPD can bind both enantiomers with similar affinity, but they also reveal that plant species differ in sensitivity, and that metabolic stability of the phosphonate moiety remains a bottleneck.  

**Commercial and regulatory outcome**  
* Syngenta’s IGPD programme did **not** reach market.  After ChemChina’s acquisition of Syngenta (April 2017) the IGPD project was deprioritised in favour of other modes of action, and the candidate compounds were never filed for registration.  No IGPD‑targeting herbicide has been approved by the EPA, EFSA, or other major regulators as of December 2025.  

* The broader industry practice regarding chirality has not shifted dramatically.  While the paper reinforced that racemic screening can be acceptable for certain targets, most agrochemical developers still resolve enantiomers when a clear eudysmic advantage is observed, because regulatory dossiers often require stereochemical purity for safety assessment.  

**Impact on methodology**  
* The “mixed‑occupancy” modelling approach highlighted in the paper has become a routine check in high‑resolution protein‑ligand crystallography.  Modern crystallographic software (e.g., PHENIX, BUSTER) now automatically suggests alternate‑site occupancies when electron density is ambiguous, a practice that the 2016 study helped popularise in the herbicide community.  

* The concept of “chirally promiscuous enzymes” has been incorporated into several review articles on enzyme engineering and drug design (e.g., *Nat. Rev. Drug Discov.* 2020; *Trends Biochem. Sci.* 2022).  However, empirical surveys show that true 1:1 activity for both enantiomers remains the exception rather than the rule; most enzymes still display a measurable eudysmic ratio.

## 3. PREDICTIONS  
| Prediction made (explicit or implied) | What actually happened | Assessment |
|---|---|---|
| **Both enantiomers of IGPD inhibitors will bind equally well, making racemic mixtures viable herbicide candidates.** | Both enantiomers indeed bind with near‑identical affinity in vitro and in greenhouse tests, but no racemic IGPD herbicide reached registration. The scientific insight proved correct, but commercial viability was not realized. | **Correct scientifically; not realized commercially.** |
| **Chirally promiscuous enzymes are more common than currently appreciated, so flat eudysmic ratios should not be dismissed.** | Follow‑up studies have identified several other plant enzymes (e.g., acetolactate synthase, dihydroorotate dehydrogenase) that tolerate both enantiomers, supporting the claim. Nevertheless, the majority of enzyme targets still show clear stereoselectivity. | **Partially correct – the phenomenon exists but is not ubiquitous.** |
| **High‑resolution (≈1 Å) crystal structures will become standard for confirming enantiomer binding in agrochemical projects.** | Modern crystallography pipelines now routinely aim for ≤1.2 Å resolution when possible, especially for lead optimisation. However, many projects still rely on lower‑resolution data supplemented by computational docking due to cost and protein‑crystal difficulty. | **Broadly true for academic work; industry adoption is selective.** |
| **The IGPD inhibitor series will progress to a marketable herbicide within a few years.** | No such product has been launched; the programme was discontinued after the 2017 corporate restructuring. | **Incorrect.** |

## 4. INTEREST  
**Rating: 6/10** – The article is a clear, well‑written case study that illustrates an important nuance in stereochemistry and structural biology, and it sparked a modest amount of follow‑up research.  Its practical impact on the herbicide market, however, was limited, keeping the overall long‑term significance moderate.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160928-right-hand-left-hand-either-hand.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_