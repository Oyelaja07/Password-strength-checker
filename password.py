import re

def check_password_strength(password):
    # Start with a score of 0
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1

    # Decide strength
    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"


# Run program
while True:
    pwd = input("Enter a password (or 'q' to quit): ")
    if pwd.lower() == "q":
        break
    print("Strength:", check_password_strength(pwd))