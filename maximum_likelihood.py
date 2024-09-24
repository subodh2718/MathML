import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def maximum_likelihood(data):
    """
    Estimate parameters of a Gaussian distribution using Maximum Likelihood Estimation (MLE).

    Args:
    data (array-like): An array of observed data.

    Returns:
    tuple: Estimated mean and standard deviation of the Gaussian distribution.
    """
    # Calculate mean and standard deviation
    mean_mle = np.mean(data)
    std_mle = np.std(data, ddof=1)  # Use ddof=1 for sample standard deviation

    return mean_mle, std_mle

def plot_distribution(data, mean, std):
    """
    Plot the data distribution and the estimated Gaussian distribution.

    Args:
    data (array-like): An array of observed data.
    mean (float): Mean of the estimated Gaussian distribution.
    std (float): Standard deviation of the estimated Gaussian distribution.
    """
    # Create a range of x values for the Gaussian curve
    x = np.linspace(min(data) - 1, max(data) + 1, 100)
    y = norm.pdf(x, mean, std)

    plt.hist(data, density=True, bins=20, alpha=0.6, color='g', label='Data Histogram')
    plt.plot(x, y, 'r-', label=f'Estimated Gaussian\nMean: {mean:.2f}, Std: {std:.2f}')
    plt.title('Maximum Likelihood Estimation of Gaussian Distribution')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Sample data: Normally distributed data
    np.random.seed(0)  # For reproducibility
    data = np.random.normal(loc=5, scale=2, size=100)

    # Estimate parameters using MLE
    mean, std = maximum_likelihood(data)

    # Print estimated parameters
    print(f"Estimated Mean: {mean:.2f}")
    print(f"Estimated Std Dev: {std:.2f}")

    # Plot the distribution
    plot_distribution(data, mean, std)
