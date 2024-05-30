from dataclasses import dataclass, field
from enum import Enum

from models.scraped_item import SciClubItem


class SourcePriority(Enum):
    bad = "student_department"
    good = "aktywni_website"


@dataclass
class SciClubMerged(SciClubItem):
    cover: str | None = field(default=None)
    priority: int | None = field(default=SourcePriority.bad.value)
    shortDescription: str | None = field(default=None)
    youtube: str | None = field(default=None)
