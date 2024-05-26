import re


def extract_href(text, keyword=""):
    matches = re.finditer(r'href="(.*?)"', text)
    for match in matches:
        href = match.group(1)
        if keyword.lower() in href.lower():
            return href
    return None
