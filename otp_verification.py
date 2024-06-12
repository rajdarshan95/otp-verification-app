import tkinter as tk
import smtplib
import random
import math
def send_otp():
    global OTP
    digit = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digit[math.floor(random.random() * 10)]
    msg = OTP + " is your OTP"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("darshang1998@gmail.com", "bdzz xpng lacf lpau")  # Update with your email and password
    emailid = email_entry.get()
    s.sendmail('sender_email@gmail.com', emailid, msg)
    s.quit()
    status_label.config(text="OTP sent to your email.")

def verify_otp():
    global attempts
    global max_attempts
    global OTP
    a = otp_entry.get()
    if a == OTP:
        result_label.config(text="OTP is Verified. Access Granted")
    else:
        attempts += 1
        result_label.config(text="Incorrect OTP. Access denied.")
        if attempts == max_attempts:
            result_label.config(text="Maximum attempts reached. Please try again later.")

# GUI
root = tk.Tk()
root.title("OTP Verification")

# OTP Entry
otp_label = tk.Label(root, text="Enter OTP:")
otp_label.pack()
otp_entry = tk.Entry(root, show="*")
otp_entry.pack()

# Email Entry
email_label = tk.Label(root, text="Enter Your Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Buttons
send_button = tk.Button(root, text="Send OTP", command=send_otp)
send_button.pack()

verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack()

# Status and Result Labels
status_label = tk.Label(root, text="")
status_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Global variables
attempts = 0
max_attempts = 3
OTP = ""

root.mainloop()
