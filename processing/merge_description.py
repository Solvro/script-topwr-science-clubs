from abc import ABC
from typing import Any


class _Config(ABC):
    title1 = "📰 Kim jesteśmy, co robimy 📰"
    title2 = "🔥 Zdobywane umiejętności i wyzwania członków zespołu! 🔥"
    title3 = "🏆 Największe sukcesy uczelnianej organizacji studenckiej! 🏆"
    title4 = "🌟 Czym się interesujemy? 🌟"


def merge_description(data_source2: dict[str, Any]) -> str:
    add_section = lambda title, key: title + data_source2[key] if data_source2.get(key) else ""
    description = ""
    description += add_section(_Config.title1, "longDescription")
    description += add_section(_Config.title2, "skillsAndChallenges")
    description += add_section(_Config.title3, "achievements")
    description += add_section(_Config.title4, "distinguishingFeatures")
    return description
