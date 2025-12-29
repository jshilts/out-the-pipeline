
https://www.science.org/content/blog-post/watson-and-pfizer
# Watson and Pfizer (December 2016)

## 1. SUMMARY

This article discusses the announcement of a partnership between Pfizer and IBM to use IBM's Watson platform for drug discovery in immuno-oncology research. Watson for Drug Discovery was described as a cloud-based platform using deep learning, natural language processing, and cognitive reasoning to analyze massive amounts of scientific literature—25 million abstracts, 1 million full-text articles, and 4 million patents—to identify new drug targets and potential drug indications.

The author expresses both support for the mission and significant skepticism about the implementation. While acknowledging the need for better literature-mining tools, the article raises four major concerns: (1) the prevalence of incorrect, sloppy, or fraudulent research in the biomedical literature that could corrupt the AI's conclusions; (2) the vast gaps in current biological understanding that make comprehensive modeling impossible; (3) the absence of negative results in published literature, which are crucial for machine learning but rarely reported; and (4) the risk of either underfitting (finding nothing new) or overfitting (generating spurious false positives), with limited useful territory in between. The author concludes with the observation that the ultimate test will be whether anything substantive emerges from the partnership.

## 2. HISTORY

The Pfizer-Watson partnership proved to be largely unsuccessful and was quietly discontinued. Despite significant investment and media attention around 2016-2017, **no FDA-approved drugs resulted from the collaboration**, and **no breakthrough drug candidates or validated targets emerged** from the platform in Pfizer's immuno-oncology pipeline.

By 2017-2018, reports began surfacing about IBM Watson Health struggling with commercial viability and producing unreliable recommendations. Internal documents and investigations revealed that Watson for Oncology often provided unsafe or incorrect treatment suggestions because it had been trained on synthetic data rather than real patient data. While this specifically referenced the oncology clinical decision product, it reflected broader issues with Watson's approach to medical AI.

In February 2022, IBM **sold Watson Health** to private equity firm Francisco Partners for approximately $1 billion—a significant writedown considering IBM had invested billions in acquisitions and development. The sale included Watson Health's data and analytics assets but notably did not generate the transformational impact on healthcare that had been promised.

**Pfizer has not reported any successful drug development outcomes** from the Watson collaboration. The company continued traditional drug discovery approaches and later invested in other AI partnerships and internal capabilities, suggesting the Watson experiment did not meet expectations. No major pharmaceutical companies subsequently adopted Watson as their primary drug discovery platform.

The broader field of AI in drug discovery continued to evolve, though largely through different approaches. Companies like DeepMind (with AlphaFold for protein folding) and specialized computational drug discovery firms demonstrated meaningful progress, but these successes came from **physics-based modeling, deep learning on molecular structures, and large-scale experimental data**—**not primarily from literature mining**. The vision of automatically extracting drug discovery insights from published papers has not materialized at scale as envisioned in 2016.

Public policy and research practices did not fundamentally change in response to this specific partnership, though research data sharing and reproducibility initiatives have continued, addressing some of the original concerns about literature quality.

## 3. PREDICTIONS

The article contained several explicit and implicit predictions about the Watson-Pfizer partnership and AI in drug discovery:

- **Prediction: The partnership would face fundamental barriers that press releases wouldn't solve**  
  **Outcome: CORRECT**. The collaboration produced no meaningful drug discovery outcomes and was ultimately abandoned. The fundamental barriers identified proved more significant than anticipated.

- **Prediction: Literature quality issues (incorrect data, fraud, poor methodology) would corrupt AI conclusions**  
  **Outcome: CORRECT**. Investigations of Watson Health revealed it produced unreliable medical advice, partly due to training on problematic data. The "garbage in, garbage out" principle applied.

- **Prediction: The "insufficient data" problem would be a major challenge**  
  **Outcome: CORRECT**. The complexity of biological systems and gaps in knowledge meant comprehensive modeling remained impossible. AI drug discovery successes came from more targeted problems with better datasets, not broad literature scanning.

- **Prediction: Negative results would be a missing element**  
  **Outcome: PARTIALLY CORRECT**. The field recognized this problem, with some initiatives to publish negative results emerging, but the fundamental asymmetry in published literature persisted and limited AI approaches.

- **Prediction: The gap between underfitting and overfitting would be narrow**  
  **Outcome: CORRECT**. Early AI drug discovery often struggled with either producing nothing useful or generating unmanageable numbers of false positives, supporting the author's concern about finding the right balance.

- **Prediction: We'd learn from this experiment's outcome, even if it failed**  
  **Outcome: CORRECT**. The Watson-Pfizer experience became a cautionary case study about overpromising AI capabilities and the importance of fundamental data quality.

- **Implicit prediction: Traditional drug discovery would continue to be necessary**  
  **Outcome: CORRECT**. Despite AI advances, pharmaceutical companies found that successful drug discovery required hybrid approaches combining AI with experimental validation, not pure AI literature mining.

## 4. INTEREST

Rating: **8/10**

This article demonstrated exceptional scientific and commercial foresight, correctly identifying fundamental barriers to AI drug discovery that the industry later confirmed through experience. It correctly predicted the failure of a highly-publicized partnership and addressed issues still highly relevant today concerning data quality and biological complexity. The combination of accurate predictions, clear reasoning, and sustained relevance to ongoing AI drug discovery efforts makes this remarkably prescient.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20161212-watson-and-pfizer.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_