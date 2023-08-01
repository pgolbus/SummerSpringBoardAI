import matplotlib.pyplot as plt
import numpy as np


def scatter_and_fit(x, y, x_label, y_label, title):
    # Fit a line to the data
    fit_coeffs = np.polyfit(x, y, 1)
    fit_slope = fit_coeffs[0]
    fit_intercept = fit_coeffs[1]
    x_fit = np.linspace(x.min(), x.max(), 1000)
    y_fit = fit_slope * x_fit + fit_intercept

    plt.plot(x_fit, y_fit, 'r')
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()