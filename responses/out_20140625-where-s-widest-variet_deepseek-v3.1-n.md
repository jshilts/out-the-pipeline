
https://www.science.org/content/blog-post/where-s-widest-variety-chemical-matter
# Where's the Widest Variety of Chemical Matter? (June 2014)

## 1. SUMMARY

This 2014 commentary posed a qualitative thought experiment: among druggable targets, which has attracted the most chemically diverse ligands? The author proposed breaking this down by target class—enzymes (active-site inhibitors), GPCRs (agonists vs antagonists), and the open field. They suggested nuclear receptors might lead due to large, flexible binding sites, and noted practical questions (e.g., clustering sulfonamide carbonic anhydrase inhibitors vs counting each zinc-binding motif distinctly). The post explicitly asked the community for nominations rather than asserting a definitive answer, and proposed exempting drug-metabolizing enzymes as outliers.

## 2. HISTORY

After 2014, large-scale cheminformatics and public bioactivity databases (ChEMBL, PubChem) made it possible to quantify scaffold and chemotype diversity against targets. Systematic analyses in the 2015–2020 period showed that traditional enzyme families and GPCRs often exhibit shallow structure–activity relationships accessible via multiple chemical series. However, unexpected “cryptic” or allosteric sites began to be systematically mapped (e.g., for kinases and GPCRs), expanding the known chemical matter per target beyond active-site and orthosteric ligands. Meanwhile, DNA-encoded library (DEL) campaigns and affinity selection–mass spectrometry screens started producing multi-binder results per target in a single experiment, demonstrating that even well-studied targets harbor more binding diversity than medicinal chemistry precedent suggests. By the late 2010s, machine-learning docking and generative chemistry (e.g., AlphaFold-powered structure-based design, generative models) further expanded the upper bound of “diverse chemical matter” for a given target. Importantly, chemically diverse ligand sets do not necessarily translate to more approved drugs, as promiscuity and polypharmacology often dominate the practical path to selectivity and safety.

## 3. PREDICTIONS

- **Implicit prediction: Nuclear receptors would lead in chemical diversity.** Subsequent data show nuclear receptors have been drugged with multiple chemotypes (e.g., PPAR pan/α/γ/δ agonists show distinct SAR; estrogen receptor modulators exhibit varied scaffolds), consistent with the idea of a flexible pocket accommodating diverse shape and polarity. However, whether NRs truly lead among all target classes is debatable; protein–protein interaction targets and certain GPCRs also display broad diversity.
- **Antagonists would outnumber agonists in GPCRs.** In aggregate, approved GPCR antagonists generally outnumber agonists across indications. Chemically, “antagonist-winning” seems plausible due to greater tolerance for bulkier, more lipophilic groups in antagonist binding modes, though the GPCR-ome is vast and exceptions exist (e.g., ultra-potent small agonists at aminergic GPCRs).
- **Carbonic anhydrase would be heavily sulfonamide-dominated.** This remained true; most marketed CA inhibitors are sulfonamide-based. However, non-sulfonamide motifs (e.g., coumarins, dithiocarbamates) also exist and were pursued post-2014.
- **Open-ended community insight would produce interesting nominations.** Public datasets after 2014 made this quantifiable; enzymes like kinases and proteases gathered diverse hits, and GPCRs like 5-HT2A or opioid receptors showed extensive chemical series across scaffolds.

## 4. INTEREST

Rating: **4/10**

This is a narrow medicinal chemistry “parlor game” with modest impact. It stimulated qualitative curiosity, but later large data resources and computational methods resolved the question empirically rather than through expert polls.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20140625-where-s-widest-variety-chemical-matter.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_