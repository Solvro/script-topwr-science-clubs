from models.merged_model import SciClubMerged, SourcePriority
from models.org_type import OrgType
from processing.fix_missing_matches import check_if_names_are_equal
from processing.merge_description import merge_description
from processing.utils import find_first_element
from source2_pull.create_assets_url import (
    create_assets_url,
    create_assets_url_for_cover,
)


def new_entities(source2_online_data):
    for key, value in NEW_NAMES.items():
        full_data = find_first_element(
            source2_online_data, lambda x: check_if_names_are_equal(key, x.get("name"))
        )
        yield SciClubMerged(
            name=key,
            type=value[0].value[0],
            department_name=value[1],
            description=merge_description(full_data),
            email=full_data.get("email"),
            website=full_data.get("website"),
            facebook=full_data.get("facebook"),
            linkedin=full_data.get("linkedin"),
            instagram=full_data.get("instagram"),
            youtube=full_data.get("youtube"),
            logo=create_assets_url(full_data.get("logo")),
            cover=create_assets_url_for_cover(full_data.get("images")[0]),
            priority=SourcePriority.good.value,
            shortDescription=full_data.get("shortDescription"),
        )


NEW_NAMES: dict[str, tuple[OrgType, str | None]] = {
    "Don Bosco": (OrgType.ORGANIZATION, None),
    "KN ElektroMed": (OrgType.SCI_CLUB, "Wydział Podstawowych Problemów Techniki"),
}
