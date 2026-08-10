# Quick Practice #1

name = input("Enter your name: ")
print(f"Hello, {name}!")

score = float(input("Enter your score: "))
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got a D!")
else:
    print("You got an F!")


# new example

students = [
    {"name": "Krishna", "score": 92},
    {"name": "Rahul", "score": 75},
    {"name": "Priya", "score": 58}
]

for student in students:
    score = student["score"]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(student["name"], "->", grade)
    # print(f"{student['name']} -> {grade}")
    print(" ")

print("------------------------------")



# DAY 3 ASSESSMENT
# Exercise 1 — Grade Calculator
""" Expected Output-
Enter your score: 87

Score: 87
Grade: B
 """
print(" ")
print("Welcome to the Grade Calculator!")
print(" ")
name = input("Enter your name: ")
print(f"Hello, {name}!")

score = float(input("Enter your score: "))
if score >= 90:
    print(f"Score: {score:.0f}")
    print("You got an A!")
    print(f"Congratulations {name}, you have excelled in your performance!")
elif score >= 80:
    print(f"Score: {score:.0f}")
    print("You got a B!")
    print(f"Good job {name}, you have done well!")
elif score >= 70:
    print(f"Score: {score:.0f}")
    print("You got a C!")
    print(f"Keep it up {name}, you can do better!")
elif score >= 60:
    print(f"Score: {score:.0f}")
    print("You got a D!")
    print(f"{name}, you need to work harder to improve your performance!")
else:
    print(f"Score: {score:.0f}")
    print("You got an F!")
    print(f"{name}, unfortunately, you have failed. Don't give up, keep trying and you will succeed!")

print(" ")
print("Thank you for using the Grade Calculator!")
print("--------------------------------------------------------------------------")

#Exercise 2 — Even and Odd
print(" ")
print(" ")
numbers = [10, 23, 44, 51, 62, 77, 80, 91]

for number in numbers:
    if number % 2 == 0:
        # print(f"{number} is an even number.")
        print(f"{number} -> Even")
    else:
        # print(f"{number} is an odd number.")
        print(f"{number} -> Odd")
print("--------------------------------------------------------------------------")
print(" ")
print(" ")

# Exercise 3 — Student Gradebook Upgrade
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

print("--------------------------------")
print(f"STUDENT GRADEBOOK".center(30, "-"))
print("--------------------------------")

for student in students:
    total_score = student["math"] + student["python"] + student["ai"]
    average_score = total_score / 3
    result = "PASSED" if average_score >= 60 else "FAILED"

    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Name: {student['name']}")
    print(f"Math Score: {student['math']}")
    print(f"Python Score: {student['python']}")
    print(f"AI Score: {student['ai']}")
    print(f"Total Score: {total_score:.2f}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    print("------------------------------")

    """ ⭐ Bonus

Add this:

Highest Scorer: Priya
Highest Average: 91.00 """

print(f"Highest Scorer: {max(students, key=lambda x: x['math'] + x['python'] + x['ai'])['name']}")
print(f"Highest Average: {max(students, key=lambda x: x['math'] + x['python'] + x['ai'])['math']/3 
                          + max(students, key=lambda x: x['math'] + x['python'] + x['ai'])['python']/3 
                          + max(students, key=lambda x: x['math'] + x['python'] + x['ai'])['ai']/3:.2f}")   

# Without using lemda expressions, you can achieve the same result by iterating through the list of students 
# and keeping track of the highest scorer and their average score. Here's how you can do it:
highest_average = 0
highest_student = ""

for student in students:
    total = student["math"] + student["python"] + student["ai"]
    average = total / 3

    if average > highest_average:
        highest_average = average
        highest_student = student["name"]

print(f"Highest Scorer: {highest_student}")
print(f"Highest Average: {highest_average:.2f}")