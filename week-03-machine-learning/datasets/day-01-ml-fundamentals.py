""" 
Feature(s), Target, Supervised/Unsupervised, and Regression/Classification if applicable.

Scenario A:
    A company has:
        Years_Experience
        Education_Level
        Job_Role
        Salary
    Goal:
        Predict employee salary.

    Features(X)= [["Years_Experience", "Education_Level", "Job_Role"]] 
    Target(y)= ["Salary"]
    Learning Type = Supervised, because X + known y (machine wants to learn to predict y)
    Problem Type = Regression, beacause regrassion predicts numeric value and salary is but obeuys numeric.

Scenario B:
    A bank has:
        Income
        Credit_Score
        Debt
        Loan_Approved
    Goal:
        Predict whether a new loan application will be Approved or Rejected.

    Features(X)= [["Income", "Credit_Score", "Debt"]] 
    Target(y)= ["Loan_Approved"]
    Learning Type = Supervised, because X + known y (we have y = loan approved a boolean column)
    Problem Type = Classification, beacause Classification predicts a category / class

Scenario C:
    A store has:
        Age
        Income
        Annual_Spending
    There is no customer category column.
    Goal:
        Automatically discover groups of similar customers.
    
    Features(X)= [["Age", "Income", "Annual_Spending"]] 

    "But there is no target y."
    Target(y)= DOES NOT EXIST 

    Learning Type = Unsupervised, because discover hidden pattern / group     (we did not have y we want to discover similer customer)   
    Problem Type = none / it is Unsupervised Learning

 """

# ML predictions do not have to exactly equal the actual values.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Score": [45, 50, 55, 60, 65, 70, 74, 80, 86, 92]
}

df = pd.DataFrame(data)

print(df)

X = df[["Study_Hours"]]
y = df["Exam_Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

result = pd.DataFrame({
    "Actual": y_test,
    "Predict": y_pred
})

print(result)

""" 
Q1. What is the difference between traditional programming and machine learning?
A1. Treditional program has rules and as per rule they get output like 
    Data + Rule -> (get) output
    when, Machine learning find answers using pattern, analytze features, search rules using algorithoms and then predict the answers.
    The algorithm learns patterns/parameters from the training data and produces a trained model.
    Features + Correct Answers --> ML Algorithom --> Model

Q2. What is the difference between a feature and a target?
A2. Features- features are the informations, using that info predict target
    Target- targets is what we are trying to redict

Q3. Why is predicting house price a regression problem?
A3. Because hosung price will be numerical value.

Q4. Why is predicting spam/not-spam a classification problem?
A3. Because, it gives yes/no answer and that predicts are categorized / classifications.

Q5. Why do we separate training data and testing data?
A5. first we tain our machine using tarining data which are known and after we test remaining data using that traing so it is kinda exam.
    training is learning and testing is kinda exam.
    And that tells us how well the model perform on the unseen examples.

Q6. What does this line actually do? "model.fit(X_train, y_train)"
A6. LEARN the relationship between the training features and training targets.

Q7. What does this line do? "model.predict(X_test)"
A7. use what was learned to PREDICT unknown answers.

Q8. Why shouldn't we give y_test to the model when making predictions?
A8. Because, it contains the actual ans. we are trying to see whether the model can predict was right or not.

 """