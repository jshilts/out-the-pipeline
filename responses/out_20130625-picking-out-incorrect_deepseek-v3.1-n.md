
https://www.science.org/content/blog-post/picking-out-incorrect-natural-products
# Picking Out Incorrect Natural Products (June 25, 2013)

## 1. SUMMARY

The article discusses a new computational method proposed to identify incorrectly assigned chemical structures of natural products. Historically, incorrect structure assignments occasionally occurred, sometimes discovered only after chemists went through the laborious process of total synthesis (a motivation even noted by R. B. Woodward). The method described in the linked paper employed carbon-13 NMR spectroscopy combined with artificial neural networks, trained on a set of 200 natural products. Rather than confirming that a proposed structure is definitively correct, the tool would flag structures with inconsistencies, functioning as a screening filter to catch likely misassignments before synthesis began. The article suggests this could motivate chemists to tackle misassigned compounds synthetically and propose corrections, potentially becoming a useful resource for natural products chemistry.

## 2. HISTORY

Computational NMR prediction and structure verification tools became more widespread in natural products and medicinal chemistry labs over the subsequent decade. While I cannot confirm the specific impact of the described NMR-based neural network, the underlying goal of catching misassignments before synthesis proved valuable. Misassigned natural products remained a persistent problem; for example, a 2016 reassessment of diterpene natural products flagged many structures as questionable based on computed NMR shifts. Methods leveraging density functional theory (DFT) calculations for NMR prediction as well as machine-learning and database-matching tools gained broader adoption. Commercial software packages (e.g., Advanced Chemistry Development, Mestrelab) increasingly incorporated such checks. Wider adoption enabled more reliable structure verification pipelines and likely reduced resource waste from synthesizing incorrectly assigned targets. Still, misassignments continued to be reported in the literature thereafter, and computational methods served as adjuncts rather than replacements for careful experimental validation.

## 3. PREDICTIONS

**Predictions mentioned:**
- Groups would be motivated to pursue synthetically misassigned compounds to revise the structure if they could propose believable alternatives.
- The tool might be less effective for extremely complex marine toxins with exceptionally large or intricate structures.

**How the predictions compared to reality:**
- Corrective total syntheses to revise misassigned structures did occur repeatedly post-2013 and became a recognized niche of natural products chemistry. Computational tools—including NMR prediction—lowered the barrier to proposing alternatives and selecting synthetic targets.
- For highly complex marine natural products, computational prediction remained challenging, often requiring careful integration of experiment, DFT calculations, and stepwise verification via synthesis or other methods. The article's cautious assessment proved reasonable: complexity frequently demanded multiple lines of evidence beyond a single neural-network screen.

## 4. INTEREST

Rating: **6/10**

The article highlights a practical computational tool that contributed to improved quality control in natural products chemistry, reflecting broader trends toward automation and machine learning in structure verification; interest is moderate because the approach became part of a wider toolkit rather than a transformative breakthrough.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20130625-picking-out-incorrect-natural-products.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_