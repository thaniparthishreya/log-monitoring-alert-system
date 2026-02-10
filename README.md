# log-monitoring-alert-system
A Python-based security monitoring tool that scans server log files, detects suspicious activity, and sends real-time email alerts.  This project simulates a lightweight Security Information and Event Monitoring (SIEM) workflow used in real IT environments.
PROJECT OVERVIEW:
System administrators often spend hours manually reviewing logs to identify - failed login attempts and suspicious activity. This project automtes that process by parsing log files using Regex, detecting anomalies, generating a daily security report and sending automated email alerts.
FEATURES:
-Log parsing using python and Regex
-Detects multiple failed login attempts
-Sends automated email alerts
-Generates a daily security report 
TECH STACK:
-Python
-Regex
-SMTP
HOW IT WORKS:
-Reads server log file
-Extracts failed login attempts and IP addresses
-Detects repeated login failures from same IP
-Generates a security report 
-Sends email alert if suspicious activity is detected
SETUP INSTRUCTIONS:
-Clone the repository
-Ensure python3 is installed
-Configure email alerts in log_monitor.py, use a gmail app password not your real password 
-Run the script 
-Script can also be automated using crontab 
EXAMPLE OUTPUT:
Security Report

Total failed logins: 3
Suspicious IPs: ['192.168.1.10']
Total system errors: 2

AUTHOR
SHREYA THANIPARTHI
