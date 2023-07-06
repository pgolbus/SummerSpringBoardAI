import numpy as np

# By "bias term" ChatGPT means the "b" in y = mx + b

class Perceptron:
    def __init__(self, input_size):
        self.weights = np.zeros(input_size + 1)  # Initialize weights to zeros, +1 for bias term

    def predict(self, inputs):
        # "dot" means sum up the linear combination
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Weighted sum + bias
        return 1 if summation >= 0 else 0  # Activation step, returns 1 if >= 0, else 0

    def train(self, training_inputs, labels, epochs, verbose=False):
        for i in range(epochs):
            score = 0
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                if prediction == label:
                    score += 1
                self.weights[1:] += (label - prediction) * inputs  # Update weights
                self.weights[0] += (label - prediction)  # Update bias term
            if verbose:
                print(f"Epoch {i + 1}: Score = {score / len(training_inputs)}")

if __name__ == "__main__":
    # Training data for AND gate
    and_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    and_labels = np.array([0, 0, 0, 1])
    
    # Training data for XOR gate
    xor_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    xor_labels = np.array([0, 1, 1, 0])
    
    # Create perceptron objects
    and_perceptron = Perceptron(input_size=2)
    xor_perceptron = Perceptron(input_size=2)
    
    # Train and test the perceptrons
    print("AND Gate:")
    and_perceptron.train(and_inputs, and_labels, epochs=10, verbose=True)
    print("Final")
    for inputs in and_inputs:
        print(f"Input: {inputs}, Output: {and_perceptron.predict(inputs)}")
    
    print("\nXOR Gate:")
    xor_perceptron.train(xor_inputs, xor_labels, epochs=10, verbose=True)
    print("Final")
    for inputs in xor_inputs:
        print(f"Input: {inputs}, Output: {xor_perceptron.predict(inputs)}")
