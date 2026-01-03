
https://www.science.org/content/blog-post/objections-some-drug-discovery-ai
# Objections to (Some) Drug Discovery AI (January 2018)

## 1. SUMMARY

This commentary by Derek Lowe discusses Mostapha Benhenda's critical analysis claiming that AI in drug discovery was overhyped. The article examines three specific examples of AI applications in drug discovery that Benhenda found problematic. First, an AstraZeneca paper using neural networks to generate molecular structures for screening - criticized for focusing on how AI-generated structures differed from natural molecules rather than ensuring diversity among generated molecules, which is crucial for effective virtual screening libraries.

Second, a Harvard paper using Generative Adversarial Networks (GANs) where one network generates structures and another critiques them. Benhenda's analysis suggested the critique network spent most of its time penalizing outputs rather than constructively improving them, and that insufficient comparison occurred between generated molecules.

Third, work from Vijay Pande's group at Stanford (related to MoleculeNet and DeepChem) was criticized for lacking depth and appearing to promote a particular data format/standard over potentially superior alternatives. The author notes Benhenda had commercial interests through his company Startcrowd but presents the critiques as independently evaluable technical objections worthy of discussion by field practitioners.

## 2. HISTORY

The skepticism expressed in this 2018 article reflected genuine challenges in the AI drug discovery field at that time, though the landscape has evolved significantly since publication.

**MoleculeNet and DeepChem**: These frameworks continued to develop and gained substantial adoption in the research community. MoleculeNet became a widely-used benchmark dataset, and DeepChem evolved into a mature open-source framework maintained by an active community. However, they did not become the exclusive standards Benhenda worried about - alternative frameworks and approaches continued to flourish.

**Generative models for molecules**: The GAN approach discussed in the Harvard paper represented early work in what became a very active research area. Subsequent years saw significant methodological advances beyond GANs, including variational autoencoders (VAEs), flow-based models, and transformer-based approaches for molecular generation. These later methods generally addressed the diversity and quality issues raised in the original critiques.

**Industry adoption**: AI drug discovery companies proliferated post-2018. Notable examples include Atomwise, Exscientia, Recursion Pharmaceuticals, Insilico Medicine, and many others. These companies moved beyond academic proof-of-concept studies to establish real drug discovery pipelines and partnerships with major pharmaceutical companies.

**Clinical translation**: Progress toward approved drugs has been slower than early hype suggested. While numerous AI-discovered drug candidates have entered clinical trials, most remain in early phases as of 2024. Exscientia's DSP-1181 (for OCD) became one of the first AI-designed molecules to enter clinical trials in 2020, but development was discontinued. Recursion Pharmaceuticals has several candidates in clinical trials. The timeline from AI design to approved drug typically exceeds a decade, so many programs initiated around 2018 are still progressing through development stages.

**Tool adoption**: AI/ML tools are now standard in drug discovery workflows at most pharmaceutical companies, but typically as augmentation tools for medicinal chemists rather than fully autonomous discovery engines. Virtual screening, QSAR modeling, and molecular property prediction have seen widespread integration.

## 3. PREDICTIONS

The article didn't make explicit forward-looking predictions, but rather questioned whether the specific AI approaches being criticized would prove valuable. However, we can evaluate the implicit concerns and expectations:

• **Diversity in generated molecular libraries**: The critique of AstraZeneca's neural network approach for not ensuring sufficient diversity among generated molecules was valid. Later work in generative molecular design has generally incorporated explicit diversity metrics and sampling strategies to address this concern. Modern generative models are indeed used to produce diverse screening libraries.

• **GAN effectiveness for molecule generation**: The skepticism about the Harvard GAN approach was largely borne out. While GANs continued to be explored for molecular generation, they proved less dominant than alternative approaches like VAEs and autoregressive models. The specific issues Benhenda identified about training dynamics and output quality were real limitations.

• **Standard dominance of specific frameworks**: DeepChem and MoleculeNet did not become exclusionary monopolies, and the field maintained multiple competing frameworks. This was generally healthy for research progress, though it did create some fragmentation.

• **Broader AI impact on drug discovery**: The article's cautious tone about AI hype was appropriate. While AI has become deeply integrated into drug discovery workflows, the revolution has been more gradual and evolutionary than some 2018-era predictions suggested. Success stories exist, but AI has primarily enhanced rather than replaced traditional medicinal chemistry expertise.

## 4. INTEREST

Rating: **7/10**

The article retains substantial historical interest because it captured a moment when the AI drug discovery field was transitioning from early hype toward more rigorous evaluation. It highlighted legitimate technical concerns that proved prescient, while the broader field ultimately matured to address many of these issues through improved methodologies.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20180110-objections-some-drug-discovery-ai.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_