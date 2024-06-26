from typing import Iterator

from models.merged_model import SciClubMerged
from processing.fix_missing_matches import custom_in
from source2_pull.fetch_orgs import fetch_orgs


def detect_missing_matches(matches: list[SciClubMerged]) -> Iterator[str]:
    raw_source_2 = list(map(lambda x: x["name"], fetch_orgs()))
    matched_names = list(map(lambda x: x.name, matches))
    yield from filter(
        lambda x: not custom_in(x, matched_names) and x not in SKIP_NAMES, raw_source_2
    )


SKIP_NAMES = [
    "Komisja ds. Aktywność Studenckiej",
    "Komisja ds. Dydaktyki i Praw Studenta",
    "Sekcja ds. Inicjatyw Społecznych i Ekologii",
    "Komisja ds. Organizacji Samorządu Studenckiego Politechniki Wrocławskiej ",
]
