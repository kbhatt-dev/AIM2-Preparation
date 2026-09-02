import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


data = {
    "Monthly_Charges": [
        35,40,42,45,48,50,52,55,58,60,
        62,65,68,70,72,75,78,80,82,85,
        88,90,92,95,98,100,105,110,115,120,
        45,55,65,75,85,95,105,115,70,90,
        38,48,58,68,78,88,98,108,118,125,
        43,53,63,73,83,93,103,113,67,87
    ],

    "Contract_Months": [
        24,24,18,24,12,18,24,12,18,12,
        24,12,18,6,12,6,12,6,3,6,
        3,6,3,1,3,1,1,3,1,1,
        6,3,12,3,6,1,3,1,12,6,
        24,18,12,12,6,6,3,3,1,1,
        24,18,12,6,6,3,3,1,12,6
    ],

    "Support_Calls": [
        0,1,0,1,1,1,2,1,2,2,
        1,2,2,3,2,3,3,4,3,4,
        4,3,5,4,5,5,4,6,5,6,
        2,3,1,4,2,5,3,6,2,4,
        0,1,2,2,3,3,4,4,5,6,
        1,1,2,3,3,4,4,5,2,4
    ],

    "Tenure_Months": [
        48,45,40,42,35,36,38,30,32,28,
        34,26,30,22,25,20,18,24,15,17,
        14,16,12,10,11,8,9,7,5,4,
        28,15,30,14,22,9,12,6,26,13,
        50,44,36,31,20,18,11,8,4,3,
        46,39,33,24,19,13,10,6,29,15
    ],

    "Churn": [
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,
        0,1,0,1,0,1,1,1,0,1,
        0,0,0,0,1,1,1,1,1,1,
        0,0,0,0,1,1,1,1,0,1
    ]
}

df = pd.DataFrame(data)
print(df)

# Task 1 — Inspect
head = df.head()
print(f" Head: \n{head}")
df.info()
churn_value_count = df["Churn"].value_counts()
print(f"Churn/stay customers: \n{churn_value_count}")

""" 
Q. Then tell me whether the target is balanced, somewhat imbalanced, or severely imbalanced.

output - 
Curn/stay customers: 
Churn
0    30
1    30

A. This dataset is balanced because, look churn and stay customers counting value both are 30 and 30 respectively, also if you persentage this data=
    churn: 30/60 = 0.50 and stay: 30/60 =0.50 both are same and balanced. as per that this dataset are balanced.
 """

# Task 2 — Define X and y
X = df[["Monthly_Charges", "Contract_Months", "Support_Calls", "Tenure_Months"]]
y = df["Churn"]

# Task 3 — Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y, 
    test_size=0.25, 
    random_state=42,
    stratify=y
    )

# Task 4 — Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

lr_accuracy = accuracy_score(y_test, y_pred)
lr_precision = precision_score(y_test, y_pred)
lr_recall = recall_score(y_test, y_pred)
lr_f1 = f1_score(y_test, y_pred)

print()
print("Logistic Regression Model Performance:")
print(f"Accuracy: {lr_accuracy}")
print(f"Precision: {lr_precision}")
print(f"Recall: {lr_recall}")
print(f"F1_Score: {lr_f1}")

# Task 5 — Decision Tree
DecisionTree_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
    )

DecisionTree_model.fit(X_train, y_train)

y_pred_dt = DecisionTree_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, y_pred_dt)
dt_precision = precision_score(y_test, y_pred_dt)
dt_recall = recall_score(y_test, y_pred_dt)
dt_f1 = f1_score(y_test, y_pred_dt)

print()
print("Decision Tree Model Performance:")
print(f"Accuracy: {dt_accuracy:.2f}")
print(f"Precision: {dt_precision:.2f}")
print(f"Recall: {dt_recall:.2f}")
print(f"F1_Score: {dt_f1:.2f}")

# Training Accuracy
train_accuracy = DecisionTree_model.score(X_train, y_train)
# Test Accuracy
test_accuracy = DecisionTree_model.score(X_test, y_test)

print()
print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Test Accuracy: {test_accuracy:.2f}")

# Task 6 — Random Forest 🌲
RandomForest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
    )

RandomForest_model.fit(X_train, y_train)
rf_pred = RandomForest_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_pred)
rf_precision = precision_score(y_test, rf_pred)
rf_recall = recall_score(y_test, rf_pred)
rf_f1 = f1_score(y_test, rf_pred)

print()
print("Random Forest Model Performance:")
print(f"Accuracy: {rf_accuracy:.2f}")
print(f"Precision: {rf_precision:.2f}")
print(f"Recall: {rf_recall:.2f}")
print(f"F1_Score: {rf_f1:.2f}")

# Training and Testing Accuracy
rf_train_accuracy = RandomForest_model.score(X_train, y_train)
rf_test_accuracy = RandomForest_model.score(X_test, y_test)

print()
print(f"Training Accuracy: {rf_train_accuracy:.2f}")
print(f"Test Accuracy: {rf_test_accuracy:.2f}")

# Task 7 — Build a Model Comparison Table ⭐
""" 
Model                 Accuracy   Precision   Recall   F1
Logistic Regression      ?          ?          ?      ?
Decision Tree            ?          ?          ?      ?
Random Forest            ?          ?          ?      ?
Don't manually type the metric results into the DataFrame.
Use the variables you calculated.
 """

table = pd.DataFrame({
    "Model": ["Logistic Regression", "Decision Tree", "Random Forest"],
    "Accuracy": [lr_accuracy, dt_accuracy, rf_accuracy],
    "Precision": [lr_precision, dt_precision, rf_precision],
    "Recall": [lr_recall, dt_recall, rf_recall],
    "F1_Score": [lr_f1, dt_f1, rf_f1]
})

print()
print("Model Comparison Table:")
print(table)

# Task 8 — Interpret the Models
""" 
QA. Which model has the highest:
"""
Accuracy_table = {table.loc[table['Accuracy'].idxmax(), 'Model']}
Precision_table =  {table.loc[table['Precision'].idxmax(), 'Model']}
Recall_table = {table.loc[table['Recall'].idxmax(), 'Model']}
F1_table = {table.loc[table['F1_Score'].idxmax(), 'Model']}

print()
print(f"Highest Accuracy: {Accuracy_table}")
print(f"Highest Precision: {Precision_table}")
print(f"Highest Recall: {Recall_table}")
print(f"Highest F1_Score: {F1_table}")

""" 
B. We really don't want to miss customers who are likely to churn.
Q.  Which model would you choose based on the Recall metric?
A. Based on the Recall metric, I would choose the model with the highest recall value,
    which is the Random Forest model. This model is better at identifying customers who are likely to churn,
    minimizing the risk of missing potential churners.
C. What is the trade-off of choosing this model?
A. The trade-off of choosing the Random Forest model based on the Recall metric is that while 
    it may have a higher recall, it could potentially have lower precision. This means that while we are better at 
    identifying customers who are likely to churn, we may also incorrectly classify some customers as churners when 
    they are not (false positives). This could lead to unnecessary interventions or marketing efforts directed at customers 
    who would not have churned, potentially increasing costs and affecting customer satisfaction.

D. If retention offers are extremely expensive and the company wants customers labeled as churners to be highly trustworthy:
    Which metric becomes particularly important?
A. In this case, precision becomes particularly important. Precision measures the proportion of true positive predictions (actual churners)
    among all positive predictions (predicted churners). A high precision value indicates that when the model predicts a customer is likely to churn, 
    it is more likely to be correct. This is crucial when retention offers are expensive, as we want to minimize the number of false positives 
    (customers incorrectly labeled as churners) to avoid unnecessary costs and ensure that resources are focused on customers who are genuinely at risk of churning.

 """

# Task 9 — Random Forest Feature Importance
importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": RandomForest_model.feature_importances_
})
print()
importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)
print(f"Feature importance : \n{importance_df}")

""" 
Q. Which feature did your Random Forest rely on most?
A. The Random Forest model relied most on the "Tenure_Months" feature,
    indicating that customer tenure is a significant factor in predicting churn.

Q. Can you say that feature causes churn?
A. No, we cannot say that the "Tenure_Months" feature causes churn. 
    Feature importance indicates how much a feature contributes to the model's predictions, 
    but it does not imply causation. Other factors may influence churn, and further analysis would be needed to establish any causal relationships.
 """

# Task 10 — Experiment With n_estimators
tree_counts = [10, 50, 100, 200]

RandomForestClassifier_model = RandomForestClassifier(
    max_depth=3,
    random_state=42
    )
""" 
Record:

Number of Trees
Training Accuracy
Testing Accuracy

 """

train_accuracy = [RandomForestClassifier(n_estimators=n, max_depth=3, random_state=42).fit(X_train, y_train).score(X_train, y_train) for n in tree_counts]
test_accuracy = [RandomForestClassifier(n_estimators=n, max_depth=3, random_state=42).fit(X_train, y_train).score(X_test, y_test) for n in tree_counts]

record = pd.DataFrame({
    "Number of Trees": tree_counts,
    "Training Accuracy": train_accuracy,
    "Testing Accuracy": test_accuracy
})
print(f"Experiment Results:\n{record}")

""" 
Q. Did adding more trees continuously improve testing accuracy?
My output: 
   Number of Trees  Training Accuracy  Testing Accuracy
0               10                1.0          0.933333
1               50                1.0          1.000000
2              100                1.0          1.000000
3              200                1.0          1.000000
A. No, adding more trees did not continuously improve testing accuracy.
   - The testing accuracy improved from 0.9333 to 1.0 when increasing the number of trees from 10 to 50, but it remained constant at 1.0 for 100 and 200 trees.
More trees ≠ automatically better forever
 """

""" 
🧠 Day 6 Assessment

Answer these after your coding exercise.

Q1. What is an ensemble model?
A1. An ensemble model is a machine learning technique that combines multiple individual models (often referred to as "base learners") to create a single,
    more powerful predictive model. The idea is that by aggregating the predictions of several models, the ensemble can achieve better performance, reduce overfitting, 
    and improve generalization compared to any single model. Common ensemble methods include bagging (e.g., Random Forest), boosting (e.g., Gradient Boosting), and stacking.

Q2. What is the basic difference between a Decision Tree and a Random Forest?
A2. The basic difference between a Decision Tree and a Random Forest is that a Decision Tree is a single predictive model that makes decisions based on 
    a series of feature-based splits, while a Random Forest is an ensemble model that consists of multiple Decision Trees. In a Random Forest, each tree is trained 
    on a random subset of the data (using bootstrap sampling) and a random subset of features, which helps to reduce overfitting and improve generalization. 
    The final prediction of the Random Forest is typically made by aggregating the predictions of all the individual trees 
    (e.g., through majority voting for classification or averaging for regression).

Q3. What does n_estimators=100 mean?
A3. The parameter `n_estimators=100` in a Random Forest means that the model will consist of 100 individual Decision Trees.

Q4. What is bootstrap sampling? What does with replacement mean?
A4. Bootstrap sampling is a statistical technique where samples are drawn from a dataset with replacement. 
    This means that each sample can be selected more than once, leading to a new dataset that may have repeated observations 
    and some observations that are not included at all.

Q5. Why does Random Forest use random subsets of features rather than letting every tree always rely on the same strongest feature?
A5. Random Forest uses random subsets of features to introduce diversity among the individual trees in the ensemble. 
    If every tree relied on the same strongest feature, they would all make similar predictions, leading to high correlation among the trees and reducing the 
    overall benefit of the ensemble. By using random subsets of features, each tree can learn different patterns in the data, which helps to reduce overfitting and 
    improve generalization. This randomness allows the Random Forest to capture a wider range of relationships in the data, making it more robust and effective as a 
    predictive model.

Q6. True or false, and explain:

Random Forest cannot overfit because it contains many trees.
A6. False. While Random Forest is less prone to overfitting than a single Decision Tree due to its ensemble nature and the use of random subsets of data and features, 
    it can still overfit, especially if the individual trees are too deep or if the number of trees is not sufficient to capture the underlying patterns in the data. 
    Overfitting can occur when the model learns noise or random fluctuations in the training data rather than the true underlying patterns, leading to poor 
    generalization on unseen data.

Q7. Suppose:

Decision Tree
Train = 1.00
Test  = 0.71

Random Forest
Train = 0.98
Test  = 0.88

Which appears to generalize better, and why?
A7. The Random Forest appears to generalize better than the Decision Tree. 
    This is evident from the training and testing accuracies of both models. The Decision Tree has a perfect training accuracy of 1.00, but its testing accuracy drops to 0.71, 
    indicating that it has likely overfit the training data and is not performing well on unseen data. In contrast, the Random Forest has a slightly lower training 
    accuracy of 0.98, but its testing accuracy is significantly higher at 0.88, suggesting that it has learned the underlying patterns in the data more effectively 
    and is better able to generalize to new data.

Q8. Why should Logistic Regression, Decision Tree, and Random Forest use the same train/test split when we're comparing them?
A8. Logistic Regression, Decision Tree, and Random Forest should use the same train/test split when comparing them to ensure a fair and consistent evaluation of their 
    performance. Using the same split allows for a direct comparison of how each model performs on the same training and testing data, eliminating variability 
    that could arise from different splits. This consistency is crucial for accurately assessing the strengths and weaknesses of each model and making informed 
    decisions about which model is best suited for the task at hand.

Q9. For churn prediction, which metric would you prioritize if the biggest concern is missing actual churners? Why?
A9. If the biggest concern is missing actual churners, I would prioritize the Recall metric. Recall measures the proportion of true positive predictions (actual churners) 
    that are correctly identified by the model. A high recall value indicates that the model is effective at capturing most of the actual churners, minimizing the risk of 
    false negatives (customers who are predicted to stay but actually churn). In this context, prioritizing recall is crucial because missing actual churners could lead 
    to lost revenue and missed opportunities for retention efforts, which can be more costly than incorrectly identifying some customers as churners (false positives).

Q10. Suppose:

Model A
Precision = .94
Recall    = .55

Model B
Precision = .78
Recall    = .86

The company says:

"Missing churners is much more expensive than contacting some customers who would have stayed."

Which model would you choose, and why?

A10. Given the company's concern that missing churners is much more expensive than contacting some customers who would have stayed, I would choose Model B.
    Model B has a higher Recall of 0.86 compared to Model A's Recall of 0.55, meaning it is better at identifying actual churners and minimizing false negatives.
    While Model B has a lower Precision of 0.78 compared to Model A's Precision of 0.94, the company's priority is to avoid missing churners, 
    making Recall the more critical metric in this scenario.
 """