## 🛡️ URL Phishing Detection Tool
A Python-based desktop application that detects potentially malicious URLs using heuristic analysis. The tool analyzes multiple URL characteristics, assigns a risk score, and classifies URLs as Safe, Suspicious, or High Risk to help users identify phishing attempts.

## 🌍 Real-World Problem
Phishing websites are designed to steal sensitive information by mimicking legitimate websites. Many users cannot easily distinguish between a safe and a malicious URL.
URL Phishing Detecton Tool helps users by automatically analyzing URLs using multiple security checks and providing a risk assessment before the website is visited.

## ✨ Features
- HTTPS Validation
- IP Address Detection
- URL Shortener Detection
- '@' Symbol Detection
- Suspicious Keyword Detection
- Long URL Detection
- Hyphen (-) Detection
- Multiple Subdomain Detection
- Risk Score Calculation
- Safe / Suspicious / High Risk Classification
- Scan History with Timestamp
- Desktop GUI using Tkinter

## 🛠️ Technologies Used
- Python
- Tkinter
- JSON
- Regular Expressions (Regex)
- urllib.parse

## 📂 Project Structure
PhishGuard URL Analyzer/
├── gui.py
├── detector.py
├── main.py
├── history.json
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots

 ## 🚀 How to Run
 1. Clone the repository
```bash
git clone https://github.com/your-username/phishguard-url-analyzer.git
```
 2. Open the project folder
```bash
cd phishguard-url-analyzer
```
 3. Run the application
```bash
python gui.py
```

## 📸 Application Screenshots
- Main Window
- URL Scan Result
- Scan History

## 🔮 Future Improvements
- Machine Learning-based phishing detection
- Real-time URL reputation checking
- Google Safe Browsing API integration
- Dark Mode
- Export scan reports
- Domain WHOIS lookup

## 👩‍💻 Author
**Ritika Pandey**
Final Year Electronics & Telecommunication Engineering Student
Aspiring Cybersecurity Engineer

## 📜 License
This project is licensed under the MIT License.
