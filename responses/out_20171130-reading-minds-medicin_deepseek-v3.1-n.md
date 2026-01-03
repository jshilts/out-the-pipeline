
https://www.science.org/content/blog-post/reading-minds-medicinal-chemists
# Reading the Minds of Medicinal Chemists (November 2017)

## 1. SUMMARY

The article critiques a press release announcing Chemistry.AI, a platform proposing to use EEG headsets to "read the minds" of medicinal chemists and capture their intuitive judgments about molecules' drug-like properties. The author, a medicinal chemist, expresses skepticism about the premise that experienced chemists can accurately distinguish good from bad molecules just by looking at their structures. While acknowledging that chemists develop useful pattern recognition—identifying likely solubility issues, metabolic liabilities, or structural motifs associated with certain target classes—the author emphasizes that these are probabilistic judgments prone to error, not reliable predictions. The real value lies in identifying the rare successes, not filtering the many expected failures. The article also references prior literature suggesting inconsistency in how chemists evaluate compounds, casting doubt on whether aggregating subjective preferences would yield robust predictive signals.

## 2. HISTORY

The proposed Chemistry.AI platform does not appear to have achieved significant adoption or commercial success. EPOC+ EEG devices from EMOTIV remain available and are used in research and brain-computer interface applications, but there is no evidence of widespread deployment for pharmaceutical drug screening or for decoding medicinal chemists' intuitions at scale. The approach—treating human experts' neural responses as a robust signal for AI training—did not become a mainstream methodology.

After the article's publication, AI and machine learning did grow substantially in drug discovery, but primarily along different paradigms:
- Deep learning for molecular property prediction and virtual screening focused on large experimental datasets rather than human neuro-feedback.
- Generative models and computational chemistry tools became widespread for de novo design, ADMET prediction, and synthesis planning.
- Pharmaceutical companies increasingly adopted computational platforms, but these rely on high-throughput data, physics-based modeling, and predictive algorithms trained on bioassay outcomes.

The vision of crowdsourcing chemists' "neurologically revealed preferences" via EEG did not translate into approved drugs, policy changes, or broadly adopted methods. The real-world impact of Chemistry.AI appears negligible, and drug discovery continued to depend heavily on running physical experiments, building predictive models from large datasets, and progressing compounds through empirical validation.

## 3. PREDICTIONS

- **Prediction by press release/company**: That machine learning coupled with medicinal chemists' EEG responses could revolutionize drug development.  
  **Outcome**: Not realized. The approach did not gain traction, and no successful drugs or widely adopted platforms emerged from this methodology.

- **Prediction (implied skepticism)**: That experienced medicinal chemists cannot reliably distinguish good from bad molecules just by looking at structure.  
  **Outcome**: Consistent with subsequent evidence. While experienced chemists retain valuable qualitative judgment about liabilities and prior art, criteria for "drug-likeness" and lead optimization depend heavily on quantitative experimental data and predictive algorithms trained on large datasets.

- **Prediction (broader implication)**: That chemists' judgments of compounds are individual and inconsistent, and attempts to aggregate them via intuition or neurological readouts might be unreliable.  
  **Outcome**: Largely accurate. The field's progress in AI-driven drug discovery has favored data-driven models (e.g., graph neural networks, transformers) over expert-opinion aggregation, as the latter risks biases and lacks scalability.

## 4. INTEREST

Rating: **6/10**

The article captures a real tension between expert intuition and AI in drug discovery, and it critiques a plausible-but-flawed approach with thoughtful skepticism. However, the project it discusses did not shape the field, so its long-term importance is modest.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20171130-reading-minds-medicinal-chemists.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_