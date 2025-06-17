# password_strength.py

import re

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

pwd = input("Enter password: ")
print("Strength:", check_strength(pwd))
