""" Exercise 1

Create a list containing 5 AIM2 subjects.

Then:

print the first subject
print the last subject
change the third subject
add a new subject
remove one subject
print the total number of subjects """

# Creating a list of AIM2 subjects
import math


subjects = ["TensorFlow and Keras", "Machine Learning", "Deep Learning with Python", "Data Visualization", "Data Mining and Analysis"]
print("First Subject:", subjects[0])

print("Last Subject:", subjects[-1])

print ("Changing the third subject...")
subjects[2] = "Natural Language Processing 1"
print("Updated Subjects List:", subjects)

subjects.append("Deep Learning with Python")
subjects.insert(1, "Data Science with Python")
print("Subjects List after adding a new subject:", subjects)
print("Total Number of Subjects:", len(subjects))

subjects.remove("Data Science with Python")
print("Subjects List after removing a subject:", subjects)
subjects.pop(5)

print("Subjects List after removing a subject by index:", subjects)
print("Total Number of Subjects:", len(subjects))


# DAY 2 MINI PROJECT
# Student Gradebook

students = [
    {
        "name": "Krishna",
        "math": 95,
        "python": 88,
        "ai": 65
    },
    {
        "name": "Rahul",
        "math": 82,
        "python": 91,
        "ai": 78
    },
    {
        "name": "Priya",
        "math": 90,
        "python": 94,
        "ai": 89
    }
]

print ("===============================")
title = "STUDENT GRADEBOOK"
print(title.center(30, " "))
print ("===============================")

for student in students:
    name = student["name"]
    math_score = student["math"]
    python_score = student["python"]
    ai_score = student["ai"]
        
    print(f"Name: {name}")
    print(f"Math: {math_score}")
    print(f"Python: {python_score}")
    print(f"AI: {ai_score}")
    print(" ")

print("-------------------------------")

for student in students:
    name = student["name"]
    math_score = student["math"]
    python_score = student["python"]
    ai_score = student["ai"]

    total_score = math_score + python_score + ai_score
    average_score = total_score / 3

    result = average_score >= 60
    if result:
        result = "PASSED"
    else:
        result = "FAILED"

    print(f"Name: {name}")
    print(f"Math: {math_score}")
    print(f"Python: {python_score}")
    print(f"AI: {ai_score}")
    print(f"Total: {total_score:.2f}")
    print(f"Average: {average_score:.2f}")
    print(f"Result: {result}")
    print(" ")

print("-------------------------------")

print (students[0])
print (students[0]["name"])
print (students[0]["math"])
