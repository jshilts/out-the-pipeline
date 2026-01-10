
https://www.science.org/content/blog-post/getting-van-der-waals-forces-right
# Getting van der Waals Forces Right (October 2013)

## 1. SUMMARY

This article discusses a 2013 *Nature Chemistry* study that challenged prevailing assumptions about van der Waals forces in drug discovery and molecular binding. The research team developed a synthetic molecular balance system to measure alkyl-chain interactions across 30+ different solvent environments—organic, fluorous, and aqueous.

The key finding was that van der Waals interactions between alkyl chains were an order of magnitude smaller than previously estimated from gas-phase measurements and dispersion-corrected calculations. Critically, the study revealed that solvent molecules strongly attenuate these interactions through competitive dispersion forces. This challenged existing computational models that relied heavily on gas-phase experimental data, raising questions about how accurately we model drug-target binding where water molecules play intermediary roles between vacuum-like protein interiors and bulk solvent environments.

## 2. HISTORY

Following the 2013 publication, this research had modest but meaningful impact on computational chemistry methodology and drug design:

The finding that solvent effects dramatically reduce van der Waals forces from gas-phase estimates led to improved implicit and explicit solvent models in molecular dynamics simulations. By 2015-2018, major computational chemistry software packages (including Schrödinger's suite, AMBER, GROMACS) had refined their force field parameters and solvent models based on these insights, though direct attribution is complex in a field with many contributing advances.

In drug discovery practice, the results reinforced the ongoing shift toward explicit consideration of water molecules in binding site modeling and the limitations of purely gas-phase quantum calculations. Pharmaceutical companies and academic groups increasingly incorporated explicit solvent molecules and better solvation thermodynamics into their computational workflows.

However, I lack confidence about specific FDA-approved drugs that resulted directly from these improved van der Waals models, as drug discovery involves hundreds of variables and takes many years. The impact appears more methodological and incremental rather than producing breakthrough therapeutics.

The fundamental chemistry finding—that solvent dramatically attenuates dispersion forces—has been validated by subsequent studies and is now widely accepted in the field, influencing both computational methods and wet-lab interpretation of binding data.

## 3. PREDICTIONS

The original article and commentary made several implicit predictions and raised questions:

• **Simplified computational approaches**: The suggestion that solvent-canceled van der Waals forces might simplify calculations has had mixed outcomes. While computational efficiency has improved dramatically since 2013, this came more from hardware advances and better algorithms than from van der Waals simplification. Researchers still calculate these forces, but with better solvent models rather than ignoring them.

• **Improved drug-binding models**: The hope that better van der Waals understanding would improve binding predictions has partially materialized. Modern computational drug design does incorporate these insights into force fields and binding calculations, contributing to incremental improvements in accuracy. However, no revolutionary breakthrough in binding affinity prediction occurred specifically from this work; progress remained gradual across multiple fronts.

• **Synthesis with gas-phase measurements**: The implicit prediction that the field would reconcile differences between gas-phase and solution measurements has been fulfilled. The scientific community now recognizes that gas-phase data provides upper bounds, while solution-phase studies provide realistic parameters for biological modeling.

• **Need for computational collaborations**: The expressed desire for computational collaborators succeeded—this line of research continued with improved computational-experimental integration in subsequent years.

## 4. INTEREST

Rating: **5/10**

This represents solid mid-tier scientific importance: significant methodological advances for specialists in computational chemistry and drug design, but not transformative enough to change clinical outcomes or public policy. The work refined existing paradigms rather than creating new ones.


----
_model_params = {'model': 'nex-agi/deepseek-v3.1-nex-n1:free', 'input': '20131021-getting-van-der-waals-forces-right.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_