
https://www.science.org/content/blog-post/mutants-among-us
# Mutants Among Us (May 2016)

## 1. SUMMARY  
The article reflects on the legacy of the Human Genome Project, pointing out that the public often conflates “the human genome” with a single reference sequence, while also believing that every individual’s DNA is completely unique. It argues that the real scientific promise lies in the space between these ideas – the massive, population‑scale sequencing now possible.  

The author highlights a 2016 Nature Biotechnology paper that screened ~589 000 individuals for known disease‑causing loss‑of‑function (LoF) mutations and then searched for people who carried such mutations yet showed no clinical signs of the associated Mendelian disease. After a stringent filtering pipeline, the study reported 13 “resilient” individuals who appeared to have escaped their genetic destiny. However, the authors could not re‑contact any of them because most of the source cohorts lacked a re‑contact clause in their consent forms, leaving the findings unvalidated and the biological mechanisms unexplored.

## 2. HISTORY  
**Follow‑up studies and larger datasets**  
- **The Resilience Project (2018)**, led by the MacArthur lab, explicitly built on the 2016 paper’s concept. Using exome data from > 30 000 individuals (later expanded to > 100 000), the team identified dozens of candidate resilient carriers for dozens of Mendelian disorders. They succeeded in re‑contacting a subset, confirming a few true “resilient” cases (e.g., carriers of pathogenic *HBB* variants without anemia). The project demonstrated that with proper consent and a dedicated outreach pipeline, validation is feasible.  
- **UK Biobank (ongoing)** and **All of Us (US)** incorporated re‑contact provisions from their inception, allowing researchers to invite participants for phenotypic follow‑up. Analyses of > 500 000 UK Biobank genomes have now catalogued > 4 000 homozygous LoF variants, many in genes previously thought essential, and have linked several to protective phenotypes (e.g., *ANGPTL3* LoF with lower LDL‑C).  
- **gnomAD v3 (2020)** aggregated > 125 000 whole‑genome sequences, providing a public reference for LoF allele frequencies and facilitating the identification of “human knockouts” across diverse ancestries.  

**Therapeutic translation**  
- The article’s mention of PCSK9 loss‑of‑function as a “reasonably good” outcome proved prescient. PCSK9 inhibitors (alirocumab, evolocumab) received FDA approval in 2015 and have since been prescribed to millions, confirming that human genetics can de‑risk drug targets.  
- Similar trajectories followed for *ANGPTL3* (evinacumab, approved 2021 for homozygous familial hypercholesterolemia) and *APOC3* (volanesorsen, approved 2019 for familial chylomicronemia). These drugs were developed after population‑scale LoF studies highlighted the protective effects of naturally occurring knockouts.  

**Consent and data‑sharing policies**  
- The consent‑form obstacle highlighted in the 2016 paper spurred policy changes. The **NIH Genomic Data Sharing (GDS) Policy** (updated 2018) now requires explicit provisions for re‑contact where feasible.  
- Commercial biobanks (e.g., 23andMe, AncestryDNA) have introduced optional “research participation” modules that allow participants to be re‑contacted for follow‑up studies, leading to several successful genotype‑phenotype validation projects.  

**Scientific impact**  
- The concept of “human knockouts” has become a standard term in genetics literature. Large‑scale CRISPR screens in cell lines and model organisms now routinely complement human LoF observations, creating a bidirectional pipeline from human genetics to functional validation.  
- Nonetheless, the number of truly resilient individuals remains small; most homozygous LoF carriers exhibit at least mild phenotypic effects, underscoring the complexity of genetic buffering and environmental interactions.  

## 3. PREDICTIONS  

| Prediction (from article or implied) | Outcome |
|---|---|
| **Massive sequencing will uncover many “resilient” individuals** | Partially true. Large biobanks have identified dozens of candidates, but true resilience (no phenotype despite a pathogenic genotype) remains rare and often requires deep phenotyping to confirm. |
| **These resilient cases will quickly reveal novel therapeutic pathways** | Mixed result. Some pathways (PCSK9, ANGPTL3, APOC3) were already known, and their drug development proceeded independently of the 2016 study. New pathways from resilient individuals have been slower to translate, largely because few robust cases have been validated. |
| **Re‑contact issues will be a major barrier** | Confirmed. The 2016 paper’s inability to follow up sparked policy reforms, but many legacy cohorts still lack re‑contact clauses, limiting retrospective validation. New cohorts now routinely include re‑contact consent, reducing the barrier for future work. |
| **Sequencing costs will drop enough to enable whole‑genome sequencing of half‑a‑million people** | Realized. By 2023, several projects (UK Biobank, All of Us) have generated > 500 000 whole‑genome datasets at < $100 per genome, fulfilling the cost‑trajectory expectation. |
| **The public will develop a nuanced view of “one genome vs many”** | Unclear. Public understanding of genetic diversity has improved (e.g., media coverage of “genetic ancestry” and “personal genomics”), but misconceptions persist; surveys in 2022 still show a majority believing that a single “reference genome” represents all humans. |

## 4. INTEREST  
**Rating: 7/10** – The article captures a pivotal moment when population genomics moved from reference sequencing to large‑scale phenotype‑genotype mining, and it correctly anticipated consent hurdles that shaped subsequent biobank design. Its specific focus on resilient individuals remains a compelling, though still emerging, research niche.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160510-mutants-among-us.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_