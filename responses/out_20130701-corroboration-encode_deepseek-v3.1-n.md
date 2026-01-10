
https://www.science.org/content/blog-post/corroboration-encode
# Corroboration for ENCODE? (July 2013)

## 1. SUMMARY

This article analyzes a 2013 PLOS Genetics paper on Long Intergenic Noncoding RNAs (lincRNAs), which reported that the vast majority of the human genome is transcribed into RNA, expanding the known number of lincRNAs from thousands to tens of thousands. The study strongly corroborated the ENCODE project's findings about pervasive transcription across the genome.

Key findings included: identification of over 50,000 putative lincRNAs expressed at minimum one copy per cell, with roughly 925 found at higher expression levels (FPKM>30); evidence that these RNAs are specifically regulated and conserved (not transcriptional noise); and enrichment of trait-associated SNPs in these regions suggesting functional importance. The authors positioned this as resolving discrepancies between observed transcription and previously known lincRNA counts, supporting the view that intergenic regions contain abundant functional elements beyond protein-coding genes, which comprised the debate between seeing these sequences as functional versus GWAS methodological artifacts.

## 2. HISTORY

Following the 2012-2013 ENCODE publications and supporting studies like this lincRNA work, genome biology underwent significant conceptual and practical evolution:

**ENCODE Data Impact and Critique:** The initial ENCODE claim that 80% of the genome is "functional" faced substantial scientific criticism, particularly regarding the definition of "function." Many researchers argued that biochemical activity (transcription, histone marks, protein binding) does not automatically confer biological function. The debate crystallized around whether observed transcription represented functional noncoding elements versus transcriptional noise.

**Conservation and Function Evidence:** In subsequent years, extensive comparative genomics studies revealed that only ~8-15% of the human genome shows evidence of evolutionary constraint (higher conservation than expected by chance), substantially lower than ENCODE's initial biochemical activity estimates. Functional validation efforts (genetic manipulation, molecular biology) demonstrated that while some lincRNAs have important regulatory roles, many show minimal impact when disrupted, suggesting that high-throughput biochemical assays overestimate functional significance.

**RNA Therapeutics Development:** The period after 2013 saw significant advances in RNA-based therapies. Several drugs targeting noncoding transcripts entered clinical trials, with some achieving FDA approval, most notably antisense oligonucleotides for diseases like spinal muscular atrophy (Spinraza, 2016) and hereditary transthyretin amyloidosis (Tegsedi, 2018; Inotersen label). However, these successes targeted specific, well-characterized noncoding mechanisms rather than the broad category of lincRNAs identified in high-throughput studies.

**LincRNA Research Maturation:** Over the following decade, lincRNA research shifted from cataloging thousands of transcripts to functionally validating specific candidates. High-profile examples like **XIST, MALAT1, NEAT1** emerged as important regulators with clear mechanisms and disease relevance. However, functional demonstration remained difficult and time-consuming, leading to a more nuanced view where most lincRNAs likely contribute minimally to phenotype, while a subset have important regulatory functions.

**GWAS Interpretation Evolution:** The concern about intergenic trait-associated SNPs raised in the article proved somewhat prescient. Subsequent research revealed that many GWAS hits in noncoding regions influence gene regulation through enhancer elements, chromatin interactions, and regulatory networks. However, establishing definitive causal mechanisms remained challenging. The **GTEx project** (launched 2013, major publications 2015-2020) provided systematic characterization of tissue-specific gene expression and eQTLs, enabling better interpretation of noncoding variants through their effects on gene expression.

**Business and Therapeutic Impact:** While genomic interpretation companies (like Third Rock-backed **Alnylam**) succeeded with RNA therapeutics, broad efforts to develop interventions targeting thousands of newly discovered lincRNAs largely did not materialize commercially. The field converged on a smaller number of high-value targets with clearer disease relevance and druggability.

## 3. PREDICTIONS

The article explicitly and implicitly made several predictions:

• **"The next phase of this debate will take place" around expression levels and tissue specificity:** ✓ **Correct.** Research indeed shifted to examining expression thresholds, with studies like the Genotype-Tissue Expression (GTEx) project providing extensive tissue-specific RNA-seq data and sophisticated analyses of read count thresholds, noise, and function.

• **Debate would remain unresolved:"But the problem is that the authors are explicitly making the case for thousands upon thousands of lincRNAs being important, and this interpretation won't be satisfied with everyone agreeing on a few hundred new transcripts":** ✓ **Substantially correct.** The debate continued for years without clear resolution. The functional significance of most lincRNAs remains unclear as of 2023, though consensus developed that only a subset of ENCODE-identified elements have strong functional support.

• **Implicit prediction that GWAS results in intergenic regions pointed to actual functional elements:** ⚠️ **Partially correct.** Some intergenic GWAS hits indeed reflect functional regulatory elements, but methodological concerns about GWAS (confounding, linkage disequilibrium, statistical power) remained valid. Many claimed associations failed to replicate, and GWAS methodology evolved to address prior limitations.

• **Implicit prediction that large numbers of lincRNAs would prove biologically important:** ✗ **Overstated.** While a subset of lincRNAs have important functions, most do not show strong evidence of biological importance when disrupted. Research focus narrowed to specific, well-validated candidates rather than comprehensive investigation of all identified transcripts.

## 4. INTEREST

**Rating: 8/10**

This article captured a pivotal moment in genome biology where high-throughput data challenged fundamental assumptions about genetic function. The ENCODE debate and lincRNA expansion represented genuine conceptual shifts in understanding genome organization and regulation, with long-term implications for genomics research and therapeutic development, even if initial claims about functional genome fraction proved inflated.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20130701-corroboration-encode.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_