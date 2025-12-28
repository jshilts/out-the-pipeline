
https://www.science.org/content/blog-post/standards-proof
# Standards of Proof (December 2013)

## 1. SUMMARY
This article discusses Anthony Nicholls' (OpenEye) critical presentation about molecular dynamics (MD) simulations in drug discovery. Nicholls argues that MD calculations are not held to the same rigorous standards of proof as simpler empirical approaches, despite their complexity and computational expense. The piece highlights several key concerns: MD benefits from cognitive dissonance within the field, where attractive attributes like "being physics" and producing "great movies" substitute for predictive reliability. 

The article introduces Nicholls' "Tanimoto of Truth" concept, which categorizes results into true positives, true negatives, false positives, and false negatives. He observes heavy publication bias where only positive results get published, false positives get buried in drawers, and false negatives either get "parameterized until publishable" or discarded. The discussion references a specific paper on allosteric muscarinic ligand modeling that claimed MD success but only tested a single compound prospectively, while admitting that simpler GLIDE docking performed nearly as well without quantification. Nicholls concludes that until MD faces the same validation standards as other methods, the field cannot mature properly.

## 2. HISTORY
In the decade following this 2013 critique, molecular dynamics simulations have become increasingly integrated into drug discovery pipelines, though validation challenges persist. Major pharmaceutical companies (Pfizer, Novartis, Roche, AstraZeneca) have invested heavily in computational modeling teams and infrastructure, using MD for target characterization, binding site prediction, and mechanistic studies.

Several MD-based approaches have demonstrated practical success. **Fragment binding site mapping** using MD (as pioneered by companies like Sosei Heptares) has informed drug design for GPCR targets, leading to clinical candidates. **WaterMap** and **SiteMap** analyses from Schrödinger have become standard tools for identifying and characterizing binding sites. Allosteric modulator discovery has particularly benefited, with MD helping rationalize binding modes for drugs like maraviroc analogs.

However, the challenge of prospective validation identified by Nicholls remains partially unresolved. While **AlphaFold2** (2020) revolutionized protein structure prediction through deep learning rather than MD, its success has influenced MD methodology. The field has moved toward **ensemble-based approaches** and **Markov state modeling** to address sampling limitations, with software like **GROMACS**, **AMBER**, and **NAMD** becoming more accessible.

Clinical pipeline impact remains limited compared to traditional methods. Most approved drugs still originate from high-throughput screening or structure-based design using simpler docking protocols. While MD provides mechanistic insights for optimization (thermodynamic integration for binding affinity calculations), prospective drug discovery campaigns rarely rely solely on MD predictions.

The reproducibility crisis in computational chemistry that Nicholls highlighted has driven the **FAIR data principles** movement. Journals now increasingly require deposition of simulation parameters, trajectories, and analysis scripts. Initiatives like the **Living Journal of Computational Molecular Science** aim to improve transparency, though field-wide standards enforcement remains inconsistent.

Antibody-drug conjugate development represents one area where MD has contributed to FDA-approved therapies (e.g., **Enhertu**, **Kadcyla**) through stability and linker design optimization, though this constitutes a small fraction of the overall computational contribution.

## 3. PREDICTIONS
The article contained several implicit predictions about molecular dynamics and computational drug discovery:

• **MD will need higher validation standards to become reliable**: This has partially materialized. While MD adoption has increased, the field still lacks consensus validation benchmarks comparable to crystallography or biochemical assays. Success remains case-dependent rather than universally reliable.

• **Publication bias will continue harming the field**: Publication practices have improved moderately with increased data transparency requirements, but positive-result bias persists in computational studies. Open datasets like **Protein Data Bank** and trajectory repositories help, but limited scope remains problematic.

• **Single-compound validation is insufficient**: Modern computational studies increasingly use larger test sets (10-100 compounds), though many still focus on "successful" examples. Prospective prediction competitions have emerged (D3R challenges, CASP) which provide broader validation.

• **Empirical methods will remain competitive with complex simulations**: This prediction proved largely accurate. Docking programs like AutoDock, GLIDE, and GOLD remain workhorses due to speed and reasonable accuracy. Deep learning approaches (AlphaFold, RoseTTAFold) have surpassed some MD applications while avoiding sampling issues.

• **MD complexity doesn't guarantee pharmaceutical utility**: Confirmed by continued industry practice. While MD provides mechanistic insights, most drug discovery programs combine multiple computational approaches rather than relying exclusively on MD predictions.

## 4. INTEREST
**Score: 7/9**

This article was prescient in identifying systemic validation problems in computational chemistry that extended beyond MD to affect the broader field. Its insights anticipated important debates about reproducibility and standards that became prominent in the 2010s, making it historically significant for understanding computational drug discovery methodology evolution.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20131210-standards-proof.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_