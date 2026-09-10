import numpy as np

feature_names = [
    "Tenure",
    "Monthly Charges",
    "Support Calls"
]

weights = np.array([-1.50, 1.20, 0.80])
bias = -0.20

customers = {
    "Customer A": np.array([0.10, 0.90, 0.80]),
    "Customer B": np.array([0.85, 0.40, 0.10]),
    "Customer C": np.array([0.40, 0.60, 0.50]),
    "Customer D": np.array([0.70, 0.75, 0.20])
}

# Create a sigmoid function  : sigmoid(value)

def sigmoid(value):
    return 1 / (1 + np.exp(-value))


# 2. Create a prediction function : predict_churn(customer_features, weights, bias, threshold)
""" 
It must calculate and return:

- Weighted sum
- Churn probability
- Predicted class

Do not print inside this function. Return the three results and print them outside the function.
 """

def predict_churn(customer_features, weights, bias, threshold):
    weighted_sum = np.dot(customer_features, weights) + bias
    churn_probability = sigmoid(weighted_sum)
    predicted_class = int(churn_probability >= threshold)
    return weighted_sum, churn_probability, predicted_class

# 3. Predict all four customers : 1st use - threshold = 0.50
""" 
print- 
Customer: Customer A
Weighted Sum: ...
Churn Probability: ...
Predicted Class: ...

Round displayed numeric results to four decimal places.
 """

for customer_name, customer_features in customers.items():
    weighted_sum, churn_probability, predicted_class = predict_churn(
        customer_features, weights, bias, threshold=0.50
    )
    print(f"Customer: {customer_name}")
    print(f"Weighted Sum: {weighted_sum:.4f}")
    print(f"Churn Probability: {churn_probability:.4f}")
    print(f"Predicted Class: {predicted_class}")

# 4. Test a second threshold : for all 4 customers , threshold = 0.65 and The probabilities must remain unchanged. Only the final classes may change.
new_threshold = 0.65

def predict_churn(customer_features, weights, bias, new_threshold):
    weighted_sum = np.dot(customer_features, weights) + bias
    churn_probability = sigmoid(weighted_sum)
    predicted_class = int(churn_probability >= new_threshold)
    return weighted_sum, churn_probability, predicted_class

for customer_name, customer_features in customers.items():
    weighted_sum, churn_probability, predicted_class = predict_churn(
        customer_features, weights, bias, new_threshold=0.65
    )
    print(f"Customer: {customer_name}")
    print(f"Weighted Sum: {weighted_sum:.4f}")
    print(f"Churn Probability: {churn_probability:.4f}")
    print(f"Predicted Class: {predicted_class}")

# 5. Analyze Customer C’s contributions
""" 
Calculate and print Customer C’s individual feature contributions: contribution_i = x_i * w_i

Example output structure:

Tenure Contribution: ...
Monthly Charges Contribution: ...
Support Calls Contribution: ...
Bias: ...
 """

customer_c_features = customers["Customer C"]
feature_contributions = customer_c_features * weights

print(f"{feature_names[0]} Contribution: {feature_contributions[0]:.4f}")
print(f"{feature_names[1]} Contribution: {feature_contributions[1]:.4f}")
print(f"{feature_names[2]} Contribution: {feature_contributions[2]:.4f}")
print(f"Bias: {bias:.4f}")


""" 
My outputs:

Customer: Customer A
Weighted Sum: 1.3700
Churn Probability: 0.7974
Predicted Class: 1

Customer: Customer B
Weighted Sum: -0.9150
Churn Probability: 0.2860
Predicted Class: 0

Customer: Customer C
Weighted Sum: 0.3200
Churn Probability: 0.5793
Predicted Class: 1

Customer: Customer D
Weighted Sum: -0.1900
Churn Probability: 0.4526
Predicted Class: 0

After thrershold was = 0.65

Customer: Customer A
Weighted Sum: 1.3700
Churn Probability: 0.7974
Predicted Class: 1

Customer: Customer B
Weighted Sum: -0.9150
Churn Probability: 0.2860
Predicted Class: 0

Customer: Customer C
Weighted Sum: 0.3200
Churn Probability: 0.5793
Predicted Class: 0

Customer: Customer D
Weighted Sum: -0.1900
Churn Probability: 0.4526
Predicted Class: 0

Tenure Contribution: -0.6000
Monthly Charges Contribution: 0.7200
Support Calls Contribution: 0.4000
Bias: -0.2000


Explaination
Tenure contribution:         -0.6000 → pushes downward
Monthly Charges contribution: 0.7200 → pushes upward
Support Calls contribution:   0.4000 → pushes upward
Bias:                        -0.2000 → pushes downward
 """

""" 
Final assessment questions
Q1. At threshold 0.50, which customers are classified as churners?
A. Customer A and Customer C

Q2. At threshold 0.65, which customers are classified as churners?
A. Customer A

Q3. Which customer’s class changed when the threshold increased?
A. Customer C

Q4. Which customer has the highest churn probability? Which has the lowest?
A. Highest = Customer A and Lowest = Customer B

Q5. For Customer C, which feature pushes the weighted sum downward?
A. Tenure -0.6000 → pushes downward

Q6. Are you using four neurons because there are four customers? Explain the difference between a customer/sample and a neuron.
A.  Four customers = four data samples.
    Each customer supplies three feature values.
    The same neuron processes every customer.
    That neuron reuses the same weights and bias.

    Four customers do not mean four neurons.

Q7. Describe the current architecture:
. How many input feature values does each customer have? - 3
. How many hidden layers are present? - 0
. How many output neurons are present? - 1

Q8. Would manually changing a weight count as model training? Why or why not?
A. No,
    Training requires the model to:

    Calculate predictions.
    Calculate loss.
    Calculate gradients using backpropagation.
    Update parameters using an optimizer.

in short -- Forward propagation → Loss calculation → Backpropagation → Optimizer update
 """