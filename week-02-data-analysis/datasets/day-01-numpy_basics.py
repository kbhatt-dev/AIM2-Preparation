import numpy as np

scores = np.array([70.25 ,20.54 ,58.24 ,74.47 ,68.65])

print(scores)
print(type(scores))
print(scores.ndim)
print(scores.shape)
print(scores.size)
print(scores.dtype)
print(scores[1:4])

print()
marks = np.array([
    [85, 90, 88],
    [72, 80, 75],
    [91, 95, 94]
])
print(marks)
print(type(marks))
print(marks.ndim)
print(marks.shape)
print(marks.size)
print(marks.dtype)
print(marks[2])
print(marks[0,0])

print()
numbers = np.zeros(5)
print(numbers)

matrix = np.zeros((3,4))
print(matrix)

oneNumber = np.ones(4)
print(oneNumber)

rangNumber = np.arange(1,10)
print(rangNumber)

evenNumber = np.arange(0,21,2)
print(evenNumber)

print()
arithMath = np.array([70, 80, 90, 100])
# sum
print(arithMath + 5)
# sub
print(arithMath - 5)
# mul
print(arithMath * 5)
# div
print(arithMath / 5)

# array + array
math = np.array([20, 30, 45])
ai = np.array([30, 35, 40])
total = math + ai
print(total)

print()
# aggregation Functions
scores1 = np.array([70, 80, 90, 100])
# sum
print(scores1.sum())
# mean
print(scores1.mean())
#maximum
print(scores1.max())
#minimum
print(scores1.min())

print()
# boolean filtering
scores2 = np.array([55, 72, 97, 45, 88, 68])
print(scores2 > 70)
print(scores2[scores2 > 70])


# Exercise 1 — Create an Array
print()
print("Exercise 1 — Create an Array")
print("-----------------------------")
numeric = np.array([10, 20, 30, 40, 50])
print(f"The array: {numeric}")
print(f"Its type: {type(numeric)}")
print(f"Its number of dimensions: {numeric.ndim}")
print(f"Its Shape: {numeric.shape}")
print(f"Its Size: {numeric.size}")
print(f"Its data type: {numeric.dtype}")

print()
print("Exercise 2 — Student Scores")
print("----------------------------")
sub = np.array(["Math", "Python", "AI", "Database"])
marks = np.array([85, 92, 78, 88])
total = marks.sum()
print(f"total: {total}")
avg = marks.mean()
print(f"Average: {avg}")
max = marks.max()
print(f"Highest Score: {max}")
min = marks.min()
print(f"Lowest Score: {min}")

print()
print("Exercise 3 — Array Operations")
print("------------------------------")
scores3 = np.array([60, 70, 80, 90, 100])
add5 = scores3 + 5
print(f"Add 5: {add5}")
sub10 = scores3 - 10
print(f"Sub 10 = {sub10}")
mul2 = scores3 * 2
print(f"Mul 2: {mul2}")
div10 = scores3 / 10
print(f"Div 10: {div10}")

print()
print("Exercise 4 — 2D Array")
print("----------------------")
subjects = np.array(["Math", "Python", "AI"])
students = np.array([
    [85, 90, 88],
    [72, 80, 75],
    [91, 95, 94]
])

print(f"Print entire array:\n {students}")
print(f"Student1's Python Score: {students[0, 1]}")
print(f"Student2's AI Score: {students[1, 2]}")
print(f"Student3's Math Score: {students[2, 0]}")
print(f"Shape: {students.shape}")
print(f"number of dimetion: {students.ndim}")
print(f"Size: {students.size}")

print()
print("Exercise 5 — Filtering")
print("-----------------------")
scores5 = np.array([45, 67, 82, 91, 56, 73, 38, 88])
print(f"Scores greater than 70: {scores5 > 70}")
print(f"Scores greater than 70: {scores5[scores5 > 70]}")
print(f"Scores less than 60: {scores5 < 60}")
print(f"Scores less than 60: {scores5[scores5 < 60]}")
print(f"Scores equal to or greater than 80: {scores5 >= 80}")
print(f"Scores equal to or greater than 80: {scores5[scores5 >= 80]}")

# 🏆 Day 1 Mini-Project
print()
print("===================================")
print("🏆 Day 1 Mini-Project".center(33, "="))
print("===================================")
studentsName = np.array(["Krishna", "Rahul", "Priya", "Amit"])
subjects = np.array(["Math", "Python", "AI"])
subScores= np.array([
    [85, 92, 88],
    [75, 80, 75],
    [91, 95, 94],
    [65, 70, 68]
])

student_averages = subScores.mean(axis=1)
subject_averages = subScores.mean(axis=0)



print(f"1. Display all scores: \n{subScores}")
print(f"2. Display shape: {subScores.shape}")
print(f"3. Display number of students: {studentsName.size}")
print(f"4. Display number of subjects: {subjects.size}")
print()
print(f"5. Calculate each student's average")
for name, average in zip(studentsName, student_averages):
    print(f"{name}: {average:.2f}")

print()
print(f"6. Calculate average for each subject:")
for subName, subAvg in zip(subjects, subject_averages):
    print(f"{subName}: {subAvg:.2f}")
print()

# Find highest score
print(f"7. Find highest score: {subScores.max()}")
print(f"8. Find lowest score: {subScores.min()}")
print(f"9. Find all scores >= 80: {subScores[subScores >= 80]}")
