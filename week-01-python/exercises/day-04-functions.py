# Exercise 1 — Simple Functions
def greet():
    print("Hello, welcome to AIM2 Python preparation!")

def greet_student(name):
    print(f"Hello, {name}!")

greet()
greet_student("Krishna")
print(" ")
print("====================================================")

# Exercise 2 — Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

add_result = add(5, 3)
subtract_result = subtract(10, 4) 
multiply_result = multiply(6, 7)
divide_result = divide(15, 3)
divide_by_zero_result = divide(10, 0)

print(f"Addition Result: {add_result}")
print(f"Subtraction Result: {subtract_result}")
print(f"Multiplication Result: {multiply_result}")
print(f"Division Result: {divide_result}")
print(f"Division by Zero Result: {divide_by_zero_result}")
print(" ")
print("====================================================")

# Exercise 3 — Student Functions ⭐
def student_info(name, age, grade):
    print(f"Student Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")

def calculate_total(math, python, ai):
    total = math + python + ai
    return total

def calculate_average(math, python, ai):
    total = calculate_total(math, python, ai)
    average = total / 3
    return average

def calculate_percentage(math, python, ai):
    total = calculate_total(math, python, ai)
    percentage = (total / 300) * 100
    return percentage

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def check_result(average):
    if average >= 60:
        return "Pass"
    else:
        return "Fail"


math_score = 85
python_score = 92
ai_score = 78

total = calculate_total(math_score, python_score, ai_score)
average = calculate_average(math_score, python_score, ai_score)
percentage = calculate_percentage(math_score, python_score, ai_score)
grade = calculate_grade(average)
result = check_result(average)

student_info("Alice", 20, grade)
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")
print(" ")
print("====================================================")

# ⭐ Exercise 4 — BIG DAY 4 PROJECT
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

print("================================")
print(f"STUDENT GRADEBOOK".center(30," "))
print("================================")

for student in students:
    name = student["name"]
    math_score = student["math"]
    python_score = student["python"]
    ai_score = student["ai"]

    total = calculate_total(math_score, python_score, ai_score)
    average = calculate_average(math_score, python_score, ai_score)
    percentage = calculate_percentage(math_score, python_score, ai_score)
    grade = calculate_grade(average)
    result = check_result(average)

    print(f"Student Name: {name}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    # print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    print(" ")
    print("================================")
    print(" ")
