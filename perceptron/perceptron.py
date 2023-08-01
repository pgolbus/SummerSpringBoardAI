import numpy as np

# By "bias term" ChatGPT means the "b" in y = mx + b

class Perceptron:
    def __init__(self, input_size):
        self.weights = np.zeros(input_size + 1)  # Initialize weights to zeros, +1 for bias term

    def predict(self, inputs):
        # "dot" means sum up the linear combination
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Weighted sum + bias
        return 1 if summation >= 0 else 0  # Activation step, returns 1 if >= 0, else 0

    def train(self, training_inputs, labels, epochs, learning_rate = 0.1, verbose=False):
        for i in range(epochs):
            score = 0
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                if prediction == label:
                    score += 1
                self.weights[1:] += learning_rate * (label - prediction) * inputs  # Update weights
                self.weights[0] += learning_rate * (label - prediction)  # Update bias term
            if verbose:
                print(f"Epoch {i + 1}: Score = {score / len(training_inputs)}")

if __name__ == "__main__":
    num_points = 200
    
    # Generate x values from -5 to 5
    x = np.linspace(-5, 5, num_points)
    
    # Generate y values from the line y = x with added noise
    y = x + np.random.normal(loc=0, scale=5, size=num_points)
    
    # Generate inputs and labels based on the relative positions to the line y = x
    inputs = np.column_stack((x, y))
    labels = np.where(y > x, 1, 0)
    
    # Create perceptron objects
    perceptron = Perceptron(input_size=2)
    perceptron.train(inputs, labels, 100, verbose=True)
    
    print(perceptron.weights)
