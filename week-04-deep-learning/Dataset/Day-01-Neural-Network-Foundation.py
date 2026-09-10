""" 
Q1. How is logistic regression connected to an artificial neuron?
-> Logistic regression can be seen as a simple form of an artificial neuron.
     In logistic regression, we take a linear combination of input features, apply a weighted sum, and then pass it through a sigmoid 
     activation function to produce an output between 0 and 1. This is similar to how an artificial neuron operates: it takes inputs, 
     applies weights, sums them up, and then applies an activation function (like the sigmoid function) to produce an output. 
     Therefore, logistic regression can be considered as a single-layer neural network with one neuron.

Q2. What is the difference between a weight and a bias?
-> In the context of neural networks, a weight is a parameter that determines the importance of an input feature in the model's prediction. 
     It is multiplied by the input feature to scale its contribution to the output. A bias, on the other hand, is an additional parameter that allows 
     the model to shift the activation function to better fit the data. It helps the model to make predictions even when all input features are zero. 
     In summary, weights control the influence of inputs, while biases allow for flexibility in the model's output. 

Q3. Why would adding several layers without activation functions not create a truly powerful neural network?
-> Adding several layers without activation functions would not create a truly powerful neural network because the composition of linear transformations is still a linear
     transformation. Without non-linear activation functions, the network would only be able to model linear relationships between inputs and outputs, regardless of the 
     number of layers. Activation functions introduce non-linearity, allowing the network to learn complex patterns and relationships in the data. 
     Therefore, to create a powerful neural network capable of capturing intricate patterns, it is essential to include activation functions between layers.

Q4. Which activation function would you normally choose for:
-- A hidden layer? -> For a hidden layer, the ReLU (Rectified Linear Unit) activation function is commonly chosen. 
                     ReLU is defined as f(x) = max(0, x), which means it outputs the input directly if it is positive; otherwise, it outputs zero. 
                     ReLU is preferred because it helps mitigate the vanishing gradient problem, allows for faster training, and introduces non-linearity to the model.
                    
-- A binary-classification output? -> For a binary-classification output, the sigmoid activation function is typically chosen. 
                                      The sigmoid function is defined as f(x) = 1 / (1 + exp(-x)), which maps any real-valued number to a value between 0 and 1. 
                                      This makes it suitable for binary classification tasks, as the output can be interpreted as a probability of belonging to 
                                      one of the two classes.

-- A ten-class MNIST output? -> For a ten-class MNIST output, the softmax activation function is commonly used.
                                      The softmax function is defined as f(x_i) = exp(x_i) / sum(exp(x_j)) for all classes j, which converts the raw output scores 
                                      (logits) into probabilities that sum to 1 across the ten classes. This makes it suitable for multi-class classification tasks, 
                                      such as recognizing handwritten digits in the MNIST dataset.  

Q5. Does forward propagation update the model’s weights? Explain what it does.
-> No, forward propagation does not update the model's weights. Forward propagation is the process of passing input data through the neural network to compute the output predictions. 
     During this process, the input features are multiplied by their corresponding weights, summed up, and passed through activation functions to produce the final output. 
     The purpose of forward propagation is to calculate the predicted output based on the current weights and biases of the model. 
     Weight updates occur during the backpropagation phase, where the model calculates gradients based on the loss function and adjusts 
     the weights accordingly to minimize the error in predictions.

Q6. Categorize each item as a parameter or hyperparameter:
-- Weight -> Parameter
-- Bias -> Parameter
-- Learning rate -> Hyperparameter
-- Number of hidden neurons -> Hyperparameter
-- Number of epochs -> Hyperparameter

Q7. Calculate the weighted sum for this neuron:
    x1​=0.60, x2​=0.40 w1​=−1.00, w2​=1.50, b=−0.10

-> use - z=w1​x1​+w2​x2​+b = - z = (-1.00 * 0.60) + (1.50 * 0.40) + (-0.10)
                        - z = (-0.60) + (0.60) + (-0.10)
                        - z = -0.10

Q8. Suppose that neuron produces a sigmoid probability of 0.475.
-- What is the prediction at threshold 0.50?
-> The prediction at threshold 0.50 would be 0, since the sigmoid probability of 0.475 is less than the threshold of 0.50. 
   In binary classification, if the predicted probability is below the threshold, the model predicts the negative class (0), 
   and if it is equal to or above the threshold, it predicts the positive class (1).

-- What is the prediction at threshold 0.40?
-> The prediction at threshold 0.40 would be 1, since the sigmoid probability of 0.475 is greater than the threshold of 0.40. 
   In binary classification, if the predicted probability is below the threshold, the model predicts the negative class (0), 
   and if it is equal to or above the threshold, it predicts the positive class (1).

-- Why did the prediction change even though the probability stayed the same?
-> The prediction changed because the threshold for classification was altered. 
   The predicted probability of 0.475 remained constant, but the decision boundary for classifying the output as either 
   class 0 or class 1 depends on the chosen threshold. When the threshold was set to 0.50, the probability of 0.475 was below this threshold, 
   resulting in a prediction of class 0. However, when the threshold was lowered to 0.40, the same probability of 0.475 exceeded this new threshold, 
   leading to a prediction of class 1. This illustrates how changing the threshold can affect the final classification outcome without altering the 
   underlying predicted probability.
 """

""" 
Tenure contribution=0.20(−1.50)
Charges contribution=0.80(1.20)
Calls contribution=0.70(0.80)

z=x1​w1​+x2​w2​+x3​w3​+b 
z = (0.20 * -1.50) + (0.80 * 1.20) + (0.70 * 0.80) + (-0.10)

Q. how do you claldulate b = -0.10 in this case?
A. In this case, the bias term (b) is a constant value that is added to the weighted sum of the inputs. 
The bias allows the model to shift the activation function and helps it make predictions even when all input features are zero.
To calculate the weighted sum (z) for this neuron, you would follow these steps:
1. Multiply each input feature by its corresponding weight:
   - Tenure contribution: 0.20 * -1.50 = -0.30
   - Charges contribution: 0.80 * 1.20 = 0.96
   - Calls contribution: 0.70 * 0.80 = 0.56

z = -0.30 + 0.96 + 0.56 + (-0.10)
z = 1.12

if b = -0.20, then the calculation would be:
z = -0.30 + 0.96 + 0.56 + (-0.20)
z = 1.02

 """
import numpy as np

feature_names = [
    "Tenure",
    "Monthly Charges",
    "Support Calls"
]

features = np.array([0.20, 0.80, 0.70])
# After the first customer works, change only tenure:
features1 = np.array([0.90, 0.80, 0.70])
weights = np.array([-1.50, 1.20, 0.80])

bias = -0.20
threshold = 0.50

def sigmoid(value):
    # TODO: Implement the sigmoid formula using np.exp()
    return 1 / (1 + np.exp(-value))

# Manual weighted-sum calculation:
# TODO: Write your manual calculation and answer here.  it is --> z = 1.02

# Use np.dot() to calculate features × weights, and then add bias.
weighted_sum = np.dot(features, weights) + bias
weighted_sum1 = np.dot(features1, weights) + bias

# Pass the weighted sum through sigmoid.
churn_probability = sigmoid(weighted_sum)
churn_probability1 = sigmoid(weighted_sum1)

# Convert the probability into class 0 or class 1.
prediction = 1 if churn_probability >= threshold else 0
prediction1 = 1 if churn_probability1 >= threshold else 0

print("Weighted sum:", weighted_sum)
print("Churn probability:", churn_probability)
print("Predicted class:", prediction)

print("\nAfter the first customer works, change only tenure:")
print("Weighted sum (updated):", weighted_sum1)
print("Churn probability (updated):", churn_probability1)
print("Predicted class (updated):", prediction1)


""" 
Output---
Weighted sum: 1.0199999999999998
Churn probability: 0.7349725994665188
Predicted class: 1

After the first customer works, change only tenure:
Weighted sum (updated): -0.030000000000000193
Churn probability (updated): 0.4925005624493795
Predicted class (updated): 0

 """

""" 
Questions to answer
Q1. What weighted sum did you calculate manually?
A1. The weighted sum calculated manually is z = 1.02.

Q2. Does the NumPy result match your manual result?
A2. Yes, the NumPy result matches the manual result. The weighted sum calculated using NumPy is approximately 1.02, 
    which is consistent with the manual calculation. Output from NumPy is Weighted sum: 1.0199999999999998.

Q3. What churn probability and predicted class did Customer 1 receive?
A3. Customer 1 received a churn probability of approximately 0.735 and a predicted class of 1 (indicating that the customer is likely to churn).

Q4. What churn probability and predicted class did Customer 2 receive?
A4. Customer 2 received a churn probability of approximately 0.493 and a predicted class of 0 (indicating that the customer is not likely to churn).

Q5. Why did increasing tenure reduce the predicted churn probability?
A5. Increasing tenure reduced the predicted churn probability because the weight associated with the tenure feature is negative (-1.50). 
    This means that as the tenure value increases, it contributes negatively to the weighted sum (z). 
    A higher tenure value leads to a lower weighted sum, which in turn results in a lower output from the sigmoid function.

Q6. Is this neuron currently trained? Explain why or why not.
A6. No, this neuron is not currently trained. Training a neuron involves adjusting its weights and bias based on the input data and 
    the corresponding target outputs (labels) to minimize the prediction error. In this case, the weights and bias are predefined and have not 
    been updated through any training process. Therefore, the neuron has not learned from any data and is not considered trained.

Q7. If all weights and the bias were 0, what would the sigmoid output be?
A7. If all weights and the bias were 0, the weighted sum (z) would be 0 regardless of the input features. 
    The sigmoid function applied to a weighted sum of 0 would yield an output of 0.5, as the sigmoid function is defined as f(x) = 1 / (1 + exp(-x)). 
    When x = 0, this simplifies to f(0) = 1 / (1 + exp(0)) = 1 / (1 + 1) = 0.5. 
    Therefore, the sigmoid output would be 0.5, indicating an equal probability for both classes in a binary classification scenario.
 """



