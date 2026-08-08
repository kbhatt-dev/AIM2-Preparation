name = "Krishna"
age = 25
programming_language = "Artificial Intelligence and Machine Learning"
score = 95.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Programming Language:", programming_language)
print("Score:", score)
print("Is Student:", is_student)

print ("Hello, my name is", name, "and I am", age, "years old. I am learning", programming_language, "and my current score is", score, ". Is it true that I am a student?", is_student)

# type() built-in function is used to get the data type of a variable. It returns the type of the object passed as an argument.
print (type(name))
print (type(age))
print (type(programming_language))
print (type(score))
print (type(is_student))

# String concatenation
first_name = "Krishna"
last_name = "Bhatt"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String formatting using f-strings
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)
print (f"My score in {programming_language} is {score}.")

#String formatting using format() method
greeting_format = "Hello, my name is {} and I am {} years old.".format  (name, age)
print(greeting_format)

#String Methods
message = "   Hello World!   "
print("Original Message:", message)
print("Message in Uppercase:", message.upper())
print("Message in Lowercase:", message.lower())
print ("Message Simple Text Title:", message.title())
# strip() removes extra spaces at the beginning and end.
print("Message after Stripping Whitespaces:", message.strip())
print("Message after Replacing 'World' with 'Python':", message.replace("World", "Python"))
print ("Message using String Methods:", message.strip().replace("World", "Python").upper())

#find the string length using len() built-in function
print("Length of the message:", len(message))

# String Slicing
sample_string = "Artificial Intelligence and Machine Learning"
print("Sample String:", sample_string)
# Slicing from index 0 to 9 (not including 10)
print("Sliced String:", sample_string[0:10])

# Numbers and Arithmetic Operations
num1 = 10
num2 = 3

print ("Addition:", num1 + num2)
print ("Subtraction:", num1 - num2)
print ("Multiplication:", num1 * num2)
print ("Division:", num1 / num2)
print ("Floor Division:", num1 // num2)
print ("Modulus:", num1 % num2)
print ("Power:", num1 ** num2)

#Boolean Operations
print (age > 18)    # True
print (age < 18)    # False
print (age == 25)   # True

#None = There is currently no value.
student_email = None

#input() function is used to take input from the user. It returns the input as a string.
user_name = input("Enter your name: ")
city = input("Enter your city: ")
print(f"Hello {user_name.strip()}, you live in {city.strip()}.")
#input() function always returns a string. if you check the type of the input, it will be <class 'str'>.
print(type(city))

#input() function always returns a string. If you want to take an integer input, you need to convert it using int() function.
user_age = int(input("Enter your age: "))
print(f"Hello {user_name.strip()}, you are {user_age} years old.")
print(type(user_age))  # <class 'int'>

score = float(input("Enter your score: "))
print(f"Hello {user_name.strip()}, your score is {score}.")
print(type(score))  # <class 'float'>

# =============================================================
# ==========================Exercises==========================
# =============================================================
print("======================Welcome to the Student Performance Program!======================")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
program = input("Enter your program of Course: ")
math_score = float(input("Enter your Math score: "))
python_score = float(input("Enter your Python score: "))
ai_score = float(input("Enter your AI score: "))

total_score = math_score + python_score + ai_score
average_score = total_score / 3

result = average_score >= 60
if result:
    result = "PASSED"
else:
    result = "FAILED"

print("===============================")
title = "Student Performance"
print(title.center(30, "="))
print("===============================")
print(" ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Program: {program}")
print(" ")
print(f"Math Score: {math_score}")
print(f"Python Score: {python_score}")
print(f"AI Score: {ai_score}")
print(" ")
print(f"Total Score: {total_score:.2f}")
print(f"Average Score: {average_score:.2f}")
print(" ")
print(f"Result: {result}")
print("===============================")


