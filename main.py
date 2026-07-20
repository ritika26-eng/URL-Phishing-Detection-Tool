from detector import analyze_url
import json
from datetime import datetime
import os

print("=== URL Phishing Detection Tool ===")

url = input("Enter a URL: ")

risk_score, findings = analyze_url(url)

if risk_score <= 20:
    status = "SAFE"
elif risk_score <= 50:
    status = "SUSPICIOUS"
else:
    status = "HIGH RISK"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

history = []

history.append({
    "url": url,
    "risk_score": risk_score,
    "status": status,
    "timestamp": timestamp,
    "findings": findings
})

print("History before saving:", history)
print("Saving to:", os.path.abspath("history.json"))

with open("history.json", "w") as file:
    json.dump(history, file, indent=4)

print("File saved!")