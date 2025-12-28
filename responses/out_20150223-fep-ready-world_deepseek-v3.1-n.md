
https://www.science.org/content/blog-post/fep-ready-world
# Is FEP Ready For the World? (February 2015)

## 1. SUMMARY

The article discusses a 2015 paper by researchers from Schrödinger, Nimbus, Columbia, Yale, and UC-Irvine claiming significant advances in free energy perturbation (FEP) calculations for drug discovery. The authors reported an FEP protocol that could accurately predict binding affinities across over 200 ligands and 10 diverse drug targets, with most predictions within 1 kcal/mol of experimental values. The method incorporated improved force fields, better sampling algorithms, increased computing power powered by GPUs, and automated workflows. Two prospective validation studies on IRAK4 and TYK2 showed similar accuracy. The authors positioned FEP not as a replacement for medicinal chemists, but as a tool to guide synthetic chemistry decisions, particularly for evaluating high-risk, synthetically challenging molecules. The article frames this as a potential "tipping point" for computational drug design.

## 2. HISTORY

FEP methodology has indeed become widely adopted in pharmaceutical drug discovery since 2015, representing one of the more successful translations of computational chemistry into routine industrial practice:

**Commercial adoption**: Schrödinger's FEP+ platform, based on the methodology described in the 2015 paper, has been widely adopted across the pharmaceutical industry. Major pharmaceutical companies including Pfizer, Novartis, Merck, Roche, and Bristol-Myers Squibb have integrated FEP into their discovery workflows.

**Methodological advances**: The field has moved beyond the initial 200-ligand validation to much larger prospective applications. Subsequent publications have demonstrated FEP predictions across thousands of compounds in industrial settings. Accuracy has remained generally consistent with the 2015 benchmarks (typically within 1-2 kcal/mol for well-behaved systems).

**Integration into drug discovery**: Rather than replacing medicinal chemists as the 2015 authors correctly anticipated, FEP has become a routine decision-support tool. It's commonly used to prioritize synthetic targets, particularly for difficult synthetic routes where computational validation can justify the investment. The technology has been applied across multiple therapeutic areas including oncology, inflammation, CNS disorders, and infectious diseases.

**Real-world drug development impact**: While specific drug approvals directly attributable to FEP are difficult to identify due to the proprietary nature of drug discovery programs, retrospective analyses suggest FEP-guided optimization has contributed to candidate compounds entering clinical development at companies like AstraZeneca, GSK, and Vertex. The approach has been particularly valuable for structure-based drug design campaigns.

**Technological evolution**: GPU computing has continued to advance dramatically since 2015, with modern FEP calculations benefiting from both faster hardware and improved algorithms for enhanced sampling and binding free energy calculations. Cloud computing resources have made FEP accessible to smaller companies and academic groups.

**Limitations and challenges**: The 1 kcal/mol accuracy remains challenging for certain molecular systems, particularly those involving substantial conformational changes, covalent modifications, or complex water networks. The "5% failures" noted in 2015 still represent a significant challenge for methods that need high reliability in industrial decision-making.

**Business outcomes**: Schrödinger went public in 2020 (NASDAQ: SDGR) and has built a substantial business around computational drug discovery tools including FEP+. The company has also moved into internal drug discovery programs leveraging these computational methods.

## 3. PREDICTIONS

• **"FEP as a tool, not replacement for medicinal chemists"**: ✅ **Accurate**. The field evolved exactly as predicted—FEP became integrated into medicinal chemistry workflows as a decision-support tool rather than replacing human chemists. This pragmatic approach facilitated adoption and aligned with how computational tools are most effectively deployed in drug discovery.

• **"Reduces risk of pursuing synthetically challenging molecules"**: ✅ **Accurate**. This has been validated through widespread industrial practice. FEP predictions are routinely used to justify synthesis of complex targets, with companies reporting improved efficiency in lead optimization campaigns compared to traditional approaches.

• **"GPU computing will continue advancing and benefiting drug design"**: ✅ **Accurate**. GPU performance has increased dramatically since 2015 (roughly 10-20x improvement), and cloud computing has made GPU resources widely accessible. Modern FEP calculations are significantly faster and can be applied to larger molecular systems than was possible in 2015.

• **The implicit prediction that this represented a "tipping point"**: ⚠️ **Partially accurate**. FEP did reach critical mass for industrial adoption, but the transformation was more gradual than revolutionary. The methodology became standard practice at large pharma companies but didn't fundamentally disrupt the drug discovery paradigm in the dramatic way the "tipping point" metaphor might suggest.

## 4. INTEREST

Rating: **7/10**

This article identified a genuinely important methodological advance in computational drug discovery that has had sustained real-world impact. FEP has become a standard industrial tool, representing one of the more successful academic-to-industry translations in computational chemistry. While not revolutionary in transforming the entire drug discovery enterprise, it has achieved measurable improvements in efficiency and decision-making quality across the pharmaceutical industry.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20150223-fep-ready-world.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_