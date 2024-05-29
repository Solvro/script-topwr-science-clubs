from typing import Iterator

from models.merged_model import SciClubMerged
from processing.load_jsonl import load_jsonl


def detect_missing_matches(matches: list[SciClubMerged], s2_file: str) -> Iterator[str]:
    raw_source_2 = list(load_jsonl(s2_file))
    matched_names = map(lambda x: x.name, matches)
    yield from map(lambda x: x["name"], filter(lambda x: x["name"] not in matched_names, raw_source_2))
