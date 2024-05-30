from directus_push.client import client
from directus_push.generate_social_links import generate_links
from directus_push.get_departments import get_departments, get_dept_id
from directus_push.import_file import import_file
from models.org_type import OrgType
from processing.utils import load_jsonl


def generate_data(fname):
    departments = get_departments()
    for sci_club in load_jsonl(fname):
        logo_id = None
        cover_id = None
        dept = None
        if logo := sci_club["logo"]:
            logo_id = import_file(
                logo, "9a0284ee-d311-4878-8e1b-ed72031fac93", sci_club["name"] + "_logo"
            )["data"]["id"]
        if cover := sci_club["cover"]:
            cover_id = import_file(
                cover,
                "9a0284ee-d311-4878-8e1b-ed72031fac93",
                sci_club["name"] + "_cover",
            )["data"]["id"]
        if sci_club["department_name"]:
            dept = get_dept_id(sci_club["department_name"], departments)

        circle_id = client.create_item(
            "Scientific_Circles",
            {
                "name": sci_club["name"],
                "description": sci_club["description"],
                "shortDescription": sci_club["shortDescription"],
                "source": sci_club["priority"],
                "type": OrgType.from_string(sci_club["type"]).value[1],
                "logo": logo_id,
                "cover": cover_id,
                "department": dept,
                "links": generate_links(sci_club),
            },
        )["data"]["id"]

        print(circle_id)


if __name__ == "__main__":
    generate_data("../data/merged_sci_clubs.jsonl")
