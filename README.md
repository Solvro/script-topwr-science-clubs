# ToPWR Science Clubs Script/Scraper

![KN Solvro banner](https://github.com/Solvro/script-topwr-science-clubs/assets/28555148/822d27f0-93e0-44f8-9004-f37577a93d9a)


This script is a versatile tool designed to scrape data from the official website of the Wrocław University of Science
and Technology's student department. Additionally, it retrieves data from the API of the student council's website,
combines this information, and sends it to the Directus platform used by [ToPWR](https://github.com/Solvro/mobile-topwr).


# Usage

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Set the `.env` file

```bash
SOURCE2_DIRECTUS_URL=https://...
DIRECTUS_URL=https:/...
DIRECTUS_TOKEN=...
```

3. Run

```bash
python3 master_scipt.py
```

# Cooming soon

- detailed instructions for adjusting usage to your use case
- specific modules instructions/descriptions
- story behind it
