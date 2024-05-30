import sys
from typing import Generator, Iterable

from scrapy.exporters import JsonLinesItemExporter

from models.merged_model import SciClubMerged, SourcePriority
from processing.add_new_entity import new_entities
from processing.detect_missing_matches import detect_missing_matches
from processing.fix_missing_matches import check_if_names_are_equal
from processing.merge_description import merge_description
from processing.utils import find_first_element, load_jsonl
from source2_pull.create_assets_url import (create_assets_url,
                                            create_assets_url_for_cover)
from source2_pull.fetch_orgs import fetch_orgs


def merge_sources(source1: Generator[dict, None, None]):
    source2_online_data = fetch_orgs()
    for sciClub in source1:
        better_sci_club = find_first_element(
            source2_online_data,
            lambda x: check_if_names_are_equal(sciClub.get("name"), x.get("name")),
        )
        if better_sci_club:
            yield SciClubMerged(
                name=better_sci_club.get("name") or sciClub.get("name"),
                description=merge_description(better_sci_club)
                            or sciClub.get("description"),
                email=better_sci_club.get("email") or sciClub.get("email"),
                website=better_sci_club.get("website") or sciClub.get("website"),
                facebook=better_sci_club.get("facebook") or sciClub.get("facebook"),
                linkedin=better_sci_club.get("linkedin") or sciClub.get("linkedin"),
                instagram=better_sci_club.get("instagram") or sciClub.get("instagram"),
                youtube=better_sci_club.get("youtube"),
                tiktok=sciClub.get("tiktok"),
                logo=create_assets_url(better_sci_club.get("logo"))
                     or sciClub.get("logo"),
                type=sciClub.get("type"),
                department_name=sciClub.get("department_name"),
                cover=create_assets_url_for_cover(better_sci_club.get("images")[0]),
                priority=SourcePriority.good.value,
                shortDescription=better_sci_club.get("shortDescription")
                                 or sciClub.get("description"),
            )
        else:
            yield SciClubMerged(
                name=sciClub.get("name"),
                description=sciClub.get("description"),
                email="mailto:" + email if (email := sciClub.get("email")) else None,
                website=sciClub.get("website"),
                facebook=sciClub.get("facebook"),
                linkedin=sciClub.get("linkedin"),
                instagram=sciClub.get("instagram"),
                tiktok=sciClub.get("tiktok"),
                logo=sciClub.get("logo"),
                department_name=sciClub.get("department_name"),
                type=sciClub.get("type"),
                priority=SourcePriority.bad.value,
                shortDescription=sciClub.get("description"),
                cover=None,
                youtube=None,
            )
    yield from new_entities(source2_online_data)


def save_merged_sci_clubs(
        merged_clubs_: Iterable[SciClubMerged], output_file_: str
) -> None:
    with open(output_file_, "wb") as file:
        exporter = JsonLinesItemExporter(file)
        exporter.start_exporting()
        for club in merged_clubs_:
            exporter.export_item(club)
        exporter.finish_exporting()


def merge_and_save(s1_data, output_file_) -> list[SciClubMerged]:
    merged_clubs = list(merge_sources(s1_data))
    if missing := list(detect_missing_matches(merged_clubs)):
        raise Exception("Missing sci clubs matches (mismatched names):" + str(missing))

    save_merged_sci_clubs(merged_clubs, output_file_)
    return merged_clubs


if __name__ == "__main__":
    s1_file = sys.argv[1] if len(sys.argv) > 1 else "../data/sci_clubs_source1.jsonl"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "../data/merged_sci_clubs.jsonl"

    merge_and_save(load_jsonl(s1_file), output_file)
