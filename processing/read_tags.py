import json


def read_tags(fname: str) -> set[str]:
    with open(fname, 'r') as file:
        tags = json.load(file)
        return set(tags.keys())
