
https://www.science.org/content/blog-post/farewell-bioinformatics
# Farewell to Bioinformatics (January 2013)

## 1. SUMMARY
The article presents a provocative critique of the bioinformatics field circa 2013,quoting an anonymous programmer's "farewell" rant. The programmer argues that bioinformatics emerged as a response to molecular biologists producing large quantities of low-quality experimental data, then calling on programmers and mathematicians to "magically extract science" from these results.

The criticism focuses on three main problems: First, that bioinformatics built extensive databases and algorithms to organize fundamentally flawed data. Second, that when certain techniques like microarrays were recognized as problematic, there was denialism and quick pivots to new unproven methods. Third, that circular annotation practices - where databases are searched to annotate new data, which is then submitted back to the same databases - created self-referential systems detached from biological reality, resulting in high error rates in repositories like GenBank.

## 2. HISTORY
The years following 2013 brought substantial changes that addressed many of these concerns while validating others:

**Technology Shifts**: Microarrays, the primary target of criticism, were indeed largely abandoned in favor of RNA-seq for transcriptomics. However, the transition wasn't merely "hasty switching" - RNA-seq offered genuinely superior quantitative accuracy, reproducibility, and dynamic range, and has remained the dominant technology.

**Database Quality**: Concerns about GenBank annotation errors proved prescient. The problem of circular annotation garnered significant attention in the scientific community, leading to more rigorous manual curation efforts, though automated pipelines still dominate. Initiatives like RefSeq, UniProt/Swiss-Prot manual curation, and GO annotations represent responses to quality concerns.

**Clinical Translation**: Bioinformatics pipelines are now standard in clinical genomics, with thousands of FDA-approved bioinformatics tools and workflows used in diagnostic settings. The field successfully moved from research curiosity to clinical utility, with germline and cancer panels now routine in medical practice.

**Regulatory Response**: The FDA established frameworks for bioinformatics tools as medical devices (SaMD - Software as Medical Devices), creating validation pathways that didn't exist in 2013.

**Commercial Success/Failure**: Many bioinformatics companies emerged and succeeded - Illumina dominates sequencing, while companies like Foundation Medicine (acquired by Roche for $2.4B), 23andMe, and Ancestry achieved significant market penetration. However, many others failed, particularly those focused purely on data repositories without clear clinical applications.

## 3. PREDICTIONS
The article doesn't make explicit predictions but implies several outcomes:
- **That bioinformatics databases would become increasingly unreliable**: Partially validated. Database quality issues became widely recognized, leading to curation efforts, but circular annotation remains a concern
- **That bioinformatics wouldn't produce meaningful results**: Strongly contradicted. Bioinformatics has become indispensable to biological research and clinical diagnostics
- **That the field would continue hopping between unproven technologies**: Partially validated. The field continued rapid technology transitions (RNA-seq, single-cell sequencing, spatial transcriptomics), but many of these represented genuine improvements rather than hype cycles

## 4. INTEREST
Rating: **7/10**
This article captured genuine pain points in bioinformatics circa 2013 with remarkable prescience about database quality issues and technology transitions, while missing how fundamentally the field would become embedded in both research and clinical practice.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20130130-farewell-bioinformatics.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_