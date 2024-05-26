from dataclasses import dataclass
from enum import Enum

from sci_clubs_scrapy.items import SciClubItem


class SourcePriority(Enum):
    bad = 0
    good = 1


@dataclass
class SciClubMerged(SciClubItem):
    cover: str | None = None
    tags: list[str] = ()
    priority: int | None = SourcePriority.bad.value
