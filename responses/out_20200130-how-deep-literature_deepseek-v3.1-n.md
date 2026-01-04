
https://www.science.org/content/blog-post/how-deep-literature
# How Deep Is That Literature? (January 2020)

## 1. SUMMARY
This commentary discusses a Georgia Tech PNAS paper (2020) analyzing the reproducibility and replication of metal-organic frameworks (MOFs) in the chemical literature. The study examined 130 randomly selected MOFs from pre-2014 literature and found that direct replication was extremely rare: only 1 material (Bio-MOF-100) had been synthesized more than 3 times by independent groups, only 15 out of 130 had been synthesized more than once by anyone, and just 7 had been resynthesized by groups other than the original authors. The distribution showed extreme concentration - an estimated 0.03% of reported MOFs accounted for 50% of replications, following what the authors suggested was a power law distribution. Even parameters like BET surface area measurements showed poor convergence over time, with bimodal distributions in some materials suggesting persistent irreproducibility issues. The commentary connects these findings to broader concerns about machine learning applications in chemistry, since ML models require reliable, well-replicated data to function properly.

## 2. HISTORY
The article's core findings about reproducibility problems in MOF literature highlighted issues that persisted and extended to other areas of chemistry and materials science. There were subsequent developments related to reproducibility standards, database improvements, and the implementation of these lessons in actual ML systems.

The reproducibility crisis in chemical sciences continued gaining attention after 2020, with several systematic studies confirming similar patterns in other subfields. Efforts to improve the situation included better reporting standards, community databases with curated experimental procedures, and the development of automated synthesis platforms that could independently verify reported procedures.

For MOFs specifically, research continued focusing heavily on the "super-repeats" mentioned in the article - well-characterized materials like HKUST-1, MOF-5, ZIF-8, UiO-66, and MIL-101 remained dominant in the literature. These materials demonstrated their continued practical advantages: commercial availability, well-understood properties, robust synthesis protocols, and proven performance in applications like gas storage, separation, and catalysis.

The machine learning applications that motivated the original concerns saw significant development. Retrosynthesis software platforms like those from companies such as PostEra, Chemify, and others incorporated reliability scoring that weighted repeatedly verified reactions more heavily. These systems increasingly used replication frequency as a key feature for predicting reaction success probability.

Regarding Bio-MOF-100 specifically (the Zn-based MOF mentioned as the sole example synthesized more than 3 times), it continued appearing in literature but did not achieve widespread commercial application compared to other framework materials, suggesting laboratory novelty and publication factors rather than practical utility drove its "popularity."

## 3. PREDICTIONS
• **Prediction about machine learning needing better data quality**: This prediction was borne out. Subsequent ML tools in chemistry heavily incorporated reliability scoring, with tools like ASKCOS, IBM RXN, and commercial platforms explicitly using replication data to weight reaction reliability. The chemical ML community increasingly recognized that publication alone was insufficient evidence of usability.

• **Prediction about unreproducible literature causing ML failures**: Validated by experience. Practical applications showed that databases filled with one-off reactions led to poor model performance, resulting in the development of curation approaches that excluded or downweighted poorly replicated procedures.

• **Prediction about "super-repeat" sociological factors**: Confirmed. The same MOFs that were popular pre-2020 remained dominant post-2020 (HKUST-1, MOF-5, ZIF-8, UiO-66, MIL-101). These materials offered the advantages recognized in the article: commercial availability, easier synthesis, established characterization protocols, and accumulated knowledge about their properties.

• **Prediction that many good transformations might be lost in old journals**: This mining of historical literature did occur to some extent, with groups using ML to identify "forgotten" reactions and transformations. However, practical challenges remained in reviving old procedures, especially those with incomplete experimental details.

• **Prediction about irreproducible BET measurements**: This problem persisted as documented. BET surface area measurements continued showing variability in publications, with researchers developing better protocols for MOF activation and measurement to improve comparability.

## 4. INTEREST 
Rating: **8/10**
This article identified and quantified critical problems in chemical literature that directly impacted the practical application of machine learning methods - issues that became even more relevant as ML adoption accelerated in chemistry. It provided empirical evidence for reproducibility problems that were widely suspected but poorly documented.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20200130-how-deep-literature.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_