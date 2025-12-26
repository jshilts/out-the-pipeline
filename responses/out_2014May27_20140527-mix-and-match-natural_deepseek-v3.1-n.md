model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20140527-mix-and-match-natural-products.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}}

# Retrospective Analysis: “Mix-and-Match Natural Products” (Science Magazine, 2014)

## 1. SUMMARY

The 2014 Science Magazine piece highlighted Martin Burke’s work at the University of Illinois on using MIDA boronates to enable mix-and-match synthesis of natural-product-like compounds. Natural products tend to be structurally complex and stereochemically rich, and conventional combinatorial libraries struggle to deliver both structural diversity and natural-product-like features at scale. The article reported that a small set of just 12 bifunctional MIDA boronate building blocks could theoretically recreate the polyene motifs found in more than 75% of all polyene natural products, and the team had already made progress extending the approach to a dozen additional motifs present in over 100,000 natural products. The goal was to shift from difficult, bespoke natural-product synthesis to systematic, iterative coupling—opening the door to screening “almost-natural” libraries to probe the role of evolutionary fine-tuning in bioactivity.

## 2. HISTORY

Subsequent developments validated the technique and expanded its reach, but also highlighted some of the method’s intrinsic limitations and competitive context.

**Technology adoption and extensions**: MIDA boronate building blocks became commercially available, lowering the barrier for broader adoption in medicinal chemistry and chemical biology. Burke’s group and others continued to refine the chemistry, applying automated iterative cross-coupling to more challenging targets and extending the approach beyond polyenes to motifs such as polyketides and peptides.

**Automation and scale**: The methodology’s intrinsic suitability for automation led to platforms for assembling complex, natural-product-like macrocycles and fragments with minimal manual intervention. This scaled output enabled screening campaigns that were previously impractical.

**Concurrent alternatives**: During the same period, other synthetic strategies also gained traction, including DNA-encoded libraries (DEL), late-stage functionalization, and advances in biocatalysis and enzyme engineering. These competing approaches offered complementary trade-offs in speed, diversity, and “drug-likeness,” and sometimes proved faster for certain scaffold classes than MIDA-boronate-based routes.

**Commercial and industrial uptake**: While widely adopted in academic settings, industrial adoption was mixed. Pharma and biotech appreciated the method’s ability to generate architecturally complex and chiral small molecules, but teams often balanced it against cost, step count, and purification overhead relative to competing technologies. The technique found strongest use in fragment-based campaigns and for generating bespoke natural-product analogs rather than as a wholesale replacement for other library-generation methods.

**Generalization to “most” natural products**: The early promise to access the remaining 99% of natural-product space proved more challenging than implied. Success depended heavily on solving difficult Csp3 stereospecific couplings and complex protecting-group strategies, resulting in slower progress than the 2014 roadmap might have suggested.

## 3. PREDICTIONS

**What the article got right**:  
- The **capability to make complex natural-product motifs with reduced synthetic burden** was broadly realized. MIDA boronates became a practical, scalable tool for iterative coupling and were applied to a variety of targets.  
- The **hypothesis that a small set of building blocks could cover a large fraction of polyene space** proved sound for that class of molecules and demonstrated the power of retrosynthetic simplification.  
- The method did **deliver new compounds for screening**, and it enabled cheminformatics and biophysical studies on natural-product-like vs. purely synthetic chemical space.

**What the article got wrong or oversimplified**:  
- The **scale and speed of expansion to the “remaining 99%” of natural products** were overestimated. The roadmap required solutions to frontier methodological problems (e.g., stereospecific Csp3 cross-coupling), and progress was incremental rather than exponential.  
- The **screening “hit rates” argument** was framed too narrowly. While many “almost-natural” libraries showed good hit rates, one missed nuance is that hits often still required subsequent optimization to attain potency, selectivity, and ADME properties—evolutionary “fine-tuning” turned out to matter more than a simple hit-rate metric might suggest.  
- The article **slightly understated the competition from other library technologies** (e.g., DEL and biocatalysis), which advanced rapidly alongside boron chemistry, sometimes offering easier routes to diversity.

## 4. INTEREST

**Decile score: 7/9**  
This article sits in the 70–79th percentile of interest and long-term importance. It introduced a conceptually elegant, pragmatic advance that became a standard tool in synthetic chemistry and chemical biology. While it did not single-handedly transform drug discovery or scale to cover “most” natural products as quickly as imagined, it was a high-impact methodology that complemented (rather than replaced) other library technologies and inspired automation efforts. The work remains a strong example of translational synthesis—bridging academic innovation with practical utility in complex-molecule synthesis, even if its ultimate scope was more modest than the 2014 roadmap suggested.