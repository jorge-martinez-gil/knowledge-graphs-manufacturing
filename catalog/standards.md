# Industrial Standards for Semantic Interoperability

Standards that manufacturing knowledge graphs map to, align with, or build upon - from Industry 4.0 reference architectures (RAMI 4.0, Asset Administration Shell) and communication/information models (OPC UA, ISA-95, AutomationML) to the W3C Semantic Web stack (RDF, OWL, SHACL, SPARQL, PROV-O).

**18 standards.** Generated from `data/standards.json` by `scripts/build.py`.

| Standard | Full name / number | Purpose | Governing body |
|---|---|---|---|
| [RAMI 4.0](https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/rami40-an-introduction.html) | Reference Architecture Model Industrie 4.0 (DIN SPEC 91345:2016) | 3D reference architecture structuring I4.0 assets across lifecycle, hierarchy, layers | Plattform Industrie 4.0 / ZVEI / DIN |
| [AAS](https://webstore.iec.ch/en/publication/65628) | Asset Administration Shell - IEC 63278-1:2023 | Standardized digital-twin / interoperable digital representation of industrial assets | IEC TC 65 / IDTA |
| [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) | IEC 62541 (OPC Unified Architecture) | Platform-independent service-oriented communication & information modeling for industry | OPC Foundation / IEC TC 65 |
| [ISA-95](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard) | IEC 62264 / ANSI-ISA-95 | Models & terminology for integrating enterprise (ERP) and control (MES) systems | ISA / IEC TC 65 |
| [ISA-88](https://www.isa.org/standards-and-publications/isa-standards/isa-88-standards) | IEC 61512 / ANSI-ISA-88 | Reference models & terminology for batch process control (recipes, equipment) | ISA / IEC TC 65 |
| [IEC 61499](https://webstore.iec.ch/en/publication/5506) | IEC 61499 Function blocks | Event-driven function-block architecture for distributed, reconfigurable control | IEC TC 65 |
| [AutomationML](https://www.automationml.org/about-automationml/specifications/) | IEC 62714 | Open XML/CAEX-based format for exchanging engineering data across tools | IEC TC 65 / AutomationML e.V. |
| [ECLASS](https://eclass.eu/en/) | ECLASS classification standard (ISO 13584 / IEC 61360 compliant) | Standardized classification system & property dictionary for product master data | ECLASS e.V. |
| [ISO 10303 (STEP)](https://www.iso.org/standard/72237.html) | ISO 10303 - Product data representation and exchange | Computer-interpretable representation & exchange of product data (CAD/CAM/PDM) | ISO TC 184/SC 4 |
| [ISO 15926](https://www.iso.org/standard/29557.html) | ISO 15926 - Integration of life-cycle data for process plants | Conceptual data model & reference data for process-plant lifecycle information | ISO TC 184/SC 4 |
| [MTConnect](https://www.mtconnect.org/) | ANSI/MTC1.4 (MTConnect Standard) | Open, royalty-free XML semantic vocabulary/protocol to read data from equipment | MTConnect Institute (AMT) |
| [QIF](https://qifstandards.org/) | Quality Information Framework (ISO 23952:2020) | Unified XML framework for exchanging metrology/quality information across the MBE lifecycle | DMSC / ISO |
| [RDF](https://www.w3.org/TR/rdf11-concepts/) | RDF 1.1 Concepts and Abstract Syntax | Graph-based data model of subject-predicate-object triples | W3C |
| [RDF 1.2 / RDF-star](https://www.w3.org/TR/rdf12-concepts/) | RDF 1.2 Concepts and Abstract Data Model | Adds triple terms (statements about statements) for edge-level metadata | W3C |
| [OWL 2](https://www.w3.org/TR/owl2-overview/) | OWL 2 Web Ontology Language | Formal ontology language for the Semantic Web with defined semantics | W3C |
| [SHACL](https://www.w3.org/TR/shacl/) | Shapes Constraint Language | Language for validating RDF graphs against constraints expressed as shapes | W3C |
| [SPARQL 1.1](https://www.w3.org/TR/sparql11-query/) | SPARQL 1.1 Query Language | Query language and protocol for retrieving and manipulating RDF data | W3C |
| [PROV-O](https://www.w3.org/TR/prov-o/) | PROV-O: The PROV Ontology | OWL 2 ontology for representing & interchanging provenance | W3C |

### How these relate to a manufacturing KG

- **RAMI 4.0 / AAS** give the *architecture and digital-twin container* a KG can populate and link.
- **ISA-95 / ISA-88** supply the *enterprise-control and batch vocabularies* often reused as KG schema.
- **OPC UA / AutomationML / MTConnect** are the *runtime and engineering data sources* lifted into RDF.
- **RDF / OWL / SHACL / SPARQL / PROV-O** are the *representation, validation, query and provenance layer* of the KG itself.

> See also the [ontology catalog](ontologies.md) for OWL renderings of several of these standards.
