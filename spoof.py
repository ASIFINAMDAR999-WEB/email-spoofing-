import smtplib
from email.mime.text import MIMEText
import random

# Email credentials and server configuration
EMAIL_ADDRESS = 'hindupriest@hindupriest.co.in'
EMAIL_PASSWORD = 'Pandit@2024'
SMTP_SERVER = 'smtp.hostinger.com'
SMTP_PORT = 587

# 20 User-Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (iPad; CPU OS 13_6 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 10)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0)",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4)",
    "Mozilla/5.0 (Windows NT 10.0; WOW64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F)",
    "Mozilla/5.0 (Windows NT 5.1; rv:40.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0)",
    "Mozilla/5.0 (Linux; Android 12; Pixel 5)",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64)",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64)",
    "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P)"
]

# 20 Referrers
REFERRERS = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.yahoo.com",
    "https://www.bing.com",
    "https://www.reddit.com",
    "https://www.github.com",
    "https://www.medium.com",
    "https://www.stackoverflow.com",
    "https://news.ycombinator.com",
    "https://www.quora.com",
    "https://www.pinterest.com",
    "https://duckduckgo.com",
    "https://www.instagram.com",
    "https://www.tumblr.com",
    "https://www.wikiwand.com",
    "https://www.nytimes.com",
    "https://www.outlook.com",
    "https://www.office.com"
]

def send_email(fake_sender_email, receiver, display_name, subject, message_content):
    msg = MIMEText(message_content)
    msg['Subject'] = subject
    msg['From'] = f'"{display_name}" <{EMAIL_ADDRESS}>'
    msg['To'] = receiver
    msg['Reply-To'] = fake_sender_email
    msg['X-User-Agent'] = random.choice(USER_AGENTS)
    msg['X-Referer'] = random.choice(REFERRERS)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, receiver, msg.as_string())
        server.quit()

        print("\nEmail sent successfully.")
        print(f"To         : {receiver}")
        print(f"Subject    : {subject}")
        print(f"From       : \"{display_name}\" ({EMAIL_ADDRESS})")
        print(f"Reply-To   : {fake_sender_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    display_name = input("Enter display name: ").strip()
    fake_sender_email = input("Enter fake sender: ").strip()
    receiver = input("Enter receiver email: ").strip()
    subject = input("Enter subject of email: ").strip()
    file_path = input("Enter file for message (e.g file.txt): ").strip()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            message_content = f.read()
    except Exception as e:
        print(f"Failed to read message file: {e}")
        exit(1)

    send_email(fake_sender_email, receiver, display_name, subject, message_content)
