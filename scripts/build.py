#!/usr/bin/env python3
"""
build.py - regenerate every derived artifact in this repository from the
canonical JSON datasets in data/.

Source of truth (edit these): data/papers.json, data/ontologies.json,
data/tools.json, data/standards.json. Everything else is generated.
No third-party dependencies (Python 3.8+ standard library only).
"""
import csv
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CAT = os.path.join(ROOT, "catalog")
FIG = os.path.join(ROOT, "figures")
DOCS = os.path.join(ROOT, "docs")

INK = "#16243a"; MUTED = "#5b6b82"; GRID = "#e3e8ef"
ACCENT = "#1f6feb"; ACCENT2 = "#0a9396"; ACCENT3 = "#ee9b00"
BAND = ["#1f6feb", "#0a9396", "#ee9b00", "#9b2226", "#5e548e", "#2a9d8f",
        "#bb3e03", "#386641", "#7048e8", "#d62828"]


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def write_papers_csv(papers):
    with open(os.path.join(DATA, "papers.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "year", "title", "authors", "venue", "type", "doi", "url", "tags"])
        for p in papers:
            w.writerow([p["id"], p["year"], p["title"], "; ".join(p["authors"]),
                        p["venue"], p["type"], p["doi"] or "", p["url"], "; ".join(p["tags"])])


def bib_type(t):
    return {"journal": "article", "conference": "inproceedings", "workshop": "inproceedings",
            "chapter": "incollection", "preprint": "misc"}.get(t, "misc")


def write_papers_bib(papers):
    lines = []
    for p in papers:
        authors = " and ".join(a for a in p["authors"] if a != "et al.")
        bt = bib_type(p["type"])
        if bt == "article":
            container = "  journal = {{{}}}".format(p["venue"])
        elif p["type"] == "preprint":
            container = "  howpublished = {{{}}}".format(p["venue"])
        else:
            container = "  booktitle = {{{}}}".format(p["venue"])
        fields = ["  title = {{{}}}".format(p["title"]),
                  "  author = {{{}}}".format(authors),
                  "  year = {{{}}}".format(p["year"]), container]
        if p["doi"]:
            fields.append("  doi = {{{}}}".format(p["doi"]))
        fields.append("  url = {{{}}}".format(p["url"]))
        lines.append("@{}{{{},\n".format(bt, p["id"]) + ",\n".join(fields) + "\n}\n")
    with open(os.path.join(DATA, "papers.bib"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_bibliography_md(papers):
    by_year = {}
    for p in papers:
        by_year.setdefault(p["year"], []).append(p)
    lines = [
        "# Bibliography - Knowledge Graphs in Manufacturing\n",
        "Full curated reading list, grouped by year and **generated from "
        "[`data/papers.json`](data/papers.json)** by `scripts/build.py` (do not edit by hand).\n",
        "Prefer to search and filter? Use the "
        "[interactive explorer](https://jorge-martinez-gil.github.io/knowledge-graphs-manufacturing/). "
        "Need citations? See [`data/papers.bib`](data/papers.bib).\n",
        "**{} papers - {}-{}.**\n".format(len(papers), min(by_year), max(by_year)),
    ]
    for year in sorted(by_year, reverse=True):
        rows = sorted(by_year[year], key=lambda r: r["authors"][0])
        n = len(rows)
        noun = "paper" if n == 1 else "papers"
        lines.append("## {} ({} {})\n".format(year, n, noun))
        for p in rows:
            tags = " ".join("`" + t + "`" for t in p["tags"])
            authors = ", ".join(p["authors"])
            lines.append("- **[{}]({})** - {}. *{}*. {}".format(
                p["title"], p["url"], authors, p["venue"], tags))
        lines.append("")
    with open(os.path.join(ROOT, "BIBLIOGRAPHY.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_catalog_csv(rows, name, cols):
    with open(os.path.join(DATA, name), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def write_ontologies_md(onts):
    rows = [["[{}]({})".format(o["name"], o["url"]), o["full_name"], o["scope"], o["license"]] for o in onts]
    body = (
        "# Manufacturing & Industrial Ontology Catalog\n\n"
        "A curated, verifiable catalog of ontologies relevant to knowledge graphs in "
        "manufacturing: upper ontologies, manufacturing-domain ontologies, sensor/IoT "
        "vocabularies, and digital-twin/standard renderings. Every entry links to a real, "
        "resolvable source. `unverified` in the License column means the source page did "
        "not state a license (it is **not** a claim that the resource is unlicensed).\n\n"
        "**{} ontologies.** Generated from `data/ontologies.json` by `scripts/build.py`.\n\n".format(len(onts))
        + md_table(["Name", "Full name", "Scope", "License"], rows) +
        "\n\n> Found a manufacturing ontology we are missing? "
        "[Open an issue](../../issues/new?template=add_resource.yml).\n")
    with open(os.path.join(CAT, "ontologies.md"), "w", encoding="utf-8") as f:
        f.write(body)


def write_tools_md(tools):
    cats = {}
    for t in tools:
        cats.setdefault(t["category"], []).append(t)
    parts = [
        "# Knowledge Graph Software & Tools Catalog\n",
        "A curated, verifiable catalog of open-source and commercial software for building, "
        "storing, reasoning over, validating, embedding, querying and visualizing knowledge "
        "graphs - the practical toolchain behind manufacturing KGs. Every entry links to a "
        "homepage or source repository.\n",
        "**{} tools across {} categories.** Generated from `data/tools.json` by `scripts/build.py`.\n".format(len(tools), len(cats))]
    for c in sorted(cats):
        rows = [["[{}]({})".format(t["name"], t["url"]), t["description"], t["license"]] for t in cats[c]]
        parts.append("## {}\n\n".format(c) + md_table(["Tool", "Description", "License"], rows) + "\n")
    parts.append("> Know a tool we should add? [Open an issue](../../issues/new?template=add_resource.yml).\n")
    with open(os.path.join(CAT, "tools.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


def write_standards_md(stds):
    rows = [["[{}]({})".format(s["name"], s["url"]), s["full_name"], s["purpose"], s["body"]] for s in stds]
    body = (
        "# Industrial Standards for Semantic Interoperability\n\n"
        "Standards that manufacturing knowledge graphs map to, align with, or build upon - "
        "from Industry 4.0 reference architectures (RAMI 4.0, Asset Administration Shell) and "
        "communication/information models (OPC UA, ISA-95, AutomationML) to the W3C Semantic "
        "Web stack (RDF, OWL, SHACL, SPARQL, PROV-O).\n\n"
        "**{} standards.** Generated from `data/standards.json` by `scripts/build.py`.\n\n".format(len(stds))
        + md_table(["Standard", "Full name / number", "Purpose", "Governing body"], rows) +
        "\n\n### How these relate to a manufacturing KG\n\n"
        "- **RAMI 4.0 / AAS** give the *architecture and digital-twin container* a KG can populate and link.\n"
        "- **ISA-95 / ISA-88** supply the *enterprise-control and batch vocabularies* often reused as KG schema.\n"
        "- **OPC UA / AutomationML / MTConnect** are the *runtime and engineering data sources* lifted into RDF.\n"
        "- **RDF / OWL / SHACL / SPARQL / PROV-O** are the *representation, validation, query and provenance layer* of the KG itself.\n\n"
        "> See also the [ontology catalog](ontologies.md) for OWL renderings of several of these standards.\n")
    with open(os.path.join(CAT, "standards.md"), "w", encoding="utf-8") as f:
        f.write(body)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_open(w, h, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            'font-family="Segoe UI, Helvetica, Arial, sans-serif" role="img" aria-label="{t}">\n'
            '<rect width="{w}" height="{h}" fill="#ffffff"/>\n').format(w=w, h=h, t=esc(title))


def text(x, y, s, size=13, color=INK, anchor="start", weight="normal"):
    return ('<text x="{x}" y="{y}" font-size="{sz}" fill="{c}" text-anchor="{a}" '
            'font-weight="{w}">{s}</text>\n').format(x=x, y=y, sz=size, c=color, a=anchor, w=weight, s=esc(s))


def fig_papers_per_year(papers):
    counts = Counter(p["year"] for p in papers)
    years = list(range(min(counts), max(counts) + 1))
    vals = [counts.get(y, 0) for y in years]
    W, H = 760, 420
    ml, mr, mt = 60, 30, 70
    pw, ph = W - ml - mr, H - mt - 60
    ymax = max(vals) + 1
    gap = pw / len(years)
    bw = gap * 0.62
    s = svg_open(W, H, "Manufacturing knowledge-graph papers per year")
    s += text(ml, 34, "Manufacturing Knowledge-Graph Publications per Year", 18, INK, weight="700")
    s += text(ml, 52, "{} curated papers - source: data/papers.json".format(len(papers)), 12, MUTED)
    for i in range(ymax + 1):
        gy = mt + ph - (i / ymax) * ph
        s += '<line x1="{}" y1="{:.1f}" x2="{}" y2="{:.1f}" stroke="{}" stroke-width="1"/>\n'.format(ml, gy, W - mr, gy, GRID)
        s += text(ml - 8, gy + 4, str(i), 11, MUTED, "end")
    for idx, (y, v) in enumerate(zip(years, vals)):
        x = ml + idx * gap + (gap - bw) / 2
        bh = (v / ymax) * ph
        by = mt + ph - bh
        col = ACCENT if y <= 2022 else ACCENT3
        s += '<rect x="{:.1f}" y="{:.1f}" width="{:.1f}" height="{:.1f}" rx="3" fill="{}"/>\n'.format(x, by, bw, bh, col)
        if v:
            s += text(x + bw / 2, by - 6, str(v), 12, INK, "middle", "700")
        s += text(x + bw / 2, mt + ph + 18, str(y), 11, MUTED, "middle")
    s += '<rect x="{}" y="62" width="12" height="12" fill="{}"/>'.format(W - mr - 210, ACCENT)
    s += text(W - mr - 192, 72, "original survey (2016-2022)", 11, MUTED)
    s += '<rect x="{}" y="80" width="12" height="12" fill="{}"/>'.format(W - mr - 210, ACCENT3)
    s += text(W - mr - 192, 90, "added & verified (2023-2026)", 11, MUTED)
    s += text(ml, H - 14, "A living, version-controlled bibliography", 11, MUTED)
    s += "</svg>\n"
    with open(os.path.join(FIG, "papers_per_year.svg"), "w", encoding="utf-8") as f:
        f.write(s)


LABELS = {
    "kg-construction": "KG construction", "interoperability": "Interoperability",
    "survey": "Surveys & reviews", "process-planning": "Process planning",
    "gnn-embedding": "Embeddings & GNNs", "ontology": "Ontologies",
    "root-cause": "Root-cause analysis", "llm-rag": "LLMs & GraphRAG",
    "cps": "Cyber-physical systems", "digital-twin": "Digital twins",
    "product-design": "Product design / PLM", "quality-control": "Quality control",
    "standards": "Standards", "process-optimization": "Process optimization",
    "iiot": "IIoT integration", "explainability": "Explainability",
    "predictive-maintenance": "Predictive maintenance", "supply-chain": "Supply chain",
    "materials": "Materials", "additive-manufacturing": "Additive manufacturing",
    "human-ai": "Human-AI teaming", "resource-allocation": "Resource allocation",
    "factory-planning": "Factory planning", "robotics": "Robotics"}


def fig_category_distribution(papers):
    c = Counter(t for p in papers for t in p["tags"])
    items = c.most_common(14)
    W = 760
    rowh = 26
    mt = 78
    H = mt + rowh * len(items) + 40
    ml, mr = 200, 60
    pw = W - ml - mr
    vmax = items[0][1]
    s = svg_open(W, H, "Manufacturing knowledge-graph research themes")
    s += text(28, 34, "Research Themes Across the Corpus", 18, INK, weight="700")
    s += text(28, 52, "papers may carry several thematic tags - source: data/papers.json", 12, MUTED)
    for i, (tag, v) in enumerate(items):
        y = mt + i * rowh
        bw = (v / vmax) * pw
        col = BAND[i % len(BAND)]
        s += text(ml - 10, y + 15, LABELS.get(tag, tag), 12, INK, "end")
        s += '<rect x="{}" y="{}" width="{:.1f}" height="{}" rx="3" fill="{}"/>\n'.format(ml, y + 3, bw, rowh - 9, col)
        s += text(ml + bw + 6, y + 15, str(v), 11, MUTED)
    s += text(28, H - 14, "Tag vocabulary is documented in data/README.md", 11, MUTED)
    s += "</svg>\n"
    with open(os.path.join(FIG, "category_distribution.svg"), "w", encoding="utf-8") as f:
        f.write(s)


TAX = [
    ("Foundations", ACCENT2, ["RDF / OWL / SHACL / SPARQL", "Upper & domain ontologies",
                              "KG embeddings & GNNs", "Reasoning & rules"]),
    ("Construction", ACCENT, ["From databases & OPC UA", "From text (NLP / LLM)",
                              "From BPMN & process models", "Fusion & completion"]),
    ("Applications", ACCENT3, ["Digital twins & CPS", "Predictive maintenance",
                               "Quality control & root-cause", "Process & production planning",
                               "Resource allocation & scheduling", "Supply chain & logistics",
                               "Product design & PLM"]),
    ("Enabling standards", "#9b2226", ["RAMI 4.0 / AAS", "ISA-95 / ISA-88",
                                       "OPC UA / AutomationML", "MTConnect / QIF"])]


def fig_taxonomy():
    W = 880
    leaf_h = 30
    pad = 14
    total_leaves = sum(len(b[2]) for b in TAX)
    H = 90 + total_leaves * leaf_h + len(TAX) * pad + 30
    s = svg_open(W, H, "A taxonomy of manufacturing knowledge graphs")
    s += text(40, 40, "A Taxonomy of Manufacturing Knowledge Graphs", 19, INK, weight="700")
    s += text(40, 60, "from semantic foundations, through construction, to industrial applications and the standards they align with", 12, MUTED)
    rooty = 90 + (H - 120) / 2
    s += '<rect x="20" y="{}" width="40" height="44" rx="8" fill="{}"/>\n'.format(rooty - 22, INK)
    s += ('<text x="40" y="{}" font-size="11" fill="#fff" text-anchor="middle" font-weight="700">MfG</text>\n'
          '<text x="40" y="{}" font-size="11" fill="#fff" text-anchor="middle" font-weight="700">KG</text>\n').format(rooty - 2, rooty + 12)
    y = 90
    bx, bw = 150, 190
    lx, lw = bx + bw + 30, 320
    for name, col, leaves in TAX:
        bh = len(leaves) * leaf_h + (len(leaves) - 1) * 4
        by = y
        bcy = by + bh / 2
        s += '<path d="M60 {:.0f} C 110 {:.0f}, 110 {:.0f}, {} {:.0f}" stroke="{}" stroke-width="2" fill="none" opacity="0.6"/>\n'.format(rooty, rooty, bcy, bx, bcy, col)
        s += '<rect x="{}" y="{}" width="{}" height="{}" rx="9" fill="{}"/>\n'.format(bx, by, bw, bh, col)
        s += text(bx + bw / 2, bcy + 5, name, 14, "#ffffff", "middle", "700")
        ly = by
        for leaf in leaves:
            lcy = ly + leaf_h / 2
            s += '<path d="M{} {:.0f} C {} {:.0f}, {} {:.0f}, {} {:.0f}" stroke="{}" stroke-width="1.4" fill="none" opacity="0.5"/>\n'.format(bx + bw, bcy, bx + bw + 15, bcy, lx - 15, lcy, lx, lcy, col)
            s += '<rect x="{}" y="{}" width="{}" height="{}" rx="6" fill="#f4f7fb" stroke="{}"/>\n'.format(lx, ly, lw, leaf_h - 6, GRID)
            s += text(lx + 12, lcy + 4, leaf, 12, INK)
            ly += leaf_h
        y += bh + pad
    s += "</svg>\n"
    with open(os.path.join(FIG, "taxonomy.svg"), "w", encoding="utf-8") as f:
        f.write(s)


LAYERS = [
    ("Industrial data sources", ACCENT2,
     ["Sensors / IIoT", "MES / ERP", "OPC UA", "CAD / PLM", "Documents & logs"]),
    ("Semantic lifting & construction", ACCENT,
     ["RML / R2RML", "NLP & LLM extraction", "Ontology mapping", "Entity resolution"]),
    ("Knowledge graph & reasoning", "#5e548e",
     ["Triplestore / graph DB", "OWL reasoning", "SHACL validation", "Embeddings / GNN"]),
    ("Manufacturing applications", ACCENT3,
     ["Digital twin", "Predictive maintenance", "Root-cause / quality", "Planning & scheduling", "GraphRAG copilots"])]


def fig_technology_landscape():
    W, H = 880, 470
    s = svg_open(W, H, "The manufacturing knowledge-graph technology landscape")
    s += text(40, 38, "The Manufacturing Knowledge-Graph Technology Stack", 19, INK, weight="700")
    s += text(40, 58, "how raw shop-floor data becomes decisions: a layered reference pipeline", 12, MUTED)
    top, lh, gap = 80, 88, 10
    mlx, mrx = 40, 40
    bw = W - mlx - mrx
    for i, (name, col, items) in enumerate(LAYERS):
        y = top + i * (lh + gap)
        s += '<rect x="{}" y="{}" width="{}" height="{}" rx="12" fill="{}" opacity="0.10"/>\n'.format(mlx, y, bw, lh, col)
        s += '<rect x="{}" y="{}" width="6" height="{}" rx="3" fill="{}"/>\n'.format(mlx, y, lh, col)
        s += text(mlx + 20, y + 26, name, 14, INK, weight="700")
        chipx, chipy = mlx + 20, y + 44
        for it in items:
            cw = 11 + len(it) * 7.0
            if chipx + cw > W - mrx - 10:
                chipx, chipy = mlx + 20, chipy + 30
            s += '<rect x="{:.0f}" y="{}" width="{:.0f}" height="24" rx="12" fill="#ffffff" stroke="{}"/>\n'.format(chipx, chipy, cw, col)
            s += text(chipx + cw / 2, chipy + 16, it, 11.5, INK, "middle")
            chipx += cw + 10
        if i < len(LAYERS) - 1:
            s += '<path d="M{} {} l 8 {} l 8 -{} z" fill="{}"/>\n'.format(W / 2 - 8, y + lh + 1, gap - 2, gap - 2, MUTED)
    s += "</svg>\n"
    with open(os.path.join(FIG, "technology_landscape.svg"), "w", encoding="utf-8") as f:
        f.write(s)


def main():
    papers = load("papers.json")
    onts = load("ontologies.json")
    tools = load("tools.json")
    stds = load("standards.json")
    for d in (CAT, FIG, DOCS):
        os.makedirs(d, exist_ok=True)
    write_papers_csv(papers)
    write_papers_bib(papers)
    write_bibliography_md(papers)
    write_catalog_csv(onts, "ontologies.csv", ["name", "full_name", "scope", "url", "license", "source"])
    write_catalog_csv(tools, "tools.csv", ["name", "category", "description", "url", "license", "source"])
    write_catalog_csv(stds, "standards.csv", ["name", "full_name", "purpose", "body", "url", "source"])
    write_ontologies_md(onts)
    write_tools_md(tools)
    write_standards_md(stds)
    fig_papers_per_year(papers)
    fig_category_distribution(papers)
    fig_taxonomy()
    fig_technology_landscape()
    with open(os.path.join(DOCS, "papers.json"), "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False)
    print("OK  papers={} ontologies={} tools={} standards={}".format(
        len(papers), len(onts), len(tools), len(stds)))
    print("by year:", dict(sorted(Counter(p['year'] for p in papers).items())))


if __name__ == "__main__":
    main()
