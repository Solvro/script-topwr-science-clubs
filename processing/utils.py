from typing import Callable, TypeVar

from sci_clubs_scrapy.items import OrgType

T = TypeVar('T')


def find_first_element(lst: list[T], condition: Callable[[T], bool]) -> T | None:
    try:
        return next(element for element in lst if condition(element))
    except StopIteration:
        return None


def get_enum_from_string(value: str) -> OrgType:
    return next(enum_member for enum_member in OrgType.__members__.values() if enum_member.value == value)

