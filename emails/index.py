import csv
import os

from emails.get_template import get_template, SUBJECT, SENDER
from emails.send_email import send_bulk_emails

from dotenv import load_dotenv

load_dotenv()
file_path = "../data/wiosna_maile_followups.csv"

if __name__ == "__main__":
    with open(file_path, newline="") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=";")
        rows = [row for row in csvreader if any(row)]

        for row in rows:
            assert len(row) >= 3

        # withouts_email = [row for row in rows if not "@" in row[1]]
        # for without_email in withouts_email:
        #     print(without_email)

        withs_email = [[row[0], row[1].strip(), row[2].strip()
        .replace(
            "https://topwr-form.sharkserver.kowalinski.dev/",
            "https://formularz.solvro.pl/",
        )] for row in rows if "@" in row[1]]

        for row in withs_email:
            print(row)

        # send_bulk_emails(
        #     SUBJECT,
        #     get_template,
        #     SENDER,
        #     [row[1] for row in withs_email],
        #     os.getenv("GMAIL_PASS"),
        #     [row[2] for row in withs_email],
        # )
