# Exercise 1- Print numbers 1–20 using range().
print("Exercise 1 - Print numbers 1-20 using range():")
print('----------------------------------------------')
print()
for number in range(1, 21):
    print(number)

print()  # Print a blank line to separate the two exercises

# Exercise 2 - Use a while loop to print:
print("Exercise 2 - Use a while loop to print:")
print('----------------------------------------------')
print()
count = 1
while count <= 20:
    print(count)
    count += 1

print()  # Print a blank line to separate the two exercises

# Exercise 3 - Use enumerate():
print("Exercise 3 - Use enumerate():")
print('----------------------------------------------')
print()
subjects = [ 
    "Python",
    "JavaScript",
    "Java",
    "MySQL"
]

for index, subject in enumerate(subjects, start=1):
    print(f"{index} -> {subject}")

print()  # Print a blank line to separate the two exercises

# Exercise 4 - Use zip():
print("Exercise 4 - Use zip():")
print('----------------------------------------------')
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

print("=============Another one===================")

students = ["David", "Eva", "Frank"]
scores = [82.67, 83.67, 91.00]

for student, score in zip(students,scores):
    print(f"{student} -> {score}")

print()  # Print a blank line to separate the two exercises

# Exercise 5 - Create a new list containing only even numbers using list comprehension.:
print("Exercise 5 - Create a new list containing only even numbers using list comprehension.:")
print('----------------------------------------------')

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
even_numbers = [x for x in numbers if x%2 == 0]
print(even_numbers)

print() # Print a blank line to separate the two exercises

# DAY 5 MINI PROJECT
students = [
    {"name": "Krishna", "score": 82.67},
    {"name": "Rahul", "score": 83.67},
    {"name": "Priya", "score": 91.00},
    {"name": "Amit", "score": 76.50},
    {"name": "Neha", "score": 88.25}
]

# Number of students
print(f"Number of students: {len(students)}")
for student in students:
    print(f"Students: {student}")

print()
print("======================================")


highest_score = float('-inf')
highest_name = ""
lowest_score = float('inf')
lowest_name = ""
total = 0.0
passed = []
failed = []
bright_student = []

for student in students:
    name = student['name']
    score = student['score']

    # Print each student's result immediately
    result = "PASSED" if score >= 60 else "FAILED"
    print(f"{name} -> {score} -> {result}")

    # Accumulate totals and find min/max
    total += score
    if score > highest_score:
        highest_score = score
        highest_name = name
    if score < lowest_score:
        lowest_score = score
        lowest_name = name

    # Track passed/failed lists
    if result == "PASSED":
        passed.append(name)
    else:
        failed.append(name)

    # List of students with score ≥ 80
    if score >= 80:
        bright_student.append(name)


# Compute average once, after loop
avg = total / len(students)

print()  # separator
print(f"Highest Score: {highest_name} -> {highest_score}")
print(f"Lowest Score: {lowest_name} -> {lowest_score}")
print(f"Average Score: {avg:.2f}")
print(f"Passed students: {', '.join(passed) if passed else 'None'}")
print(f"Failed students: {', '.join(failed) if failed else 'None'}")
print(f"Students with score 80+: {','.join(bright_student) if bright_student else 'None'}")


