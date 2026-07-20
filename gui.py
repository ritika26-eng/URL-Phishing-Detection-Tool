import tkinter as tk
from tkinter import messagebox
from detector import analyze_url
import json

# ------------------ FUNCTIONS ------------------

def scan_url():
    url = url_entry.get().strip()

    if url == "":
        messagebox.showwarning("Warning", "Please enter a URL.")
        return

    risk_score, findings = analyze_url(url)

    if risk_score <= 20:
        status = "🟢 SAFE"
    elif risk_score <= 50:
        status = "🟡 SUSPICIOUS"
    else:
        status = "🔴 HIGH RISK"

    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)

    result_box.insert(tk.END, f"Risk Score : {risk_score}\n")
    result_box.insert(tk.END, f"Status     : {status}\n\n")

    result_box.insert(tk.END, "Security Scan Report\n")
    result_box.insert(tk.END, "-" * 35 + "\n")

    if findings:
        for i, finding in enumerate(findings, start=1):
            result_box.insert(tk.END, f"{i}. {finding}\n")
    else:
        result_box.insert(tk.END, "✅ No suspicious indicators found.\n")

    result_box.config(state="disabled")


def clear_fields():
    url_entry.delete(0, tk.END)
    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    result_box.config(state="disabled")


def view_history():
    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)

    try:
        with open("history.json", "r") as file:
            history = json.load(file)

        if not history:
            result_box.insert(tk.END, "No scan history available.")
        else:
            for scan in history:
                result_box.insert(tk.END, f"URL: {scan['url']}\n")
                result_box.insert(tk.END, f"Risk Score: {scan['risk_score']}\n")
                result_box.insert(tk.END, f"Status: {scan['status']}\n")
                result_box.insert(tk.END, f"Time: {scan['timestamp']}\n")
                result_box.insert(tk.END, "-" * 50 + "\n")

    except FileNotFoundError:
        result_box.insert(tk.END, "history.json not found.")

    result_box.config(state="disabled")


# ------------------ WINDOW ------------------

window = tk.Tk()
window.title("URL Phishing Detection Tool")
window.geometry("800x600")
window.configure(bg="#F4F6F8")
window.resizable(False, False)

# ------------------ HEADING ------------------

heading = tk.Label(
    window,
    text="🛡 URL Phishing Detection Tool",
    font=("Segoe UI", 22, "bold"),
    bg="#F4F6F8",
    fg="#1F3A5F"
)
heading.pack(pady=20)

# ------------------ URL INPUT ------------------

url_label = tk.Label(
    window,
    text="Enter URL",
    font=("Segoe UI", 12, "bold"),
    bg="#F4F6F8"
)
url_label.pack()

url_entry = tk.Entry(
    window,
    width=70,
    font=("Segoe UI", 12)
)
url_entry.pack(pady=10)

# ------------------ BUTTONS ------------------

button_frame = tk.Frame(window, bg="#F4F6F8")
button_frame.pack(pady=10)

scan_btn = tk.Button(
    button_frame,
    text="Scan URL",
    command=scan_url,
    width=15,
    bg="#007ACC",
    fg="white",
    font=("Segoe UI", 11, "bold")
)
scan_btn.grid(row=0, column=0, padx=8)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=15,
    bg="#6C757D",
    fg="white",
    font=("Segoe UI", 11)
)
clear_btn.grid(row=0, column=1, padx=8)

history_btn = tk.Button(
    button_frame,
    text="View History",
    command=view_history,
    width=15,
    bg="#28A745",
    fg="white",
    font=("Segoe UI", 11)
)
history_btn.grid(row=0, column=2, padx=8)

# ------------------ RESULTS ------------------

result_box = tk.Text(
    window,
    width=90,
    height=20,
    font=("Consolas", 10),
    state="disabled"
)
result_box.pack(pady=20)

window.mainloop()