import json
from typing import Generator, Dict


def load_jsonl(file_path: str) -> Generator[Dict, None, None]:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield json.loads(line.strip())
