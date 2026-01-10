
https://www.science.org/content/blog-post/evolving-enzymes-let-em-rip
# Evolving Enzymes: Let 'Em Rip (July 2013)

## 1. SUMMARY

This commentary discusses the field of enzyme engineering, focusing on the interplay between computational enzyme design and directed evolution (random mutations plus selection). The author highlights a new paper from University of Washington and ETH Zürich that evolved an improved retro-aldolase enzyme.

The researchers started with a computationally designed retro-aldolase that already showed 15,000× rate enhancement but was still far from natural enzyme performance. Through multiple rounds of random mutagenesis (error-prone PCR, DNA shuffling) and screening, they achieved a variant over 4,000× faster than the original. Surprisingly, X-ray crystallography revealed that the active site had completely changed from the computationally designed architecture—a new substrate-binding pocket formed and a newly acquired lysine became the catalytic residue, suggesting the original design mechanism was completely replaced rather than refined.

## 2. HISTORY

Following this 2013 article, directed enzyme evolution continued advancing rapidly. The field's growth was catalyzed by several key developments:

**Methodological advances**: High-throughput screening technologies improved significantly, enabling the "quickly run the random-mutation process" that the article contemplated. Platforms like droplet microfluidics and automation reduced screening time/cost, making directed evolution more accessible.

**Commercial success**: Companies specializing in enzyme evolution (such as Codexis, which the article referenced indirectly through David Baker's work) continued developing enzymes for pharmaceutical intermediates, specialty chemicals, and other applications. For example, Codexis supported development of enzymes for drugs like sitagliptin and atorvastatin.

**Broader adoption**: Academic labs increasingly adopted structure-guided approaches combined with directed evolution for enzyme engineering. The strategy illustrated in the Nature Chemical Biology paper—design, then evolve, with results diverging from design—became a standard paradigm.

**API and drug development impact**: Evolved enzymes found applications in manufacturing pharmaceutical intermediates, some enabling more sustainable or cost-effective synthetic routes, though specific approval details and timelines would require source access to confirm.

**Technology maturation**: Machine learning began complementing directed evolution by predicting mutational effects, reducing screening burden while still leveraging evolutionary discovery of unexpected solutions.

## 3. PREDICTIONS

• **Prediction**: Computational design might become less important if random mutation/screening could be accelerated.
  - **Outcome**: Computational design still plays an important role but increasingly focuses on generating starting points and hypotheses rather than final catalysts. The combination approach—design plus evolution—remains the gold standard, however, random mutagenesis has become more efficient through improved screening methods, automation, and machine learning guidance.

• **Prediction**: Natural enzymes achieve specific changes through mechanistic competition between active site residues that could be replicated.
  - **Outcome**: This insight proved prescient. The unexpected mechanistic divergence seen in the retro-aldolase study became recognized as a common occurrence (not all design mechanisms are evolutionarily stable), and researchers now intentionally design for evolvability and are less surprised when evolutionary trajectories deviate from computational predictions.

• **Implicit prediction**: "We're usually not smart enough to purposefully tweak things every time" – suggesting successful projects need both design and evolution.
  - **Outcome**: Confirmed. Even with advances in computational methods (like deep learning structure prediction), rational design alone rarely achieves natural enzyme-level performance. Directed evolution remains indispensable for identifying non-obvious solutions and optimizing activity.

## 4. INTEREST

Rating: **6/10**

The article captures a meaningful example of enzyme engineering and offers insights about design/evolution interplay, but the topic is relatively niche and more of a technical methodological discussion than a major biotechnology breakthrough with broad long-term importance.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20130731-evolving-enzymes-let-em-rip.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_