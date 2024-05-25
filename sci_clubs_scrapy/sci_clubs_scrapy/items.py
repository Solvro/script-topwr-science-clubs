from dataclasses import dataclass, field

from itemloaders import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


@dataclass
class SciClubItem:
    title: str | None = field(default=None)
    description: str | None = field(default=None)
    email: str | None = field(default=None)
    website: str | None = field(default=None)
    facebook: str | None = field(default=None)
    linkedin: str | None = field(default=None)
    logotype: str | None = field(default=None)
    org_type: str | None = field(default=None)
    department_name: str | None = field(default=None)


class SciClubItemLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
