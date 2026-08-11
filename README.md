# AIM2 Preparation 🚀

My preparation journey for the **Artificial Intelligence and Machine Learning (AIM2)** graduate program.

The goal of this repository is to build a strong foundation in Python, data analysis, machine learning, and deep learning before starting the AIM2 program.

---

## 🎯 Preparation Goals

Before starting AIM2, my main goals are to become comfortable with:

* Python programming
* NumPy
* Pandas
* Data visualization
* Machine learning fundamentals
* Scikit-learn
* TensorFlow / Keras
* Basic PyTorch
* NLP fundamentals
* Git and GitHub

I already completed a Microservices course covering Java, Spring Boot, Spring Cloud, Docker, Kubernetes, Helm, and Microservices Security. The current preparation therefore focuses primarily on Python and AI/ML foundations.

---

## 🗂️ Project Structure

```text
AIM2-Preparation/
│
├── .venv/
│
├── week-01-python/
│   ├── notes/
│   ├── exercises/
│   └── student-performance-analyzer/
│
├── week-02-data-analysis/
│   ├── notebooks/
│   ├── datasets/
│   └── canadian-housing-analysis/
│
├── week-03-machine-learning/
│   ├── notebooks/
│   ├── datasets/
│   └── customer-churn-prediction/
│
├── week-04-deep-learning/
│   └── mnist-digit-classifier/
│
└── README.md
```

---

# 📅 Preparation Progress

# Week 1 — Python 🐍

## Day 1 — Python Fundamentals ✅

Topics completed:

* Variables
* Data types
* Strings
* String methods
* String slicing
* Numbers
* Arithmetic operators
* Boolean values
* `None`
* `input()`
* Type conversion
* `int()`
* `float()`
* `type()`
* f-strings
* Basic conditional logic

### Mini Project

**Student Performance Analyzer**

The program accepts student information and scores and calculates:

* Total score
* Average score
* Pass/fail result

---

## Day 2 — Data Structures & Student Gradebook ✅

Topics completed:

* Lists
* List indexing
* Negative indexing
* Updating list elements
* `append()`
* `insert()`
* `remove()`
* `pop()`
* `len()`
* Dictionaries
* Dictionary keys and values
* Accessing dictionary data
* Iterating through a list of dictionaries
* Basic data processing

### Mini Project

**Student Gradebook**

The program stores multiple students and calculates:

* Individual scores
* Total score
* Average score
* Pass/fail result

---

## Day 3 — Control Flow ✅

Topics completed:

* `if`
* `elif`
* `else`
* Comparison operators
* Logical conditions
* `for` loops
* Modulo operator
* Even/odd checking
* Grade calculation
* Nested decision-making
* Conditional expressions
* `max()`
* Basic `lambda` usage

### Mini Projects

**Grade Calculator**

Calculates a student's grade based on their score.

**Student Gradebook Upgrade**

The gradebook was upgraded to calculate:

* Total score
* Average score
* Letter grade
* Pass/fail result
* Highest-scoring student

---

## Day 4 — Functions & Modular Programming ✅

Topics completed:

* `def`
* Function calls
* Parameters
* Arguments
* `return`
* Multiple parameters
* Function reuse
* Functions calling other functions
* Local variables
* Basic error handling
* Modular programming

### Mini Project

**Refactored Student Gradebook**

The Student Gradebook was redesigned using reusable functions:

```text
calculate_total()
        ↓
calculate_average()
        ↓
calculate_percentage()
        ↓
calculate_grade()
        ↓
check_result()
```

This made the program more organized, reusable, and easier to maintain.

---

## Day 5 — Loops & Iteration ✅

Topics completed:

* `for` loops
* `while` loops
* `range()`
* `enumerate()`
* `zip()`
* Iterating through collections
* List comprehensions
* Accumulating values
* Finding minimum and maximum values
* Filtering data
* Basic data aggregation

### Mini Project

**Student Performance Analyzer**

The program processes multiple students and calculates:

* Number of students
* Individual results
* Highest score
* Lowest score
* Average score
* Passed students
* Failed students
* Students with scores of 80+

This introduced more practical techniques for processing collections of data.

---

## Day 6 — File Handling, Exceptions & Modules ✅

Topics completed:

* File writing
* File reading
* `open()`
* `with open()`
* Reading files line by line
* `read()`
* `readlines()`
* `try`
* `except`
* `FileNotFoundError`
* `ValueError`
* `IndexError`
* Creating custom Python modules
* Importing custom modules
* Reusing functions from another file
* Combining file data with Python processing

### Mini Project

**Student File Analyzer**

The program reads student information from a text file and processes:

* Student names
* Subject scores
* Total scores
* Average scores
* Letter grades
* Pass/fail results

The project also introduced basic error handling for missing or invalid student data.

---

## Day 7 — Object-Oriented Programming ✅

Topics completed:

* Classes
* Objects
* `__init__()`
* `self`
* Instance attributes
* Instance methods
* Creating multiple objects
* Inheritance
* Parent and child classes
* `super()`
* Combining OOP with file handling
* Combining OOP with exception handling
* Object-based data processing

### Mini Project

**Student Grade Sheet Analyzer**

The Day 6 Student File Analyzer was upgraded using Object-Oriented Programming.

The program:

1. Reads student data from a file
2. Creates a `StudentGradeSheet` object for each student
3. Calculates total scores
4. Calculates averages
5. Determines grades
6. Determines pass/fail results
7. Finds the highest scorer
8. Finds the lowest scorer
9. Calculates the class total
10. Calculates the class average
11. Tracks passed and failed students
12. Identifies high-performing students

This project combined several Week 1 concepts:

```text
File Handling
      +
Exception Handling
      +
Classes & Objects
      +
Methods
      +
Loops
      +
Lists
      +
Conditional Logic
      ↓
Student Grade Sheet Analyzer
```

---

# 📊 Week 1 Summary

Week 1 focused on building a practical Python programming foundation.

The progression was:

```text
Day 1
Python Fundamentals
      ↓
Day 2
Lists & Dictionaries
      ↓
Day 3
Control Flow
      ↓
Day 4
Functions
      ↓
Day 5
Loops & Data Processing
      ↓
Day 6
Files + Exceptions + Modules
      ↓
Day 7
Object-Oriented Programming
```

### Week 1 Outcome

By the end of Week 1, I can:

* Write Python programs using variables and different data types
* Work with lists and dictionaries
* Use conditions and loops
* Create reusable functions
* Read and write files
* Handle common exceptions
* Create and import custom modules
* Create classes and objects
* Use inheritance and `super()`
* Combine multiple Python concepts into a practical project

---

# 🔜 Upcoming Preparation

## Week 2 — Data Analysis 📊

Planned topics:

* NumPy
* NumPy arrays
* Array operations
* Indexing and slicing
* Pandas
* Series
* DataFrames
* Loading datasets
* Data inspection
* Data cleaning
* Filtering and sorting
* Grouping and aggregation
* Basic statistical analysis
* Matplotlib
* Seaborn
* Data visualization

### Mini Project

**Canadian Housing Analysis**

The project will use a real dataset to practice:

```text
Load Data
    ↓
Inspect Data
    ↓
Clean Data
    ↓
Transform Data
    ↓
Analyze Data
    ↓
Visualize Data
    ↓
Find Insights
```

---

# 📊 Main Preparation Roadmap

| Week       | Focus                             | Status       |
| ---------- | --------------------------------- | ------------ |
| Week 1     | Python                            | 🟢 Completed |
| Week 2     | NumPy + Pandas + Visualization    | 🟡 Next      |
| Week 3     | Machine Learning                  | ⚪ Upcoming   |
| Week 4     | Deep Learning + TensorFlow/Keras  | ⚪ Upcoming   |
| Final Days | Revision + NLP/GitHub preparation | ⚪ Upcoming   |

---

# 🧠 Target Skills Before AIM2

| Skill              | Target |
| ------------------ | ------ |
| Python             | ⭐⭐⭐⭐☆  |
| NumPy              | ⭐⭐⭐⭐☆  |
| Pandas             | ⭐⭐⭐⭐☆  |
| Data Visualization | ⭐⭐⭐⭐☆  |
| Machine Learning   | ⭐⭐⭐☆☆  |
| Scikit-learn       | ⭐⭐⭐☆☆  |
| TensorFlow/Keras   | ⭐⭐⭐☆☆  |
| PyTorch            | ⭐⭐☆☆☆  |
| NLP                | ⭐⭐☆☆☆  |
| Git/GitHub         | ⭐⭐⭐⭐☆  |

---

# 🛠️ Development Environment

Current environment:

```text
Python: 3.12.10
pip: 26.2.1
Git: 2.46.0.windows.1
```

Python virtual environment:

```text
.venv/
```

Main Python libraries currently installed include:

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* SciPy
* Jupyter
* JupyterLab

---

# 🎓 AIM2 Preparation Philosophy

The goal is not to become an AI/ML expert before college.

The goal is to enter AIM2 with enough foundation to think:

> "I've seen this before."

The preparation focuses on understanding concepts, writing code, and building small projects rather than simply watching tutorials.

**Learn → Code → Practice → Build → Review**

---

# 🚀 Progress

**Week 1: 7 / 7 Days Completed ✅**

**Current focus:** Moving from Python programming into Data Analysis.

**Next milestone:**

**Complete Week 2 → Build a Canadian Housing Analysis project → Move into Machine Learning.**
