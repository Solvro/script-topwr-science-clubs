from typing import Iterator

from models.merged_model import SciClubMerged
from processing.fix_missing_matches import custom_in
from processing.load_jsonl import load_jsonl


def detect_missing_matches(matches: list[SciClubMerged], s2_file: str) -> Iterator[str]:
    raw_source_2 = list(map(lambda x: x["name"], list(load_jsonl(s2_file))))
    matched_names = list(map(lambda x: x.name, matches))
    yield from filter(lambda x: not custom_in(x, matched_names), raw_source_2)
