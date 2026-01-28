# Smart Grade Calculator

A simple Python project that acts as a smart calculator for student grades. It collects test, assignment, and exam scores, calculates the total and average, determines pass/fail status, and checks award eligibility using logical conditions.

## 📂 Project Structure

smart-grade-calculator/
│
├── main.py        # Main Python program
├── README.md      # Project documentation

## 🛠️ Requirements

Python 3.x

No external libraries are required.

## ▶️ How to Run the Program

Clone the repository:

git clone https://github.com/your-username/smart-grade-calculator.git

Navigate into the project folder:

cd smart-grade-calculator

Run the program:

python main.py

Enter the required scores when prompted.

## 🧠 Program Logic

Inputs: Test score, Assignment score, Exam score

Calculations:

Total Score = sum of all scores

Average Score = total / 3

Pass Mark: 50

Award Eligibility:

Average score ≥ 70 AND

Exam score ≥ 60

Note: Scores are assumed to be out of 100.

## 📌 Sample Output 1

Enter test score: 20
Enter assignment score: 25
Enter exam score: 60

--- Student Result ---
Total Score: 105.0
Average Score: 35.0
Status: FAILED
Award Status: DOES NOT QUALIFY FOR AWARD

## 📌 Sample Output 2

Enter test score: 60
Enter assignment score: 56
Enter exam score: 97

--- Student Result ---
Total Score: 213.0
Average Score: 71.0
Status: PASSED
Award Status: QUALIFIES FOR AWARD

## ✅ Learning Outcomes

Use of variables

Arithmetic operations

Comparison operators

Logical operators

Conditional statements in Python

## 📄 License

This project is for educational purposes.

Author: Mustapha Usman Khalifa
