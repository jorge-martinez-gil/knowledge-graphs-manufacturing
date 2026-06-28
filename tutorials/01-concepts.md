# Tutorial 1 — Concepts: Knowledge Graphs for Manufacturing

A plain-language primer on the ideas behind **knowledge graphs in manufacturing**. No prior
semantic-web background needed. Each concept is grounded in a shop-floor example.

## Why a knowledge graph?

A factory's knowledge lives in many disconnected places: a CAD model, a maintenance log, an
MES database, an OPC UA server, an operator's experience. A **knowledge graph (KG)** connects
these as a network of *things* and *relationships* with explicit meaning, so both people and
machines can query and reason over them. Instead of asking five systems "what do you know
about machine #1?", you ask one graph.

A KG is built from **triples** — small statements of the form *subject → predicate → object*:

```
CNCMill1   hasFailureMode   SpindleWear
SpindleWear indicatedBy     VibrationSensor1
MillingOp1  produces        BracketA
```

Chain enough triples together and you get a graph you can traverse: *which products are at
risk if a given sensor trips?*

## RDF — the data model

**RDF (Resource Description Framework)** is the W3C standard for expressing triples. Things are
named with IRIs (web-style identifiers), so `CNCMill1` becomes
`https://example.org/mfg#CNCMill1`. RDF can be written in several syntaxes; we use **Turtle**,
the most human-readable one:

```turtle
@prefix ex: <https://example.org/mfg#> .
ex:CNCMill1 a ex:Machine ;
    ex:hasFailureMode ex:SpindleWear .
```

`a` is shorthand for "is a / has type". The `;` lets you add more statements about the same
subject. (See [`example-manufacturing-kg.ttl`](example-manufacturing-kg.ttl).)

## Ontologies and OWL — the schema and meaning

An **ontology** defines the *vocabulary*: the classes (Machine, Process, FailureMode), the
properties (`produces`, `performedOn`) and the rules relating them. **OWL (Web Ontology
Language)** lets you state this formally — e.g. that `produces` only links a `Process` to a
`Product`, or that every `MachiningProcess` is a kind of `Process`. A **reasoner** can then
infer new facts (if X is a MachiningProcess, X is a Process) and detect contradictions.

Manufacturing rarely starts from scratch: reusable ontologies exist for the domain (MASON, the
Industrial Ontologies Foundry, P-PSO, SAREF4INMA, and more — see the
[ontology catalog](../catalog/ontologies.md)). Reusing them is what makes graphs from different
sources **interoperable**.

## SPARQL — the query language

**SPARQL** is to RDF what SQL is to relational tables. You describe a pattern of triples with
variables (prefixed `?`), and the engine returns every match:

```sparql
SELECT ?machine ?failure WHERE {
  ?m a ex:Machine ; rdfs:label ?machine ;
     ex:hasFailureMode ?f .
  ?f rdfs:label ?failure .
}
```

Tutorial 2 runs queries like this, including a predictive-maintenance query that joins sensor
readings to failure modes.

## SHACL — validation and data quality

**SHACL (Shapes Constraint Language)** checks that a graph meets expectations: "every Machine
must have a criticality", "a Process must produce at least one Product". In manufacturing,
where data feeds decisions, this guards quality before bad data propagates. SHACL *shapes* are
themselves written in RDF.

## How these fit together

```
Industrial data  ──►  RDF triples  ──►  Ontology (OWL) gives meaning
   (sensors, MES,        (the graph)        + SHACL checks quality
    OPC UA, docs)                           + SPARQL answers questions
                                            + reasoning/embeddings add inferences
```

See the [technology-stack figure](../figures/technology_landscape.svg) for the full pipeline.

## The manufacturing context: Industry 4.0, 5.0, digital twins

- **Industry 4.0** — the drive to connect machines, products and systems into smart,
  data-driven factories (IIoT, cyber-physical systems). KGs are the semantic glue that makes
  the connected data *meaningful and interoperable*.
- **Industry 5.0** — adds a human-centric, sustainable and resilient lens on top of 4.0. KGs
  support explainable, human-in-the-loop decisions (e.g. a maintenance copilot that can justify
  its advice).
- **Cyber-physical systems (CPS)** — physical assets tightly coupled with computation. A KG
  gives a CPS a shared semantic model of itself and its environment.
- **Digital twin** — a live virtual replica of a physical asset/process. A *knowledge-graph-backed*
  ("cognitive") digital twin stores not just sensor values but the *relationships and knowledge*
  needed to reason about them.

## Learning more: KG embeddings & GNNs

Beyond logic-based reasoning, KGs can be turned into vectors. **Knowledge graph embeddings**
(TransE, RotatE, …) and **graph neural networks (GNNs)** learn patterns for tasks like link
prediction (suggesting a likely missing relationship) and similarity. Tools such as PyKEEN and
DGL-KE (see the [tools catalog](../catalog/tools.md)) implement these.

---

**Next:** [Build your first manufacturing knowledge graph →](02-build-your-first-manufacturing-kg.md)
