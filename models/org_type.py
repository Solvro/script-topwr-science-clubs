from enum import Enum


class OrgType(Enum):
    SCI_CLUB = "kola-naukowe", "scientific_cirlce"
    CULTURAL_AGENCY = "agendy-kultury", "cultural_agenda"
    MEDIA = "media-studenckie", "student_media"
    ORGANIZATION = "organizacje-studenckie", "student_organization"

    @classmethod
    def from_string(cls, string):
        for member in cls:
            if string in member.value:
                return member
        raise ValueError(f"{string} is not a valid {cls.__name__}")
