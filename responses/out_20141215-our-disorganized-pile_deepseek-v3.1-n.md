
https://www.science.org/content/blog-post/our-disorganized-piles-chemical-information
# Our Disorganized Piles of Chemical Information (December 2014)

## 1. SUMMARY

This article examines the state of pharmaceutical chemistry databases in 2014, highlighting the tension between publicly available information and commercial curated databases like CAS/SciFinder. The author reviews a research paper that documented several critical problems: while public databases had grown to surpass proprietary ones in sheer volume, they suffered from poor curation and inconsistent annotation. The article cites a striking example where a single patent (US20090163545) incorporated 132,781 compounds by reference to a PubChem HTS assay, creating confusion in IP due diligence searches where SciFinder showed different substance counts than the original patent.

Key issues identified include difficulties in compound standardization (SMILES strings, tautomers, salt forms), unreliable commercial availability listings (many "makeable on demand" compounds were never actually synthesized), and lack of detailed biological assay protocols that would enable cross-comparison. The research paper found that half of supposedly available compounds weren't actually obtainable, creating a "parallel worlds" problem where databases contained conflicting or incomplete information.

## 2. HISTORY

The database fragmentation and curation challenges identified in 2014 largely persisted and often worsened. The call for a "summit meeting" of database vendors mentioned in the article did not materialize in any coordinated fashion. Instead, the landscape became even more fragmented with new players entering the space.

**Commercial Database Evolution:** CAS/SciFinder continued to dominate the high-end market for IP due diligence, maintaining their curation advantage but at substantial cost. By the late 2010s and 2020s, alternative databases emerged but none achieved comprehensive coverage. The fundamental problems of compound standardization (tautomers, stereochemistry, salt forms) remained largely unsolved at scale.

**PubChem and Public Databases:** PubChem continued growing explosively, reaching over 100 million compounds by 2020. However, data quality issues persisted—compounds without experimental verification, incomplete annotations, and the "prophetic compounds" problem where chemical structures existed only on paper. No systematic solution emerged for linking biological assay data across different experimental conditions.

**Industry Response:** Pharmaceutical companies increasingly relied on multiple overlapping databases and sophisticated informatics teams to navigate the fragmentation. Third-party services emerged offering "database of databases" searches. However, this created exactly the scenario the article warned about—organizations needing to search across multiple incompatible systems to achieve reasonable confidence in their results.

**Regulatory and IP Landscape:** The IP due diligence problems worsened with the continued growth of patents incorporating public HTS data by reference. The confusion around prior art for compounds without experimental data remained unresolved through 2024. No major policy changes addressed the database curation standards or data quality requirements.

## 3. PREDICTIONS

- **Prediction:** The authors called for database vendors and curators to hold a summit meeting to prevent further divergence of standards and practices.
  - **Outcome:** No such coordinated summit occurred. The database ecosystem became more fragmented with new entrants, not less.

- **Prediction:** The article warned we would end up in a situation requiring searches across multiple incompatible semi-redundant databases, noting "that's the situation we're already in."
  - **Outcome:** This prediction proved accurate. By 2024, pharmaceutical companies routinely searched 5-10 different databases (public and commercial) for comprehensive coverage, with significant manual effort required to reconcile results.

- **Prediction:** The authors expressed concern that without intervention, the situation would "keep it from getting any worse."
  - **Outcome:** The situation did get worse. Database fragmentation increased, the volume of uncurated data grew exponentially, and no industry-wide standards emerged to address the fundamental problems identified.

## 4. INTEREST

**Score: 4**

The article identified a real and persistent problem in pharmaceutical informatics, but the issues were already well-recognized within the industry. While the specific examples were interesting, the broader challenge of chemical data curation was not a transformative insight and the piece did not substantially influence how the field developed.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20141215-our-disorganized-piles-chemical-information.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_