from source2_pull.client import client


def fetch_orgs():
    return client.get_items(
        "Organizacje",
    )


if __name__ == "__main__":
    print(fetch_orgs())
