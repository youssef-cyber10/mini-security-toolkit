import socket
import re
import requests

# ---------- 1. Port Scanner ----------
def scan_ports(target, ports):
    print(f"\nScanning {target}...")
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Could not resolve hostname.")
        return

    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("No open ports found.")
    else:
        print(f"\nOpen ports: {open_ports}")


# ---------- 2. Password Strength Checker ----------
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters (12+ recommended).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    levels = {0: "Very Weak", 1: "Weak", 2: "Weak", 3: "Moderate", 4: "Strong", 5: "Strong", 6: "Very Strong"}
    print(f"\nPassword Strength: {levels.get(score, 'Very Strong')}")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"  - {tip}")


# ---------- 3. Security Headers Checker ----------
def check_security_headers(url):
    if not url.startswith("http"):
        url = "https://" + url

    important_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
    ]

    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException as e:
        print(f"Error: Could not reach {url} ({e})")
        return

    print(f"\nChecking security headers for {url}...\n")
    for header in important_headers:
        if header in response.headers:
            print(f"[OK] {header}: {response.headers[header]}")
        else:
            print(f"[MISSING] {header}")


# ---------- Main Menu ----------
def main():
    while True:
        print("\n=== Mini Security Toolkit ===")
        print("1. Port Scanner")
        print("2. Password Strength Checker")
        print("3. Website Security Headers Checker")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            target = input("Enter target IP or domain (e.g. scanme.nmap.org): ")
            common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080]
            scan_ports(target, common_ports)

        elif choice == "2":
            pwd = input("Enter password to check: ")
            check_password_strength(pwd)

        elif choice == "3":
            url = input("Enter website URL (e.g. github.com): ")
            check_security_headers(url)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
