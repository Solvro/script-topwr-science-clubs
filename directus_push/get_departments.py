from directus_push.client import client
from processing.utils import find_first_element


def get_departments() -> list[dict]:
    return client.get_items("Departments")


def get_dept_id(department_name: str, departments: list[dict]) -> int:
    return find_first_element(departments, lambda d: d["name"] == department_name)["id"]
