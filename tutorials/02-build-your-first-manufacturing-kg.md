# Tutorial 2 — Build Your First Manufacturing Knowledge Graph

In ~20 minutes you will model a small **CNC machining cell** as a knowledge graph in RDF/Turtle
and answer real questions with SPARQL — including a predictive-maintenance query. Everything
runs locally with one dependency.

> New to the vocabulary? Skim [Tutorial 1 — Concepts](01-concepts.md) first.

## Setup

```bash
pip install rdflib
```

That is the only requirement. The example files live in this folder.

## Step 1 — Understand the scenario

Our cell has a CNC mill and a lathe. The mill runs a milling operation that turns Aluminium
6061 into a mounting bracket. A vibration sensor watches the mill's spindle; rising vibration
indicates spindle-bearing wear. We want a graph that captures these *things* and their
*relationships*.

## Step 2 — Read the graph

Open [`example-manufacturing-kg.ttl`](example-manufacturing-kg.ttl). It has two parts.

**The schema** (a tiny ontology) declares the classes and properties:

```turtle
ex:Machine     a owl:Class ; rdfs:label "Machine" .
ex:Process     a owl:Class ; rdfs:label "Manufacturing process" .
ex:produces    a owl:ObjectProperty ; rdfs:domain ex:Process ; rdfs:range ex:Product .
```

**The data** (instances) describes the actual cell and reuses W3C **SOSA** for sensing:

```turtle
ex:CNCMill1 a ex:Machine ; rdfs:label "CNC milling machine #1" ;
    ex:hasFailureMode ex:SpindleWear .

ex:Obs2 a sosa:Observation ;
    sosa:madeBySensor ex:VibrationSensor1 ;
    sosa:hasSimpleResult "4.8"^^xsd:double .
```

Notice how `ex:` terms (manufacturing-specific) mix freely with `sosa:` terms (a reused
standard vocabulary) — that is interoperability in action.

## Step 3 — Run the queries

```bash
python3 run_example.py
```

You should see the graph load (71 triples) and four query results. The runner reads every
query from [`queries.sparql`](queries.sparql).

### Q1 — Machines and their failure modes
```
CNC lathe #1            |
CNC milling machine #1  | Spindle bearing wear
```
`OPTIONAL` keeps the lathe in the results even though it has no recorded failure mode.

### Q2 — Process → product → machine → material
```
Milling operation for bracket A | Mounting bracket A | CNC milling machine #1 | Aluminium 6061-T6
```
This traverses four relationships in one pattern using property paths (`ex:produces/rdfs:label`).

### Q3 — Predictive maintenance (the interesting one)
```
Spindle bearing wear | CNC milling machine #1 | 4.8
```
It joins a **failure mode** to the **sensor** that indicates it, then to that sensor's
**observations**, and keeps only readings above 4.0 — surfacing an at-risk machine from raw
sensor data and domain knowledge together. This is the essence of a KG-driven maintenance
assistant.

### Q4 — Inventory by type
A `GROUP BY` count of every instance, grouped by class.

## Step 4 — Extend it (exercises)

1. **Add a machine.** Give `ex:Lathe1` a failure mode and a sensor with two observations, then
   re-run Q1 and Q3.
2. **Add an operator query.** Write a SPARQL query listing each operator and the machines they
   operate (hint: `ex:operates`).
3. **Lower the threshold.** Change `4.0` to `2.0` in Q3 — which machines now appear, and why?
4. **Validate with SHACL.** Install `pyshacl`, write a shape requiring every `ex:Machine` to
   have an `ex:criticality`, and check the graph. Which machine fails, if any?
5. **Reuse a real ontology.** Map `ex:FailureMode` to a class from the IOF Maintenance ontology
   (see the [ontology catalog](../catalog/ontologies.md)) and discuss what interoperability you gain.

## Where to go next

- Browse the [literature explorer](https://jorge-martinez-gil.github.io/knowledge-graphs-manufacturing/)
  and filter by `predictive-maintenance` or `digital-twin` to see how researchers scale these ideas.
- Pick a triplestore from the [tools catalog](../catalog/tools.md) (e.g. Apache Jena Fuseki,
  GraphDB) and load the Turtle file to query it over HTTP.
- Read the [taxonomy](../taxonomy.md) to place your graph within the wider field.

---

*Built something with this? Contributions of new examples and exercises are welcome — see
[CONTRIBUTING](../CONTRIBUTING.md).*
