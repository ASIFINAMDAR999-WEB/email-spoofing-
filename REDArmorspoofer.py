#!/usr/bin/env python3
"""
REDArmor 2.0 - Advanced Email Spoofer
Enhanced with professional UI/UX, animations, and additional features
Termux compatible with no external dependencies
"""

import smtplib
import random
import csv
import os
import time
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# Email credentials and server configuration
EMAIL_ADDRESS = 'hindupriest@hindupriest.co.in'
EMAIL_PASSWORD = 'Pandit@2024'
SMTP_SERVER = 'smtp.hostinger.com'
SMTP_PORT = 587

# Color codes for terminal UI
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# 20 User-Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36"
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

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.03, color=Colors.WHITE):
    """Animate text printing with delay"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    """Print the REDArmor banner with animation"""
    clear_screen()
    banner = [
        f"{Colors.RED}{Colors.BOLD}",
        "██████╗ ███████╗██████╗      █████╗ ██████╗ ███╗   ███╗ ██████╗ ██████╗ ██████╗ ",
        "██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔═══██╗██╔══██╗",
        "██████╔╝█████╗  ██████╔╝    ███████║██████╔╝██╔████╔██║██║     ██║   ██║██████╔╝",
        "██╔══██╗██╔══╝  ██╔══██╗    ██╔══██║██╔══██╗██║╚██╔╝██║██║     ██║   ██║██╔══██╗",
        "██║  ██║███████╗██║  ██║    ██║  ██║██║  ██║██║ ╚═╝ ██║╚██████╗╚██████╔╝██║  ██║",
        "╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝",
        f"{Colors.END}",
        f"{Colors.RED}{Colors.BOLD}REDArmor 2.0 - Advanced Email Dispatcher{Colors.END}",
        f"{Colors.YELLOW}{'='*60}{Colors.END}"
    ]
    
    for line in banner:
        print(line)
        time.sleep(0.1)

def loading_animation(duration=2, message="Loading"):
    """Display a loading animation"""
    animation_chars = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    start_time = time.time()
    i = 0
    
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Colors.CYAN}{message} {animation_chars[i % len(animation_chars)]}{Colors.END}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")
    sys.stdout.flush()

def validate_email(email):
    """Basic email validation"""
    return '@' in email and '.' in email.split('@')[-1]

def get_recipients():
    """Get recipient emails with validation"""
    print(f"\n{Colors.CYAN}Recipient Options:{Colors.END}")
    print(f"1. Single recipient")
    print(f"2. Multiple recipients (comma separated)")
    print(f"3. Load from CSV file")
    
    choice = input(f"\n{Colors.YELLOW}Enter your choice (1-3): {Colors.END}").strip()
    recipients = []
    
    if choice == "1":
        recipient = input(f"{Colors.YELLOW}Enter recipient email: {Colors.END}").strip()
        if validate_email(recipient):
            recipients.append(recipient)
        else:
            print(f"{Colors.RED}Invalid email format.{Colors.END}")
            return get_recipients()
    elif choice == "2":
        recipient_input = input(f"{Colors.YELLOW}Enter recipient emails (comma separated): {Colors.END}").strip()
        recipient_list = [r.strip() for r in recipient_input.split(",")]
        for r in recipient_list:
            if validate_email(r):
                recipients.append(r)
            else:
                print(f"{Colors.RED}Invalid email format: {r}{Colors.END}")
        if not recipients:
            print(f"{Colors.RED}No valid emails provided.{Colors.END}")
            return get_recipients()
    elif choice == "3":
        file_path = input(f"{Colors.YELLOW}Enter CSV file path: {Colors.END}").strip()
        if not os.path.exists(file_path):
            print(f"{Colors.RED}File not found.{Colors.END}")
            return get_recipients()
        try:
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    for email in row:
                        email = email.strip()
                        if validate_email(email):
                            recipients.append(email)
            if not recipients:
                print(f"{Colors.RED}No valid emails found in the CSV file.{Colors.END}")
                return get_recipients()
        except Exception as e:
            print(f"{Colors.RED}Failed to read CSV file: {e}{Colors.END}")
            return get_recipients()
    else:
        print(f"{Colors.RED}Invalid choice.{Colors.END}")
        return get_recipients()
    
    return recipients

def get_message_content():
    """Get message content with options"""
    print(f"\n{Colors.CYAN}Message Options:{Colors.END}")
    print(f"1. Plain text message")
    print(f"2. HTML message")
    print(f"3. Load from file")
    
    choice = input(f"\n{Colors.YELLOW}Enter your choice (1-3): {Colors.END}").strip()
    is_html = False
    message = ""
    
    if choice == "1":
        print(f"{Colors.YELLOW}Enter your message (press Ctrl+D when finished):{Colors.END}")
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            message = "\n".join(lines)
    elif choice == "2":
        print(f"{Colors.YELLOW}Enter your HTML message (press Ctrl+D when finished):{Colors.END}")
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            message = "\n".join(lines)
        is_html = True
    elif choice == "3":
        file_path = input(f"{Colors.YELLOW}Enter file path: {Colors.END}").strip()
        if not os.path.exists(file_path):
            print(f"{Colors.RED}File not found.{Colors.END}")
            return get_message_content()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                message = f.read()
            if file_path.endswith('.html') or '<html>' in message.lower():
                is_html = True
        except Exception as e:
            print(f"{Colors.RED}Failed to read file: {e}{Colors.END}")
            return get_message_content()
    else:
        print(f"{Colors.RED}Invalid choice.{Colors.END}")
        return get_message_content()
    
    return message, is_html

def test_smtp_connection():
    """Test SMTP connection before sending emails"""
    loading_animation(1, "Testing SMTP connection")
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.quit()
        print(f"\r{Colors.GREEN}✓ SMTP connection successful{Colors.END}")
        return True
    except Exception as e:
        print(f"\r{Colors.RED}✗ SMTP connection failed: {e}{Colors.END}")
        return False

def send_email(fake_sender_email, recipients, display_name, subject, message_content, is_html=False, attachment_path=None):
    """Send email with enhanced features and error handling"""
    success_count = 0
    failure_count = 0
    results = []
    
    for i, recipient in enumerate(recipients, 1):
        try:
            # Create message container
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f'"{display_name}" <{EMAIL_ADDRESS}>'
            msg['To'] = recipient
            msg['Reply-To'] = fake_sender_email
            msg['X-User-Agent'] = random.choice(USER_AGENTS)
            msg['X-Referer'] = random.choice(REFERRERS)
            msg['Date'] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
            msg['Message-ID'] = f'<{datetime.now().strftime("%Y%m%d%H%M%S")}.{random.randint(1000, 9999)}@{SMTP_SERVER.split(".")[-2]}>'
            
            # Attach message
            if is_html:
                msg.attach(MIMEText(message_content, 'html'))
            else:
                msg.attach(MIMEText(message_content, 'plain'))
            
            # Attach file if specified
            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, "rb") as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
                msg.attach(part)
            
            # Show sending progress
            sys.stdout.write(f"\r{Colors.CYAN}Sending [{i}/{len(recipients)}] to {recipient}...{Colors.END}")
            sys.stdout.flush()
            
            # Send email
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
            server.quit()
            
            success_count += 1
            results.append((recipient, True, "Success"))
            
        except Exception as e:
            failure_count += 1
            results.append((recipient, False, str(e)))
    
    # Clear the progress line
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()
    
    return success_count, failure_count, results

def print_summary(success, failure, results):
    """Print a detailed summary of the sending process"""
    print(f"\n{Colors.GREEN}{'='*60}{Colors.END}")
    print(f"{Colors.GREEN}Emails successfully sent: {success}{Colors.END}")
    print(f"{Colors.RED}Failed deliveries: {failure}{Colors.END}")
    print(f"{Colors.GREEN}{'='*60}{Colors.END}")
    
    if failure > 0:
        print(f"\n{Colors.RED}Failed deliveries details:{Colors.END}")
        for recipient, success, error in results:
            if not success:
                print(f"{Colors.RED}  {recipient}: {error}{Colors.END}")

def main():
    """Main function with enhanced UI/UX"""
    print_banner()
    
    # Test SMTP connection first
    if not test_smtp_connection():
        retry = input(f"\n{Colors.YELLOW}Continue anyway? (y/N): {Colors.END}").strip().lower()
        if retry != 'y':
            print(f"{Colors.RED}Exiting.{Colors.END}")
            return
    
    # Get sender details
    print(f"\n{Colors.CYAN}Sender Details:{Colors.END}")
    display_name = input(f"{Colors.YELLOW}Enter display name: {Colors.END}").strip()
    fake_sender_email = input(f"{Colors.YELLOW}Enter fake sender email: {Colors.END}").strip()
    
    if not validate_email(fake_sender_email):
        print(f"{Colors.RED}Invalid fake sender email format.{Colors.END}")
        fake_sender_email = input(f"{Colors.YELLOW}Enter valid fake sender email: {Colors.END}").strip()
    
    # Get recipients
    recipients = get_recipients()
    if not recipients:
        print(f"{Colors.RED}No valid recipients provided. Exiting.{Colors.END}")
        return
    
    # Get subject and message
    print(f"\n{Colors.CYAN}Email Content:{Colors.END}")
    subject = input(f"{Colors.YELLOW}Enter subject of email: {Colors.END}").strip()
    message_content, is_html = get_message_content()
    
    # Attachment option
    attachment = None
    attach_choice = input(f"\n{Colors.YELLOW}Add attachment? (y/N): {Colors.END}").strip().lower()
    if attach_choice == 'y':
        attachment = input(f"{Colors.YELLOW}Enter attachment file path: {Colors.END}").strip()
        if not os.path.exists(attachment):
            print(f"{Colors.RED}File not found. Skipping attachment.{Colors.END}")
            attachment = None
    
    # Confirmation
    print(f"\n{Colors.YELLOW}{'='*60}{Colors.END}")
    print(f"{Colors.CYAN}Ready to send email to {len(recipients)} recipient(s){Colors.END}")
    print(f"{Colors.CYAN}Subject: {subject}{Colors.END}")
    print(f"{Colors.CYAN}From: {display_name} <{fake_sender_email}>{Colors.END}")
    print(f"{Colors.YELLOW}{'='*60}{Colors.END}")
    
    confirm = input(f"\n{Colors.YELLOW}Proceed? (Y/n): {Colors.END}").strip().lower()
    
    if confirm and confirm != 'y':
        print(f"{Colors.RED}Operation cancelled.{Colors.END}")
        return
    
    # Send emails
    loading_animation(1, "Preparing to send")
    success, failure, results = send_email(
        fake_sender_email, 
        recipients, 
        display_name, 
        subject, 
        message_content, 
        is_html,
        attachment
    )
    
    # Results
    print_summary(success, failure, results)
    
    # Save results to file
    save_choice = input(f"\n{Colors.YELLOW}Save results to file? (y/N): {Colors.END}").strip().lower()
    if save_choice == 'y':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"redarmor_results_{timestamp}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(f"REDArmor 2.0 - Email Campaign Results\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Subject: {subject}\n")
                f.write(f"From: {display_name} <{fake_sender_email}>\n")
                f.write(f"Success: {success}\n")
                f.write(f"Failure: {failure}\n\n")
                
                if failure > 0:
                    f.write("Failed deliveries:\n")
                    for recipient, success, error in results:
                        if not success:
                            f.write(f"  {recipient}: {error}\n")
            
            print(f"{Colors.GREEN}Results saved to {filename}{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}Failed to save results: {e}{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Operation cancelled by user.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}An unexpected error occurred: {e}{Colors.END}")
    finally:
        print(f"\n{Colors.CYAN}Thank you for using REDArmor 2.0!{Colors.END}\n")
