"""
============================================================
Q1. Quiz Auto-Marker
============================================================
You are building an auto-marker system for a multiple-choice quiz.
The program must compare a student's answers with the answer key.
It should calculate the score, identify which questions were wrong, and assign a grade.

- Write 3 functions:
    1) score_quiz(key, ans)
    2) wrong_questions(key, ans)
    3) grade(score, total)
- Do not change the function names or parameters.
- After writing your functions, uncomment the test code at the bottom to test.

============================================================
"""

# ============================================================
# Step 1: Write function score_quiz(key, ans)
# ============================================================
# - key and ans are lists of equal length
# - Compare answers at the same position
# - Return total number of correct answers
# ============================================================

# 1) score_quiz(key, ans)
# Takes two lists of equal length.
# Compares each answer in the same position.
# Returns the total number of correct answers.
# Example:

# score_quiz(answer_key, student_ans)
# # returns 8

answer_key = ["B","D","A","A","C","B","C","D","B","A"]
student_ans = ["B","D","C","A","C","B","C","A","B","A"]

def score_quiz(key, ans):
    score = 0
    for i in range(en(key)):
        if key[i] == ans[i:]:
            score += 1


# ============================================================
# Step 2: Write function wrong_questions(key, ans)
# ============================================================
# - Return a list of question numbers (starting from 1) that are wrong
# - If all answers are correct, return an empty list
# ============================================================

# 2) wrong_questions(key, ans)
# Returns a list of question numbers (starting from 1) that were answered incorrectly.
# If all answers are correct, return an empty list [ ].
# Example:

# wrong_questions(answer_key, student_ans)
# # returns [3, 8]

def wrong_questions(key, ans):
    wrong = []
    for i in range(len(key)):
        if key[i] != ans[i]:
            wrong.append(i + 1)
            return wrong

# ============================================================
# Step 3: Write function grade(score, total)
# ============================================================
# - Compute percentage = (score / total) * 100
# - Return:
#     "A" if percentage >= 80
#     "B" if percentage >= 70
#     "C" if percentage >= 60
#     "D" otherwise
# ============================================================

# 3) grade(score, total) -> str
# Takes the student’s score and total number of questions total.
# Calculates percentage internally: (score / total) * 100.
# Returns:
# "A" if percentage ≥ 80%
# "B" if percentage ≥ 70%
# "C" if percentage ≥ 60%
# "D" otherwise
# Example:

# grade(8, 10)
# # returns "A"

def grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"

# ============================================================
# Step 4: Main Code Testing
# ============================================================

score = score_quiz(answer_key, student_ans)
wrong = wrong_questions(answer_key, student_ans)
final_grade = grade(score, len(answer_key))

print("Score:", score)
print("Wrong Questions:", wrong)
print("Grade:", final_grade)

