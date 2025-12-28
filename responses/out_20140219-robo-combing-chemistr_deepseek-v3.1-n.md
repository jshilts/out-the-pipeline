
https://www.science.org/content/blog-post/robo-combing-chemistry-literature-mistakes
# Robo-Combing the Chemistry Literature For Mistakes (February 2014)

## 1. SUMMARY

The article discusses Peter Murray-Rust's development of a software system called **ChemVisitor** and **OSCAR** that can automatically scan chemical literature to detect **errors and fraud** in molecular structures and experimental data. Using open databases like Pubchem, the software identifies incorrect structures, misdrawn compounds, and deliberate fraud. The post highlights a contentious battleground between **open scientific infrastructure** (like NIH's Pubchem) and **commercial publishers** (Elsevier, ACS, Wiley), noting that ACS previously tried to shut down Pubchem. The software can parse ancient papers with poor diagrams, reconstruct correct chemical structures, detect image manipulations (such as scientists covering up inconvenient data peaks), and analyze thousands of papers per hour. A commenter on Ycombinator warns that similar fraud is found in most chemistry papers analyzed, suggesting widespread issues that traditional peer review misses.

## 2. HISTORY

**Academic Infrastructure and Adoption:**
- **Open data efforts expanded**: Pubchem remained operational and grew, becoming a key NIH resource. The NIH Common Fund launched the **Illuminating the Druggable Genome** (IDG) program in 2015, leveraging large databases to classify understudied proteins, indirectly supporting text/data mining.
- **Mining policies evolved**: Many publishers now permit limited text and data mining for non-commercial research, often via API agreements, although debates over terms and attribution continue.
- **Tools matured**: The OSCAR/ChemVisitor concepts influenced later chemistry-aware NLP, such as named-entity recognition for molecules, but did not become a dominant open referee tool in chemistry journals.
- **Community efforts**: Initiatives like **ChemDataExtractor** (developed by Murray-Rust's group and others) gained academic traction for automated extraction, while platforms like **Sci-Hub** and **Open Access** activism pressured publishers to improve accessibility.

**Commercial Landscape:**
- **Elsevier** maintained its proprietary **Reaxys** database, integrating reaction and property data with curated content.
- **ACS** retained its **Chemical Abstracts Service** (CAS) registry and pricing model.
- **New entrants**: Platforms like **ChemRxiv** (preprint server for chemistry, launched 2017) and commercial AI tools for medicinal chemistry drew on data-mining techniques, but often relied on curated/licensed databases rather than raw-paper mining.

**Evidence of Automated Error/Fraud Detection Impact:**
- **Retraction Watch** documented thousands of retractions in chemistry, including image manipulation scandals. While some were caught via manual review or post-publication comments, systematic automated screening was **not widely adopted** by top-tier chemistry journals in the period immediately following 2014.
- **Image forensics tools** (e.g., **ImageJ plugins**) became more common for detecting duplications and alterations, but broad adoption of the "robotic referee" concept for chemistry papers did not materialize at scale.
- **Regulatory and clinical impact**: This line of work did not directly lead to **FDA approvals** or specific drug pipelines. Its influence was more indirect (data quality in public databases supporting drug discovery).

**Business Models:**
- Paywalls remained strong for major chemistry publishers; some publishers introduced content-mining APIs or permitted limited reuse.
- Open-access mandates (e.g., Plan S) gained traction later in the decade, driving policy changes and more open licensing.
- No major chemistry journal adopted automated chemical-structure validation as a default screening step during 2014–2020, though some preprint servers began using automated checks.

## 3. PREDICTIONS

The article implicitly predicted several developments:

- **Automated refereeing in chemistry**: The author believed we would "hear a lot more about this." While academic prototypes like ChemDataExtractor and related tools advanced, widespread adoption of automated refereeing **did not happen** by journals—most still rely on human peer review.
- **Publishers resisting criticism**: The article anticipated publishers would object to public error-highlighting. This proved true; lawsuits or threats over mining terms occurred periodically, though open-access advocacy and policy pressures slowly shifted norms.
- **Discovery of widespread errors and fraud**: The claim that automated tools "find this in most chemistry papers" presaged broader awareness of the replication crisis and image manipulation issues. However, systematic automated screening at scale **never exposed "most" papers** as fraudulent—it remained concentrated in specific cases, often flagged via post-publication scrutiny.

## 4. INTEREST

Rating: **5/10**

This article raised important questions about quality control in scientific publishing and highlighted tensions between commercial publishers and open infrastructure. While the specific concept of robotic refereeing did not revolutionize chemistry review in subsequent years, it anticipated broader debates over open science and automated quality assurance.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20140219-robo-combing-chemistry-literature-mistakes.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_