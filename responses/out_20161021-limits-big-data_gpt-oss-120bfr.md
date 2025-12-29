
https://www.science.org/content/blog-post/limits-big-data
# The Limits of Big Data (Oct 2016)

## 1. SUMMARY  
The Wired piece critiques the hype surrounding “big‑data” genomics by focusing on Eric Schadt’s “Resilience Project.” Schadt’s team had assembled ~600 000 whole‑genome sequences from a patchwork of sources (23andMe, BGI, Broad Institute, etc.) and searched for individuals who carried disease‑causing mutations yet remained healthy. The effort uncovered only eight putative “resilient” cases out of 170 diseases, leading the authors to conclude that the sample size was far too small. Schadt argued that a truly useful dataset would need on the order of **10 million** genomes, and he founded the company **Sema4** to pursue that scale. The article stresses that even if such a dataset were gathered, turning the data into cures is non‑trivial: protective variants may be rare, polygenic, or environmentally mediated, and many disease‑relevant proteins remain “undruggable.” In short, the author warns that massive data collection alone will not magically produce a “cure for cancer” or other breakthroughs.

## 2. HISTORY  
**What actually happened after 2016?**

* **Sema4’s trajectory** – Sema4 grew rapidly as a clinical‑genomics company, raising > $300 M and obtaining CLIA‑certified laboratory status. It launched FDA‑cleared tests for hereditary cancer panels, newborn screening, and COVID‑19 diagnostics. In 2022, data‑analytics firm **Tempus** acquired Sema4 for roughly $1.5 B, integrating its genomic data platform into a broader precision‑medicine ecosystem. Sema4 never built a single 10 M‑genome repository; instead it leveraged partnerships (e.g., with health systems, biobanks) to access large, but fragmented, datasets.

* **The Resilience Project** – The original effort published a few papers describing protective loss‑of‑function variants (e.g., in **PCSK9**, **ANGPTL3**, **APOB**) that informed drug development. However, the project did not expand to millions of genomes and was effectively superseded by larger population biobanks. No “miracle” protective mutation that blocks cancer or Alzheimer’s emerged from the Resilience cohort.

* **Large‑scale biobanks** – Since 2016, several national and commercial initiatives have approached the multi‑million scale:  
  * **UK Biobank** now hosts ~500 k whole‑genome sequences (2023 release).  
  * **All of Us Research Program** (US) aims for 1 M participants, with > 300 k genomes sequenced as of 2024.  
  * **China’s National Genomics Data Center** announced a target of 100 M genomes by 2030; the **China Kadoorie Biobank** and **China Precision Medicine Initiative** have already contributed > 10 M samples (mostly genotyping, some sequencing).  
  * **FinnGen**, **Estonian Biobank**, and **Million Veteran Program** each exceed 200 k–500 k sequenced genomes.

* **From data to therapeutics** – The “big‑data → drug” pipeline has produced concrete successes, but not the sweeping cures imagined in the article:  
  * **PCSK9 inhibitors** (evolocumab, alirocumab) were developed after loss‑of‑function variants were identified in population sequencing studies.  
  * **ANGPTL3** and **APOB** loss‑of‑function findings have led to antisense and monoclonal‑antibody drugs now in late‑stage trials.  
  * Polygenic risk scores (PRS) for breast cancer, coronary artery disease, and type‑2 diabetes have entered limited clinical use, primarily for risk stratification rather than cure.  

* **Cancer and Alzheimer’s** – No single protective germline variant that confers broad resistance to cancer or Alzheimer’s has been validated. Large‑scale GWAS and sequencing have clarified many risk loci, but therapeutic translation remains incremental.  

* **Policy and data‑sharing** – The challenges of consent, re‑contact, and data interoperability highlighted in the article have been partially addressed by the **GA4GH** framework, the **FAIR** data principles, and new “dynamic consent” platforms (e.g., **MyDataHelix**, **All of Us**). Nonetheless, fragmented consent still limits the ability to re‑engage participants at scale.

Overall, the field has moved toward **larger, more harmonized biobanks** and **integrated analytics**, but the scale envisioned (10 M genomes in a single, freely accessible repository) remains a work in progress, and the direct translation to cures has been modest.

## 3. PREDICTIONS  

| Prediction in the article (or implied) | What actually happened |
|----------------------------------------|------------------------|
| **~10 million genomes are needed to find enough resilient individuals** | As of 2025, no single dataset reaches 10 M whole‑genome sequences. The closest are distributed across multiple biobanks (e.g., China’s initiatives). The need for tens of millions is still cited in the literature, but the field relies on meta‑analyses across cohorts rather than a single monolithic database. |
| **Sema4 will build the data infrastructure and become a major player** | Sema4 became a successful clinical‑genomics company and was acquired by Tempus in 2022. It never amassed a 10 M‑genome internal cohort but leveraged external data through partnerships. |
| **Finding protective mutations will quickly point to druggable targets and lead to cures (e.g., cancer, Alzheimer’s)** | Protective loss‑of‑function variants have indeed yielded drug targets (PCSK9, ANGPTL3), but these are for cardiovascular disease, not cancer or Alzheimer’s. No cancer‑curing or Alzheimer‑preventing therapies have emerged from the resilience‑type approach. |
| **Big data collection is the main bottleneck; once data are gathered, analysis will be straightforward** | Data collection remains a bottleneck (consent, diversity, re‑contact). Moreover, analytical challenges (population stratification, polygenicity, functional validation) have proven equally demanding. |
| **The “Resilience Project” will identify many healthy carriers of disease‑causing mutations** | The project identified only a handful of candidates and did not scale up. Larger biobanks have found additional “resilient” individuals, but they are rare and often explained by incomplete penetrance rather than a single protective allele. |

## 4. INTEREST  
**Rating: 7/10** – The article is a thoughtful, early‑skeptical take on big‑data genomics that anticipated many real‑world hurdles; its discussion of consent, data integration, and the limits of sheer scale remains highly relevant, though the specific “10 M genome” vision has not yet materialized.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20161021-limits-big-data.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_