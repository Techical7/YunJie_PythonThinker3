# In this activity, you will build a system to:
# Grade all students based on their answers.
# Calculatethe average score for the class.
# Identify the student(s) with the highest score.
# Display all results in an organized format.

#Create a list of students and their answers
students = [
    {"name": "Alice", "answers": ["A", "B", "C", "D"]},
    {"name": "Bob", "answers": ["A", "C", "C", "D"]},
    {"name": "Charlie", "answers": ["B", "B", "C", "D"]},
]
# Define the correct answers
correct_answers = ["A", "B", "C", "D"]

# Create afunction to grade a student's answers
def grade_student(student):
    score = 0
    for student_answer, correct_answer in zip(student["answers"], correct_answers):
        if student_answer == correct_answer:
            score += 1
    return score

# Grade all students and store their scores
for student in students:
    student["score"] = grade_student(student)

# Calculate the average score for the class
total_score = sum(student["score"] for student in students)
average_score = total_score / len(students)

# Identify the student(s) with the highest score
highest_score = max(student["score"] for student in students)
top_students = [student["name"] for student in students if student["score"] == highest_score]

# Display all results in an organized format
print("Student Scores:")
for student in students:
    print(f"{student['name']}: {student['score']}")
print(f"\nAverage Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print("Top Student(s): " + ", ".join(top_students))
