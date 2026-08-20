# AIM2 Preparation 🚀

My preparation journey for the **Artificial Intelligence and Machine Learning (AIM2)** graduate program at Fanshawe College.

The goal of this repository is to build a strong practical foundation in **Python, Data Analysis, Machine Learning, and Deep Learning** through hands-on exercises, mini-projects, and end-to-end projects.

---

## 🎯 Preparation Goals

`Python` · `NumPy` · `Pandas` · `Matplotlib` · `Seaborn` · `Scikit-learn` · `TensorFlow/Keras` · `PyTorch` · `NLP` · `Git/GitHub`

Previous learning includes **Java, Spring Boot, Spring Cloud, Docker, Kubernetes, Helm, and Microservices Security**, so this preparation focuses primarily on Python and AI/ML.

---

## 🗂️ Repository Structure

```text
AIM2-Preparation/
│
├── week-01-python/
│   ├── notes/
│   ├── exercises/
│   └── student-performance-analyzer/
│
├── week-02-data-analysis/
│   ├── notes/
│   ├── datasets/
│   └── canadian-housing-analysis/
│
├── week-03-machine-learning/
│   ├── notes/
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

# 📅 Learning Progress

## Week 1 — Python 🐍 ✅

| Day | Topic                           | Status |
| --: | ------------------------------- | :----: |
|   1 | Python Fundamentals             |    ✅   |
|   2 | Lists & Dictionaries            |    ✅   |
|   3 | Control Flow                    |    ✅   |
|   4 | Functions & Modular Programming |    ✅   |
|   5 | Loops & Data Processing         |    ✅   |
|   6 | Files, Exceptions & Modules     |    ✅   |
|   7 | Object-Oriented Programming     |    ✅   |

### Key Concepts

* Variables, data types, strings, and string methods
* Lists and dictionaries
* Conditional logic with `if`, `elif`, and `else`
* `for` and `while` loops
* Functions, parameters, and return values
* File handling
* Exception handling with `try` / `except`
* Modules and imports
* `enumerate()`, `zip()`, and list comprehensions
* Classes and objects
* Constructors with `__init__`
* Inheritance and `super()`

### Projects

#### 🎓 Student Performance / Gradebook Analyzer

Built a Python program for working with student information and scores, including:

* Student data management
* Total score calculation
* Average score calculation
* Pass/fail determination
* Grade analysis

#### 📄 Student Grade Sheet Analyzer

Applied Python fundamentals, file handling, data processing, and OOP to:

* Read student data from files
* Calculate student statistics
* Determine pass/fail results
* Identify highest and lowest performers

---

## Week 2 — Data Analysis 📊 ✅

| Day | Topic                            | Status |
| --: | -------------------------------- | :----: |
|   1 | NumPy Fundamentals               |    ✅   |
|   2 | Pandas Fundamentals              |    ✅   |
|   3 | Data Cleaning                    |    ✅   |
|   4 | Exploratory Data Analysis        |    ✅   |
|   5 | Matplotlib Visualization         |    ✅   |
|   6 | Seaborn / Advanced Visualization |    ✅   |
|   7 | Canadian Housing Analysis        |    ✅   |

### Key Concepts

* NumPy arrays, dimensions, shapes, and data types
* Array slicing and indexing
* Vectorized operations
* Aggregation and broadcasting
* Pandas `Series` and `DataFrame`
* Data inspection with `head()`, `tail()`, `info()`, and `describe()`
* Filtering with `loc`, `iloc`, and Boolean masks
* Missing-value detection and handling
* Duplicate detection and removal
* String cleaning and datatype conversion
* Mean, median, and standard deviation
* `value_counts()`, `groupby()`, and `agg()`
* Sorting and ranking
* `idxmax()` and `idxmin()`
* Correlation analysis
* Correlation vs. causation
* Matplotlib chart fundamentals
* Histograms and distributions
* Seaborn statistical visualization
* KDE plots
* Box plots
* Regression plots
* Correlation heatmaps
* Pair plots

### 🏠 Day 7 Final Project — Canadian Housing Analysis

Completed an end-to-end housing data analysis workflow:

```text
Load
  ↓
Inspect
  ↓
Clean
  ↓
Analyze
  ↓
Visualize
  ↓
Interpret
```

#### Project Work

* Inspected dataset structure, data types, missing values, and duplicates
* Standardized `City`, `Province`, and `Property Type` values
* Removed duplicate records
* Handled missing `Price` and `Year_Built` values
* Validated the cleaned dataset
* Analyzed property prices by city, province, and property type
* Identified highest and lowest priced properties
* Compared property area and prices
* Calculated numerical correlations
* Created Matplotlib visualizations
* Created Seaborn statistical visualizations
* Analyzed distributions and relationships
* Interpreted findings and dataset limitations

#### Key Findings

* **Vancouver / British Columbia** had the highest average property price in the sample
* **Detached properties** had the highest average price and largest average area
* `Area_sqft` showed a moderate positive relationship with `Price`
* `Year_Built` had the strongest positive correlation with `Price` among the examined predictors
* Correlation was interpreted as **association, not causation**
* The small dataset was recognized as a limitation and was not considered representative of the entire Canadian housing market

**Final Project:** Canadian Housing Analysis ✅

---

## Week 3 — Machine Learning 🤖 🟡

| Day | Topic                         |     Status     |
| --: | ----------------------------- | :------------: |
|   1 | Machine Learning Fundamentals | 🟡 In Progress |
|   2 | Upcoming                      |        ⚪       |
|   3 | Upcoming                      |        ⚪       |
|   4 | Upcoming                      |        ⚪       |
|   5 | Upcoming                      |        ⚪       |
|   6 | Upcoming                      |        ⚪       |
|   7 | Customer Churn Prediction     |        ⚪       |

### Current Focus

Building the foundation required to move from **data analysis** into **machine learning**, including understanding how data is used to train models and how machine learning problems are structured.

### Planned Final Project

#### 📉 Customer Churn Prediction

The Week 3 project will apply the complete machine learning workflow to a practical prediction problem.

```text
Data
  ↓
Prepare
  ↓
Split
  ↓
Train
  ↓
Predict
  ↓
Evaluate
  ↓
Interpret
```

---

## Week 4 — Deep Learning 🧠 ⚪

Planned focus:

* Neural network fundamentals
* TensorFlow
* Keras
* PyTorch fundamentals
* Deep learning workflow
* Model training and evaluation

### Planned Final Project

#### 🔢 MNIST Digit Classifier

Build and train a neural network to classify handwritten digits.

---

# 🗺️ Preparation Roadmap

| Week       | Focus                            |     Status     |
| ---------- | -------------------------------- | :------------: |
| Week 1     | Python                           |  🟢 Completed  |
| Week 2     | NumPy + Pandas + Visualization   |  🟢 Completed  |
| Week 3     | Machine Learning                 | 🟡 In Progress |
| Week 4     | Deep Learning + TensorFlow/Keras |   ⚪ Upcoming   |
| Final Days | Revision + NLP + GitHub          |   ⚪ Upcoming   |

---

## 🛠️ Development Environment

```text
Python 3.12.10
pip 26.2.1
Git 2.46.0
```

### Main Libraries

`NumPy` · `Pandas` · `Matplotlib` · `Seaborn` · `Scikit-learn` · `SciPy` · `Jupyter`

---

## 📈 Current Progress

```text
Week 1 — Python
██████████  7/7  ✅

Week 2 — Data Analysis
██████████  7/7  ✅

Week 3 — Machine Learning
░░░░░░░░░░  In Progress 🟡

Week 4 — Deep Learning
░░░░░░░░░░  Upcoming ⚪
```

**Completed:** Week 1 — Python 🐍 ✅
**Completed:** Week 2 — Data Analysis 📊 ✅
**Current Focus:** Week 3 — Machine Learning 🤖
**Current Day:** Day 1 — Machine Learning Fundamentals

---

## 🎯 Learning Approach

The goal is not to become an AI/ML expert before starting the program.

The goal is to build enough practical foundation so that new concepts feel familiar and easier to understand when they are introduced in greater depth.

### Learn → Code → Practice → Build → Review

Each stage of this preparation focuses on understanding concepts first, applying them through code, practicing independently, and finally combining those skills into practical projects.

---

## 🚀 Progress So Far

Two major stages of the preparation roadmap are complete:

**Python → Data Analysis → Machine Learning → Deep Learning**

```text
Python                 ✅
   ↓
NumPy & Pandas         ✅
   ↓
Data Cleaning          ✅
   ↓
EDA                    ✅
   ↓
Visualization          ✅
   ↓
Machine Learning       🟡
   ↓
Deep Learning          ⚪
```

The next stage is focused on learning how to move from **analyzing existing data** to **building models that learn patterns from data and make predictions**.
