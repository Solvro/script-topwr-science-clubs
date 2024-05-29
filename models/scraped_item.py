from dataclasses import dataclass, field
from enum import Enum

from itemloaders import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


@dataclass
class SciClubItem:
    name: str | None = field(default=None)
    description: str | None = field(default=None)
    email: str | None = field(default=None)
    website: str | None = field(default=None)
    facebook: str | None = field(default=None)
    linkedin: str | None = field(default=None)
    instagram: str | None = field(default=None)
    tiktok: str | None = field(default=None)
    logo: str | None = field(default=None)
    type: str | None = field(default=None)
    department_name: str | None = field(default=None)


class OrgType(Enum):
    SCI_CLUB = "kola-naukowe"
    CULTURAL_AGENCY = "agendy-kultury"
    MEDIA = "media-studenckie"
    ORGANIZATION = "organizacje-studenckie"


class SciClubItemLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
