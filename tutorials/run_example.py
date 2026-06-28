#!/usr/bin/env python3
"""Load the example manufacturing KG and run every query in queries.sparql.

Requires rdflib:  pip install rdflib
Usage:            python3 tutorials/run_example.py
"""
import os
import re
import sys

try:
    from rdflib import Graph
except ImportError:
    sys.exit("This tutorial needs rdflib. Install it with:  pip install rdflib")

HERE = os.path.dirname(os.path.abspath(__file__))
TTL = os.path.join(HERE, "example-manufacturing-kg.ttl")
SPARQL = os.path.join(HERE, "queries.sparql")


def load_queries(path):
    blocks = re.split(r"(?m)^### ", open(path, encoding="utf-8").read())
    out = []
    for b in blocks:
        b = b.strip()
        if not b or b.startswith("#"):
            continue
        title, _, body = b.partition("\n")
        out.append((title.strip(), body.strip()))
    return out


def main():
    g = Graph()
    g.parse(TTL, format="turtle")
    print("Loaded {} triples from {}\n".format(len(g), os.path.basename(TTL)))
    for title, q in load_queries(SPARQL):
        print("=" * 70)
        print(title)
        print("-" * 70)
        rows = list(g.query(q))
        if not rows:
            print("(no results)")
        for row in rows:
            vals = [str(v) if v is not None else "" for v in row]
            print("  " + " | ".join(vals))
        print()


if __name__ == "__main__":
    main()
