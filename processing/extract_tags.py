import os
import sys
from collections import Counter
from typing import Iterable
import json

from processing.load_jsonl import load_jsonl


def _source_tags_stream(fname: str) -> Iterable[str]:
    for org in load_jsonl(fname):
        yield org["field"].lower()
        yield from set(map(lambda x: x.lower(), org["tags"]))


def extract_tags(fname: str) -> dict[str, int]:
    return dict(filter(lambda x: x[1] > 1, Counter(_source_tags_stream(fname)).items()))


def save(tags: dict[str, int], fname: str) -> None:
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(dict(sorted(tags.items(), key=lambda x: -x[1])), f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "../data/sci_clubs_source2.jsonl"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "../data/tags_source2.json"

    save(extract_tags(input_file), output_file)
