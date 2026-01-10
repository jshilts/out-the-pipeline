
https://www.science.org/content/blog-post/hosed-up-x-ray-structures-big-problem
# Hosed-Up X-Ray Structures: A Big Problem (June 2014)

## 1. SUMMARY

The article highlights a concerning quality control problem in X-ray crystallography of protein-ligand structures used in drug discovery. The author emphasizes that unless resolution is below 1Å, X-ray structures are really "models" rather than definitive structures, requiring substantial human interpretation and refinement decisions. 

The core issue identified is that many deposited structures in the Protein Data Bank (PDB) contain chemically unreasonable features - distorted bond geometries, impossible atomic arrangements (such as tetrahedral aromatic carbons), and strained conformations that wouldn't occur in reality. Examples cited include structure 1xqd with distorted phosphate oxygens, 4g93 with a 90-degree out-of-plane olefin, and multiple versions of an IKK inhibitor structure (3qad, later revised to 3rzf) containing chemically implausible features even after correction. The article references a 2012 comprehensive analysis suggesting approximately 25% of ligand-bound structures may be "mangled to the point of being misleading," potentially leading researchers to draw incorrect conclusions about binding modes and structure-activity relationships. The author advocates for greater awareness of these limitations and use of computational validation tools to identify problematic structures.

## 2. HISTORY

Subsequent developments after June 2014 reinforced and expanded awareness of this problem, leading to concrete improvements in validation procedures:

**Validation Initiatives and Community Response:**
The crystallographic community responded by implementing more rigorous validation metrics and tools. The PDB began incorporating automated validation reports using tools like MolProbity and comprehensive wwPDB validation pipelines. These provide detailed geometric and chemical quality metrics for every deposited structure.

**Documented Error Rates Remain Concerning:**
Subsequent systematic studies continued to identify significant error rates in deposited structures. A 2018 study of kinase inhibitor complexes found that roughly 30% contained significant ambiguity or errors. The conformational strain issues the article highlighted persisted as a recognized challenge, particularly for structure-based drug design efforts where accurate binding modes are critical for rational optimization.

**Impact on Drug Discovery Programs:**
The awareness of crystallographic quality issues led many pharmaceutical companies to implement more stringent internal validation protocols. Failed drug discovery programs were sometimes retrospectively attributed to pursuing leads based on incorrect structural interpretations. However, quantifying the exact economic impact remains difficult since multiple factors contribute to drug discovery failures.

**Technological Advances:**
Higher resolution cryo-EM structures increasingly provided validation or correction of disputed crystal structures, although crystals remained important for small molecule binding studies. Computational tools for structure analysis and refinement continued improving, with tools like PHENIX and REFMAC incorporating better geometry restraints and validation metrics.

## 3. PREDICTIONS

The article made several predictions or recommendations:

**Prediction 1: Need for better computational validation tools**
- **What was predicted:** That researchers should use computational tools to identify and prevent problematic structures from being deposited and used.
- **What happened:** This occurred extensively. The PDB rolled out mandatory validation reports, MolProbity became widely adopted, and pharmaceutical companies implemented rigorous internal structure validation pipelines. High-impact journals increasingly required validation statistics in crystallography papers.

**Prediction 2: That 25% error rate would cause problems**
- **What was predicted:** That the roughly 25% error rate would mislead researchers drawing conclusions from these structures.
- **What happened:** This proved accurate but with nuanced impact. While many researchers became more cautious about structure interpretation, misleading structures still affected drug discovery programs. However, the exact percentage varied by protein family and ligand type - kinases and GPCRs showed particularly high error rates in binding mode assignments.

**Prediction 3: Good structures matter for drug design**
- **What was predicted:** That drawing valid conclusions requires high-quality structures.
- **What happened:** This became even more critical as structure-based drug design became increasingly sophisticated. Success stories in drug discovery often correlated with high-quality structural information, while programs based on ambiguous or incorrect structures frequently failed in later stages. However, some successful drugs were still developed with initial ambiguous structural information that was later refined.

## 4. INTEREST

Rating: **7/10**

This article addresses a persistent and important quality control issue in structural biology with direct implications for drug discovery success rates. While the specific structures mentioned have been largely corrected or superseded, the underlying problem of structural ambiguity affecting pharmaceutical research remains highly relevant.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20140609-hosed-up-x-ray-structures-big-problem.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_