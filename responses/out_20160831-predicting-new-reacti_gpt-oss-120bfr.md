
https://www.science.org/content/blog-post/predicting-new-reactions
# Predicting New Reactions (August 2016)

## 1. SUMMARY  
The 2016 commentary discusses a paper from the University of Münster that attempts to predict previously unseen organic reactions by mining a massive reaction corpus (≈8 M binary reactions, 14.4 M distinct species) extracted from Reaxys. The authors treat chemistry as a graph‑theory problem: each molecule is a node, each reaction an edge. By finding “similar” reactants that share known partners, the algorithm extrapolates to new partner combinations and even proposes the likely product structure.  

Two performance regimes are reported:  

* **General test set** – 180 k random reactions from the post‑2013 literature were predicted with ~67 % top‑1 accuracy.  
* **Novel‑space test set** – after removing any reaction that could be covered by existing rule‑based systems, 13 k reactions were evaluated, yielding ~35 % accuracy.  

The authors note that many failures are chemically reasonable (e.g., alternative reactive sites) and that the method’s success scales with the size of the underlying graph. They suggest the approach could be used to flag potentially useful, yet undocumented, transformations or to map “rich” versus “poor” regions of synthetic space.

---

## 2. HISTORY  

### Evolution of data‑driven reaction prediction (2016‑2024)  

| Year | Development | Impact on the Münster approach |
|------|-------------|--------------------------------|
| **2017‑2018** | Introduction of **sequence‑to‑sequence (seq2seq) and transformer** models for reaction prediction (e.g., the “Molecular Transformer” by Schwaller et al.). | Demonstrated top‑1 accuracies of 80‑90 % on USPTO test sets, surpassing the Münster graph‑based 67 % figure for known reactions. |
| **2019** | Release of **IBM RXN for Chemistry** (a cloud‑based transformer model) and **ASKCOS** (MIT) for forward and retro‑synthesis. | Made AI‑driven prediction accessible to bench chemists; the Münster method never saw a comparable public interface. |
| **2020** | **Chematica** (now **Synthia**) commercialized a rule‑based/graph‑search engine that integrates expert knowledge with data‑driven scoring. | Shows that hybrid systems (rules + ML) remain competitive; the pure similarity‑graph approach of Münster is rarely cited as a core component. |
| **2021‑2022** | Large‑scale **self‑supervised pre‑training** on millions of SMILES strings (e.g., ChemBERTa, Chemformer). | Improves handling of out‑of‑distribution chemistry, addressing the “novel‑space” weakness highlighted in the 35 % result. |
| **2023** | **Open‑source reaction datasets** (USPTO‑50k, Pistachio, Reaxys‑Lite) become standard benchmarks; community adopts **top‑k accuracy** and **coverage** metrics. | The Münster paper’s evaluation (single‑top prediction) is now considered incomplete; modern studies report top‑5/10 accuracies that are more relevant for discovery. |
| **2024** | **Multimodal models** (graph + text + reaction conditions) start to predict not only products but also optimal reagents, solvents, and temperatures. | Extends the original idea of “predicting new nodes/edges” to a richer chemical graph that includes reaction conditions, something the Münster work did not address. |

### Concrete outcomes  

* **No direct commercial adoption** of the Münster graph‑based predictor has been documented. The method is cited in a handful of follow‑up academic papers (mostly as a baseline) but never released as a widely used tool.  
* **Reaction‑prediction accuracy** has improved overall, especially for *known* reaction classes. For *truly novel* transformations, modern models still hover around 40‑50 % top‑1 accuracy, similar to the Münster 35 % figure, indicating that the fundamental challenge remains.  
* **Policy & funding** – The rise of AI‑driven chemistry attracted significant public and private investment (e.g., DARPA’s “Accelerating Chemical Discovery” program, EU Horizon 2020 projects). This broader trend validates the article’s claim that high‑throughput prediction would become a strategic priority, even though the specific graph‑approach did not dominate.  
* **Business impact** – Companies such as **BenevolentAI**, **Insilico Medicine**, and **PostEra** have built pipelines that combine reaction prediction with synthesis planning. Their success stories (e.g., rapid synthesis routes for COVID‑19 antivirals in 2020‑2021) illustrate that the *concept* of data‑driven reaction discovery matured, but the *implementation* shifted toward deep‑learning architectures rather than pure graph similarity.  

---

## 3. PREDICTIONS  

| Prediction made (or implied) in the article | What actually happened | Assessment |
|----------------------------------------------|------------------------|------------|
| **“Accuracy improves linearly with graph size.”** | Larger reaction corpora (USPTO > 1 M, Reaxys > 10 M) did enable higher top‑1 scores for many models, but the relationship became **sub‑linear** once deep‑learning architectures were introduced; model capacity and representation learning mattered more than raw size. | Partially correct – more data helps, but the scaling law changed with algorithmic advances. |
| **“The method can suggest useful, undocumented transformations.”** | Some groups (e.g., **MIT ASKCOS**, **IBM RXN**) have indeed identified previously unreported reactions that were later validated experimentally, but these successes were largely driven by transformer‑based models, not the Münster similarity graph. | The *idea* proved true; the *specific* graph method did not become the primary driver. |
| **“Two‑thirds of novel predictions would waste chemists’ time.”** | Modern tools still report that a sizable fraction of top‑k suggestions are chemically implausible, leading to “filter‑first” workflows. However, the community now routinely screens predictions with rapid *in‑silico* feasibility checks, reducing wasted effort. | The concern remains valid; mitigation strategies have emerged. |
| **“The approach will expose regions of synthetic space that are rich or poor in predictable transformations.”** | Recent network‑analysis studies (e.g., 2022 – 2023 papers on “synthetic accessibility” and “reaction coverage”) have mapped “hot spots” in chemical space, but they rely on a combination of reaction databases, ML scores, and expert rules rather than the Münster graph alone. | Conceptually realized, but via more sophisticated hybrid methods. |

---

## 4. INTEREST  

**Rating: 6/10**  

The article is a clear snapshot of the state of AI‑assisted reaction prediction just before the deep‑learning revolution. It is interesting for historians of the field and for understanding why graph‑similarity methods fell out of favor, but it does not introduce a technology that persisted as a dominant tool.


----
_model_params = {'model': 'openai/gpt-oss-120b:free', 'input': '20160831-predicting-new-reactions.txt', 'reasoning': {'effort': 'high'}, 'text': {'verbosity': 'medium'}, 'prompt-template': 'prompt-template-2'}_