# Data — canonical datasets & dictionary

This folder is the **machine-readable heart** of the repository. Everything else (catalog
pages, figures, the interactive website) is generated from the JSON files here by
[`../scripts/build.py`](../scripts/build.py).

## Files

| File | Source of truth? | Description |
|---|---|---|
| `papers.json` | ✅ edit this | The curated bibliography (one record per paper). |
| `papers.csv` | generated | Flattened bibliography for spreadsheets / pandas. |
| `papers.bib` | generated | BibTeX for all papers, ready to drop into a reference manager. |
| `ontologies.json` | ✅ edit this | Manufacturing/industrial ontology catalog. |
| `tools.json` | ✅ edit this | KG software & tools catalog. |
| `standards.json` | ✅ edit this | Industrial & semantic-web standards catalog. |
| `*.csv` | generated | CSV mirror of each catalog. |

**Workflow:** edit a `*.json` file → run `python3 scripts/build.py` → commit the regenerated
CSV/BibTeX/Markdown/figures alongside it.

## `papers.json` schema

```jsonc
{
  "id":      "xiao2023processplanning",      // stable citation key (also the BibTeX key)
  "year":    2023,                            // integer publication year
  "title":   "Knowledge graph-based ...",     // full title
  "authors": ["Xiao, Y.", "Zheng, S.", "..."],// list; "et al." allowed when truncated
  "venue":   "Journal of Manufacturing Systems",
  "type":    "journal",                       // journal|conference|workshop|chapter|preprint
  "doi":     "10.1016/j.jmsy.2023.08.006",    // DOI without the resolver, or null
  "url":     "https://doi.org/10.1016/...",   // resolvable link (required)
  "tags":    ["survey", "process-planning"]   // controlled vocabulary (see below)
}
```

## Controlled tag vocabulary

Tags map onto the [taxonomy](../taxonomy.md). Use existing tags where possible; propose new
ones in a pull request.

`survey` · `kg-construction` · `ontology` · `digital-twin` · `cps` · `iiot` ·
`predictive-maintenance` · `quality-control` · `root-cause` · `process-planning` ·
`process-optimization` · `resource-allocation` · `factory-planning` · `supply-chain` ·
`product-design` · `materials` · `additive-manufacturing` · `robotics` ·
`gnn-embedding` · `llm-rag` · `explainability` · `interoperability` · `standards` · `human-ai`

## Provenance & integrity rules

This dataset follows three rules so it stays trustworthy and citable:

1. **Every record resolves.** Each paper, ontology, tool and standard has a real, working
   URL. DOIs are preferred for papers.
2. **No invented metadata.** Where a field (e.g. a license) could not be verified from the
   source, it is recorded as `unverified` rather than guessed. `unverified` is *not* a claim
   that something is unlicensed — only that the source page did not state it.
3. **Scope is stated, not exaggerated.** The 2016–2022 records come from the peer-reviewed
   survey this repository accompanies; 2023–2026 records are community additions verified
   against publisher/Crossref/arXiv records.

## Coverage at a glance

- **64** papers, spanning **2016–2026**
- **24** ontologies · **33** tools · **18** standards

Counts are asserted by `scripts/build.py` on every build; see
[`../scripts/validate.py`](../scripts/validate.py) for the link/consistency checks.
