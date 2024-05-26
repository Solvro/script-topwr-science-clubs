import sys
from typing import Generator, Iterable

from scrapy.exporters import JsonLinesItemExporter

from processing.load_jsonl import load_jsonl
from processing.merge_description import merge_description
from processing.merged_model import SciClubMerged, SourcePriority
from processing.read_tags import read_tags
from processing.utils import find_first_element


def merge_sources(source1: Generator[dict, None, None], source2: Generator[dict, None, None], tags: set[str]):
    source22 = list(source2)
    for sciClub in source1:
        better_sci_club = find_first_element(source22, lambda x: sciClub.get("title") == x.get("name"))
        if better_sci_club:
            yield SciClubMerged(
                title=better_sci_club.get("name") or sciClub.get("title"),
                description=merge_description(better_sci_club) or sciClub.get("description"),
                email=better_sci_club.get("email") or sciClub.get("email"),
                website=better_sci_club["contact"].get("website") or sciClub.get("website"),
                facebook=better_sci_club["contact"].get("facebook") or sciClub.get("facebook"),
                linkedin=better_sci_club["contact"].get("linkedin") or sciClub.get("linkedin"),
                instagram=better_sci_club["contact"].get("instagram") or sciClub.get("instagram"),
                tiktok=sciClub.get("tiktok"),
                logotype=better_sci_club.get("logoUrl") or sciClub.get("logotype"),
                org_type=sciClub.get("org_type"),
                department_name=sciClub.get("department_name"),
                cover=better_sci_club.get("photos")[0],
                tags=list(filter(lambda x: x in tags, better_sci_club.get("tags", []))),
                priority=SourcePriority.good.value
            )
        yield SciClubMerged(
            title=sciClub.get("title"),
            description=sciClub.get("description"),
            email=sciClub.get("email"),
            website=sciClub.get("website"),
            facebook=sciClub.get("facebook"),
            linkedin=sciClub.get("linkedin"),
            instagram=sciClub.get("instagram"),
            tiktok=sciClub.get("tiktok"),
            logotype=sciClub.get("logotype"),
            department_name=sciClub.get("department_name"),
            org_type=sciClub.get("org_type"),
            priority=SourcePriority.bad.value
        )


def save_merged_sci_clubs(merged_clubs_: Iterable[SciClubMerged], output_file_: str) -> None:
    with open(output_file_, 'wb') as file:
        exporter = JsonLinesItemExporter(file)
        exporter.start_exporting()
        for club in merged_clubs_:
            exporter.export_item(club)
        exporter.finish_exporting()


if __name__ == '__main__':
    s1_file = sys.argv[1] if len(sys.argv) > 1 else "../data/sci_clubs_source1.jsonl"
    s2_file = sys.argv[2] if len(sys.argv) > 2 else "../data/sci_clubs_source2.jsonl"
    tags_file = sys.argv[3] if len(sys.argv) > 3 else "../data/tags_source2.json"
    output_file = sys.argv[4] if len(sys.argv) > 4 else "../data/merged_sci_clubs.json"

    merged_clubs = list(merge_sources(load_jsonl(s1_file), load_jsonl(s2_file), read_tags(tags_file)))
    save_merged_sci_clubs(merged_clubs, output_file)
