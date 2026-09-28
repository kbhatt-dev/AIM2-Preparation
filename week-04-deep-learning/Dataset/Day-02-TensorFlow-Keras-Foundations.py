# -------------------------------
# Exercise 2 — Tensor exploration
# -------------------------------
""" 
Scalar:
7

Vector:
[0.20, 0.80, 0.70]

Customer batch:
[
    [0.10, 0.90, 0.80],
    [0.85, 0.40, 0.10],
    [0.40, 0.60, 0.50],
    [0.70, 0.75, 0.20]
]
 """
import numpy as np
import tensorflow as tf
import keras
from keras import layers

# 1. Scalar (0-D Tensor)
scalar_tensor = tf.constant(7, dtype=tf.float32)

# 2. Vector (1-D Tensor)
vector_tensor = tf.constant([0.20, 0.80, 0.70], dtype=tf.float32)

# 3. Customer Batch (2-D Tensor)
customer_tensor = tf.constant([
    [0.10, 0.90, 0.80],
    [0.85, 0.40, 0.10],
    [0.40, 0.60, 0.50],
    [0.70, 0.75, 0.20]
], dtype=tf.float32)

# Display Properties
tensors = {
    "Scalar": scalar_tensor,
    "Vector": vector_tensor,
    "Cutomer Batch": customer_tensor
}

for name, tensor in tensors.items():
    print(f"====== {name} ======")
    print(f"Value: \n{tensor.numpy()}")
    print(f"Shape: {tensor.shape}")
    print(f"Rank (Dimentions): {tf.rank(tensor).numpy()}")
    print(f"Datatype : {tensor.dtype}\n")

# -------------------------------
# Exercise 3 — Build your first Keras network
# ------------------------------- 
""" 
Build this architecture:
Three customer features
        ↓
Four-neuron hidden layer with ReLU
        ↓
One-neuron output layer with sigmoid
 """

model = keras.Sequential([
    keras.Input(
        shape=(3,),
        name="Customer Features"
    ),

    layers.Dense(
        units= 4,
        activation='relu',
        name="hidden layer"
    ),

    layers.Dense(
        units= 1,
        activation="sigmoid",
        name="output layer"
    )
], name = "Customer_churn_network")

""" 
Hidden-layer weights = 3*4 = 12
Hidden-layer biases = 4
Hidden-layer total parameters = 16
Output-layer weights = 4*1 = 4
Output-layer biases = 1
Output-layer total parameters = 5
Total model parameters = 16+5 = 21
 """

print("============Model Summary====================")
model.summary()
print()

# -------------------------------
# Exercise 4 — Inspect the layers
# -------------------------------

print("==================Model Layers======================")

# build a model so shapes are defined
model.build()
print(model.layers)

# Loop through each layer and print the request attributes
for layer in model.layers:
    print(f"Layer Name: {layer.name}")

    # kernal shape
    if hasattr(layer, 'bias') and layer.bias is not None:
        print(f"Bias Shape: {layer.bias.shape}")
    else:
        print(f"Bias Shape: No bias(N/A)")

    # Activation Function
    if hasattr(layer, 'activation') and layer.activation is not None:
        print(f"Activation: {layer.activation.__name__}")
    else:
        print("Activation None (Linear/N/A)")

    print("-"*30)

print()

""" 
Q. Why does model.layers contain two layers rather than three, even though the model includes keras.Input()?
A. It contains two layers rather than three because, "Input" object dos not appear inside "model.layer"
   cause it is not considered a regular model layer. 
 """

# -------------------------------
# Exercise 5 — Perform an untrained forward pass
# -------------------------------

# Pass the tensor through the model
probabilities = model(customer_tensor, training=False)

# print Requested attributes
print("=== Probability Tensor ===")
print(probabilities)

print(f"\nProbability-tensor shape: {probabilities.shape}")
print(f"Datatype: {probabilities.dtype}")

print("\n=== NumPy Version of Probabilities ===")
print(probabilities.numpy())

# Convert probabilities into classes using threshold 0.50 via TF operations
threshold = 0.50
boolean_mask = probabilities >= threshold
classes = tf.cast(boolean_mask, tf.int32)

print("\n=== Converted Classes (Threshold >= 0.50) ===")
print(classes.numpy())

customer_numpy = customer_tensor.numpy()

print("First customer:", customer_tensor[0])
print("Complete NumPy array:")
print(customer_numpy)
print("Python type:", type(customer_numpy))