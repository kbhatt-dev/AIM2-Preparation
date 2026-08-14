# AIM2 Preparation 🚀

My preparation journey for the **Artificial Intelligence and Machine Learning (AIM2)** graduate program at Fanshawe College.

The goal of this repository is to build a practical foundation in **Python, data analysis, machine learning, and deep learning** through hands-on exercises and projects.

---

## 🎯 Preparation Goals

`Python` · `NumPy` · `Pandas` · `Matplotlib` · `Seaborn` · `Scikit-learn` · `TensorFlow/Keras` · `PyTorch` · `NLP` · `Git/GitHub`

Previous learning includes Java, Spring Boot, Spring Cloud, Docker, Kubernetes, Helm, and Microservices Security, so this preparation focuses primarily on Python and AI/ML.

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
│   ├── notebooks/
│   ├── datasets/
│   └── canadian-housing-analysis/
│
├── week-03-machine-learning/
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
| --- | ------------------------------- | ------ |
| 1   | Python Fundamentals             | ✅      |
| 2   | Lists & Dictionaries            | ✅      |
| 3   | Control Flow                    | ✅      |
| 4   | Functions & Modular Programming | ✅      |
| 5   | Loops & Data Processing         | ✅      |
| 6   | Files, Exceptions & Modules     | ✅      |
| 7   | Object-Oriented Programming     | ✅      |

### Key Concepts

* Variables, data types and strings
* Lists and dictionaries
* Conditions and loops
* Functions and modules
* File handling and exceptions
* `enumerate()`, `zip()` and list comprehensions
* Classes, objects, inheritance and `super()`

### Projects

**Student Performance / Gradebook Analyzer**

**Student Grade Sheet Analyzer**

Combined Python fundamentals, OOP, files, exceptions, functions, modules, loops and data processing.

---

## Week 2 — Data Analysis 📊 🟡

### Day 1 — NumPy Fundamentals ✅

Learned:

* NumPy arrays and dimensions
* `shape`, `ndim`, `size`, `dtype`
* Indexing and slicing
* Vectorized operations
* Aggregations
* Boolean filtering
* Reshaping and transpose

**Mini Project:** Student Score Analyzer — NumPy Edition

---

### Day 2 — Pandas Fundamentals ✅

Learned:

* `Series` and `DataFrame`
* DataFrame creation
* `shape`, `columns`, `index`, `dtypes`
* `head()`, `tail()`, `info()`, `describe()`
* Column selection
* `loc` and `iloc`
* Boolean filtering and multiple conditions
* Calculated columns
* `mean(axis=1)`

Key distinction:

```python
df["Math"]      # Series
df[["Math"]]    # DataFrame

df["Math"] > 80       # Boolean mask
df[df["Math"] > 80]   # Filtered DataFrame
```

**Mini Project:** Student Performance DataFrame Analyzer

---

### Day 3 — Data Cleaning ✅

Learned:

* Detecting missing values with `isna()` / `isnull()`
* Counting missing values
* `notnull()`
* `dropna()` and `fillna()`
* Mean-based imputation
* Understanding mean vs rounded values
* Detecting duplicates with `duplicated()`
* Removing duplicates with `drop_duplicates()`
* String cleaning with `str.strip()` and `str.title()`
* Data type conversion with `astype()`
* Safe numeric conversion using `pd.to_numeric()`
* `errors="coerce"` for invalid numeric data
* Cleaning inconsistent categorical values
* Data validation after cleaning

Key lesson:

```text
Inspect
   ↓
Identify Problems
   ↓
Clean Strings
   ↓
Convert Data Types
   ↓
Handle Missing Values
   ↓
Remove Duplicates
   ↓
Validate
```

**Mini Project:** Messy Student Dataset Cleaner

Cleaned student data containing:

* Missing values
* Duplicate rows
* Inconsistent names and cities
* Incorrect numeric data types
* Invalid values such as `"unknown"`
* Missing student scores

Created a final calculated `Average` column and validated that the cleaned dataset contained no remaining missing values or duplicates.

---

### Week 2 — Next

* 🔜 EDA / Data Analysis
* ⏳ Grouping & Aggregation
* ⏳ Matplotlib
* ⏳ Seaborn
* ⏳ Data Visualization

### Week 2 Final Project

**Canadian Housing Analysis**

```text
Load → Inspect → Clean → Analyze → Visualize → Insights
```

---

# 🗺️ Preparation Roadmap

| Week       | Focus                            | Status         |
| ---------- | -------------------------------- | -------------- |
| Week 1     | Python                           | 🟢 Completed   |
| Week 2     | NumPy + Pandas + Visualization   | 🟡 In Progress |
| Week 3     | Machine Learning                 | ⚪ Upcoming     |
| Week 4     | Deep Learning + TensorFlow/Keras | ⚪ Upcoming     |
| Final Days | Revision + NLP + GitHub          | ⚪ Upcoming     |

---

## 🛠️ Development Environment

```text
Python 3.12.10
pip 26.2.1
Git 2.46.0
```

Main libraries:

`NumPy` · `Pandas` · `Matplotlib` · `Seaborn` · `Scikit-learn` · `SciPy` · `Jupyter`

---

## 📈 Current Progress

```text
Week 1 — Python
██████████ 7/7 ✅

Week 2 — Data Analysis
████░░░░░░ 3/7 🟡
```

**Current focus:** Data Cleaning ✅

**Next:** Week 2 Day 4 — EDA / Data Analysis

---

## 🎯 Learning Approach

The goal is not to become an AI/ML expert before starting the program.

The goal is to build enough practical foundation that new concepts feel familiar and easier to understand.

**Learn → Code → Practice → Build → Review**
