import smtplib
import random
import time
import os
from email.mime.text import MIMEText

# === SMTP CONFIGURATION ===
EMAIL_ADDRESS = 'hindupriest@hindupriest.co.in'
EMAIL_PASSWORD = 'Pandit@2024'
SMTP_SERVER = 'smtp.hostinger.com'
SMTP_PORT = 587

# === Random headers for disguise
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 10)", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (X11; Linux x86_64)", "Mozilla/5.0 (Windows NT 6.3; Win64; x64)"
]
REFERRERS = [
    "https://www.google.com", "https://www.facebook.com", "https://www.reddit.com",
    "https://www.bing.com", "https://twitter.com", "https://github.com"
]

def print_banner():
    os.system('clear')
    print("╔══════════════════════════════════════╗")
    print("║   🛡️  𝐑𝐄𝐃𝐀𝐫𝐦𝐨𝐫 𝐯𝟎.𝟐 - 𝐄𝐌𝐀𝐈𝐋 𝐓𝐎𝐎𝐋         ║")
    print("╚══════════════════════════════════════╝")
    print("💌 Send spoofed emails with HTML/plain content.")
    print("📍 End message input with 'END' on a new line.\n")

def send_email(fake_sender, receiver, display_name, subject, content, html=True):
    msg = MIMEText(content, 'html' if html else 'plain')
    msg['Subject'] = subject
    msg['From'] = f'"{display_name}" <{EMAIL_ADDRESS}>'
    msg['To'] = receiver
    msg['Reply-To'] = fake_sender
    msg['X-User-Agent'] = random.choice(USER_AGENTS)
    msg['X-Referer'] = random.choice(REFERRERS)

    try:
        print(f"📤 Sending to {receiver.strip()}...", end=" ")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, receiver.strip(), msg.as_string())
        server.quit()
        print("✅ Success")
        log_sent(receiver.strip(), subject)
    except Exception as e:
        print(f"❌ Failed: {e}")

def log_sent(receiver, subject):
    with open("logs.txt", "a", encoding="utf-8") as log:
        log.write(f"{time.ctime()} | To: {receiver} | Subject: {subject}\n")

def get_message():
    print("\n🖊️  Compose your message content below:")
    print("(Type 'END' on a new line to finish)")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def preview(display_name, reply_to, to_list, subject, message):
    print("\n📋 EMAIL PREVIEW")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📧 From     : {display_name} <{EMAIL_ADDRESS}>")
    print(f"📨 Reply-To : {reply_to}")
    print(f"👥 To       : {', '.join(to_list)}")
    print(f"📝 Subject  : {subject}")
    print("🖊 Message  :")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(message[:1000] + ("\n... (truncated)" if len(message) > 1000 else ""))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    return input("🚀 Proceed with sending? (Y/N): ").strip().lower() == 'y'

if __name__ == "__main__":
    print_banner()

    display_name = input("👤 Display Name (From)         : ").strip()
    fake_reply = input("🕵️  Fake Reply-To Email         : ").strip()
    receivers = input("📧 Recipient(s) (comma-separated): ").strip().split(',')
    subject = input("📝 Subject of the email         : ").strip()
    html_or_text = input("📄 Send as HTML? (y/n)           : ").strip().lower()
    is_html = html_or_text == 'y'

    message = get_message()

    if preview(display_name, fake_reply, receivers, subject, message):
        for r in receivers:
            send_email(fake_reply, r, display_name, subject, message, is_html)
    else:
        print("\n❌ Sending cancelled.")