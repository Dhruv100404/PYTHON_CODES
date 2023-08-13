student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for list in student_scores:
    score = student_scores[list]
    if score > 90:
        student_grades[list] = "Outstanding"
    elif score > 80:
        student_grades[list] = "acceptable"
    else:
        student_grades[list] = "fail"
# 🚨 Don't change the code below 👇
print(student_grades)
