# ToPWR Science Clubs Script/Scraper

![KN Solvro Banner](https://private-user-images.githubusercontent.com/28555148/333665281-1da32ff9-341c-4e9b-b446-e875601cb7e9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTcxMDU0MTQsIm5iZiI6MTcxNzEwNTExNCwicGF0aCI6Ii8yODU1NTE0OC8zMzM2NjUyODEtMWRhMzJmZjktMzQxYy00ZTliLWI0NDYtZTg3NTYwMWNiN2U5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTMwVDIxMzgzNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZjZDJhYjNhOTIzZGQ2MGZmNzExNGQwN2M4OGMxNjQwOWJjM2I5MDE2NzNmOWNjMzk3N2IzZDFlZWUxYmEzYTQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.HeJjt5e1PtdM3pSOUMKdO6uWMUnu-m7rdGl34AWC2uw)

This script is a versatile tool designed to scrape data from the official website of the Wrocław University of Science
and Technology's student department. Additionally, it retrieves data from the API of the student council's website,
combines this information, and sends it to the Directus platform used by ToPWR.


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
