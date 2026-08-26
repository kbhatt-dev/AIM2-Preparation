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

| Day | Topic                         | Status |
| --: | ----------------------------- | :----: |
|   1 | Machine Learning Fundamentals |    ✅   |
|   2 | Upcoming                      |    ⚪   |
|   3 | Upcoming                      |    ⚪   |
|   4 | Upcoming                      |    ⚪   |
|   5 | Upcoming                      |    ⚪   |
|   6 | Upcoming                      |    ⚪   |
|   7 | Customer Churn Prediction     |    ⚪   |

### ✅ Day 1 — Machine Learning Fundamentals

Started the transition from **data analysis** into **machine learning** by learning how models use historical data to discover patterns and make predictions.

### Key Concepts

* What Machine Learning is
* Traditional programming vs Machine Learning
* Features (`X`) and target (`y`)
* Supervised Learning
* Unsupervised Learning
* Regression
* Classification
* Clustering concept
* Training data vs testing data
* Model training and prediction
* Generalization to unseen data
* `train_test_split()`
* `random_state`
* `LinearRegression`
* `model.fit()`
* `model.predict()`
* `y_test` vs `y_pred`
* Actual vs predicted values
* Basic prediction-error interpretation

### Machine Learning Workflow

```text
Load Data
   ↓
Inspect Data
   ↓
Clean Data
   ↓
Explore Data
   ↓
Select Features (X)
   ↓
Select Target (y)
   ↓
Split Train/Test Data
   ↓
Choose Model
   ↓
Train Model
   ↓
Make Predictions
   ↓
Evaluate Model
```

### Supervised vs Unsupervised Learning

```text
Supervised Learning

X + known y
     ↓
Learn relationship
     ↓
Predict y
```

```text
Unsupervised Learning

X only
  ↓
Discover hidden patterns,
structure, or groups
```

An important distinction learned during Day 1 was that in unsupervised clustering there is **no predefined target `y`**.

The groups or clusters are discovered by the algorithm instead of being supplied as known answers.

### Regression vs Classification

**Regression**

Used when predicting numerical values.

Examples:

* House price
* Salary
* Temperature
* Exam score

**Classification**

Used when predicting a category or class.

Examples:

* Spam / Not Spam
* Approved / Rejected
* Fraud / Legitimate
* Cat / Dog / Horse

### 🧪 Day 1 Practical Exercise — Study Hours → Exam Score

Built the first Machine Learning model using **Linear Regression**.

Dataset features:

```text
Feature:
Study_Hours

Target:
Exam_Score
```

The dataset was split into:

```text
80% Training Data
20% Testing Data
```

using:

```python
train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
```

The model was created and trained using:

```python
model = LinearRegression()

model.fit(X_train, y_train)
```

Predictions were generated using:

```python
y_pred = model.predict(X_test)
```

### Prediction Results

| Actual Score | Predicted Score |
| -----------: | --------------: |
|           86 |           85.58 |
|           50 |           49.67 |

The predictions were very close to the actual values.

This introduced an important Machine Learning idea:

> A prediction does not need to exactly equal the actual value. Model evaluation measures how far predictions are from the correct answers.

### Day 1 Conceptual Assessment

Practiced identifying the correct Machine Learning structure for different problems.

#### Employee Salary Prediction

```text
Features:
Years_Experience
Education_Level
Job_Role

Target:
Salary

Learning Type:
Supervised Learning

Problem Type:
Regression
```

#### Loan Approval Prediction

```text
Features:
Income
Credit_Score
Debt

Target:
Loan_Approved

Learning Type:
Supervised Learning

Problem Type:
Classification
```

#### Customer Grouping

```text
Features:
Age
Income
Annual_Spending

Target:
None

Learning Type:
Unsupervised Learning

Task:
Clustering
```

### Day 1 Key Mental Models

```text
X → Model → y
```

```text
.fit() → LEARN
.predict() → PREDICT
```

```text
Training Data
     ↓
Model Learns

Testing Data
     ↓
Unseen Exam
```

```text
X_test
   ↓
Trained Model
   ↓
y_pred

y_pred ↔ y_test
```

### Current Focus

Continue building the foundation required to move from **analyzing existing data** into **training, evaluating, and improving Machine Learning models**.

### Planned Final Project

#### 📉 Customer Churn Prediction

The Week 3 final project will apply the complete Machine Learning workflow to a practical prediction problem.

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
█░░░░░░░░░  1/7  🟡

Week 4 — Deep Learning
░░░░░░░░░░  Upcoming ⚪
```

**Completed:** Week 1 — Python 🐍 ✅
**Completed:** Week 2 — Data Analysis 📊 ✅
**Current Focus:** Week 3 — Machine Learning 🤖
**Completed Week 3 Days:** 1/7
**Latest Completed Day:** Day 1 — Machine Learning Fundamentals ✅
**Next:** Week 3 — Day 2

---

## 🎯 Learning Approach

The goal is not to become an AI/ML expert before starting the program.

The goal is to build enough practical foundation so that new concepts feel familiar and easier to understand when they are introduced in greater depth.

### Learn → Code → Practice → Build → Review

Each stage of this preparation focuses on understanding concepts first, applying them through code, practicing independently, and finally combining those skills into practical projects.

---

## 🚀 Progress So Far

Two complete stages of the preparation roadmap are finished, and Machine Learning is now underway:

**Python → Data Analysis → Machine Learning → Deep Learning**

```text
Python                  ✅
   ↓
NumPy & Pandas          ✅
   ↓
Data Cleaning           ✅
   ↓
EDA                     ✅
   ↓
Visualization           ✅
   ↓
Machine Learning        🟡
   │
   └── Day 1            ✅
   ↓
Deep Learning           ⚪
```

The Machine Learning stage has now begun with the fundamentals of **features, targets, supervised and unsupervised learning, regression, classification, train/test splitting, model training, and prediction**.

The next step is to continue building the Machine Learning workflow and gradually move from simple models toward the **Customer Churn Prediction** final project.
