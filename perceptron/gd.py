import random

import numpy as np

# # Set the seed for reproducibility
np.random.seed(42)

class Perceptron:

    def __init__(self, lr=0.01, epochs=1000, thresh=0):
        self.lr = lr
        self.epochs = epochs
        self.thresh = thresh
        self.b = [random.uniform(-1, 1) for _ in range(2)]
        self.e = random.uniform(-1, 1)

    def predict(self, x):
        if self.b[0] * x[0] + self.b[1] * x[1] + self.e >= self.thresh:
            return 1
        return 0

    def update(self, x, labels):
        acc = 0
        skip = False
        for i in range(len(x)):
            pred = self.predict(x[i])
            loss = labels[i] - pred
            grad_x = self.lr * loss * x[i][0]
            grad_y = self.lr * loss * x[i][1]
            grad_e = self.lr * loss
            if pred == labels[i]:
                acc += 1
            else:
                if not skip:
                    print(f"coord: ({x[i][0]:.2f}, {x[i][1]:.2f})")
                    print(f"class: {labels[i]} pred: {pred}")
                    print(f"weights: {self.b[0]:.4f}, {self.b[1]:.4f}, {self.e:.4f}")
                    print(f"grad: x, y, b {grad_x:.4f}, {grad_y:.4f}, {grad_e:.4f}")
                    self.b[0] += grad_x
                    self.b[1] += grad_y
                    self.e += grad_e
                    print(f"new weights: {self.b[0]:.4f}, {self.b[1]:.4f}, {self.e:.4f}")

                    key = input()
                    if key == "s":
                        skip = True
                    if key == "q":
                        return -1
        loss = 1 - (acc / len(x))
        return loss

    def train(self, x, labels):
        for i in range(self.epochs):
            loss = self.update(x, labels)
            if loss == -1:
                return
            print(f"{i}, {self.b[0]:.2f}, {self.b[1]:.2f}, {self.e:.2f}, {loss:.2f}")
            if loss == 0:
                break


# Set the seed for reproducibility
np.random.seed(42)

# Number of data points
num_points = 100

# Generate x values from -1 to 1
x = np.linspace(-1, 1, num_points)

# Generate y values from the line y = x with added noise
y = x + np.random.normal(loc=0, scale=1, size=num_points)
input_array = np.array(list(zip(y, x)))
labels = np.where(y > x, 1, 0)

perceptron = Perceptron()
perceptron.train(input_array, labels)
m = -1 * perceptron.b[1] / perceptron.b[0]
bias = -1 * perceptron.e / perceptron.b[0]
print(f"y = {m:.2f}x + {bias:.2f}")