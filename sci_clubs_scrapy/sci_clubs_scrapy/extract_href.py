import re


def extract_href(text):
    href_match = re.search(r'href="(.*?)"', text)
    if href_match:
        return href_match.group(1)
    else:
        return None
