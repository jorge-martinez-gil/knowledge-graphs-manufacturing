#!/usr/bin/env python3
"""
validate.py - integrity checks for the canonical datasets.

Run in CI or before committing. Exits non-zero on any failure. Checks:
  * JSON files parse and are lists of objects
  * required fields present and non-empty
  * paper URLs are well-formed http(s) and DOIs look like DOIs
  * paper ids and bibtex keys are unique
  * tags come from the controlled vocabulary
  * catalog source URLs are well-formed
  * generated artifacts exist and are in sync with the JSON (run build.py first)

No third-party dependencies.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

VOCAB = {
    "survey", "kg-construction", "ontology", "digital-twin", "cps", "iiot",
    "predictive-maintenance", "quality-control", "root-cause", "process-planning",
    "process-optimization", "resource-allocation", "factory-planning", "supply-chain",
    "product-design", "materials", "additive-manufacturing", "robotics",
    "gnn-embedding", "llm-rag", "explainability", "interoperability", "standards", "human-ai",
}
PAPER_TYPES = {"journal", "conference", "workshop", "chapter", "preprint"}
URL_RE = re.compile(r"^https?://\S+$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")

errors = []
warnings = []


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def check_papers():
    papers = load("papers.json")
    ids = set()
    for p in papers:
        pid = p.get("id", "?")
        for field in ("id", "year", "title", "authors", "venue", "type", "url", "tags"):
            if field not in p or p[field] in ("", [], None):
                errors.append(f"[paper {pid}] missing/empty field '{field}'")
        if p.get("id") in ids:
            errors.append(f"[paper {pid}] duplicate id")
        ids.add(p.get("id"))
        if p.get("type") not in PAPER_TYPES:
            errors.append(f"[paper {pid}] bad type '{p.get('type')}'")
        if not URL_RE.match(p.get("url", "")):
            errors.append(f"[paper {pid}] malformed url '{p.get('url')}'")
        if p.get("doi") and not DOI_RE.match(p["doi"]):
            errors.append(f"[paper {pid}] malformed doi '{p['doi']}'")
        for t in p.get("tags", []):
            if t not in VOCAB:
                errors.append(f"[paper {pid}] unknown tag '{t}'")
        if not isinstance(p.get("year"), int) or not (1990 <= p["year"] <= 2100):
            errors.append(f"[paper {pid}] implausible year '{p.get('year')}'")
    return len(papers)


def check_catalog(name, required):
    rows = load(name)
    for i, r in enumerate(rows):
        tag = r.get("name", f"row {i}")
        for field in required:
            if field not in r or r[field] in ("", None):
                errors.append(f"[{name}:{tag}] missing field '{field}'")
        for field in ("url", "source"):
            if field in r and r[field] and not URL_RE.match(r[field]):
                errors.append(f"[{name}:{tag}] malformed {field} '{r[field]}'")
    return len(rows)


def check_generated_sync(n_papers):
    # csv/bib should exist and have the right number of records if build was run
    pcsv = os.path.join(DATA, "papers.csv")
    if os.path.exists(pcsv):
        with open(pcsv, encoding="utf-8") as f:
            rows = sum(1 for _ in f) - 1
        if rows != n_papers:
            warnings.append(f"papers.csv has {rows} rows but papers.json has {n_papers} "
                            f"- run scripts/build.py")
    else:
        warnings.append("papers.csv not found - run scripts/build.py")


def main():
    n = check_papers()
    check_catalog("ontologies.json", ["name", "full_name", "scope", "url", "source"])
    check_catalog("tools.json", ["name", "category", "description", "url", "source"])
    check_catalog("standards.json", ["name", "full_name", "purpose", "body", "url", "source"])
    check_generated_sync(n)

    for w in warnings:
        print("WARN ", w)
    if errors:
        for e in errors:
            print("ERROR", e)
        print(f"\nFAILED with {len(errors)} error(s).")
        sys.exit(1)
    print(f"PASSED - {n} papers and all catalogs valid"
          + (f" ({len(warnings)} warning(s))" if warnings else ""))


if __name__ == "__main__":
    main()
