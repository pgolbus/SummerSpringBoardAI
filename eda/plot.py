import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest, norm, spearmanr
import seaborn as sns


def draw_violinplots(df):
    num_columns = df.shape[1]
    fig, axes = plt.subplots(1, num_columns, figsize=(12, 4))

    for i, column in enumerate(df.columns):
        ax = axes[i]

        sns.violinplot(data=df[column], ax=ax)
        ax.set_xlabel(column)
        ax.set_ylabel('Value')

    plt.tight_layout()
    plt.show()

def compare_one(x, y, x_label, y_label, title, deg=1):
    # Fit a line to the data
    fit_coeffs = np.polyfit(x, y, deg)
    fit_curve = np.poly1d(fit_coeffs)
    x_fit = np.linspace(x.min(), x.max(), 1000)
    y_fit = fit_curve(x_fit)

    rho = spearmanr(x, y)[0]

    plt.plot(x_fit, y_fit, 'r')
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.text(0.95, 
             0.05, 
             f'rho = {rho:.2f}', 
             ha='right', 
             va='bottom',
             transform=plt.gca().transAxes, 
             fontsize=10)
    plt.show()


def apply_cutoff(series1, series2, cutoff):
    # Apply cutoff to the first series
    cutoff_series1 = series1[series1 <= cutoff]

    # Truncate the second series to match the length of the first series
    truncated_series2 = series2[series1.index.isin(cutoff_series1.index)]

    return cutoff_series1, truncated_series2


def compare_all(df):
    num_columns = df.shape[1]
    fig, axes = plt.subplots(num_columns, num_columns, figsize=(12, 12))
    
    for i, col1 in enumerate(df.columns):
        for j, col2 in enumerate(df.columns):
            ax = axes[i, j]
            
            if i == j:
                ax.hist(df[col1], bins=10, alpha=0.5)
                ax.set_xlabel(col1)
                ax.set_ylabel('Frequency')
            else:
                ax.scatter(df[col2], df[col1])
                ax.set_xlabel(col2)
                ax.set_ylabel(col1)
                
                # Fit a line to the data
                fit_coeffs = np.polyfit(df[col2], df[col1], 1)
                fit_curve = np.poly1d(fit_coeffs)
                x_fit = np.linspace(df[col2].min(), df[col2].max(), 1000)
                y_fit = fit_curve(x_fit)
                rho = spearmanr(df[col2],df[col1])[0]
                ax.plot(x_fit, y_fit)
                
                # Display R-squared value
                ax.text(0.95, 0.05, f'rho = {rho:.2f}', ha='right', va='bottom',
                        transform=ax.transAxes, fontsize=10)
    
    plt.tight_layout()
    plt.show()

def plot_histogram(series, cutoff=None, draw_normal=False):
    plt.figure(figsize=(8, 6))
    if cutoff:
        series = series[series <= cutoff]
    plt.hist(series, bins='auto', alpha=0.7, color='steelblue', edgecolor='black', density=True)

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')

    if draw_normal:
        mean = series.mean()
        std = series.std()
        x = np.linspace(series.min(), series.max(), 100)
        y = norm.pdf(x, loc=mean, scale=std)
        plt.plot(x, y, color='green', linewidth=2)

    plt.grid(True)
    plt.show()