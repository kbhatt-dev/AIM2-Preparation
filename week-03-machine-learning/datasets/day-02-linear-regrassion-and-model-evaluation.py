import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score

# 1. Dataset Setup
data = {
    "Experience_Years": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                         11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    
    "Salary": [42000, 45000, 48000, 52000, 55000,
               59000, 62000, 66000, 70000, 73000,
               77000, 81000, 85000, 88000, 92000,
               96000, 100000, 103000, 108000, 112000]
}
df = pd.DataFrame(data)
print(df)

# 2. Features and Target
X = df[["Experience_Years"]]
y = df["Salary"]

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.20,
    random_state = 42
)

# 4. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Prediction
y_pred = model.predict(X_test)

# 6. Construct Results DataFrame Safely
# extract the column as a 1D Series by passing a single string X_test["Experience_Years"] instead of the entire 2D object
result = pd.DataFrame({
    "Experience_Years": X_test["Experience_Years"], # Extracted as a 1D Series
    "Actual_Salary": y_test,
    "Predict_Salary": y_pred
})

print(result)

# 7. Print Scope and intercept
Salary_slope = model.coef_[0]
Salary_intercept = model.intercept_

print(f"\nSlope: {Salary_slope:.2f}")
print(f"Intercept: {Salary_intercept:.2f}")

# 8.Calculate and print
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
rSquered = r2_score(y_test, y_pred)

print(f"\nMAE = {mae:.2f}")
print(f"MSE = {mse:.2f}")
print(f"RMSE (Function) = {rmse:.2f}")
print(f"RMSE (Manual) = {(mse ** 0.5):.2f}")
print(f"R-Squared = {rSquered:.4f}")

""" 
mae = the model salary pridictions are off about 1045.85 on average 
mse = the model salary pridictions are off about 1561674 on Suered
rmse = the model salary pridictions are off about 1249.66 on root squered
r^2 =  excellent fit on this particular test set
 """

""" 
Day 2 Assessment

Q1. What does the coefficient/slope tell you in your salary model?
A1. slope/coefficient of salary model is 3747.85 - and it tells the learned coefficients,
    For each uint increase in expirence year , the predicted predicted_salary increases by approx 3747.85 dollers, according to this model.
    -> According to this fitted model, each additional year of experience is associated with approximately $3,747.85 higher predicted salary.

Q2. What does the intercept represent?, Also tell me why it might not be practically meaningful in this dataset.
A2. in y = mX + b equavtion b is the intercept. this is where the regression line crosses the target axis when the feature is zero
    it is methodically importent but isn't always practically meaningful beacuse if their some hase 0 years of expirence has 36226.36 expected salary it is some times not practical.
    -> There isn't even a zero-year employee in the training examples; So interpreting the zero-experience prediction too literally would be risky.

Q3. Actual Salary = $80,000, Predicted Salary = $76,000 - What is the prediction error? And what is the absolute error?
    prediction error is = $4,000 and absolute erro is same = $4,000; because |$4,000| = $4,000

Q4. What does MAE tell us?
A4. The model has a typical prediction error magnitude of roughly $1,249.67, with larger errors receiving more weight than they do under MAE.

Q5. Why does MSE punish large prediction errors more strongly than MAE?
A5. The average squared prediction error is approximately 1,561,674.37 salary-units².

Q6. Why might RMSE be easier to interpret than MSE?
A6. cause it returns the matric to original target units.

Q7. if R² = 0.95 does that mean "The model is 95% accurate."
A7. NO, R^2 is not classification accuracy.
it explain about 95% of the varictions in the target values in the evaluated dataset.
-> On this test set, the model explains approximately 99.8% of the variation in salary relative to the mean-prediction baseline.
-> R² is not an error amount; It measures model fit relative to a baseline.

Q8. Which is better?
    Model A
    MAE = $2,500

    Model B
    MAE = $7,500

Model A is better- it explain average moderated error are around $2,500. 
-> Because lower MAE means predictions are closer to the actual values on average

Q9. Suppose:
    Training R² = 0.98
    Testing R² = 0.60
What might these numbers make you suspicious about?

it give you R² error of training is 0.98 -> 
    as we learn today and tommorow both ->
        as per today's matric 0.98 is the better prediction for R² Training ( and it is training error so their has around 80% of dataset to learn machine so at that time it has been given  better prediction)
    and R² Testing gave 0.60 predication so it has been moderated result and low then training prediction.

--> I would be suspicious that the model learned the training data very well but does not generalize nearly as well to unseen data.
Overfitting
A model is overfitting when it learns the training data too specifically, including patterns/noise that do not generalize well to unseen data.
-> Conceptually:
            Training performance
                Excellent
                0.98
                    ↓
            Testing performance
                Much worse
                0.60
 """

# 9. Single Value Prediction 
# Fixed: Wrapped the input value inside a 2D DataFrame to match feature names
single_input = pd.DataFrame({"Experience_Years": [10.5]})
single_pred = model.predict(single_input)

# Fixed: Constructed the new employee DataFrame to display just this specific prediction
new_employee = pd.DataFrame({
    "Experience_Years": single_input["Experience_Years"],
    "Predict_Salary": single_pred
})
print("\n--- Single Employee Prediction ---")
print(new_employee)

""" 
Q. Based on the pattern in the training data, does the predicted salary seem reasonable? Why?
A. as per my opinion - Yes, look in trable first- 
                     10   73000
                     11   77000
    10 year expirence has 73000 and 11 years has 77000 salary and as per we learn to machine it give  75578.796562 predicted salary and it has average MAE = 1045.85 moderator error and for not it is okay.
    so for todays it gave reasonable predicted salary.
 """