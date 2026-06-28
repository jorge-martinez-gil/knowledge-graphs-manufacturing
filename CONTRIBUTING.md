# Contributing

Thank you for helping make this the definitive open reference for **knowledge graphs in
manufacturing**! Contributions of all sizes are welcome — a single missing paper is a
valuable contribution.

## Ways to contribute

- 📄 **Add a paper** to the bibliography (2016–present).
- 🧩 **Add a resource** — a manufacturing ontology, a KG tool, a standard, or an open dataset.
- 🐛 **Fix metadata** — a wrong year, author, DOI or dead link.
- 🧭 **Improve the taxonomy, tutorials, or figures.**

The fastest path is to **open an issue** using one of our templates
([add a paper](../../issues/new?template=add_paper.yml) ·
[add a resource](../../issues/new?template=add_resource.yml)). Prefer a pull request? Read on.

## Golden rule: everything must be verifiable

This repository is trusted because every entry is real and sourced. Please:

1. **Provide a resolvable link** for every entry (a DOI for papers; a homepage or repo for
   tools/ontologies/standards).
2. **Do not guess metadata.** If you can't verify a field (e.g. a license), leave it empty or
   write `unverified` — never invent it.
3. **No fabricated benchmark numbers or rankings.** We publish *criteria* for evaluation, not
   invented scores for third-party resources.

## Editing the data (pull request)

The data lives in **`data/*.json`** — these are the single source of truth. Everything else
(CSV, BibTeX, catalog Markdown, figures, the website's `papers.json`) is **generated**.

1. Add or edit a record in the relevant JSON file. For papers, follow the schema in
   [`data/README.md`](data/README.md) and use a tag from the controlled vocabulary.
2. Regenerate derived files and validate (Python 3.8+, no dependencies):

   ```bash
   python3 scripts/build.py      # regenerates CSV, BibTeX, catalogs, figures, docs/papers.json
   python3 scripts/validate.py   # checks links, fields, tags, uniqueness, sync
   ```

3. Commit **both** the JSON change and the regenerated files.
4. Open a pull request describing what you added and where you verified it.

`validate.py` runs automatically on every pull request (see
[`.github/workflows/validate.yml`](.github/workflows/validate.yml)); a green check means the
data is consistent.

## Paper record example

```json
{
  "id": "lastname2025keyword",
  "year": 2025,
  "title": "Full paper title",
  "authors": ["Lastname, A.", "Other, B."],
  "venue": "Journal or Conference name",
  "type": "journal",
  "doi": "10.xxxx/xxxxx",
  "url": "https://doi.org/10.xxxx/xxxxx",
  "tags": ["digital-twin", "ontology"]
}
```

## Code of conduct

By participating you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md). Be kind and
constructive.

— Thanks again! Every verified addition makes this resource more useful to the whole field.
