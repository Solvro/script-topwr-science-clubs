from abc import ABC
from typing import Any


class _Config(ABC):
    title1 = "<h1>📰 Kim jesteśmy, co robimy 📰</h1>\n"
    title2 = "<h1>🔥 Zdobywane umiejętności i wyzwania członków zespołu! 🔥</h1>\n"
    title3 = "<h1>🏆 Największe sukcesy uczelnianej organizacji studenckiej! 🏆</h1>\n"
    title4 = "<h1>🌟 Czym się interesujemy? 🌟</h1>\n"


def merge_description(data_source2: dict[str, Any]) -> str:
    add_section = lambda title, key: (
        title + data_source2[key] if data_source2.get(key) else ""
    )
    description = ""
    description += add_section(_Config.title1, "longDescription")
    description += add_section(_Config.title2, "skillsAndChallenges")
    description += add_section(_Config.title3, "achievements")
    description += add_section(_Config.title4, "distinguishingFeatures")
    return description
