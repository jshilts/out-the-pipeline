
https://www.science.org/content/blog-post/simulation-and-understanding
# Simulation and Understanding (November 2019)

## 1. SUMMARY

This article reviews a three-part essay by Roald Hoffmann and Jean-Paul Malrieu in *Angewandte Chemie* about artificial intelligence and machine learning in chemistry research. The central thesis draws from René Thom's aphorism: "To predict is not to explain." The authors examine the distinction between simulation/modeling (broadly including numerical approximation, ML, and AI) and true scientific understanding. They place theory, simulation, and understanding at three vertices of a conceptual triangle, emphasizing that experimental data alone are "mute" without interpretation.

The article highlights concerns that AI hype could demote theory to "biased stuff that people fumbled along with before they had cool software." True understanding is framed as a human cognitive state—being able to teach or explain a concept to bring another person to the same level of comprehension. The piece uses Euclid's proof of infinite primes as an exemplar of understanding: a clear chain of reasoning that allows one to "see it, feel it" rather than merely accept computed results.

The authors discuss a neural network that, when fed astronomical data about Mars's retrograde motion, derived heliocentric equations similar to Copernicus's model. However, they stress that "nothing was understood until a human looked at the output"—the software produced correct formulas but lacked comprehension. Historical epicycle models could predict planetary positions accurately while being fundamentally wrong about cosmology, illustrating how simulation can get "right numbers for wrong reasons."

## 2. HISTORY

Since November 2019, the AI/ML landscape has evolved dramatically, but the core tension between prediction and explanation remains unresolved and arguably more relevant than ever.

**Scientific applications**: AI/ML has achieved remarkable predictive success in scientific domains, yet the interpretability gap persists. AlphaFold2 (2020) revolutionized protein structure prediction with unprecedented accuracy, but the models do not provide mechanistic understanding of folding pathways or energetics—they predict structures without explaining the underlying biophysics. Similarly, large language models and transformer architectures now assist in drug discovery and materials science, screening vast chemical spaces and generating novel molecules, yet their decision-making processes often remain opaque "black boxes."

**The interpretability crisis deepened**: Rather than receding, the problem of AI opacity has intensified. Neural networks in scientific applications frequently achieve superhuman performance on specific tasks while offering minimal insight into causal mechanisms. Explainable AI (XAI) has emerged as a subfield attempting to address this, but fundamental tensions remain between model complexity and interpretability—the most accurate models tend to be the least transparent.

**Scientific practice transformed**: Hoffmann and Malrieu's prediction that "human theoreticians will move up a meta-level" has materialized in some domains. Computational methods are now indispensable across chemistry, biology, and physics, not as replacements for theory but as collaborators. However, the division of labor remains: AI handles pattern recognition and prediction at scale, while human scientists formulate hypotheses, design experiments, and seek explanatory frameworks. The "shut up and calculate" ethos has if anything strengthened in many computational fields, with pragmatic focus on predictive power often outpacing theoretical understanding.

**No resolution on AI "understanding"**: Searle's Chinese Room problem remains a live philosophical debate. Large language models now generate syntactically sophisticated scientific text, but whether they possess semantic understanding or merely sophisticated pattern matching remains contested. The Mars retrograde motion example from 2019 presaged current issues: AI can rediscover known scientific laws from data, but whether it can generate genuinely novel explanatory theories remains unproven.

## 3. PREDICTIONS

The article and the essays it reviewed made several explicit and implicit predictions:

• **"Human theoreticians will move up a meta-level"**  
**Outcome**: Partially realized. Computational tools are now integral to theory-building across sciences, but human scientists remain central to hypothesis generation and explanatory frameworks. The predicted meta-level shift is incomplete—AI assists rather than replaces theoretical work.

• **"The wave of AI... Let's stop fighting and start swimming"**  
**Outcome**: Largely accurate. Scientific communities have broadly integrated ML/AI methods rather than resisting them. However, substantive debates continue about appropriate use cases, validation standards, and the epistemological status of AI-generated results.

• **Prediction vs. explanation dichotomy would persist**  
**Outcome**: Confirmed. The gap between predictive success and explanatory insight has widened. AlphaFold exemplifies this: revolutionary predictive tool, minimal explanatory power regarding protein folding mechanisms.

• **Simulations getting "right numbers for wrong reasons" would remain problematic**  
**Outcome**: Accurate prediction. Model brittleness, adversarial vulnerabilities, and out-of-distribution failures continue to plague ML systems. The epicycle analogy remains apt—complex models can achieve high accuracy while encoding spurious correlations or faulty causal assumptions.

• **AI would not achieve genuine "understanding" soon**  
**Outcome**: Correct so far. Despite dramatic advances in LLM capabilities, whether any current AI system possesses semantic understanding versus sophisticated pattern matching remains philosophically and empirically unresolved.

## 4. INTEREST

Rating: **8/10**

This article proved prescient in identifying enduring tensions between predictive AI and scientific explanation that have only intensified. It articulated fundamental epistemological questions that remain central to AI integration across sciences, making it more relevant today than when written.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20191113-simulation-and-understanding.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_