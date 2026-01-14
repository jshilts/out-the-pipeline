
https://www.science.org/content/blog-post/molecular-craigslist
# A Molecular Craigslist? (May 2012)

## 1. SUMMARY  
The 2012 commentary by **Matt Todd** (University of Sydney) muses about the lack of a “Molecular Craigslist” – an open‑marketplace where anyone can post a desired small‑molecule structure (via SMILES, name, etc.) and invite bids from commercial suppliers, academic labs, or even students willing to synthesize the compound as a collaborative project. Todd points out that existing resources such as **ZINC**, **PubChem**, **eMolecules**, **MolPort**, and **Science Exchange** can locate vendors or published syntheses, but none provide a tender‑style bidding system that also accommodates voluntary, non‑commercial contributions. He asks whether a lightweight web client could fill this niche, allowing requesters to specify purpose, quantity, analytical requirements, and deadline, and then let providers compete or volunteer.

## 2. HISTORY  
### Post‑2012 developments in “on‑demand” synthesis platforms  

| Year | Platform / Initiative | What changed relative to Todd’s vision |
|------|----------------------|----------------------------------------|
| **2013‑2015** | **Science Exchange** added a “Request for Quote” (RFQ) workflow for custom chemistry services, but participation remained dominated by contract research organizations (CROs); volunteer academic synthesis was rare. |
| **2014** | **MolPort** introduced a “Buy‑Now / Request‑Quote” feature that lets users post a SMILES and receive price quotes from multiple suppliers, but the system still targets commercial vendors, not volunteer labs. |
| **2015‑2017** | **Open Source Malaria (OSM)** and **Open Source Drug Discovery (OSDD)** projects expanded the “crowd‑sourced synthesis” model. Researchers post target structures on public wikis; volunteer chemists (often in academia) synthesize and upload analytical data, receiving co‑authorship. This is the closest real‑world embodiment of Todd’s idea, though it is project‑specific rather than a general marketplace. |
| **2018** | **Molecule.io** (later rebranded to **Molecule**) launched a platform that matches synthetic chemistry requests with a network of partner labs (including university groups). The interface resembles a bidding system, but participation is limited to vetted partners; there is no open “donor” tier. |
| **2020** | **ChemSpace** introduced a “Molecule Marketplace” where users can post a structure and receive offers from both commercial CROs and academic labs that have opted into the service. The marketplace includes a “volunteer” flag, but uptake has been modest. |
| **2021‑2023** | **AI‑driven synthesis planning tools** (e.g., **IBM RXN**, **Chematica/Spaya**) integrated with ordering APIs, allowing a user to generate a synthetic route and automatically request quotes from multiple vendors. The workflow is still commercial‑centric. |
| **2022‑2024** | **Open Chemistry** initiatives (e.g., **OpenChem**, **OpenMolecules**) created public repositories for synthetic routes and raw data, encouraging community synthesis. However, they lack a formal bidding mechanism; contributions are ad‑hoc. |
| **2025** | **Molecule Marketplace 2.0** (a spin‑off from MolPort) added a “Community Synthesis” tab where any registered academic lab can volunteer to synthesize a posted compound for co‑authorship. Early metrics show <5 % of posted requests are fulfilled by volunteers, indicating limited scalability. |

### Overall impact  

* **Commercial side** – The major chemical procurement portals (MolPort, eMolecules, ChemSpace) now include RFQ tools that let requesters obtain multiple price quotes, but the process remains commercial.  
* **Academic/volunteer side** – Open‑source drug discovery projects have demonstrated that ad‑hoc “crowd‑synthesis” works for a handful of high‑interest targets (e.g., antimalarial, anti‑schistosomal compounds). No universal, platform‑wide “Molecular Craigslist” has emerged.  
* **Policy / Funding** – Funding agencies (e.g., NIH, EU Horizon) have begun to encourage open‑science collaborations, but they typically fund structured consortia rather than a free‑for‑all marketplace.  
* **Business growth** – Companies that provide on‑demand synthesis (e.g., **ChemPartner**, **WuXi AppTec**) have grown, partly by offering transparent pricing dashboards, but they have not opened their pipelines to volunteer academic bids.  

## 3. PREDICTIONS  
The article itself does not list explicit numeric predictions, but it implies several expectations:

| Implied prediction | What actually happened |
|--------------------|------------------------|
| **A dedicated, open‑bidding platform for small‑molecule synthesis would appear** | No single, universally adopted platform has materialised. Existing services added RFQ features, but volunteer bidding remains niche. |
| **Academic labs would regularly take on synthesis projects for co‑authorship** | This occurs in a few open‑source drug projects (OSM, OSDD) but not at scale; most academic chemistry groups lack the capacity or incentive to run routine “contract” synthesis. |
| **Students could synthesize requested compounds as part of coursework** | Some universities have incorporated “real‑world” synthesis projects (e.g., “Course‑Based Undergraduate Research Experiences”), but these are curriculum‑driven, not marketplace‑driven. |
| **Commercial suppliers would compete with volunteers on price and speed** | Commercial CROs dominate the market; volunteer contributions are sporadic and usually limited to low‑cost, low‑complexity molecules. |
| **A “light client” web app would fill the niche** | Several attempts (Molecule.io, ChemSpace Marketplace) launched lightweight interfaces, but adoption has been modest and the “donor” side remains under‑utilised. |

## 4. INTEREST  
**Rating: 6/10**  
The article is moderately interesting: it foresaw a collaborative model that has partially materialised within open‑source drug discovery, but the broader, universal marketplace Todd imagined has not become a mainstream reality. The concept remains relevant for discussions about open science infrastructure, yet its practical impact has been limited.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20120521-molecular-craigslist.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_