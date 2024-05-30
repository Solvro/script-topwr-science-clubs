import json
from typing import Callable, Generator, TypeVar

T = TypeVar("T")


def find_first_element(lst: list[T], condition: Callable[[T], bool]) -> T | None:
    try:
        return next(element for element in lst if condition(element))
    except StopIteration:
        return None


def load_jsonl(file_path: str) -> Generator[dict, None, None]:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield json.loads(line.strip())
