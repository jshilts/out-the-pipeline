
https://www.science.org/content/blog-post/hard-look-liquid-biopsies
# A Hard Look At Liquid Biopsies (January 2018)

## 1. SUMMARY

The article examines a landmark Science paper on CancerSEEK, a multicancer early detection (MCED) blood test that combined 16 DNA markers and 8 protein biomarkers to detect eight cancer types (ovarian, liver, stomach, pancreatic, esophageal, colorectal, lung, and breast). The test showed variable sensitivity by cancer type—over 95% for ovarian and liver cancers but only ~30% for breast cancer—while demonstrating a 1% false positive rate in healthy controls. Critically, CancerSEEK detected only 43% of Stage I cancers overall, raising concerns about its real-world utility for early detection.

The author highlights a planned $50 million, five-year study involving 50,000 women aged 65-75, then performs sobering calculations showing that even with two consecutive positive tests, the approach would miss ~63% of actual cancers while generating significant false alarms in healthy individuals. Most importantly, the article raises fundamental questions about overdiagnosis and overtreatment—whether detecting indolent cancers would lead to unnecessary interventions that harm patients without extending life, noting that conventional cancer screening benefits are often overstated and measured by disease-specific rather than overall mortality.

## 2. HISTORY

The CancerSEEK study published in Science marked the beginning of intense commercial and academic development of liquid biopsy technologies, though the field has taken longer to mature than initially hoped.

**Clinical Development and Commercial Landscape:**
Multiple companies have advanced MCED tests, with Grail's Galleri test (acquired by Illumina) becoming the most prominent. Galleri uses methylation patterns rather than the protein/DNA combination in CancerSEEK and claims detection of over 50 cancer types. However, as of 2024, no MCED test has received FDA approval for screening asymptomatic populations—they remain available only through prescriptions or clinical studies.

**Real-World Evidence:**
Large prospective studies have been initiated, including Grail's PATHFINDER study (published 2021) involving over 6,600 participants. Results showed that among 6,621 participants, 92 had positive MCED tests, leading to cancer diagnoses in 35 individuals (38% positive predictive value). However, 57 participants with positive tests had extensive workups showing no cancer. The study confirmed the critical challenge identified in the original article: false positives drive costly and stressful follow-up evaluations.

The NHS in England launched the largest real-world evaluation in 2021, planning to enroll 140,000 participants to better understand MCED test performance and clinical utility. Interim results continue to show the tension between detection sensitivity and specificity that the 2018 article highlighted.

**Approved Applications:**
Liquid biopsy has found meaningful clinical adoption in **monitoring established cancers** rather than screening. FDA-approved tests like Guardant360 CDx and FoundationOne Liquid CDx are widely used for:
- Identifying targetable mutations in advanced cancer patients
- Tracking treatment response through circulating tumor DNA
- Detecting minimal residual disease after surgery

These applications avoid the overdiagnosis problem because they're used in patients already diagnosed with cancer, where treatment decisions depend on accurate molecular profiling.

**Regulatory and Coverage Status:**
The FDA has taken a cautious approach to MCED screening tests, requiring large clinical trials demonstrating actual mortality reduction (overall, not disease-specific) before approval. No test has yet met this bar. Medicare and private insurers do not cover MCED screening, limiting access to patients willing to pay out-of-pocket (~$900-1,000 for Galleri).

**Scientific Evolution:**
Research has shifted toward more sophisticated approaches than CancerSEEK's protein/DNA panel. Current approaches emphasize:
- DNA methylation patterns (epigenetic signatures)
- Fragmentomics (DNA fragment size and patterns)
- Multi-analyte integration with machine learning

However, the fundamental statistical challenges remain: rare diseases create Bayes' theorem problems where even highly specific tests generate more false positives than true positives in low-prevalence populations.

## 3. PREDICTIONS

**Prediction: CancerSEEK's planned five-year study would reveal major practical challenges**
- **Accuracy**: Correct. The PATHFINDER and similar studies confirmed exactly the statistical issues predicted. Even with improved sensitivity (~40-50% for Stage I cancers in current tests versus CancerSEEK's 43%), false positives substantially outnumber true positives in screening populations, creating the predicted cascade of anxiety, costs, and potential overdiagnosis.

**Prediction: The test would miss ~63% of actual cancers while generating many false alarms**
- **Accuracy**: Partially correct directionally, though specific numbers evolved. Modern MCED tests have slightly improved sensitivity (detecting ~50-60% of Stage I cancers), but the false positive/false negative tradeoff persists as predicted. The NHS study's early results showed 38% positive predictive value—meaning ~62% of positive tests were false alarms, closely matching the article's concerns.

**Prediction: Overdiagnosis and overtreatment would become major problems**
- **Accuracy**: Correct, though this remains a theoretical concern rather than proven harm since MCED tests aren't yet widely deployed for screening. The fundamental issue—that MCED might detect indolent or slow-growing cancers that wouldn't cause morbidity—remains unresolved and is a primary reason for regulatory caution.

**Prediction: CancerSEEK wouldn't be the definitive screening solution**
- **Accuracy**: Correct. CancerSEEK itself did not become a commercial product. The field evolved toward different technological approaches (methylation-based rather than protein/mutation-based), and no FDA-approved MCED screening test exists as of 2024.

**Implicit prediction: Liquid biopsy would find value in monitoring, not screening**
- **Accuracy**: Prescient. The most successful liquid biopsy applications have been monitoring known cancers—detecting recurrence, tracking treatment response, and identifying targetable mutations. These applications avoid the prevalence/Bayes' theorem problem because patients already have diagnosed cancer, making test interpretation more straightforward.

## 4. INTEREST

Rating: **8/10**

This article demonstrated remarkable prescience about liquid biopsy development, correctly identifying the fundamental statistical challenges (Bayes' theorem in low-prevalence screening), overdiagnosis concerns, and the gap between technical feasibility and clinical utility—issues that have dominated the following six years of research. Its clear-eyed analysis of a "promising" technology provided exactly the scientific rigor and long-term perspective needed in biotechnology journalism.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20180122-hard-look-liquid-biopsies.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_