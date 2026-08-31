import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


data = {
    "Study_Hours": [
        1,2,2,3,3,4,4,5,5,6,
        6,7,7,8,8,9,9,10,10,11,
        2,3,4,5,6,7,8,9,10,11,
        3,4,5,6,7,8,9,10,11,12
    ],

    "Attendance": [
        45,50,55,52,60,58,65,62,70,68,
        75,72,80,78,85,82,90,88,92,95,
        65,70,55,75,60,85,68,92,72,88,
        80,62,85,70,90,74,95,78,93,85
    ],

    "Assignments_Completed": [
        2,3,3,4,4,5,5,6,6,7,
        7,8,8,9,9,9,10,10,10,10,
        4,5,4,7,5,8,6,9,7,9,
        6,5,7,6,8,7,9,8,10,9
    ],

    "Pass": [
        0,0,0,0,0,0,0,0,1,0,
        1,1,1,1,1,1,1,1,1,1,
        0,0,0,1,0,1,0,1,1,1,
        1,0,1,0,1,1,1,1,1,1
    ]
}

df = pd.DataFrame(data)
print(df)

# 0 = Fail and 1 = Pass

# Task 1 — Inspect
head_data = df.head()
print(f"Head: \n{head_data}")
df.info()
pass_stds = df["Pass"].value_counts()
print(f"How many Students are Pass / Fail: \n{pass_stds}")

""" 
Q. Does the target appear reasonably balanced, somewhat imbalanced, or severely imbalanced?
A. As per given datasets pass = 24 students, fail = 16 students
    pass = 0.6 and faile = 0.4
    there is not magger diffrence but it is not shows blanced. for my perspective it was somewhat imbalanced.
 """

# Task 2 — X and y
X = df[["Study_Hours", "Attendance", "Assignments_Completed"]]
y = df["Pass"]

# Task 3 — Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    random_state= 42,
    test_size=0.25,
    stratify=y,
)

# Task 4 — Train Logistic Regression
model = LogisticRegression()
#Train it.
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Task 5 — Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion matrix:\n{cm}")
""" 
TN = 4,
FP = 0,
FN = 1,
TP = 5
 """

# Task 6 — Calculate Four Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy Score: {accuracy:.4f}")
print(f"Precision Score: {precision:.4f}")
print(f"Recall Score: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

# Task 7 — Classification Report
classification = classification_report(y_test,y_pred)
print(f"Classification Report: \n{classification}")

""" 
and tell me what its:

Precision - class 0 = 0.80 and class 1 = 1.00 and it means: out of evrything the model predicted as POSITIVE, how many were "actually positive" 
Recall- class 0 = 1.00 and class 1 = 0.83 and it means: out of actual positive clas, how many did the model succesfully find possitive?
F1 - Class 0 = 0.89 and class 1 = 0.91 and it means: it shows that precisions and recall are ballanced or not and currently both are balanced as per output.
Support - support are the counts of class 0 and class 1. it not shows any scores.

Precision = 1.00
→ Every student predicted as Pass actually passed.

Recall = 0.8333
→ The model found 5 out of the 6 actual passing students.

F1 = 0.9091
→ Precision and Recall are reasonably strong overall.

Accuracy = 0.90
→ 9 out of 10 test predictions were correct.
 """

# Task 8 — Threshold Experiment
# Get probabilities for class 1 if you want to inspect them.
y_prob = model.predict_proba(X_test)[:, 1]
print(f"\n{y_prob}")

# --- THRESHOLD 0.5 ---
threshold_05 = 0.5
y_pred_05 = (y_prob >= threshold_05).astype(int)
print(f"Threshold - 0.5:\n{y_pred_05}")

accuracy_05 = accuracy_score(y_test, y_pred_05)
precision_05 = precision_score(y_test, y_pred_05)
recall_05 = recall_score(y_test, y_pred_05)
f1_05 = f1_score(y_test, y_pred_05)
print(f"Accuracy Score: {accuracy_05:.4f}")
print(f"Precision Score: {precision_05:.4f}")
print(f"Recall Score: {recall_05:.4f}")
print(f"F1 Score: {f1_05:.4f}")

# --- THRESHOLD 0.3 ---
threshold_03 = 0.3
y_pred_03 = (y_prob >= threshold_03).astype(int)
print(f"Threshold - 0.3:\n{y_pred_03}")

accuracy_03 = accuracy_score(y_test, y_pred_03)
precision_03 = precision_score(y_test, y_pred_03)
recall_03 = recall_score(y_test, y_pred_03)
f1_03 = f1_score(y_test, y_pred_03)
print(f"Accuracy Score: {accuracy_03:.4f}")
print(f"Precision Score: {precision_03:.4f}")
print(f"Recall Score: {recall_03:.4f}")
print(f"F1 Score: {f1_03:.4f}")


# --- THRESHOLD 0.7 --
threshold_07 = 0.7
y_pred_07 = (y_prob >= threshold_07).astype(int)
print(f"Threshold - 0.7: \n{y_pred_07}")
accuracy_07 = accuracy_score(y_test, y_pred_07)
precision_07 = precision_score(y_test, y_pred_07)
recall_07 = recall_score(y_test, y_pred_07)
f1_07 = f1_score(y_test, y_pred_07)
print(f"Accuracy Score: {accuracy_07:.4f}")
print(f"Precision Score: {precision_07:.4f}")
print(f"Recall Score: {recall_07:.4f}")
print(f"F1 Score: {f1_07:.4f}")


# --- FINAL SUMMARY TABLE ---
# Group the variables into lists for the final DataFrame columns
result = pd.DataFrame({
    "Threshold": [threshold_03, threshold_05, threshold_07],
    "Precision": [precision_03, precision_05, precision_07],
    "Recall": [recall_03, recall_05, recall_07],
    "F1": [f1_03, f1_05, f1_07]
})

print("\nFinal Performance Summary Table:")
print(result.to_string(index=False))


y_probs = model.predict_proba(X_test)[:, 1]

thresholds = [0.3, 0.5, 0.7]
table_data = []

for t in thresholds:
    # Convert probabilities to binary 0 or 1 based on the current threshold
    y_pred_threshold = (y_probs >= t).astype(int)

    #Calculate metrics for class1 (pass)
    p = precision_score(y_test, y_pred_threshold, zero_division=0)
    r = recall_score(y_test, y_pred_threshold, zero_division=0)
    f = f1_score(y_test, y_pred_threshold, zero_division=0)

    #Append row data as a dictionory
    table_data.append({
        "Threshold": f"{t:.2f}",
        "Precision": f"{p:.4f}",
        "Recall": f"{r:.4f}",
        "F1": f"{f:.4f}"
    })
# Convert the list of dictionaries into a DataFrame
metrics_table = pd.DataFrame(table_data)

print("\nThreshold Performance Table:")
print(metrics_table.to_string(index=False))

""" 
Q1. What does Precision measure?
A1. It measure as model predication prositive value how many are acurate positive values?

Q2. What does Recall measure?
A1. It measure as actual postivie values model gess how many postive values.

Q3. Suppose:

TP = 40
FP = 10
FN = 20

Calculate:

Precision =  TP / TP + FP = 40/50 = 0.8
Recall = TP / TP+FN = 40/60 = 0.66666

Q4. A cancer-screening model has very low False Negatives but more False Positives. Which metric is likely being prioritized, and why?
A4. Recall - of the all the real positives. because model it hase to masure who accutly have disease. and recall -> how many did i find?

Q5. A spam filter sends many legitimate emails to the spam folder. Is that mainly a False Positive or False Negative problem if
     Spam = Positive? Which metric should we pay attention to?
A5. positive = spam and negative = normal email
    false positive means - normal email and 
    false negative means - spam
    -> if flase positive are expensive, we strongly about precison-> can i trust the positive prediction?
    spem filtering -> don't incorrectly block important mail -> false possitive matters -> precision is important.

Q6. What does F1 Score combine?
A6. It combine Precisions and Recall values.

Q7. What does support mean in a classification report?
A7. It will be count class 0 and class 1 values it not shows any scores.

Q8. If we lower a classification threshold from:

0.50 → 0.30

what generally happens to the number of positive predictions?
precision - decrease  and  false positive - increase

What might happen to:

Recall - increase
Precision - decrease 

because, if whe lower the threshold 0.50->0.30 so, we have less likely to miss positive cases. so there are a tread-off.

Q9. If we raise the threshold from:

0.50 → 0.80

why might Recall decrease?
-> because , it shows fewer positive predictions and it may decrease false positives and for that reason recall decrteases.
-> Raising the threshold usually produces fewer positive predictions. Some actual positive cases may now be predicted negative,
     increasing False Negatives. Since Recall = TP / (TP + FN), increasing FN can decrease Recall.

Q10. You're building a customer-churn model.

Suppose:

Model A

Precision = 0.90
Recall    = 0.45

Model B

Precision = 0.72
Recall    = 0.80

The company's main goal is:

"We really don't want to miss customers who are likely to leave."

Which model would you initially prefer, and why?
-> model B- "We want a good balance between catching churners and avoiding unnecessary retention offers."
 """