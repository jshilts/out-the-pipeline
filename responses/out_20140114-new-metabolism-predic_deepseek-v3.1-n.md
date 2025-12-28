
https://www.science.org/content/blog-post/new-metabolism-predictor
# A New Metabolism Predictor (January 2014)

## 1. SUMMARY
The article discusses FAME (FAME), a new sites-of-metabolism predictor that uses a decision-tree approach trained on data from 20,000 known compounds. The software handles both Phase I and Phase II drug metabolism, addressing the critical challenge in small-molecule drug development where promising compounds are often metabolized by the liver before reaching therapeutic targets. The author, writing from a pharmaceutical industry perspective, introduces this tool as potentially valuable for medicinal chemists and pharmacokinetics (PK) researchers who routinely face metabolism challenges. The piece is framed as both an informational review and a community inquiry, with the author asking experienced practitioners about their real-world experiences with predictive metabolism software.

## 2. HISTORY

The period following the article's publication saw significant evolution in metabolism prediction tools and their role in drug discovery:

**Commercial metabolism prediction software landscape (2014-2024):** Several established platforms remained dominant, including Schrödinger's QikProp (later absorbed into broader platforms), Simulations Plus' ADMET Predictor, and Certara's MetaDrug and MetaSite. These tools evolved from decision-tree and rule-based approaches toward more sophisticated machine learning, QSAR models, and later deep learning architectures.

**Scientific methodology evolution:** The field shifted dramatically from classical decision-tree methods like those described for FAME toward ensemble methods, random forests, and eventually graph neural networks and transformer-based models for molecular property prediction. Studies in 2015-2020 increasingly demonstrated the limitations of small training datasets (20,000 compounds was modest even in 2014) compared to larger datasets and multi-task learning approaches.

**Metabolism prediction in pharmaceutical practice:** By 2020, metabolism prediction had become standard practice in early-stage drug discovery across major pharmaceutical companies. However, the field also recognized significant challenges: accurate prediction of metabolites remained difficult (typically 60-80% accuracy for major metabolites), and in vitro microsome/hepatocyte assays remained essential complements to computational predictions. No single software tool achieved dominance or eliminated the need for experimental validation.

**FAME's trajectory:** Evidence suggests FAME had limited commercial or academic impact after 2014. It is referenced in few subsequent publications, not listed among widely-used commercial platforms, and does not appear prominently in pharmaceutical company toolkits. The tool did not appear to gain significant market adoption compared to established or newly emerging competitors.

## 3. PREDICTIONS

- **Implicit prediction about metabolism software adoption:** The article assumes predictive metabolism software would become valuable for medicinal chemists and PK researchers. Reality: Such tools did become standard in drug discovery, but accuracy limitations meant they complemented rather than replaced experimental studies.
- **Implicit expectation that decision-tree approaches would be valuable:** FAME's decision-tree methodology was presented as potentially useful. Reality: Decision-tree methods were largely superseded by ensemble methods and neural networks in modern metabolism prediction.
- **Size of training data:** 20,000 compounds was presented as substantial in 2014. Reality: State-of-the-art models now train on hundreds of thousands to millions of compounds, and 20,000 compounds would be considered small by modern standards.

## 4. INTEREST
Rating: **4/10**

The article is moderately interesting as a snapshot of mid-2010s computational ADMET methodology, but it describes a specific tool that had limited subsequent impact and focuses on prediction methods that were already being superseded, making its long-term importance modest.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20140114-new-metabolism-predictor.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_