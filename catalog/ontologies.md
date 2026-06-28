# Manufacturing & Industrial Ontology Catalog

A curated, verifiable catalog of ontologies relevant to knowledge graphs in manufacturing: upper ontologies, manufacturing-domain ontologies, sensor/IoT vocabularies, and digital-twin/standard renderings. Every entry links to a real, resolvable source. `unverified` in the License column means the source page did not state a license (it is **not** a claim that the resource is unlicensed).

**24 ontologies.** Generated from `data/ontologies.json` by `scripts/build.py`.

| Name | Full name | Scope | License |
|---|---|---|---|
| [MASON](https://sourceforge.net/projects/mason-onto/) | MAnufacturing's Semantics ONtology | Upper/domain ontology for manufacturing (entities, operations, resources; OWL-DL) | unverified |
| [IOF-Core](https://spec.industrialontologies.org/iof/ontology/core/Core/) | Industrial Ontologies Foundry Core Ontology | BFO-aligned mid-level ontology of terms common across manufacturing operations | MIT |
| [IOF-Maintenance](https://spec.industrialontologies.org/iof/ontology/maintenance/Maintenance/) | IOF Maintenance Reference Ontology | IOF/BFO-aligned modular ontology for industrial maintenance (OWL 2 DL) | MIT |
| [IOF-SupplyChain](https://github.com/iofoundry/ontology) | IOF Supply Chain Reference Ontology (SCRO) | IOF Core extension for supply chain & logistics interoperability | MIT |
| [P-PSO](https://link.springer.com/chapter/10.1007/978-3-319-22759-7_56) | Politecnico di Milano Production Systems Ontology | Meta-model/domain ontology of production systems (discrete + process, logistics) | unverified |
| [MSDL](https://labs.engineering.asu.edu/semantics/ontology-download/msdl-ontology/) | Manufacturing Service Description Language | OWL-DL ontology for manufacturing service/capability description & supplier matchmaking | unverified |
| [ADACOR](https://www.researchgate.net/publication/226253278_Foundations_for_a_Core_Ontology_of_Manufacturing) | ADAptive holonic COntrol aRchitecture core ontology | DOLCE-aligned ontology for holonic/distributed manufacturing control | unverified |
| [ONTO-PDM](https://doi.org/10.1016/j.aei.2011.12.002) | Product-driven ONTOlogy for Product Data Management | Product-centric ontology for PDM / product-lifecycle interoperability | unverified |
| [PRONTO](https://www.sciencedirect.com/science/article/abs/pii/S0952197611000388) | PRoduct ONTOlogy (Vegetti, Henning & Leone) | Domain ontology for product information modelling (variants/BOMs) | unverified |
| [MaRCO](https://doi.org/10.1007/s10845-018-1427-6) | Manufacturing Resource Capability Ontology | OWL ontology for resource capabilities + inference of combined capabilities | unverified |
| [OntoCAPE](https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/) | OntoCAPE | Large-scale formal ontology for Computer-Aided Process Engineering | unverified |
| [AAS-RDF](https://github.com/admin-shell-io/aas-specs-metamodel) | Asset Administration Shell RDF/OWL Ontology | Semantic (RDF/OWL) representation of the Industrie 4.0 AAS metamodel | unverified |
| [SAREF](https://saref.etsi.org/core/) | Smart Applications REFerence ontology (Core) | ETSI core ontology for smart appliances/IoT interoperability | ETSI (open) |
| [SAREF4INMA](https://saref.etsi.org/saref4inma/) | SAREF extension for Industry and Manufacturing | ETSI TS 103 410-5 extension (equipment, items, batches, traceability) | ETSI (open) |
| [SSN](https://www.w3.org/TR/vocab-ssn/) | Semantic Sensor Network Ontology | W3C/OGC standard ontology for sensors, observations, sampling, actuation | W3C Document License |
| [SOSA](https://www.w3.org/ns/sosa/) | Sensor, Observation, Sample, and Actuator | Lightweight self-contained core of SSN (W3C Recommendation) | W3C Document License |
| [BFO](https://basic-formal-ontology.org/bfo-2020.html) | Basic Formal Ontology (2020) | Top-level/upper ontology (ISO/IEC 21838-2); foundation for IOF | open (BSD/CC) |
| [CCO](https://github.com/CommonCoreOntology/CommonCoreOntologies) | Common Core Ontologies | BFO-aligned mid-level ontology suite bridging BFO to domain ontologies | BSD-3-Clause |
| [ifcOWL](https://technical.buildingsmart.org/standards/ifc/) | Industry Foundation Classes (OWL) | OWL ontology of the IFC built-environment/AEC data model (ISO 16739) | unverified |
| [DOLCE](https://www.loa.istc.cnr.it/index.php/dolce/) | Descriptive Ontology for Linguistic and Cognitive Engineering | Foundational/top-level ontology (LOA-ISTC-CNR) | unverified |
| [OntoSTEP](https://www.nist.gov/services-resources/software/ontostep-plugin) | OntoSTEP (NIST) | OWL-DL ontology/translation of ISO 10303 STEP product model data | US Govt / public domain |
| [Brick](https://brickschema.org/) | Brick Schema | Ontology for buildings/facility automation systems & assets (smart-factory facility layer) | BSD-3-Clause |
| [OPC-UA-ODP](https://github.com/hsu-aut/IndustrialStandard-ODP-OPC-UA) | OPC UA NodeSet / Ontology Design Pattern (OWL) | OWL ontologies mapping OPC UA information models & companion specs to RDF/OWL | unverified |
| [IndustryPortal](https://industryportal.enit.fr/) | IndustryPortal - FAIR ontology repository for Industry 4.0 | AgroPortal-based registry hosting/curating industrial ontologies (registry hub, not an ontology) | n/a (repository) |

> Found a manufacturing ontology we are missing? [Open an issue](../../issues/new?template=add_resource.yml).
