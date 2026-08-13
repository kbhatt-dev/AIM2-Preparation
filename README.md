# AIM2 Preparation 🚀

My preparation journey for the **Artificial Intelligence and Machine Learning (AIM2)** graduate program at Fanshawe College.

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

# 📊 Week 2 — Data Analysis

## Day 1 — NumPy Fundamentals ✅

Topics completed:

* NumPy fundamentals
* Importing NumPy with `import numpy as np`
* NumPy `ndarray`
* Creating 1D arrays
* Creating 2D arrays
* `ndim`
* `shape`
* `size`
* `dtype`
* `np.array()`
* `np.zeros()`
* `np.ones()`
* `np.arange()`
* Array indexing
* Array slicing
* 2D array indexing
* Vectorized arithmetic operations
* Array-to-array operations
* Aggregation functions
* `sum()`
* `mean()`
* `max()`
* `min()`
* Boolean comparisons
* Boolean filtering
* `axis=0`
* `axis=1`

### Practice

Completed exercises covering:

* NumPy array creation and inspection
* Student score analysis
* Vectorized array operations
* 2D student score matrices
* Array indexing and slicing
* Boolean filtering

### Mini Project

**Student Score Analyzer — NumPy Edition**

The project represents student scores using a 2D NumPy array and calculates:

* All student scores
* Number of students
* Number of subjects
* Array shape
* Individual student averages
* Subject averages
* Highest score
* Lowest score
* Scores greater than or equal to 80

The project also introduced NumPy's `axis` concept:

```text
                 Math   Python   AI
Krishna           85      92     88
Rahul             75      80     75
Priya             91      95     94
Amit              65      70     68

axis=1 → calculate across columns → student averages

axis=0 → calculate down rows → subject averages
```
---

## Day 2 — Pandas Fundamentals ✅

Topics completed:

* Pandas fundamentals
* Importing Pandas with `import pandas as pd`
* Pandas `Series`
* Pandas `DataFrame`
* Creating a `Series`
* Creating a `Series` with custom indexes
* Creating DataFrames from dictionaries
* Understanding rows and columns
* `shape`
* `columns`
* `index`
* `dtypes`
* `head()`
* `tail()`
* `info()`
* `describe()`
* Selecting a single column
* Selecting multiple columns
* Understanding Series vs DataFrame output
* `loc`
* `iloc`
* Boolean conditions
* Boolean masks
* Filtering DataFrames
* Multiple filtering conditions using `&`
* Adding new columns
* Calculating row averages with `mean(axis=1)`

### Important Concepts Learned

#### Series vs DataFrame

```text
df["Math"]
     ↓
Series
```

A single column name passed directly returns a Pandas `Series`.

```text
df[["Math"]]
     ↓
DataFrame
```

A list of column names returns a Pandas `DataFrame`, even when the list contains only one column.

#### Boolean Mask vs Filtered DataFrame

```python
df["Math"] > 80
```

creates a Boolean mask:

```text
True
False
True
False
```

Using the Boolean mask inside the DataFrame:

```python
df[df["Math"] > 80]
```

returns only the matching rows.

This concept connects directly with NumPy Boolean filtering learned during Day 1.

### Practice

Completed exercises covering:

* Creating Pandas Series
* Creating DataFrames
* Inspecting DataFrame structure
* Selecting single and multiple columns
* Accessing rows using `loc`
* Accessing rows using `iloc`
* Filtering using single conditions
* Filtering using multiple conditions
* Adding calculated columns
* Calculating student averages
* Statistical summaries using `describe()`

### Mini Project

**Student Performance DataFrame Analyzer**

The project stores student performance data using a Pandas DataFrame.

The program:

1. Creates the student dataset
2. Displays the complete DataFrame
3. Displays its shape
4. Displays column names
5. Inspects data types
6. Displays the first rows using `head()`
7. Displays the last rows using `tail()`
8. Creates an `Average` column
9. Displays student names and averages
10. Filters students with an average of 80 or higher
11. Filters students with Math scores of 85 or higher
12. Uses multiple conditions to filter Python and AI scores
13. Generates a statistical summary using `describe()`
14. Finds the highest student average
15. Finds the lowest student average

### Day 2 Outcome

I can now:

* Understand the difference between a Pandas `Series` and `DataFrame`
* Create DataFrames from Python dictionaries
* Inspect dataset structure and data types
* Select rows and columns
* Use `loc` and `iloc`
* Create Boolean conditions
* Distinguish between a Boolean mask and a filtered DataFrame
* Filter rows using one or multiple conditions
* Add calculated columns
* Use NumPy-style `axis` operations inside Pandas
* Generate basic statistical summaries

---

## 🔜 Week 2 — Upcoming Topics

Remaining Week 2 topics:

* Data cleaning
* Missing values
* Duplicate values
* Incorrect data types
* Data transformation
* Exploratory Data Analysis
* Filtering and sorting
* Grouping and aggregation
* Basic statistical analysis
* Matplotlib
* Seaborn
* Data visualization

### Final Week 2 Project

**Canadian Housing Analysis**

The project will use a real dataset to practice:


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

| Week       | Focus                             | Status         |
| ---------- | --------------------------------- | -------------- |
| Week 1     | Python                            | 🟢 Completed   |
| Week 2     | NumPy + Pandas + Visualization    | 🟡 In Progress |
| Week 3     | Machine Learning                  | ⚪ Upcoming     |
| Week 4     | Deep Learning + TensorFlow/Keras  | ⚪ Upcoming     |
| Final Days | Revision + NLP/GitHub preparation | ⚪ Upcoming     |

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

**Week 2: 2 / 7 Days Completed 🟢**

Completed so far:

```text
Day 1 → NumPy Fundamentals ✅
          ↓
Day 2 → Pandas Fundamentals ✅
          ↓
Day 3 → Data Cleaning 🔜
```

**Current focus:** Pandas → Data Cleaning → Data Analysis → Data Visualization

**Next milestone:**

**Complete Week 2 → Build the Canadian Housing Analysis project → Move into Machine Learning.**
