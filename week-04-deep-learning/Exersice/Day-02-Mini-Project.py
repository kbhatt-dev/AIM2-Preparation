""" 
Day 2 Mini-Project
Keras Architecture Inspector
Build a second model with this architecture:
3 input features
       ↓
6-neuron hidden layer using ReLU
       ↓
3-neuron hidden layer using ReLU
       ↓
1-neuron output layer using sigmoid

Name the model:
deep_churn_network

Name the layers:
hidden_layer_1
hidden_layer_2
output_layer

Mini-project requirements
1. Build the model using keras.Sequential.
2. Specify the three-feature input using keras.Input.
3. Calculate every layer’s parameter count manually before running summary().
4. Run model.summary() and compare it with your calculation.
5. Print each layer’s:
   - Name
   - Kernel shape
   - Bias shape
   - Activation name
6. Pass all four customer samples through the model.
7. Produce classes using threshold 0.50.
8. Produce classes again using threshold 0.65.
9. Confirm that changing the threshold changes only the classes—not the underlying probabilities.
10. Clearly print:
These predictions come from an untrained model and are not meaningful business predictions.

Do not use:
model.fit()
Training begins on Day 3.
 """

import tensorflow as tf
import keras
from keras import layers


# 1 & 2. Build the model using keras.Sequential and keras.Input
deep_churn_network = keras.Sequential([
    keras.Input(shape=(3,)),
    layers.Dense(6, activation="relu", name="hidden_layer_1"),
    layers.Dense(3, activation="relu", name="hidden_layer_2"),
    layers.Dense(1, activation="sigmoid", name="output_layer")
], name="deep_churn_network")
# 4. Run model.summary() to verify manual calculations
print("=== 4. Model Summary ===")
deep_churn_network.summary()
print("\n" + "="*50 + "\n")

# 5. Print each layer's detailed structural attributes
print("=== 5. Layer Architecture Details ===")
print(deep_churn_network.layers)
for layer in deep_churn_network.layers:
    print(f"Layer Name: {layer.name}")
    print(f"Kernal shape: {layer.kernel.shape}")
    print(f"Bias Shape: {layer.bias.shape}")
    print(f"Activation: {layer.activation.__name__}")
    print("-"*30)
print("\n"+ "="*50 +"\n")

# 6. Pass all four customer samples through the model
customer_tensor = tf.constant([
    [0.10, 0.90, 0.80],
    [0.85, 0.40, 0.10],
    [0.40, 0.60, 0.50],
    [0.70, 0.75, 0.20]
], dtype=tf.float32)

probabilities = deep_churn_network(customer_tensor, training = False)
print("=== 6. Underlying Probabilities ===")
print(probabilities.numpy())
print("\n" + "="*50 + "\n")


# 7. Produce classes using threshold 0.50
probabilities_50 = deep_churn_network(customer_tensor, training=False)
classes_50 = tf.cast(probabilities_50 >= 0.50, tf.int32)
print("=== 7. Classes (Threshold 0.50) ===")
print(classes_50.numpy())
print("\n" + "="*50 + "\n")

# 8. Produce classes again using threshold 0.65
probabilities_65 = deep_churn_network(customer_tensor, training=False)
classes_65 = tf.cast(probabilities_65 >= 0.65, tf.int32)
print("=== 8. Classes (Threshold 0.65) ===")
print(classes_65.numpy())
print("\n" + "="*50 + "\n")

probabilities_identical = tf.reduce_all(
    tf.equal(probabilities_50, probabilities_65)
)

print(
    "Probabilities identical:",
    probabilities_identical.numpy()
)

print(
    "No classes changed in this run because all probabilities "
    "were below 0.50."
)

probabilities_identical = tf.reduce_all(
    tf.equal(probabilities_50, probabilities_65)
)

changed_count = tf.reduce_sum(
    tf.cast(classes_50 != classes_65, tf.int32)
)

# 9. Confirm that probabilities remain identical
print("=== 9. Probabilities Verification ===")
print("Probabilities identical:", probabilities_identical.numpy())
print("Number of changed classes:", changed_count.numpy())
print("Only the class labels changed; the probabilities remained unchanged.")
print("\n" + "="*50 + "\n")

# 10. Important business disclaimer
print("🚨 DISCLAIMER:")
print("These predictions come from an untrained model and are not meaningful business predictions.")

""" 
hidden_layer_1:
kernels = 18 weights
bias = 6
total = 24 perameters

hidden_layer_2:
kernels = 18 weights
bias = 3
total = 21 perameters

output_layer:
kernels = 3 weights
bias = 1
total = 4 perameters

Total Network Perameter= 49 perameters
 """

""" 
Answer in your own words:
1. What is the difference between TensorFlow and Keras?
-> Tensorflow is a engin that perform the calculations.
-> Keras is a high-network api it gives us convenieant building blocks.
-> keras controls the engin so the tensorflow engine easier to use.

2. How is a tensor similar to a NumPy array?
-> tensor is the multidimential collection of values with one containt datatype 
-> and numpy array follow the same things. although standerd tensors are immutables.

3. What are the rank and shape of a tensor containing four customers and three features?
-> rank = 2 
-> shape (4, 3)

4. Why is the model input declared as shape=(3,) instead of shape=(4, 3)?
-> because 4 shows the data rows / how many data are there is shows as 4 but it has realtime and dynamic.
-> when it will change 4 to 50, 100, 25 using only features it shows the same model process with diffrent datasets.
-> it shows, every sample must still have three features.

5. What does None mean in an output shape such as (None, 6)?
-> it means the model can accepts available number of samples in each batch.
-> the features or neuron dimentions remains fixed.

6. In Dense(6), what does the number 6 represent?
-> the number of neurons (units) inside that specific dense layer.

7. What makes a Dense layer “fully connected”?
-> because every single input node is connected to every single neuron in the layer. 

8. Calculate the parameter count for this layer: 3 inputs -> 6 neurons
-> Kernels (Weights): 3 * 6 = 18 
    Biases: 6 
    Total: 18 + 6 = 24 parameters

9. Calculate the parameter count for: 6 inputs -> 3 neurons
-> Kernels (Weights): 6 *  3 = 18
    Biases: 3
    Total: 18 + 3 =  21 parameters

10. Calculate the parameter count for: 3 inputs -> 1 neuron
-> Kernels (Weights): 3 * 1 = 3
    Biases: 1
    Total: 3 + 1 = 4 parameters

11. What is the total parameter count of the mini-project model?
-> The network has 49 total parameters (24 + 21 + 4). All 49 are trainable.

12. Why does the input object not count as a hidden layer?
-> it contains no neurons, performs no mathematical operations, and has 0 parameters.

13. Why does the output layer use one sigmoid neuron?
-> produce a single probability value between 0.0 and 1.0. A single neuron generates the solitary score, 
    and the sigmoid activation function compresses that raw score into the restricted 0 to 1 mathematical 
    range.

14. Are the forward-pass probabilities meaningful before training? Explain.
-> The outputs are valid mathematical results, but they are not meaningful churn 
    predictions because the model has not learned from training data. They are based on
    initialized weights.

15. Does model.compile() train the model?
-> No, it does not train the model. model.compile() merely configures the training process by 
    assigning the optimizer, defining the loss function, and selecting performance metrics. 
    It packages the model for execution but does not process any training data.

16. Which operation will actually begin training the model?
-> The model.fit() operation officially initiates the training process. This is the stage where
     data cycles through the network to update parameters.

17. If the model expects three features but receives a tensor with shape (4, 2), what problem will occur?
-> A shape incompatibility or dimension-mismatch error will occur because the model expects three 
    features but receives only two. Keras will commonly report this as a ValueError, although the 
    exact exception can vary.

18. How does today’s Dense-layer calculation connect to your Day 1 NumPy neuron?
-> Today’s Dense layers use the exact same foundational formula you calculated in NumPy:
     Y=XW+B (or inputs * weights + bias). The key difference is that instead of manually looping 
     or structuring a single math equation, TensorFlow's Dense layers automate this matrix multiplication 
     across massive batches of data concurrently.

 """