class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old.")

student1 = Student("Krishna", 28)
student2 = Student("Rahul", 25)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)   

student1.introduce()

# ⭐ Exercise 3 — Student Grade Class
print()
print("====================================")
print("Student Scores".center(30,"="))
print("====================================")

class StudentScore:
    def __init__(self, name, math, python, ai):
        self.name = name
        self.math = math
        self.python = python
        self.ai = ai

    def calculate_total(self):
        return self.math + self.python + self.ai

    def calculate_average(self):
        return self.calculate_total()/3

    def calculate_grade(self):
        average = self.calculate_average()

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

    def get_result(self):
        if self.calculate_average() >= 60:
            return "PASSED"
        else:
            return "FAILED"

student = StudentScore("Krishna", 95, 88, 65)
print(f"Name: {student.name}")
print(f"Total: {student.calculate_total()}")
print(f"Average: {student.calculate_average():.2f}")
print(f"Grade: {student.calculate_grade()}")
print(f"Result: {student.get_result()}")
print("-------------------------")

# Multiple Objects
students = [
    StudentScore("Kuntal", 98, 78, 75),
    StudentScore("Rahul", 82, 91, 78),
    StudentScore("Priya", 90, 94, 89),
    StudentScore("Parth", 86, 75, 63),
    StudentScore("Heta", 65, 20, 42)
]

for student in students:
    print(f"Name: {student.name}")
    print(f"Total: {student.calculate_total()}")
    print(f"Average: {student.calculate_average():.2f}")
    print(f"Grade: {student.calculate_grade()}")
    print(f"Result: {student.get_result()}")
    print("-------------------------")

# Inheritance
class Person:

    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"My name is {self.name}.")

class Student(Person):
# super
    def __init__(self, name, program):
        super().__init__(name)
        self.program = program

    def study(self):
        print(f"{self.name} is Studying")

student11 = Student("Krishna", "AIM2")
student11.introduce()
student11.study()
print(f"name:  {student11.name}")
print(f"program name: {student11.program}")
print()
print("============================================")


#Exercise 1 — Basic Class
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

cars = [
    Car("Toyota", "Corolla", 2022),
    Car("Hundai", "verna", 2021)
]

for car in cars:
    print(f"Brand: {car.brand}")
    print(f"Model: {car.model}")
    print(f"Year: {car.year}")
    print('----------------------')

#Exercise 2 - Student Class
class Student_Ex2:
    def __init__(self, name, age, program):
        self.name = name
        self.age = age
        self.program = program
    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am studying {self.program}.")
        print(f"I am {self.age} year old.")

student_ex2 = Student_Ex2("Krishna", 28, "AIM2")
student_ex2.introduce()   

print()
print("=========================================")
print("Student Grade List".center(30,"="))
print("=========================================")
print()
#DAY 7 MINI PROJECT
class StudentGradeSheet:

    def __init__(self, name, math, python, ai, age):
        self.name = name
        self.math = math
        self.python = python
        self.ai = ai
        self.age = age

    def calculate_total(self):
        total = self.math + self.python + self.ai 
        return total

    def calculate_average(self):
        average = self.calculate_total() /3
        return average

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return ""
        elif average >= 60:
            return "D"
        else:
            return "F"

    def calculate_result(self):
        average = self.calculate_average()

        if average >= 60:
            return "PASSED"
        else:
            return "FAILED"

try:
    with open("student_list.txt", "r") as file:
        lines = file.readlines()

    highest_score = float('-inf')
    highest_name = ""
    highest_grade = " "
    lowest_score = float('inf')
    lowest_name = ""
    lowest_grade = ""
    total = 0.0
    count = 0
    passed = []
    failed = []
    bright_student = []

    for line in lines[1:]:
        try:
            line = line.strip()
            if not line:
                continue
            data = line.split(",")
            name = data[0]
            math = float(data[1])
            python = float(data[2])
            ai = float(data[3])
            age = int(data[4])

            student = StudentGradeSheet(name, math, python, ai, age)
            total_score = student.calculate_total()
            average_score = student.calculate_average()
            grade = student.calculate_grade()
            result = student.calculate_result()

            # Find the highest and lowest scorer
            if total_score > highest_score:
                highest_score = total_score
                highest_name = name
                highest_grade = grade

            if total_score < lowest_score:
                lowest_score = total_score
                lowest_name = name
                lowest_grade = grade

            total += total_score
            count += 1

            if average_score >= 90:
                bright_student.append(name)

            if result == "PASSED":
                passed.append(name)
            else:
                failed.append(name)

            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Math Score: {math}")
            print(f"Python Score: {python}")
            print(f"AI Score: {ai}")
            print()
            print(f"Total: {total_score}")
            print(f"Average: {average_score:.2f}")
            print(f"Grade: {grade}")
            if result == "PASSED":
                print("Congratulation, You are PASSED...!!!!")
            else:
                print("You are FAILED, Better luck next time")
            print("-------------------------")

        except (ValueError, IndexError):
            print("Error::::: Invalid student data.")
            print("------------------------------------")

    if count > 0:
        print(f"Highest scorer: {highest_name} with total {highest_score} and grade {highest_grade}")
        print(f"Lowest scorer: {lowest_name} with total {lowest_score} and grade {lowest_grade}")
        print(f"Class total: {total}")
        print(f"Class average total: {total/count:.2f}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Bright students: {bright_student}")

except FileNotFoundError:
    print("Error:::: student_list.txt file not found.")
    