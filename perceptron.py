import numpy as np

class Perceptron:
    def __init__(self, input_size):
        self.weights = np.zeros(input_size + 1)  # Initialize weights to zeros, +1 for bias term

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Weighted sum + bias
        return 1 if summation >= 0 else 0  # Activation step, returns 1 if >= 0, else 0

    def train(self, training_inputs, labels, epochs):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += (label - prediction) * inputs  # Update weights
                self.weights[0] += (label - prediction)  # Update bias term

# Training data for AND gate
and_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
and_labels = np.array([0, 0, 0, 1])

# Training data for XOR gate
xor_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
xor_labels = np.array([0, 1, 1, 0])

# Create perceptron objects
and_perceptron = Perceptron(input_size=2)
xor_perceptron = Perceptron(input_size=2)

# Train the perceptrons
and_perceptron.train(and_inputs, and_labels, epochs=10)
xor_perceptron.train(xor_inputs, xor_labels, epochs=10)

# Test the perceptrons
print("AND Gate:")
for inputs in and_inputs:
    print(f"Input: {inputs}, Output: {and_perceptron.predict(inputs)}")

print("\nXOR Gate:")
for inputs in xor_inputs:
    print(f"Input: {inputs}, Output: {xor_perceptron.predict(inputs)}")
