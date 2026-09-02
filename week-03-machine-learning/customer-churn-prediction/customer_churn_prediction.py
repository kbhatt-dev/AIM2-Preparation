""" 
🎯 Project Scenario
Imagine you work for a telecom company.

Management is concerned that customers are cancelling their service.

They ask your ML team:
Can we predict which customers are likely to churn so that the company can intervene before they leave?

Your job is to build a classification system where:
0 = Customer stays
1 = Customer churns

Your complete workflow should be:
Business Problem
       ↓
Load Data
       ↓
Inspect Data
       ↓
Clean / Validate
       ↓
EDA
       ↓
Define X & y
       ↓
Train/Test Split
       ↓
Train Models
       ↓
Evaluate Models
       ↓
Compare Models
       ↓
Feature Importance
       ↓
Business Recommendation
       ↓
Predict New Customers

 """


from dbm import error

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay

def analyze_customer_churn(filename):
    """
    - Phase 1 — Load & Inspect 🔍
        Your program should determine:
        Dataset shape
        Column names
        Data types
        First 5 rows
        Missing values
        Duplicate rows
        Churn class counts
        Churn percentages

    -phase 2 — Basic EDA 📊
        Calculate at least:
        Churn vs Stay averages
        Compare average:
            Monthly_Charges
            Contract_Months
            Support_Calls
            Tenure_Months
            Data_Usage_GB
        between:
            Churn = 0
            Churn = 1
        You should be able to create something like:
                    Monthly_Charges  Contract_Months  ...
        Churn
        0                  ?
        1                  ?

    -phase 3 — Define Features & Target 🎯
        Your target:
            Churn
        Your candidate features:
            Monthly_Charges
            Contract_Months
            Support_Calls
            Tenure_Months
            Data_Usage_GB
    """
    try:
        df = pd.read_csv(filename)
        print(f"Data loaded successfully: {df.shape}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nChurn Class Counts:")
        print(df['Churn'].value_counts())

        print("\nChurn Percentages:")
        print(df['Churn'].value_counts(normalize=True) * 100)

        # Phase 2 — Basic EDA
        churn_vs_stay_averages = df.groupby('Churn').mean(numeric_only=True)
        print("\nChurn vs Stay Averages:")
        print(churn_vs_stay_averages[['Monthly_Charges', 'Contract_Months', 'Support_Calls', 'Tenure_Months', 'Data_Usage_GB']])

        # Phase 3 — Define Features & Target 🎯
        X = df[['Monthly_Charges', 'Contract_Months', 'Support_Calls', 'Tenure_Months', 'Data_Usage_GB']]
        y = df['Churn']

        # Phase 4 — Train/Test Split ✂️
        X_train, X_test, y_train, y_test = train_test_split(
            X, 
            y, 
            test_size=0.25, 
            random_state=42,
            stratify=y
            )
        print(f"\nTrain/Test Split: X_train: {X_train.shape}, X_test: {X_test.shape}, y_train: {y_train.shape}, y_test: {y_test.shape}")

        training_sample = pd.concat([X_train, y_train], axis=1)
        testing_sample = pd.concat([X_test, y_test], axis=1)
        print("\nTraining Sample:")
        print(training_sample.head())
        print("\nTesting Sample:")
        print(testing_sample.head())

        # Phase 5 — Build Three Models 🧠
        lr_model = LogisticRegression()
        dt_model = DecisionTreeClassifier(
            max_depth=3,
            random_state=42
            )
        rf_model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
            )

        lr_model.fit(X_train, y_train)
        dt_model.fit(X_train, y_train)
        rf_model.fit(X_train, y_train)

        lr_pred = lr_model.predict(X_test)
        dt_pred = dt_model.predict(X_test)
        rf_pred = rf_model.predict(X_test)

        # Phase 6 — Evaluate Every Model 📏
        print("\nModel Evaluation Metrics:")
        for i, (model, y_pred) in enumerate(zip([lr_model, dt_model, rf_model], [lr_pred, dt_pred, rf_pred])):
            print(f"\n{model.__class__.__name__}:")
            print(f"  Accuracy: {accuracy_score(y_test, y_pred):.2f}")
            print(f"  Precision: {precision_score(y_test, y_pred):.2f}")
            print(f"  Recall: {recall_score(y_test, y_pred):.2f}")
            print(f"  F1-Score: {f1_score(y_test, y_pred):.2f}")

        print("\nTraining and Testing Accuracy:")
        print(f"Logistic Regression - Train: {lr_model.score(X_train, y_train):.2f}, Test: {accuracy_score(y_test, lr_pred):.2f}")
        print(f"Decision Tree - Train: {dt_model.score(X_train, y_train):.2f}, Test: {accuracy_score(y_test, dt_pred):.2f}")
        print(f"Random Forest - Train: {rf_model.score(X_train, y_train):.2f}, Test: {accuracy_score(y_test, rf_pred):.2f}")

        # create one comparison DataFrame:
        comparison_df = pd.DataFrame({
            'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest'],
            'Train Accuracy': [lr_model.score(X_train, y_train), dt_model.score(X_train, y_train), rf_model.score(X_train, y_train)],
            'Test Accuracy': [accuracy_score(y_test, lr_pred), accuracy_score(y_test, dt_pred), accuracy_score(y_test, rf_pred)],
            'Precision': [precision_score(y_test, lr_pred), precision_score(y_test, dt_pred), precision_score(y_test, rf_pred)],
            'Recall': [recall_score(y_test, lr_pred), recall_score(y_test, dt_pred), recall_score(y_test, rf_pred)],
            'F1-Score': [f1_score(y_test, lr_pred), f1_score(y_test, dt_pred), f1_score(y_test, rf_pred)]
        })
        print("\nModel Comparison:")
        print(comparison_df)

        # Phase 7 — Confusion Matrix 🔢
        cm_rf = confusion_matrix(y_test, rf_pred)
        print("\nConfusion Matrix for Random Forest:")
        print(cm_rf)
        # Display the confusion matrix as a heatmap
        disp = ConfusionMatrixDisplay(confusion_matrix=cm_rf, display_labels=['Not Churn', 'Churn'])
        disp.plot()
        plt.title("Confusion Matrix - Random Forest")
        plt.show()
        # confusion matrix for logistic regression and decision tree
        cm_lr = confusion_matrix(y_test, lr_pred)
        print("\nConfusion Matrix for Logistic Regression:")
        print(cm_lr)
        cm_dt = confusion_matrix(y_test, dt_pred)
        print("\nConfusion Matrix for Decision Tree:")
        print(cm_dt)

        # Phase 8 — Feature Importance 🌲
        print("\nFeature Importance for Random Forest:")
        feature_importances = pd.DataFrame(rf_model.feature_importances_,
                                           index=X_train.columns,
                                           columns=['Importance']
                                           ).sort_values('Importance', ascending=False)
        print(feature_importances)
        # Plot feature importance
        plt.figure(figsize=(10, 6))
        sns.barplot(x=feature_importances.index, y=feature_importances['Importance'])
        plt.title("Feature Importance - Random Forest")
        plt.ylabel("Importance")
        plt.xlabel("Features")
        # plt.xticks(rotation=45)
        plt.show()

        # Phase 9 — Business Recommendation 💼
        print("\nBusiness Recommendation:")
        print("Based on the model evaluation metrics, the Random Forest model performed the best with the highest accuracy," \
        " precision, recall, and F1-score. The feature importance analysis indicates that 'Tenure_Months' is the most significant factor "
        "in predicting customer churn. Therefore, it is recommended that the company focuses on retaining customers with shorter tenure by " \
        "implementing targeted retention strategies and improving customer engagement.")

        # Phase 10 — Predict New Customers 🔮
        # Customer A
        # Monthly Charges = 45
        # Contract Months = 24
        # Support Calls = 0
        # Tenure Months = 40
        # Data Usage = 20 GB

        # Customer B
        # Monthly Charges = 90
        # Contract Months = 6
        # Support Calls = 4
        # Tenure Months = 14
        # Data Usage = 65 GB

        # Customer C
        # Monthly Charges = 115
        # Contract Months = 1
        # Support Calls = 6
        # Tenure Months = 5
        # Data Usage = 90 GB

        new_customers = pd.DataFrame({
            'Monthly_Charges': [45, 90, 115],
            'Contract_Months': [24, 6, 1],
            'Support_Calls': [0, 4, 6],
            'Tenure_Months': [40, 14, 5],
            'Data_Usage_GB': [20, 65, 90]
        })
        print()
        new_customer_predictions = rf_model.predict(new_customers)
        print("\nPredictions for New Customers:")
        for i, prediction in enumerate(new_customer_predictions):
            print(f"Customer {i+1}: {'Churns' if prediction == 1 else 'Does Not Churn'}")

        print("\nPredicted Probabilities for New Customers:")
        new_customer_probabilities = rf_model.predict_proba(new_customers)[:, 1]
        for i, probability in enumerate(new_customer_probabilities):
            print(f"Customer {i+1}: {probability:.4f}")

        print("\nBusiness Recommendation for New Customers:")
        for i, prediction in enumerate(new_customer_predictions):
            if prediction == 1:
                print(f"Customer {i+1} is predicted to churn. Recommend proactive retention strategies.")
            else:
                print(f"Customer {i+1} is predicted to stay. Continue engagement and support.")

        print("\nEnd of Analysis.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except Exception as error:
        print(f"Error reading data: {error}")

if __name__ == "__main__":
    analyze_customer_churn("customer_churn.csv")

""" 
Questions

--phase 1 — Load & Inspect 🔍

Q1. How many rows and columns are there?
A1. The dataset has a shape of 60 rows and 7 columns. This means there are 60 customer records and 7 features (including the target variable 'Churn').

Q2. Are there missing values?
A2. There are no missing values in the dataset.

Q3. Are there duplicate rows?
A3. There are no duplicate rows in the dataset.

Q4. Is the target balanced, somewhat imbalanced, or severely imbalanced? Explain using percentages.
A4. Churn class counts shows that there are 30 customers who stayed (0) and 30 customers who churned (1), making it a balanced dataset.

--phase 2 — Basic EDA 📊

Q5. Do churners appear to have higher or lower monthly charges?
A5. In this dataset, churn is associated with higher monthly charges. The average monthly charges for churners (Churn = 1) are higher compared to those who stayed (Churn = 0).

Q6. Do churners appear to make more support calls?
A6. In this dataset, churn is associated with more support calls. The average number of support calls for churners (Churn = 1) is higher compared to those who stayed (Churn = 0).

Q7. Do churners generally have shorter or longer tenure?
A7. In this dataset, churn is associated with shorter tenure. The average tenure for churners (Churn = 1) is shorter compared to those who stayed (Churn = 0).

Q8. Based only on this dataset, what patterns seem associated with churn?
A8. In this dataset, churn is associated with higher monthly charges, more support calls, and shorter tenure. 
    These patterns suggest that customers who are paying more, experiencing issues that require support, and have been with the company for 
    a shorter period are more likely to churn.

--phase 3 — Define Features & Target 🎯
Q9. Why should Customer_ID NOT be included as a model feature?
A9. Customer_ID should not be included as a model feature because it is a unique identifier for each customer and does not provide any 
    predictive information about churn. Including it could lead to overfitting, where the model learns to memorize the training data rather than generalize to new data.

--phase 4 — Train/Test Split ✂️
Q10. Why are we using: stratify=y here?
A10. We are using stratify=y to ensure that the train and test sets have the same proportion of churners and non-churners as the original dataset. 
    This helps maintain the balance of the target variable in both sets, which is important for training a model that can generalize well to unseen data.

--phase 6 — Evaluate Every Model 📏
        
        Model Comparison:
                        Model  Train Accuracy  Test Accuracy  Precision  Recall  F1-Score
        0  Logistic Regression             1.0       0.933333      0.875     1.0  0.933333
        1        Decision Tree             1.0       0.933333      0.875     1.0  0.933333
        2        Random Forest             1.0       1.000000      1.000     1.0  1.000000

Q11. Which model has the highest Accuracy?
A11. The Random Forest model has the highest Test Accuracy of 1.0, indicating it correctly predicted all instances in the test set.

Q12. Which has the highest Precision?
A12. The Random Forest model has the highest Precision of 1.0.

Q13. Which has the highest Recall?
A13. All 3 models tie for Recall = 1.00

Q14. Which has the highest F1?
A14. The Random Forest model has the highest F1-Score of 1.0.

--phase 7 — Confusion Matrix 🔢
        Confusion Matrix for Random Forest:
        [[8 0]  - as TN = 7, FP = 0, FN = 0, TP = 8
        [0 7]]

        Confusion Matrix for Logistic Regression:
        [[7 1]  - as TN = 7, FP = 1, FN = 0, TP = 7
        [0 7]]

        Confusion Matrix for Decision Tree:
        [[7 1]  - as TN = 7, FP = 1, FN = 0, TP = 7
        [0 7]]

Q15. Which model produced the fewest False Negatives?
A15. All 3 models produced the fewest False Negatives, with a count of 0.

Q16. Why are False Negatives especially important in a churn prediction problem?
A16. False Negatives are especially important in a churn prediction problem because they represent customers 
     who are predicted to stay (negative) but actually churn (positive). Missing these customers means the company 
     will not take action to retain them, potentially leading to lost revenue. Therefore, minimizing False Negatives is crucial 
     to ensure that the company can intervene and retain customers who are at risk of leaving.

--phase 8 — Feature Importance 🌲
        Feature Importance for Random Forest:
                        Importance
        Tenure_Months      0.405655
        Monthly_Charges    0.245114
        Data_Usage_GB      0.202635
        Support_Calls      0.121008
        Contract_Months    0.025588
Q17. Which feature has the highest importance?
A17. The feature with the highest importance is Tenure_Months, with an importance score of 0.405655. 
     This indicates that the length of time a customer has been with the company is the most significant factor in predicting whether they will churn or stay.

Q18. What does that actually mean?
A18. "Tenure_Months" having the highest feature importance means the fitted Random Forest relied on this feature 
     more than the other features when making predictions. Feature importance itself does not tell us the direction 
     of the relationship. However, our separate EDA showed that churners had shorter average tenure than customers who stayed.

Q19. Does it prove that feature causes churn? Why not?
A19. No, feature importance does not prove causation. It only indicates that there is a strong association between the feature and the target variable (churn). 
     Other factors not included in the model could also influence churn, and correlation does not imply causation. 
     Further analysis and experimentation would be needed to establish a causal relationship.

--phase 9 — Business Recommendation 💼
Q20. Which evaluation metric should be prioritized?
A20. In this churn prediction problem, Recall should be prioritized. The company's main goal is to identify customers who are likely to 
     churn so that they can take action to retain them. A high Recall means that the model is able to identify a larger proportion of actual churners, 
     minimizing False Negatives. This is crucial because missing potential churners could result in lost revenue and missed opportunities for customer retention.

Q21. Based on your actual results, which model would you recommend?
A21. Based on the evaluation metrics, I would recommend the Random Forest model. It achieved the highest Test Accuracy (1.0), Precision (1.0), Recall (1.0), and F1-Score (1.0). 
     This indicates that the model is highly effective at correctly identifying both churners and non-churners, making it the best choice for predicting customer 
     churn and helping the company take proactive measures to retain customers.
"""
""" 
🧠 Final Week 3 Assessment

After the project, answer these 10 questions without looking back at your notes if possible.

A1. What is the difference between a feature and a target?
-> A feature is an input variable used to make predictions, 
   while a target is the output variable that the model is trying to predict. 
   In this case, features are the customer attributes (e.g., Monthly_Charges, Contract_Months), and the target is whether the customer churns (1) or stays (0).

A2. What's the difference between regression and classification?
-> Regression is used to predict continuous numerical values, while classification is used to predict categorical outcomes. 
   In this case, we are performing classification because we are predicting whether a customer will churn (1) or stay (0), which are categorical outcomes.

A3. Why do we separate training and testing data?
-> We separate training and testing data to evaluate the model's performance on unseen data. 
   The training data is used to train the model, while the testing data is used to assess how well the model generalizes to new, unseen examples. 
   This helps prevent overfitting and ensures that the model can make accurate predictions on real-world data.

A4. What does overfitting mean?
-> Overfitting occurs when a model learns the training data too well, capturing noise and details that do not generalize to new, unseen data. 
   This results in poor performance on the testing data.

A5. What's the difference between Precision and Recall?
-> Precision measures the proportion of true positive predictions among all positive predictions made by the model, 
   while Recall measures the proportion of true positive predictions among all actual positive instances in the dataset. 
   In other words, Precision focuses on the accuracy of positive predictions, while Recall focuses on the model's ability to identify all relevant positive cases.

A6. If False Negatives are very costly, which metric usually becomes particularly important?
-> If False Negatives are very costly, Recall becomes particularly important. 
   A high Recall means that the model is able to identify a larger proportion of actual positive cases, minimizing the number of False Negatives. 
   This is crucial in scenarios where missing positive cases can lead to significant negative consequences, such as in medical diagnoses or customer churn prediction.

A7. Why can Accuracy be misleading on an imbalanced dataset?
-> Accuracy can be misleading on an imbalanced dataset because it may give a false sense of model performance. 
   If one class is significantly more prevalent than the other, a model that predicts the majority class for all instances can achieve high accuracy, 
   even though it fails to correctly identify instances of the minority class. In such cases, metrics like Precision, Recall, 
   and F1-Score provide a more informative evaluation of model performance.

A8. What's the main difference between a Decision Tree and Random Forest?
-> A Decision Tree is a single model that makes predictions by recursively splitting the data based on feature values, 
   while a Random Forest is an ensemble of multiple Decision Trees that work together to make predictions. 
   Random Forests typically provide better performance and generalization than a single Decision Tree because they reduce overfitting by 
   averaging the predictions of multiple trees.

A9. Does high feature importance prove causation?
-> No, high feature importance does not prove causation. It indicates that a feature is strongly associated with the target variable, 
   but it does not establish a cause-and-effect relationship. Other factors not included in the model could also influence the target variable, 
   and correlation does not imply causation. Further analysis and experimentation would be needed to establish a causal relationship.

A10. Why shouldn't we automatically select whichever model has the highest training accuracy?
-> We shouldn't automatically select the model with the highest training accuracy because it may be overfitting the training data. 
   A model that performs exceptionally well on the training data may not generalize well to unseen data, leading to poor performance on the test set. 
   It's important to evaluate models based on their performance on the testing data and consider other metrics like Precision, Recall, and F1-Score to 
   ensure that the selected model is robust and effective in real-world scenarios.

 """