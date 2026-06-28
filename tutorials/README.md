# Tutorials — Knowledge Graphs in Manufacturing

A hands-on, classroom-ready path from zero to a working **manufacturing knowledge graph**.
Everything here is self-contained and runnable; no proprietary data or services needed.

| # | Tutorial | You will learn |
|---|----------|----------------|
| 1 | [Concepts primer](01-concepts.md) | What KGs, RDF, OWL, SHACL, SPARQL, ontologies, digital twins and Industry 4.0/5.0 actually mean — with manufacturing examples. |
| 2 | [Build your first manufacturing KG](02-build-your-first-manufacturing-kg.md) | Model a CNC machining cell in RDF/Turtle and query it with SPARQL, including a predictive-maintenance query. |

**Files used by Tutorial 2**

- [`example-manufacturing-kg.ttl`](example-manufacturing-kg.ttl) — a small example KG (a CNC cell).
- [`queries.sparql`](queries.sparql) — runnable SPARQL queries.
- [`run_example.py`](run_example.py) — loads the graph and runs every query.

**Quick start**

```bash
pip install rdflib
python3 tutorials/run_example.py
```

For instructors: these materials suit courses in semantic web, manufacturing informatics,
industrial AI and knowledge engineering. They pair with the [taxonomy](../taxonomy.md), the
[ontology catalog](../catalog/ontologies.md) and the [literature database](../data/papers.json).
Reuse is encouraged under the [MIT license](../LICENSE) — a citation of the
[survey](../README.md#-cite-this-work) is appreciated.
