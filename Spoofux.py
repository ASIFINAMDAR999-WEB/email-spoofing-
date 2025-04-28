#!/usr/bin/env python3
import sys
import time
import random
import smtplib
from email.mime.text import MIMEText

# ======================
#   TERMUX UI DESIGN
# ======================
class TermuxTheme:
    COLORS = {
        "cyber_blue": "\033[38;5;45m",
        "hacker_green": "\033[38;5;82m",
        "neon_purple": "\033[38;5;93m",
        "alert_red": "\033[38;5;196m",
        "reset": "\033[0m"
    }

    @classmethod
    def banner(cls):
        print(cls.COLORS['cyber_blue'] + r"""
         _____                  _  __  __ 
        / ____|                | |/ _|/ _|
       | (___  _ __   ___  __ _| | |_| |_ 
        \___ \| '_ \ / _ \/ _` | |  _|  _|
        ____) | |_) |  __/ (_| | | | | |  
       |_____/| .__/ \___|\__,_|_|_| |_|  
             _| |    TERMUX EDITION v3.1
            |___/                          
        """ + cls.COLORS['reset'])

    @classmethod
    def show_loading(cls, duration=3):
        frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            print(f"\r{cls.COLORS['hacker_green']}🚀 {frames[i % len(frames)]} Preparing cyber package... {random.choice(['ENCRYPTING', 'SPOOFING DNS', 'ROUTING'])}{cls.COLORS['reset']}", end='')
            time.sleep(0.1)
            i += 1
        print()

# ======================
#   CORE FUNCTIONALITY
# ======================
class EmailSpoofer:
    CONFIG = {
        "SMTP_SERVER": "smtp.hostinger.com",
        "SMTP_PORT": 587,
        "EMAIL": "hindupriest@hindupriest.co.in",
        "PASSWORD": "Pandit@2024"
    }

    def __init__(self):
        self.headers = {
            "User-Agents": [
                "Mozilla/5.0 (Windows NT 13.0; Win64; x64)",
                "AppleWebKit/537.36 (KHTML, like Gecko)",
                "Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
            ],
            "X-Headers": [
                "X-Originating-IP: [127.0.0.1]",
                "X-Forwarded-For: 192.168.1.1"
            ]
        }

    def create_email(self, fake_from, target, subject, message):
        msg = MIMEText(message, 'html' if '<html>' in message else 'plain')
        msg['From'] = fake_from
        msg['To'] = target
        msg['Subject'] = subject
        msg.add_header('X-Mailer', random.choice(self.headers["User-Agents"]))
        return msg

    def send_email(self, msg):
        try:
            with smtplib.SMTP(self.CONFIG["SMTP_SERVER"], self.CONFIG["SMTP_PORT"]) as server:
                server.starttls()
                server.login(self.CONFIG["EMAIL"], self.CONFIG["PASSWORD"])
                server.sendmail(self.CONFIG["EMAIL"], msg['To'], msg.as_string())
                return True
        except Exception as e:
            print(TermuxTheme.COLORS['alert_red'] + f"\n‼️ CRITICAL ERROR: {str(e)}" + TermuxTheme.COLORS['reset'])
            return False

# ======================
#   MAIN EXECUTION
# ======================
def main():
    TermuxTheme.banner()
    TermuxTheme.show_loading()

    print(TermuxTheme.COLORS['neon_purple'] + "\n" + "═"*40 + TermuxTheme.COLORS['reset'])
    
    # Get user input
    fake_from = input(TermuxTheme.COLORS['cyber_blue'] + "[🛡️] Spoofed Identity: " + TermuxTheme.COLORS['reset'])
    target = input(TermuxTheme.COLORS['cyber_blue'] + "[🎯] Target Email: " + TermuxTheme.COLORS['reset'])
    subject = input(TermuxTheme.COLORS['cyber_blue'] + "[📩] Email Subject: " + TermuxTheme.COLORS['reset'])
    message = input(TermuxTheme.COLORS['cyber_blue'] + "[📝] Message File: " + TermuxTheme.COLORS['reset'])

    # Read message content
    try:
        with open(message, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(TermuxTheme.COLORS['alert_red'] + "\n⚠️ File not found! Using default message." + TermuxTheme.COLORS['reset'])
        content = "Default message content"

    # Create and send email
    spoofer = EmailSpoofer()
    email = spoofer.create_email(fake_from, target, subject, content)
    
    print(TermuxTheme.COLORS['hacker_green'] + "\n🔥 Initializing dark mode transmission..." + TermuxTheme.COLORS['reset'])
    if spoofer.send_email(email):
        print(TermuxTheme.COLORS['hacker_green'] + """
        ╔══════════════════════════╗
        ║   ✔ CYBER TRANSMISSION   ║
        ║      SUCCESSFUL!         ║
        ╚══════════════════════════╝
        """ + TermuxTheme.COLORS['reset'])
    else:
        print(TermuxTheme.COLORS['alert_red'] + """
        ╔══════════════════════════╗
        ║   ✖ TRANSMISSION FAILED  ║
        ║    INITIATE SELF-DESTRUCT║
        ╚══════════════════════════╝
        """ + TermuxTheme.COLORS['reset'])

if __name__ == "__main__":
    main()