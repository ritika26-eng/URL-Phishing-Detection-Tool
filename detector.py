import re
from urllib.parse import urlparse

def analyze_url(url):
    risk_score = 0
    findings = []

    # Check HTTPS
    if not url.startswith("https://"):
        findings.append("URL does not use HTTPS.")
        risk_score += 15

    # Check for IP address
    ip_pattern = r"\d+\.\d+\.\d+\.\d+"
    if re.search(ip_pattern, url):
        findings.append("URL contains an IP address.")
        risk_score += 25

    # Check for @ symbol
    if "@" in url:
        findings.append("URL contains '@' symbol.")
        risk_score += 20

    # Check for URL shorteners
    shorteners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "is.gd",
        "ow.ly",
        "buff.ly"
    ]

    for shortener in shorteners:
        if shortener in url:
            findings.append("URL uses a URL shortening service.")
            risk_score += 20
            break

    # Check suspicious keywords
    suspicious_keywords = [
        "login",
        "verify",
        "update",
        "secure",
        "bank",
        "account",
        "password"
    ]

    for keyword in suspicious_keywords:
        if keyword in url.lower():
            findings.append(f"Suspicious keyword detected: {keyword}")
            risk_score += 10

    # Check URL length
    if len(url) > 75:
        findings.append("URL is unusually long.")
        risk_score += 15

    # Check for hyphens in the domain
    domain = urlparse(url).netloc

    if "-" in domain:
        findings.append("Domain contains hyphens.")
        risk_score += 10

    # Check number of subdomains
    parts = domain.split(".")

    if len(parts) > 3:
        findings.append("URL contains multiple subdomains.")
        risk_score += 15

    print("\n========== Security Scan Report ==========")

    if findings:
        for i, finding in enumerate(findings, start=1):
            print(f"{i}. {finding}")
    else:
        print("No suspicious indicators found.")

    print("==========================================")

    return risk_score, findings