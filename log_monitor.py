import re 
from collections import Counter
import smtplib
from email.mime.text import MIMEText
with open("server.log", "r") as file:
    logs = file.readlines()
for line in logs:
    print(line.strip())
failed_login_pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
failed_ips = []
for line in logs:
    match = re.search(failed_login_pattern, line)
    if match:
        ip = match.group(1)
        failed_ips.append(ip)
print("Failed login attempts:", failed_ips)
error_pattern = r"ERROR (.*)"
errors = []
for line in logs:
    match = re.search(error_pattern, line)
    if match:
        errors.append(match.group(1))
print("Errors found:", errors)
ip_count = Counter(failed_ips)
for ip, count in ip_count.items():
    if count >= 2:
        print(f"ALERT: Multiple failed logins from {ip}")
suspicious_ips = [ip for ip, count in ip_count.items() if count >= 2]
def send_email_alert(report):
    sender = "your_email@gmail.com"
    receiver = "your_email@gmail.com"
    password = "app_password"
    msg = MIMEText(report)
    msg['Subject'] = "Security Alert: Suspicious Activity Detected"
    msg['From'] = sender
    msg['To'] = receiver
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
    print("Email alert sent!")
report = f"""
Security Report

Total failed logins: {len(failed_ips)}
Suspicious IPs: {suspicious_ips}
Total system errors: {len(errors)}
"""
print(report)
if suspicious_ips or errors:
    send_email_alert(report)
else:
    print("No suspicious activity detected.")

