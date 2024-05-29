import requests

from source2_pull.client import client


def create_assets_url(file_hash: str | None) -> str | None:
    if file_hash is None:
        return None
    return client.get_url_file(file_hash)


def create_assets_url_for_cover(id_: int | None) -> str | None:
    if id_ is None:
        return None
    file_hash = requests.get(client.url + "/items/Organizacje_files/" + str(id_)).json()["data"]
    return create_assets_url(file_hash["directus_files_id"])
