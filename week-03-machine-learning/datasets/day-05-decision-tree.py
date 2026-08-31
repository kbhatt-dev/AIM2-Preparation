import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix

    )

data = {
    "Monthly_Charges": [
        35,40,42,45,48,50,52,55,58,60,
        62,65,68,70,72,75,78,80,82,85,
        88,90,92,95,98,100,105,110,115,120,
        45,55,65,75,85,95,105,115,70,90,
        38,48,58,68,78,88,98,108,118,125
    ],

    "Contract_Months": [
        24,24,18,24,12,18,24,12,18,12,
        24,12,18,6,12,6,12,6,3,6,
        3,6,3,1,3,1,1,3,1,1,
        6,3,12,3,6,1,3,1,12,6,
        24,18,12,12,6,6,3,3,1,1
    ],

    "Support_Calls": [
        0,1,0,1,1,1,2,1,2,2,
        1,2,2,3,2,3,3,4,3,4,
        4,3,5,4,5,5,4,6,5,6,
        2,3,1,4,2,5,3,6,2,4,
        0,1,2,2,3,3,4,4,5,6
    ],

    "Churn": [
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,
        0,1,0,1,0,1,1,1,0,1,
        0,0,0,0,1,1,1,1,1,1
    ]
}

df = pd.DataFrame(data)
print(df)

# 0 = Stay and 1 = Churn

# Task 1 — Inspect the Dataset
dataset_head = df.head()
print(f" Head: \n{dataset_head}")
df.info()
churn_value_count = df["Churn"].value_counts()
print(f"Curn/stay customers: \n{churn_value_count}")

""" 
Q. Is this dataset balanced, somewhat imbalanced, or severely imbalanced?
A. Yes this dataset is fully balanced because, look churn and stay customers counting value both are 25 equals, also if you persentage this data=
    churn: 25/50 = 0.5 and stay: 25/50 =0.5 both are same and blanced. as per that this dataset are balanced.
 """

# Task 2 — Define X and y
X = df[["Monthly_Charges", "Contract_Months", "Support_Calls"]]
y = df["Churn"]

""" 
Q. What information is available to the model?
A. Mothly charge, contarct months and support clls columns are available in the available dataset/model

Q. What exactly am I trying to predict?
A. why customers are leave and what to identify at the risk customers. 
 """

# Task 3 — Split the Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
    
)

# Task 4 — Build an Unrestricted Decision Tree
model = DecisionTreeClassifier(
    random_state= 42
)
# train
model.fit(X_train, y_train)
# predict
y_pred = model.predict(X_test)
# calculate
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
# confusion_matrix:
confusionMatrix = confusion_matrix(y_test, y_pred)
# Classification Reposr:
classificationReport = classification_report(y_test, y_pred)


print(f"Training Accuracy: \n{train_accuracy}")
print(f"Testing Accuracy: \n{test_accuracy}")

""" 
Q. Do you see evidence of possible overfitting?
A. The unrestricted tree achieved 100% training and test accuracy on this particular split. There is no train/test evidence of overfitting here,
    but the dataset is small and simple, so more unseen data would be needed to evaluate generalization reliably.
 """

# Task 5 — Try Different Tree Depths ⭐
depths = [1, 2, 3, 4, 5, None]

# 1. Create empty lists to store the performance scores
train_accuracies = []
test_accuracies = []

# 2. Iterate through each depth, train the model, and record scores
for d in depths:
    model_depth = DecisionTreeClassifier(max_depth=d, random_state=42)
    model_depth.fit(X_train, y_train)
    
    train_accuracies.append(model_depth.score(X_train, y_train))
    test_accuracies.append(model_depth.score(X_test, y_test))

# 3. Compile the collected data into your final DataFrame
result = pd.DataFrame({
    "Depth": depths,
    "Train Accuracy": train_accuracies,
    "Test Accuracy": test_accuracies,
})

print(result)

# Task 6 — Choose the Best Depth
""" 
Pick the model with the highest training accuracy.
-> depth = 5

Which depth would you choose from this experiment, and why?
I choose deph 1 coase -> 1.00-0.918= 0.022 that has not too much gap or not too less it is balaced so that is good generlization as per my opinion.

"I would choose depth 1 because it achieves the same 100% test accuracy as the deeper trees while using the simplest model. 
There is currently no test-performance benefit from adding complexity."

and also you say- If multiple depths perform identically, prefer the simpler tree unless there's a good reason not to.
and That's an important ML principle.
 """

# Task 7 — Feature Importance
best_model = DecisionTreeClassifier(max_depth=1, random_state=42)
best_model.fit(X_train, y_train)
feature_importance = best_model.feature_importances_
print(f"Feature importance : {feature_importance}")

# also using pandas
importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": best_model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)
print(f"Feature importance : \n{importance_df}")

""" 
Q. Which feature was most important to this particular fitted tree?
A. Support Calls is the most important features for this particular fitted tree.
yes but it is not the causions of customer leaving. 
because.
Importance does not mean causation.
 """

# Task 8 — Make New Predictions
new_customers = pd.DataFrame({
    "Monthly_Charges": [40, 85, 115],
    "Contract_Months": [24, 6, 1],
    "Support_Calls": [0, 3, 6]
})

# 1. Generate predictions using your best_model (max_depth=1)
predictions = best_model.predict(new_customers)

# 2. Add the array of predictions back to the DataFrame as a new column
new_customers["Predicted_Churn"] = predictions

# 3. Print the final evaluation dataframe
print("\nHypothetical Customer Predictions:")
print(new_customers)

""" 
🧠 Day 5 Assessment
Q1. In your own words, how does a Decision Tree make a prediction?
A. asking a sequanc eof queastions about features.

Q2. What is the difference between a root node and a leaf node?
A. rood node is the main node / first node and 
    leaf node is the final predications

Q3. Conceptually, what does Gini impurity measure?
A. how mixed are the classes inside the node?
 after split how many predictions are there if pass =10 and fial = 0then gini = 0 it is complitly pure gini
 if pass = 5 and fail = 5 then it is high mixed.

 means pure node -> low gini.

Q4. Which node is purer?

Node A:
10 Churn
0 Stay

Node B:
5 Churn
5 Stay

Why?

node A is pure ,  same as upper given example just values are diffrent.

Q5. Suppose:

Training Accuracy = 1.00
Testing Accuracy  = 0.68

What problem might you suspect, and why? 
diff - 1.00 - 0.68 = 0.32 ( thants a large gap)
model may be overfitting.
->we are concerned when the taining performance is strong while unseen performance is meaningfully worse.

Q6. Suppose:

Training Accuracy = 0.61
Testing Accuracy  = 0.59

Would you be more concerned about overfitting or underfitting? Why?
-> both are poor.
this is indicates = underfitting
the model is'nt complex enogh to represnt the pattern well.

Q7. What does max_depth control?
-> it says - don't let the tree grow beyound approx tree levels of decisions.

Q8. You test:

Depth 3:
Train = 0.91
Test  = 0.88

Depth 10:
Train = 1.00
Test  = 0.73

Which would you choose initially, and why?
i choose depth 3 reathor then depth 10 because depth 10 is 1.00-0.73 = 27,it is quite large gap 
and depth 3 has 0.91-0.88 = 0.03 it has  enogh complexity with good gerealization.

Q9. Your feature importance result is:

Support_Calls       0.55
Monthly_Charges     0.30
Contract_Months     0.15

Can you conclude:

"Support calls cause customers to churn."

Why or why not?

no because - Importance does not mean causation.

Q10. Why shouldn't we simply choose whichever model gets the highest training accuracy?
-> a model complex enoh to learn the real pattern, but not so complex that it memorize noise.
 """

