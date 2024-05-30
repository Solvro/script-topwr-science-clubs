from directus_push.client import client


def import_file(f_url: str, folder: str, title: str):
    return client.post(
        "/files/import",
        json={
            "url": f_url,
            "data": {
                "title": title,
                "folder": folder,
            },
        },
    )
