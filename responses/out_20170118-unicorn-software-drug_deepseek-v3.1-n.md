
https://www.science.org/content/blog-post/unicorn-software-drug-discovery
# Unicorn Software for Drug Discovery (January 2017)

## 1. SUMMARY

The article critiques the persistent hype around computational drug discovery software that promises to revolutionize virtual screening. The author uses a recent JACS paper on bromodomain enzymes as a case study, describing how researchers applied absolute binding free energy (ABFE) calculations to predict affinities of three ligands (RVX-OH, RVX-208, and bromosporine) across 22 bromodomain proteins.

The computational results showed mixed accuracy: for compounds with known crystal structures (RVX compounds), predictions were within 2 kcal/mol of experimental values, with about two-thirds within 1 kcal/mol. However, for bromosporine (without prior structural data), only one-third of predictions fell within 1 kcal/mol, with another third showing errors exceeding 30-fold in dissociation constants. The authors had to reparameterize sulfonamide groups to improve accuracy, highlighting the computational challenges even for common functional groups.

The article's central argument is that despite decades of effort, truly reliable "unicorn software" for drug discovery remains elusive, and anyone claiming otherwise is selling something. The author contrasts the computational chemist's optimism about incremental progress with the experimental medicinal chemist's continued need for physical assays and synthesis.

## 2. HISTORY

**Bromodomain Drug Development:**
The article mentions RVX-208 (resveratrol derivative) - this compound was being investigated for cardiovascular applications at the time. Subsequent development showed mixed results. RVX-208 (apabetalone) advanced through clinical trials for cardiovascular disease but ultimately failed to meet primary endpoints in major Phase 3 trials around 2019-2020. It did not receive FDA approval for its intended indications.

**Bromosporine:** The compound mentioned as a non-selective bromodomain inhibitor has remained primarily a research tool rather than a drug candidate, used in academic settings for studying bromodomain biology.

**BET Bromodomain Inhibitors:** This target class did see continued pharmaceutical interest after 2017. Several BET inhibitors entered clinical trials (e.g., molibresib, AZD5153, ABBV-744) for oncology applications, though most have faced challenges with toxicity or efficacy and none have achieved FDA approval as of 2024. The field validated the importance of bromodomain selectivity that the JACS paper was exploring.

**Computational Methods Evolution:** Free energy perturbation (FEP) and ABFE methods did see increased adoption in the pharmaceutical industry between 2017-2024. Companies like Schrödinger, OpenEye, and others commercialized more sophisticated platforms. However, the limitations described in the article largely persisted - these methods remain computationally expensive, require high-quality protein structures, and still need experimental validation. Major pharma companies use them as decision support tools rather than as standalone discovery engines.

**Drug Discovery Technology Companies:** No company has delivered the "unicorn software" described in the article. While companies like Atomwise, Exscientia, and others gained significant funding and attention for AI-driven drug discovery, their impact has been measured in specific projects and partnerships rather than transforming the entire discovery paradigm.

## 3. PREDICTIONS

• **"Anyone who tells you that we're there [with reliable virtual screening software] is trying to sell you something"** - This prediction proved largely accurate. While computational methods improved, no company delivered the complete virtual screening solution described in the article's opening dream scenario. AI drug discovery companies emerged with significant hype but faced the same fundamental challenges.

• **Implicit prediction that experimental synthesis and assays would remain necessary** - This prediction proved correct. Despite advances in computational chemistry, drug discovery still relies heavily on iterative cycles of design, synthesis, and testing. High-throughput synthesis and screening platforms remain central to pharmaceutical R&D.

• **Implicit prediction that computational accuracy would remain challenging for certain chemical groups** - This prediction held true. Issues like sulfonamide parameterization and the dependence on high-quality structural data continued to limit computational predictions. The search for better force fields and quantum mechanical methods remained active areas of research.

• **Implicit prediction about the difficulty of achieving selectivity predictions** - This proved accurate. As BET bromodomain inhibitors progressed, selectivity remained a major challenge contributing to clinical failures due to on-target toxicity.

## 4. INTEREST

Rating: **8/10**

This article demonstrates remarkable prescience about the persistent gap between computational chemistry promises and practical drug discovery reality. The skepticism about revolutionary software solutions proved well-founded, and the specific case study remained relevant as bromodomain inhibitor development unfolded over the subsequent seven years with mixed clinical success.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20170118-unicorn-software-drug-discovery.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_