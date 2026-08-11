# Exercise 1 — File Writing
with open("students.txt", "w") as file:
    file.write("Krishna, 82.67\n")
    file.write("Kuntal, 90.21\n")
    file.write("Parth, 98.12 \n")

# Read the file and print each student.
with open ("students.txt", "r") as file:
    data = file.read()
print(data)

# or 
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
        

# Exercise 3 — Exception Handling
try:
    age = int (input("Enter your age: "))
except ValueError:
    print("Invalid age, Please enter a valid number.")

# Exercise 4 — Create Your Own Module
import student_utils


total = student_utils.calculate_total(94.21,65.25,87.21)
print(f"{total:.2f}")
avg = student_utils.calculate_average(total)
print(f"average = {avg:.2f}")
grade = student_utils.calculate_grade(avg)
print(f"grade = {grade}")
result = student_utils.calculate_result(grade)
print("result=", result)

print()
print("=================================================")
print()
# ⭐ DAY 6 MINI PROJECT
# with open ("student_list.txt", "w") as file:
#     file.write("Name,Math,Python,AI \n")
#     file.write("Krishna,95,88,65 \n")
#     file.write("Kuntal,90,92,87 \n")
#     file.write("Parth,98,95,94 \n")
#     file.write("Rahul,82,91,78 \n")
#     file.write("Priya,90,94,89 \n")

# with open("student_list.txt", "r") as file:
#     for line in file:
#         print(line.strip())

import student_utils

print("========================================")
print("       STUDENT FILE ANALYZER")
print("========================================")
print()

try:
    with open("student_list.txt", "r") as file:
        lines = file.readlines()

    # Skip the header
    for line in lines[1:]:

        try:
            # Remove whitespace and newline
            line = line.strip()

            # Split the line into separate values
            data = line.split(",")

            # Extract student information
            name = data[0]
            math = float(data[1])
            python = float(data[2])
            ai = float(data[3])

            # Calculate student performance
            total = student_utils.calculate_total(math, python, ai)
            average = student_utils.calculate_average(total)
            grade = student_utils.calculate_grade(average)
            result = student_utils.calculate_result(grade)

            # Display result
            print(f"Student: {name}")
            print(f"Math: {math:.2f}")
            print(f"Python: {python:.2f}")
            print(f"AI: {ai:.2f}")
            print(f"Total: {total:.2f}")
            print(f"Average: {average:.2f}")
            print(f"Grade: {grade}")
            print(f"Result: {result}")
            print("----------------------------------------")

        except (ValueError, IndexError):
            print("Error: Invalid student data.")
            print("----------------------------------------")

except FileNotFoundError:
    print("Error: student_list.txt was not found.")