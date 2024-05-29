from dataclasses import dataclass
from enum import Enum

from models.scraped_item import SciClubItem


class SourcePriority(Enum):
    bad = 0
    good = 1


@dataclass
class SciClubMerged(SciClubItem):
    cover: str | None = None
    tags: list[str] = ()
    priority: int | None = SourcePriority.bad.value