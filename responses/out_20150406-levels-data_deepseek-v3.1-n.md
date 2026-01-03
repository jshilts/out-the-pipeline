
https://www.science.org/content/blog-post/levels-data
# Levels of Data (April 2015)

## 1. SUMMARY

This brief commentary discusses a Science article that outlines a six-level hierarchy of data analysis, moving from simple to complex: (1) **Descriptive**—summarizing data; (2) **Exploratory**—looking for trends to form hypotheses; (3) **Inferential**—using statistics to assess whether a pattern is likely real; (4) **Predictive**—using subsets to forecast outcomes (e.g., biomarkers predicting treatment response); (5) **Causal**—quantifying how changing inputs affects outputs; and (6) **Mechanistic**—detailed, explanatory models of how A causes B. The author then contextualizes these levels within drug research, noting that mechanistic understanding—common in engineering—remains aspirational in biology due to complexity and variability. The example given is that we can make some population-level predictions about ACE inhibitors after decades of study, but nothing approaching the tight specifications of aeronautical engineering, where components are standardized and outcomes are deterministic. The piece argues that public expectations often assume science operates at mechanistic levels, leading to frustration, and urges awareness of where drug research actually sits on this spectrum.

## 2. HISTORY

**Growth of data-centric approaches in drug discovery and approval**:  
After 2015, a number of technologies and policies moved drug research toward higher levels of the data hierarchy, especially predictive and causal uses. AI/ML for target identification, lead optimization, and clinical trial design became widespread; biomarker-driven and basket trials increased; regulators adopted more flexible evidence standards; cell and gene therapies introduced high-stakes, mechanism-focused data capture; and real-world data (RWD) gained acceptance to complement randomized trials. However, mechanistic certainty remained rare outside narrowly controlled systems.

**Biomarkers and predictive analytics**  
- FDA approvals increasingly relied on predictive biomarkers (e.g., PD-L1, MSI-H/dMMR, BRCA mutations), enabling patient selection for immunotherapies and targeted agents. By the late 2010s, CDx (companion diagnostics) became common, with several drugs approved with mandatory or recommended biomarker testing.  
- AI-driven biomarker discovery expanded, though many candidate biomarkers did not reach clinical utility due to lack of prospective validation or generalizability.  
- Predictive toxicology remained challenging, with notable failures in translating in silico models to human outcomes, but some successes in early screening (e.g., hERG, metabolic stability) became routine.

**Causal inference in medicine and policy**  
- Mendelian randomization grew as an approach to strengthen causal claims in observational data, informing guideline updates and risk stratification (e.g., lipid-lowering targets, cardiovascular outcomes).  
- Adaptive trial designs and platform trials (e.g., I-SPY 2, RECOVERY) enabled causal estimation under uncertainty and faster go/no-go decisions.

**Mechanistic understanding**  
- Progress was domain-specific. In oncology, resistance mechanisms were partly elucidated (e.g., EGFR T790M, ALK bypass pathways), enabling next-generation inhibitors and combinations, but exceptions and adaptive resistance remained common.  
- Cell and gene therapies (e.g., CAR-T) required deep mechanistic validation of manufacturing and potency assays, pushing toward mechanistic characterization for some products.  
- Rare diseases saw some successes when genetic causality was strong and surrogate endpoints were mechanistically justified, speeding approvals (e.g., SMA therapies, some enzyme-replacement therapies).

**Regulatory and methodological shifts**  
- FDA’s 21st Century Cures Act (2016) and subsequent framework updates encouraged use of RWD, biomarkers, and model-informed drug development (MIDD) as part of the evidence package.  
- Real-world evidence accelerated some label expansions and comparative effectiveness insights, though causal claims often remained weaker than RCTs.  
- Pharma invested heavily in computational platforms, but continued to face high attrition rates; many AI-predicted targets or compounds failed to translate.

**Public and investor expectations**  
- Hype cycles around AI/ML led to unrealistic expectations about predictive accuracy and mechanistic certainty, causing volatility and some backlash when early AI-driven programs failed.  
- Precision medicine initiatives expanded, but granular, mechanism-level matching of patients to therapies remained more aspiration than reality for most diseases.

## 3. PREDICTIONS

- **Prediction 1**: The article implies that predictive use (Level 4)—specifically biomarkers predicting patient response—would remain a frontier, and that mechanistic understanding (Level 6) would rarely be achieved outside engineering.  
  - **Outcome**: Broadly validated. Predictive biomarkers became standard in oncology and some other areas, with multiple FDA approvals tied to CDx and biomarker-defined subsets. Mechanistic insights did improve in narrow contexts (e.g., pathway-specific resistance, mode of action for biologics), but true, exception-free mechanistic models remained elusive in most complex diseases.

- **Prediction 2**: The author’s analogy contrasts drug development (high variability, probabilistic outcomes) with aeronautical engineering (tight tolerances, deterministic performance), suggesting drug research would not soon match engineering’s predictability.  
  - **Outcome**: Validated. Drug discovery timelines and attrition rates did not collapse to engineering-like precision, despite AI advances. Trial failures continued for programs with promising biomarkers and preclinical data, and off-target effects or population heterogeneity limited predictive accuracy.

- **Prediction 3**: The article suggests public and stakeholder expectations would clash with the actual maturity of data analysis, and that “is this pill going to help me or not?” would remain hard to answer definitively.  
  - **Outcome**: Partially validated. Precision medicine and CDx have allowed more targeted, individualized answers in select settings, but population-level variability and unpredictable responses remain prevalent. Frustration persists in areas with few validated biomarkers or weak mechanistic understanding.

- **Prediction 4**: The discussion implies levels below causal/mechanistic (descriptive, exploratory, inferential) would remain the workhorses of routine practice.  
  - **Outcome**: Validated. Descriptive and inferential statistics remain dominant in publications and regulatory filings, with exploratory work driving hypothesis generation. Causal and mechanistic claims are still reserved for well-controlled subsystems and face intense scrutiny.

## 4. INTEREST

**Rating: 6/10**  
This is a concise, durable conceptual framework that helps structure thinking about evidence strength in drug research. Although it summarizes well-known ideas in statistics, its application to drug development is apt, and the engineering-versus-biology contrast remains relevant.

---

--- The article ---


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20150406-levels-data.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_