import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

data = {
    "Income": [
        30000, 35000, 40000, 45000, 50000,
        55000, 60000, 65000, 70000, 75000,
        80000, 85000, 90000, 95000, 100000,
        105000, 110000, 115000, 120000, 125000,
        38000, 48000, 58000, 68000, 78000,
        88000, 98000, 108000, 118000, 128000
    ],

    "Credit_Score": [
        520, 540, 560, 580, 600,
        620, 640, 660, 680, 700,
        720, 740, 760, 780, 800,
        820, 840, 850, 860, 870,
        550, 590, 630, 670, 710,
        750, 790, 830, 845, 880
    ],

    "Debt": [
        25000, 24000, 23000, 22000, 21000,
        20000, 19000, 18000, 17000, 16000,
        15000, 14000, 13000, 12000, 11000,
        10000, 9000, 8000, 7000, 6000,
        26000, 23000, 20000, 17000, 14000,
        12000, 10000, 8000, 7000, 5000
    ],

    "Loan_Approved": [
        0, 0, 0, 0, 0,
        0, 0, 0, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        0, 0, 0, 1, 1,
        1, 1, 1, 1, 1
    ]
}

""" 
Look at the pattern:
    Low income + low credit + high debt → mostly rejected
    High income + high credit + low debt → mostly approved
 """

df = pd.DataFrame(data)
print(df)

# 1. Create the DataFrame and inspect it.
first_five = df.head()
print(f"Head of table: {first_five}")
df.info()
approved_Loan_Count = df["Loan_Approved"].value_counts()
print(f"Toatl Approved/Not Loan: \n{approved_Loan_Count}") 

""" 
Q. Before doing ML, tell me whether the target looks reasonably balanced or clearly imbalanced.
A. It is somewhat imbalanced, but not severely imbalanced.
        Approved = 19 / 30 ≈ 63%
        Rejected = 11 / 30 ≈ 37%
    That is not a perfect 50/50 split, but it is nowhere near something extreme like:
        99% vs 1%
    So for this small beginner dataset, it is reasonable to work with.
--> We should not say the model is perfect just because it achieved 100% accuracy.
    The dataset is very small and the model was tested on only 6 examples. 
    The data is also intentionally simple, so the model needs to be evaluated on much more unseen and realistic data before we can say it generalizes well.
 """

# 2. Create your features and target.
X = df[["Income", "Credit_Score", "Debt"]]
y = df["Loan_Approved"]

# 3. Split the data.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.20,
    random_state = 42,
    stratify = y
)

# 4. Create the model.
model = LogisticRegression()

# 5. Train it.
model.fit(X_train, y_train)

# 6. Make class predictions.
y_pred = model.predict(X_test)

# Optional: Get probabilities for class 1 if you want to inspect them.
y_prob = model.predict_proba(X_test)[:, 1]
print(f"\n{y_prob}")

# 7. Create a result DataFrame containing:
result = pd.DataFrame({
    "Actual": y_test,
    "Predict": y_pred,
    "Predict_Prob": y_prob
})

print(result)

# 8. Calculate accuracy.
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# 9. Generate the confusion matrix.
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion matrix:\n{cm}")
""" 
TN = 2 - Rejected - 33%
FP = 0
FN = 0
TP = 4 - Approved - 67%
 """

# 10. Inspect probabilities.
Probability_Class_0 = model.predict_proba(X_test)[:, 0]
Probability_Class_1 = model.predict_proba(X_test)[:, 1]

# Create another DataFrame containing:
new_df = pd.DataFrame({
    "Actual": y_test,
    "Predict": y_pred,
    "Probability_Class_0": Probability_Class_0,
    "Probability_Class_1": Probability_Class_1
})
print(new_df)

""" 
Q1. Why is loan approval a classification problem even though we store the target as 0 and 1?
A1. it has exactly two possible classes like approved and rejected and that predicts category / classes not numaric value so for that reasonloan approval is a pure classification problem.

Q2. What's the difference between binary classification and multiclass classification?
A2- binary classification- has exactly two possible classes
    multiclass classification - has more than two possible classes

Q3. Why do we use Logistic Regression instead of Linear Regression for this problem?
A3. We use Logistic Regression because the target is a category with two classes. Linear Regression predicts unrestricted continuous numerical values,
    while Logistic Regression models class probabilities and then assigns a class
    Remember:
        Linear Regression
        → continuous number

        Logistic Regression
        → classification

Q4. What's the difference between: model.predict(X_test) vs. model.predict_proba(X_test)
A4. model.predict(X_test) - it can shows the predicted values.
    model.predict_proba(X_test) - logistic regression can give probabilities for each class.

Q5. If the probability of class 1 is: 0.82, and the threshold is 0.5, which class would normally be predicted? Why?
A5. predication is : class 1;  because, it is 0.82 means 82% of that class.

Q6. Explain in your own words:
A6. using this example it shows 
TN = 2 -> true negative  ->  predication and Actual value are negative and both are same
FP = 0 -> false possitive -> actual = magative and predication = possitive , both are diifrent; in short the model said megative but is was false
FN = 0 -> false negative -> actual = possitive and predication = nagative , both are diifrent; in short the model said positive but is was false
TP = 4 -> true Positive ->predication and Actual value are possitive and both are same

Q7. Suppose:

[[15, 3],
 [ 2, 20]]

Tell me:

TN = 15
FP =  3
FN = 2
TP = 20

How many predictions were correct? => 15+20 = 35


Q8. Why can 99% accuracy still describe a terrible model?
A8. because high accuracy does not mean a good classification model.
    for example there are 1000 transactions
    990 = Legitimate
    10 = Fraud

    Now create a useless model: Predict everything as Legitimate
    Its results: 990 legitimate → correctly predicted
                 10 fraud       → incorrectly predicted
    Accuracy: 990 / 1000 = 99%
    Looks fantastic. 
        But: Fraud detected = 0 / 10
    The model completely failed at the important task.
    That's why:
        99% accuracy can still describe a terrible model when the classes are highly imbalanced.

Q9. Why did we use: stratify=y
A9. As you said - it tries to preserve roughly the same target_class proporions in the training and testing like trainging has ~= 60% Approved and ~=40% regected then 
    in test it has taken same proposition like ~= 60% Approved and ~=40% regected.

 """