from dataclasses import dataclass
from enum import Enum

from models.scraped_item import SciClubItem


class SourcePriority(Enum):
    bad = "student_department"
    good = "aktywni_website"


@dataclass
class SciClubMerged(SciClubItem):
    cover: str | None = None
    priority: int | None = SourcePriority.bad.value
    shortDescription: str | None = None
    youtube: str | None = None
