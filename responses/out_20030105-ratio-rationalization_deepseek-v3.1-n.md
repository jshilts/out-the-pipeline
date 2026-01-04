
https://www.science.org/content/blog-post/ratio-rationalizations
# Ratio Rationalizations (5 Jan 2003)

## 1. SUMMARY

This commentary highlights a fundamental challenge in drug discovery: the overinterpretation of selectivity ratios. The author explains that medicinal chemists routinely rank compounds using ratios (e.g., "10x selective" or "100-fold over that enzyme") across secondary assays, and later use exposure ratios (Cmax or AUC relative to binding potency) to prioritize compounds for animal studies. However, these ratio-derived numbers often appear more reliable than they actually are, because the original error bars and variability of the underlying assays disappear when results are expressed as ratios. Biological assays exhibit substantial variability—often ±100% or more—with more realistic systems (cell assays, tissue preps, animal studies) generally showing greater scatter than simpler systems (cloned proteins). When highly variable assays sit in the denominator of a ratio, the resulting values can be erratic and misleading. The author stresses that "N of 1" data should not be trusted, especially when it seems startling or unusual; replication is essential before sharing results to avoid propagating junk data in the high-stakes drug discovery environment.

## 2. HISTORY

The core challenges described in this 2003 article remain relevant in drug discovery today, though practices and available tools have evolved to address them.

- **Statistical Rigor in Early Discovery**: Since 2003, pharmaceutical companies increasingly adopted standardized protocols and statistical frameworks for hit-to-lead and lead optimization. Greater emphasis was placed on determining the appropriate number of replicates, outlier handling, and error propagation when reporting ratios (e.g., selectivity, efflux, exposure multiples). Best practices converged on reporting both the ratio and confidence intervals from replicated measurements, often with thermal shift assays, SPR, or orthogonal assays to confirm binding.

- **Automation and Quality Control**: High-throughput screening and automated dose-response workflows reduced, but did not eliminate, assay variability. Laboratory information management systems (LIMS) and standardized data pipelines became common, helping flag irreproducible results early and enforce replication before advancing compounds.

- **PK/PD Modeling and Exposure Ratios**: The use of exposure ratios (Cmax/IC50 or AUC/IC50) as cutoffs for advancing compounds continued to be widespread in pharmacokinetic-pharmacodynamic (PK/PD) decision-making. However, the field increasingly recognized that these ratios are context-dependent—what constitutes an effective multiple varies by target, pathway, and indication. Population PK/PD and mechanistic modeling supplemented simple ratio-based rules to guide dosing and candidate selection.

- **Selectivity Screening and Safety Profiling**: Large panels (e.g., kinases, GPCRs, safety screens) became routine to quantify selectivity across hundreds of targets, not just a few secondary assays. Off-target profiling via broad screening and computational prediction reduced reliance on one-dimensional ratio cutoffs and prompted more holistic assessments of polypharmacology and safety margins.

- **Regulatory and Replication Standards**: High-profile replication failures across scientific fields (including preclinical research) led journals and funders to adopt stricter standards for reporting experimental details, statistical power, and reproducibility. Initiatives like the FDA's "21st Century Cures" provisions and ICH harmonization emphasized robust evidence standards, pushing sponsors to present replicated, well-controlled data rather than single-trial claims.

- **Continue Relevance of Warnings**: Instances of clinical failures due to unvalidated target engagement or exaggerated selectivity persisted post-2003, reinforcing the article’s caution. The imperative to "fail fast and fail cheap" drove better statistical literacy, but the tension between speed and rigor remained—especially in competitive, fast-moving organizations.

In summary, the article’s concerns became widely appreciated, leading to more systematic approaches to assay variability and reporting. However, the underlying challenges did not disappear; they were managed through better tools, processes, and statistical awareness rather than fundamental solutions.

## 3. PREDICTIONS

- **Implicit prediction that overreliance on ratios would lead to costly missteps**: This proved true repeatedly. Well-documented examples include late-stage clinical failures where selectivity claims based on in vitro ratios did not translate to in vivo safety margins, and marketed drugs later found to have broader off-target effects than originally claimed. On the other hand, systematic adoption of ratio cutoffs in early discovery did help prune unpromising series earlier, improving the quality of candidate nominations.

- **Implicit emphasis that assay variability matters most when cascading assays (cloned protein → cells → tissue → animals)**: This held true. Assay cascades remained central to drug discovery, and variability did increase along that realism gradient. Consequently, organizations invested heavily in tiered, orthogonal assays and used statistical simulations to anticipate failure points, directly reflecting the caution advocated in the article.

- **Prediction (via criticism) that "N of 1" data often yields misleading claims**: This concern became deeply embedded in modern practice. Most discovery organizations now require at least duplicate or triplicate measurements, dose-response confirmation, and confirmatory assays before advancing compounds. Nonetheless, pressure to generate "starling results" sometimes still leads teams to overinterpret preliminary data—industry lore is replete with examples of promising "ratio hero" compounds that crashed on replication.

- **No explicit long-term forecast about which therapeutic areas or modalities would be most affected**: The principles apply broadly across small molecules, biologics, and more recent modalities (e.g., PROTACs, molecular glues), where selectivity, target engagement, and exposure ratios are equally critical. The fundamentals of assay variability and error propagation continue to shape decision-making, with no single modality escaping these constraints.

## 4. INTEREST

Rating: **7/10**

Although written as a short commentary, the article focuses on a foundational, persistent issue in drug discovery—assay variability and the statistical illusions created by ratio-based reporting—making it broadly applicable and time-relevant. Its core message remains standard teaching in medicinal chemistry and pharmacology.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20030105-ratio-rationalizations.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_