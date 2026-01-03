
https://www.science.org/content/blog-post/here-s-what-s-been-done
# Here's What's Been Done Before (November 2018)

## 1. SUMMARY

This commentary reflects on an ACS Medicinal Chemistry Letters perspective about AI and machine learning in medicinal chemistry, focusing on a critical limitation: literature-mining AI systems can only extract knowledge that already exists in published literature, potentially leading to self-reinforcing loops in chemical synthesis recommendations.

The author highlights a specific concern with retrosynthesis software: these platforms tend to prioritize frequently used reactions (like palladium-mediated couplings and amide formations) based on utilization frequency. This creates a feedback loop where popular reactions become even more likely to be suggested, potentially reducing creative exploration of alternative synthetic routes. The author notes this amplifies existing human behavior - medicinal chemists already tend to reuse familiar reactions for "just make the compound" tasks rather than exploring novel approaches.

The commentary distinguishes between different user groups: academic total synthesis researchers and industrial process chemists are more likely to adopt genuinely new reactions because they face different constraints (difficult transformations or optimization for scale/cost), while medicinal chemists focused on rapid compound generation may perpetuate the status quo. The author suggests AI systems could incorporate both "exemplification" (established, reliable) and "novelty" scoring to balance reliability with innovation.

## 2. HISTORY

The concerns raised in this 2018 article proved remarkably prescient and largely accurate in describing the subsequent trajectory of AI in chemistry:

**Retrosynthesis Software Evolution**: Major retrosynthesis platforms like those from IBM (RXN for Chemistry), Chematica (acquired by Merck and rebranded as Synthia), and others have indeed worked to address the diversity issue. By 2020-2024, leading platforms incorporated algorithms to balance "tried-and-true" routes with novel approaches, though the tension between reliability and creativity persists.

**Palldium Coupling Catalysts**: The specific example of tetrakis palladium catalysts remained relevant. While newer, more efficient catalysts (e.g., G3-XantPhos, RuPhos, BrettPhos-based systems) gained adoption in process chemistry and academic synthesis, many medicinal chemistry labs continued using established protocols for routine couplings, validating the author's observation about different adoption rates across user groups.

**Literature Mining Limitations**: The fundamental constraint that literature-mining AI can only discover what's already published has remained true. Subsequent developments focused on combining known transformations in novel ways rather than discovering entirely new reaction types through AI alone.

**Industry Adoption Patterns**: By 2022-2024, pharmaceutical companies increasingly integrated retrosynthesis software into drug discovery pipelines, but primarily for rapid analog generation rather than pushing synthetic innovation boundaries - aligning with the "get the compound made" mindset the author described.

## 3. PREDICTIONS

The article made several explicit and implicit predictions:

• **Prediction**: AI retrosynthesis software will prioritize frequently used reactions, creating self-reinforcing cycles
- **Outcome**: ✓ Largely confirmed. Early versions of commercial retrosynthesis tools did show bias toward conventional routes, prompting developers to implement diversity scoring and novelty parameters.

• **Prediction**: Different user groups will adopt new reactions at different rates (academic/process chemists faster than medicinal chemists focused on rapid compound delivery)
- **Outcome**: ✓ Confirmed. Academic synthetic chemistry continued to pioneer novel methodologies and difficult transformations, while medicinal chemistry workflows optimized for speed and reliability.

• **Prediction**: New reactions that enable previously difficult transformations (like photoredox chemistry) will gain adoption faster than incremental improvements to existing methods
- **Outcome**: ✓ Confirmed. Photoredox catalysis, C-H functionalization, and other transformative methods saw rapid uptake in both academia and pharmaceutical applications where they solved specific problems.

• **Prediction**: AI systems could incorporate "exemplification" vs "novelty" scoring to balance reliability and creativity
- **Outcome**: ✓ Implemented. Major retrosynthesis platforms developed scoring systems that allow users to specify preference for established routes versus potentially shorter but less-proven alternatives.

• **Implicit prediction**: Piling-on effects in ML systems could extend beyond synthesis to create "conventional wisdom machines"
- **Outcome**: ✓ Broader concern validated. Similar patterns emerged in other AI applications across drug discovery, where models trained on existing data reproduced existing biases rather than discovering fundamentally new patterns.

## 4. INTEREST

Rating: **7/10**

This article merits a high interest score because it identified a fundamental limitation in AI-driven chemistry that remained relevant for years afterward and influenced how computational tools were developed. The specific examples (tetrakis catalyst usage, different adoption patterns across user groups) showed genuine domain expertise and provided concrete illustrations of broader AI/wisdom-of-crowds problems. While focused on a niche area, the self-reinforcing dynamics it described apply to many ML applications beyond chemistry.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20181108-here-s-what-s-been-done.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_