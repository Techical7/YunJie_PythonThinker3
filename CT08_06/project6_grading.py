# Predefined data
answer_key = ["A", "B", "B", "D"]
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}

# ## Task 1: Grade all Students
# **Grade all the student’s answers by answer key.​**

def grade_student(student_name):
    answers = student_answers[student_name]
    score = sum(1 for a, b in zip(answers, answer_key) if a == b)
    return score

print(f"John scored {grade_student('john')} out of {len(answer_key)}")
print(f"Jane scored {grade_student('jane')} out of {len(answer_key)}")
print(f"Alice scored {grade_student('alice')} out of {len(answer_key)}")
print(f"Bob scored {grade_student('bob')} out of {len(answer_key)}")
## Task 2: Calculate Class Average
# **Calculate the average score of the class.​**

def calculate_class_average():
    total_score = sum(grade_student(student) for student in student_answers.keys())
    average_score = total_score / len(student_answers)
    return average_score

print(calculate_class_average())

## Task 3: Find the Highest Scorer
# **Find the Highest Scorer​**

def find_highest_scorer():
    highest_score = 0
    highest_scorers = []
    for student in student_answers.keys():
        score = grade_student(student)
        if score > highest_score:
            highest_score = score
            highest_scorers = [student]
        elif score == highest_score:
            highest_scorers.append(student)
    return highest_scorers, highest_score

print(find_highest_scorer())


## Task 4: Display all results
# **Display Class Results​**

## Task 5: Build an interactive menu
# **Build an interactive menu for all the different functions​**
