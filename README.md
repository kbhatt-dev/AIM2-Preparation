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

| Day | Topic | Status |
| --- | --- | --- |
| 1 | Python Fundamentals | ✅ |
| 2 | Lists & Dictionaries | ✅ |
| 3 | Control Flow | ✅ |
| 4 | Functions & Modular Programming | ✅ |
| 5 | Loops & Data Processing | ✅ |
| 6 | Files, Exceptions & Modules | ✅ |
| 7 | Object-Oriented Programming | ✅ |

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

* Arrays and dimensions
* Indexing and slicing
* Vectorized operations
* Aggregations
* Boolean filtering
* Broadcasting
* Reshaping and transpose

**Mini Project:** Student Score Analyzer — NumPy Edition

---

### Day 2 — Pandas Fundamentals ✅

* `Series` and `DataFrame`
* DataFrame creation
* `shape`, `columns`, `index`, `dtypes`
* `head()`, `tail()`, `info()`, `describe()`
* Column selection
* `loc` and `iloc`
* Boolean filtering
* Multiple conditions
* Calculated columns
* `mean(axis=1)`

**Mini Project:** Student Performance DataFrame Analyzer

---

### Day 3 — Data Cleaning ✅

* Missing-value detection with `isna()` / `isnull()`
* `notnull()`, `dropna()` and `fillna()`
* Mean / median considerations
* Numerical vs categorical missing values
* Duplicate detection and removal
* String cleaning
* `astype()`
* `pd.to_numeric(errors="coerce")`
* Invalid-value handling
* Dataset validation

**Mini Project:** Messy Student Dataset Cleaner

---

### Day 4 — Exploratory Data Analysis ✅

* `describe()`
* Mean, median and standard deviation
* `unique()` and `nunique()`
* `value_counts()`
* Percentage distributions
* `sort_values()`
* `idxmax()` and `idxmin()`
* `groupby()` and `agg()`
* Correlation with `corr()`
* Correlation vs causation

**Mini Project:** Student Performance EDA

---

### Day 5 — Matplotlib Visualization ✅

* `matplotlib.pyplot`
* Figure size, titles and labels
* Bar charts
* Histograms and bins
* Scatter plots
* Line plots
* Markers, grids and legends
* Axis-label rotation
* Visualizing grouped Pandas results

Chart selection:

```text
Bar Chart
→ Compare categories

Histogram
→ Understand numerical distribution

Scatter Plot
→ Study relationships between numerical variables

Line Plot
→ Show trends or ordered changes
```

Histogram understanding:

```text
Fewer bins
→ Wider intervals
→ More values grouped together
→ Less detail

More bins
→ Narrower intervals
→ Fewer values per interval
→ More detail
```

**Mini Project:** Student Performance Visualization Dashboard

---

### Day 6 — Seaborn / Advanced Visualization ✅

Learned how to create statistical visualizations using Seaborn and Pandas.

Key concepts:

* Seaborn with Pandas DataFrames
* `sns.barplot()`
* `sns.histplot()`
* KDE (`kde=True`)
* `sns.boxplot()`
* Median and distribution comparison
* `sns.scatterplot()`
* Categorical grouping with `hue`
* `sns.regplot()`
* Regression trend lines
* `sns.heatmap()`
* Correlation visualization
* `annot=True`
* `sns.pairplot()`
* Multi-variable relationship analysis
* Correlation vs causation

Visualization selection:

```text
Bar Plot
→ Compare categories

Histogram + KDE
→ Understand numerical distribution

Box Plot
→ Compare distributions across groups

Scatter Plot + Hue
→ Study relationships with categorical grouping

Regression Plot
→ Visualize relationship and trend

Heatmap
→ Visualize correlation matrix

Pair Plot
→ Explore multiple numerical relationships
```

Important concepts:

```text
hue="City"
→ Adds categorical grouping

kde=True
→ Adds a smooth distribution estimate

annot=True
→ Displays numerical values inside heatmap cells

Correlation ≠ Causation
```

**Mini Project:** Student Performance Advanced Visualization

Created visualizations for:

* Student average scores
* Math score distribution with KDE
* Math score distributions by city
* Python vs AI scores grouped by city
* Python vs AI regression trend
* Subject correlation heatmap
* Math/Python/AI pairwise relationships

---

### Week 2 — Next

* 🔜 Canadian Housing Analysis

### Week 2 Final Project

**Canadian Housing Analysis**

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
  ↓
Insights
```

This project will combine the complete Week 2 workflow:

`NumPy` → `Pandas` → `Data Cleaning` → `EDA` → `Matplotlib` → `Seaborn`

---

# 🗺️ Preparation Roadmap

| Week | Focus | Status |
| --- | --- | --- |
| Week 1 | Python | 🟢 Completed |
| Week 2 | NumPy + Pandas + Visualization | 🟡 In Progress |
| Week 3 | Machine Learning | ⚪ Upcoming |
| Week 4 | Deep Learning + TensorFlow/Keras | ⚪ Upcoming |
| Final Days | Revision + NLP + GitHub | ⚪ Upcoming |

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
█████████░ 6/7 🟡
```

**Current focus:** Seaborn / Advanced Visualization ✅

**Next:** Week 2 Day 7 — Canadian Housing Analysis 🏠📊

---

## 🎯 Learning Approach

The goal is not to become an AI/ML expert before starting the program.

The goal is to build enough practical foundation that new concepts feel familiar and easier to understand.

**Learn → Code → Practice → Build → Review**