# Knowledge Graph Software & Tools Catalog

A curated, verifiable catalog of open-source and commercial software for building, storing, reasoning over, validating, embedding, querying and visualizing knowledge graphs - the practical toolchain behind manufacturing KGs. Every entry links to a homepage or source repository.

**33 tools across 10 categories.** Generated from `data/tools.json` by `scripts/build.py`.

## KG embeddings / ML

| Tool | Description | License |
|---|---|---|
| [PyKEEN](https://github.com/pykeen/pykeen) | Python library for training and evaluating knowledge graph embedding models | MIT |
| [AmpliGraph](https://github.com/Accenture/AmpliGraph) | TensorFlow-based library for knowledge graph representation learning | Apache-2.0 |
| [DGL-KE](https://github.com/awslabs/dgl-ke) | Scalable package for large-scale knowledge graph embeddings, built on DGL | Apache-2.0 |
| [OpenKE](https://github.com/thunlp/OpenKE) | Open-source knowledge embedding toolkit (PyTorch/TensorFlow) from Tsinghua NLP | MIT |
| [LibKGE](https://github.com/uma-pi1/kge) | PyTorch KG embedding library for reproducible research and HPO studies | MIT |

## Mapping / ETL

| Tool | Description | License |
|---|---|---|
| [RMLMapper](https://github.com/RMLio/rmlmapper-java) | Java engine executing RML rules to generate RDF from CSV, JSON, XML, DBs, APIs | MIT |
| [Morph-KGC](https://github.com/morph-kgc/morph-kgc) | Scalable RDF KG construction engine for R2RML/RML mappings (Python) | Apache-2.0 |
| [D2RQ](http://d2rq.org/) | Maps relational databases to virtual RDF graphs with a SPARQL-to-SQL engine | Apache-2.0 |

## Mapping / ETL (OBDA)

| Tool | Description | License |
|---|---|---|
| [Ontop](https://ontop-vkg.org/) | Virtual knowledge graph system exposing relational DBs as RDF via SPARQL-to-SQL | Apache-2.0 |

## Ontology editor

| Tool | Description | License |
|---|---|---|
| [Protege](https://protege.stanford.edu/) | Stanford's widely used OWL 2 ontology editor with reasoner integration | BSD-2-Clause |
| [WebProtege](https://webprotege.stanford.edu/) | Cloud-based collaborative OWL ontology editor from Stanford | BSD-2-Clause |

## Ontology editor / Governance

| Tool | Description | License |
|---|---|---|
| [TopBraid EDG](https://www.topquadrant.com/topbraid-edg/) | Enterprise data governance platform on RDF knowledge graphs and SHACL | proprietary |

## Query

| Tool | Description | License |
|---|---|---|
| [YASGUI](https://github.com/TriplyDB/Yasgui) | Browser-based SPARQL query editor with autocompletion and result views | MIT |

## Reasoner

| Tool | Description | License |
|---|---|---|
| [HermiT](http://www.hermit-reasoner.com/) | OWL 2 DL reasoner using a hypertableau calculus | LGPL-3.0 |
| [Pellet](https://github.com/stardog-union/pellet) | OWL 2 DL reasoner in Java (maintained by Stardog Union) | AGPL-3.0 |
| [Openllet](https://github.com/Galigator/openllet) | OWL 2 reasoner in Java built on Pellet (OWL API 5 compatible) | AGPL-3.0 |
| [ELK](https://github.com/liveontologies/elk-reasoner) | High-performance OWL 2 EL profile reasoner | Apache-2.0 |

## SHACL / Validation

| Tool | Description | License |
|---|---|---|
| [pySHACL](https://github.com/RDFLib/pySHACL) | Pure-Python validator for RDF graphs against SHACL shapes (built on RDFLib) | Apache-2.0 |
| [TopBraid SHACL API](https://github.com/TopQuadrant/shacl) | Java SHACL Core + SHACL-SPARQL reference implementation on Apache Jena | Apache-2.0 |
| [SHACL Play!](https://shacl-play.sparna.fr/) | Web-based SHACL validator plus docs/diagram/SHACL generators (Sparna) | LGPL-3.0 |

## Triplestore / Graph DB

| Tool | Description | License |
|---|---|---|
| [GraphDB](https://www.ontotext.com/products/graphdb/) | Enterprise RDF triplestore by Ontotext with reasoning, SHACL and SPARQL | proprietary (Workbench UI Apache-2.0) |
| [Apache Jena / Fuseki](https://jena.apache.org/) | Java RDF framework with TDB store and Fuseki SPARQL 1.1 server | Apache-2.0 |
| [Stardog](https://www.stardog.com/) | Enterprise knowledge graph platform with RDF storage, reasoning and virtualization | proprietary (free tier) |
| [Virtuoso](https://github.com/openlink/virtuoso-opensource) | Multi-model RDBMS, RDF triplestore and SPARQL/Linked Data server | GPL-2.0 (open edition) |
| [Blazegraph](https://github.com/blazegraph/database) | High-performance RDF/SPARQL graph database (powers Wikidata Query Service) | GPL-2.0 (dual) |
| [Neo4j](https://github.com/neo4j/neo4j) | Native property-graph database with the Cypher query language | GPLv3 (Community) |
| [RDFox](https://www.oxfordsemantic.tech/rdfox) | In-memory RDF store with Datalog (OWL 2 RL) and SWRL reasoning, SPARQL | proprietary |
| [Amazon Neptune](https://aws.amazon.com/neptune/) | Fully managed AWS graph database supporting RDF/SPARQL and property graphs | proprietary (managed) |
| [Oxigraph](https://github.com/oxigraph/oxigraph) | SPARQL 1.1 graph database written in Rust, based on RocksDB | Apache-2.0 OR MIT |
| [QLever](https://github.com/ad-freiburg/qlever) | Very fast SPARQL engine scaling to trillions of triples with text search | Apache-2.0 |

## Visualization

| Tool | Description | License |
|---|---|---|
| [WebVOWL](http://vowl.visualdataweb.org/webvowl.html) | Interactive web-based visualizer for OWL ontologies using the VOWL notation | MIT |
| [Gephi](https://gephi.org/) | Open-source desktop platform for visualizing and analyzing large graphs | CDDL-1.0 / GPL-3.0 |
| [yEd](https://www.yworks.com/products/yed) | Free desktop graph/diagram editor from yWorks | proprietary freeware |

> Know a tool we should add? [Open an issue](../../issues/new?template=add_resource.yml).
