# Manufacturing Knowledge-Graph Datasets & Benchmarks

A curated, **community-growing** catalog of openly available datasets, knowledge graphs and
benchmarks relevant to manufacturing. The goal is to make empirical work in this field
**reproducible**: where a paper in our [bibliography](../data/papers.json) releases data, it
belongs here with a resolvable link and provenance.

> This catalog is deliberately conservative — it lists only resources we can verify. It is
> also the part of the repository where contributions help most. If you know an open
> manufacturing KG, ontology population, or benchmark, please
> [add it](../../issues/new?template=add_resource.yml).

## Open datasets & knowledge graphs

| Resource | Domain | Description | Source |
|---|---|---|---|
| **FabKG** | Manufacturing science | A knowledge graph of the manufacturing-science domain built from textbooks and crowd-sourced annotations (Kumar et al., 2022). | [arXiv:2206.10318](https://doi.org/10.48550/arXiv.2206.10318) |
| **FabNER** | Manufacturing NLP | Named-entity-recognition dataset over manufacturing process-science literature; useful for KG construction from text (Kumar & Starly, 2022). | [doi.org/10.1007/s10845-021-01807-x](https://doi.org/10.1007/s10845-021-01807-x) |
| **IOF reference ontologies** | Cross-domain manufacturing | Reference ontologies (Core, Maintenance, Supply Chain) that double as schemas/seed graphs for industrial KGs. | [github.com/iofoundry/ontology](https://github.com/iofoundry/ontology) |

## Where to find more data in this repository

Many empirical papers release evaluation data or graphs. Filter the bibliography to find
them quickly:

- Papers tagged **`kg-construction`** typically describe a constructed graph and its sources.
- Papers tagged **`gnn-embedding`** often evaluate on a released triple set.
- The [interactive explorer](https://jorge-martinez-gil.github.io/knowledge-graphs-manufacturing/)
  lets you filter by tag and jump straight to each paper.

## How to evaluate a manufacturing knowledge graph (checklist)

When assessing a dataset/KG for reuse, this repository recommends recording — transparently —
the following, in line with **FAIR** principles. (We do *not* publish scored rankings of
third-party resources; we provide the criteria so you can assess them consistently.)

1. **Findable** — does it have a persistent identifier (DOI) and rich metadata?
2. **Accessible** — is it downloadable under a stated license?
3. **Interoperable** — RDF/OWL or a documented schema; alignment to standard vocabularies?
4. **Reusable** — clear provenance, versioning, and usage license.
5. **Scale & quality** — number of entities/relations, and how quality was assessed.
6. **Reasoning support** — are OWL semantics / SHACL shapes provided?
7. **Maintenance** — last update and whether it is actively maintained.

---

*Contributions that add verifiable open datasets — especially with provenance and licensing —
are the single most valuable way to grow this catalog.*
