# OTP Verification App

<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python" width="200"/>

## Project Description
This is a Python Tkinter application for OTP verification via email. Users can request an OTP to be sent to their email and then verify the OTP within the application.

## Features
- Generate a 6-digit OTP
- Send OTP to the user's email
- Verify OTP input by the user
- Limit the number of verification attempts to 3

## Prerequisites
- Python 3.x
- Tkinter (usually included with Python)
- smtplib (part of the Python standard library)

## Usage
1. Run the application:
    ```bash
    python otp_verification.py
    ```

2. Enter your email and click "Send OTP".
3. Check your email for the OTP.
4. Enter the OTP in the application and click "Verify OTP".

## Code Overview
### `otp_verification.py`
This file contains the main logic for generating, sending, and verifying OTPs using a simple Tkinter GUI.
