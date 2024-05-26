from typing import Callable, TypeVar

T = TypeVar('T')


def find_first_element(lst: list[T], condition: Callable[[T], bool]) -> T | None:
    try:
        return next(element for element in lst if condition(element))
    except StopIteration:
        return None
