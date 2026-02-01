# Practice Excerise 1: Creating a Disctionary
# Create a dictionary to store students names and their grades.

# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print(f"Student grades: {students}")

# Try adding more students to this dictionary with their grades.

# students = {"Alice": 85, "Bob": 90, "Charlie": 78, "John": 92, "Emma": 88, "Michael": 76}
# print(f"Student grades: {students}")

# Try using an input() to ask which student you want to check the score for?
# What happens if you try accessing a student that does not exist?

students = {"Alice": 85, "Bob": 90, "Charlie": 78, "John": 92, "Emma": 88, "Michael": 76}
student_name = input("Enter the student's name to check the score: ")
if student_name in students:
    print(f"{student_name}'s grade: {students[student_name]}")
else:
    print(f"Sorry, {student_name} is not in the student list.")

