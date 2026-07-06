# 🛡️ Mini Security Toolkit

A simple all-in-one Python CLI tool for basic security checks — port scanning, password strength analysis, and website security headers auditing. Built as a hands-on project to practice network programming, regex, and HTTP request handling.

## Features
- **Port Scanner**: Checks common ports (21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080) on any target IP/domain
- **Password Strength Checker**: Scores passwords based on length, uppercase/lowercase, digits, and special characters, with actionable suggestions
- **Security Headers Checker**: Verifies presence of key HTTP security headers (HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy) on any website

## How it works
1. Run the script and pick an option from the menu (1-4)
2. **Port Scanner** resolves the target hostname and attempts a socket connection on each port to detect which are open
3. **Password Checker** runs the password against a set of rules and returns a strength rating (Very Weak → Very Strong)
4. **Headers Checker** sends a GET request to the target URL and compares the response headers against a checklist of security best practices

## Usage
1. Install dependencies:

    pip install requests

2. Run the tool:

    python toolkit.py

3. Follow the menu prompts to choose a scan type.

## Use Cases
- Quick reconnaissance/audit tool for personal projects or small websites
- Learning tool for network programming and HTTP fundamentals
- Foundation for a larger security automation suite (e.g. adding vulnerability scanning, SSL checks)

## Disclaimer
Only scan systems and websites you own or have explicit permission to test.

## Author
Built by Youssef — Cybersecurity & Automation student, building practical tools as part of a broader security portfolio.
