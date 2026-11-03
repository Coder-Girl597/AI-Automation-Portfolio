
import os
import json
import re
import smtplib
import ssl

from email.message import EmailMessage
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


URL = os.environ.get("PPSC_URL") or "https://ppsc.gop.pk/"

SEEN_FILE = "seen.json"

KEYWORDS = [
    k.strip().lower()
    for k in os.environ.get("KEYWORDS", "").split(",")
    if k.strip()
]

RELEVANT = re.compile(r"advert|job|vacanc|\.pdf", re.I)

EMAIL_USER = os.environ["EMAIL_USER"]
EMAIL_PASS = os.environ["EMAIL_PASS"]
EMAIL_TO = os.environ.get("EMAIL_TO") or EMAIL_USER


def fetch_links():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        )
    }

    r = requests.get(URL, headers=headers, timeout=60)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    links = {}

    for a in soup.find_all("a", href=True):
        href = urljoin(URL, a["href"].strip())

        if not href.startswith("http"):
            continue

        text = " ".join(a.get_text(" ", strip=True).split())

        if RELEVANT.search(href) or RELEVANT.search(text):
            links[href] = text or href

    return links


def send_mail(subject, body):
    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO

    msg.set_content(body)

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        context=ssl.create_default_context()
    ) as s:

        s.login(EMAIL_USER, EMAIL_PASS)
        s.send_message(msg)


def main():

    links = fetch_links()

    print(f"Found {len(links)} relevant links on the page")

    first_run = not os.path.exists(SEEN_FILE)

    seen = {}

    if not first_run:
        with open(SEEN_FILE, encoding="utf-8") as f:
            seen = json.load(f)

    new = {
        h: t
        for h, t in links.items()
        if h not in seen
    }

    if first_run:

        send_mail(
            "PPSC monitor is running",
            f"The monitor is active. {len(links)} links have been "
            f"recorded as the baseline.\n"
            "You will now be emailed only when something new appears.\n\n"
            f"{URL}"
        )

        print("First run: test email sent")

    elif new:

        hits = {
            h: t
            for h, t in new.items()
            if not KEYWORDS
            or any(
                k in (t + " " + h).lower()
                for k in KEYWORDS
            )
        }

        if hits:

            lines = [
                f"- {t}\n  {h}"
                for h, t in hits.items()
            ]

            send_mail(
                f"PPSC: {len(hits)} new advertisement(s) / link(s)",
                "New items:\n\n"
                + "\n\n".join(lines)
                + f"\n\nPage: {URL}"
            )

            print(f"Email sent for {len(hits)} new item(s)")

        else:
            print("New items found but none matched the keywords")

    else:
        print("Nothing new")

    seen.update(links)

    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(
            seen,
            f,
            ensure_ascii=False,
            indent=1
        )


if __name__ == "__main__":
    main()
