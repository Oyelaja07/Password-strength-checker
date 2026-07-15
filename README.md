# 🔐 Password Strength Checker

A beginner-friendly Python project that checks the strength of a password based on commonly accepted security rules. The program analyzes the password and classifies it as **Strong**, **Medium**, or **Weak**.

---

## 📖 Project Description

This project was built as part of my Python programming practice.

The Password Strength Checker evaluates a user's password using regular expressions and assigns a strength rating based on the following criteria:

- Minimum length of 8 characters
- Contains uppercase letters
- Contains lowercase letters
- Contains numbers
- Contains special characters

The program continuously allows users to test different passwords until they choose to quit.

---

## 🚀 Features

- 🔒 Checks password strength
- 📏 Validates password length
- 🔠 Detects uppercase letters
- 🔡 Detects lowercase letters
- 🔢 Detects numeric digits
- ✨ Detects special characters
- 🔁 Allows multiple password checks
- ❌ Quit anytime by typing **q**

---

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (`re` module)

---

## 🧠 Python Concepts Practiced

This project helped me practice:

- Variables
- Functions
- User Input (`input()`)
- While Loops
- Conditional Statements (`if`, `elif`, `else`)
- Regular Expressions (`re`)
- String Handling
- Program Flow Control
- Return Statements

---

## 📂 Project Structure

```
Password-Strength-Checker/
│
├── password.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/Oyelaja07/Password-Strength-Checker.git
```

### Open the project folder

```bash
cd Password-Strength-Checker
```

### Run the program

```bash
python password.py
```

---

## 💻 Example Output

### Example 1

```
Enter a password (or 'q' to quit): Password123!

Strength: Strong 💪
```

---

### Example 2

```
Enter a password (or 'q' to quit): Hello123

Strength: Medium ⚠️
```

---

### Example 3

```
Enter a password (or 'q' to quit): abc

Strength: Weak ❌
```

---

## 📊 Password Strength Criteria

| Requirement | Points |
|-------------|--------|
| At least 8 characters | ✅ |
| Contains uppercase letter | ✅ |
| Contains lowercase letter | ✅ |
| Contains number | ✅ |
| Contains special character | ✅ |

### Rating

- **5 Points** → 💪 Strong
- **3–4 Points** → ⚠️ Medium
- **0–2 Points** → ❌ Weak

---

## 💡 Future Improvements

I plan to add the following features in future versions:

- Show why a password is weak
- Suggest improvements for stronger passwords
- Check for repeated characters
- Detect common passwords
- Display password score out of 100
- Build a graphical user interface (GUI)
- Generate secure random passwords

---

## 📚 What I Learned

While building this project, I learned how to:

- Use Python's `re` module
- Validate user input
- Write reusable functions
- Analyze strings using regular expressions
- Build interactive command-line applications
- Organize Python projects on GitHub

---

## 🎯 Project Objective

The objective of this project is to help users understand the characteristics of a strong password while improving my knowledge of Python programming and regular expressions.

---

## 👨‍💻 Author

**Umar Oyelaja**

GitHub: https://github.com/Oyelaja07

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful or interesting, feel free to **star** ⭐ this repository.

Thank you for visiting my project!
