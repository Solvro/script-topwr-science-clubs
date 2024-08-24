import smtplib
from email.mime.text import MIMEText
from typing import Callable, List


def send_email(subject, body, sender, recipient, password):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, [recipient], msg.as_string())
    print("Message sent!")


def send_bulk_emails(
    subject: str,
    get_body: Callable[[str], str],
    sender: str,
    recipients: List[str],
    password: str,
    links: List[str]
):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender, password)
        for recipient in zip(recipients, links):
            msg = MIMEText(get_body(recipient[1]), "html")
            msg["Subject"] = subject
            msg["From"] = sender
            msg["To"] = recipient[0]
            smtp_server.sendmail(sender, recipient[0], msg.as_string())
            print(f"Message sent to {recipient[0]}!")
