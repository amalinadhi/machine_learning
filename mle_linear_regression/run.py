# IMPORT LIBRARY
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)    # reproducible random


# FUNCTIONS
def generate_data(n):
    """
    Generate n random data (x, y) following these equations:
        y = x + sin(1.5pi.x) + random data, x = [0, 2]
    Input:
        n       (int)   : number of generated data
    Output
        data    (list)  : the generated data
    """
    x = np.linspace(0, 2, n)
    y = x - np.sin(1.5*np.pi*x) + np.random.rand(n)

    data = np.column_stack((x, y))
    return data

def fit_MLE(data):
    """
    Fit the line using maximum likelihood
    Input:
        data    (list)  : x, y generated data
    
    Output:
        theta   (list)  : model parameters
    """
    # Solve the normal equations
    n = data.shape[0]
    x = data[:, 0]
    y = data[:, 1]

    X = np.column_stack((np.ones(n), x))
    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    return theta

def metrics_MLE(data, theta):
    """
    Find the accuracy and likelihood of the model
    Input:
        data    (list)  : x, y generated data
        theta   (list)  : the model parameter from solving the MLE
    Output:
        results (float) : the log-likelihood functions
    """
    n = data.shape[0]
    x = data[:, 0]
    y = data[:, 1]
    X = np.column_stack((np.ones(n), x))

    # Find the new data
    y_hat = X @ theta.T

    # Find the variance
    results = np.var(y - y_hat)

    return results

def plot_results(data, theta):
    """
    A function to plot the results
    Input:
        data    (list)  : x, y generated data
        theta   (list)  : the model parameter from solving the MLE
    Output:
        None
    """
    n = data.shape[0]
    x = data[:, 0]
    y = data[:, 1]
    X = np.column_stack((np.ones(n), x))

    # Find the predicted data
    y_hat = X @ theta

    # Plot the data
    fig, ax = plt.subplots(nrows=1, ncols=1, constrained_layout=True, dpi=120)

    ax.scatter(x, y, c='red', label='initial data')
    ax.plot(x, y_hat, c='blue', label='MLE model')
    ax.grid(linestyle="--")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")

    plt.show()

def execute(N):
    # Generate data
    data = generate_data(N)

    # Find model parameters
    theta = fit_MLE(data)

    # Perform post processing
    variance = metrics_MLE(data, theta)
    print(f"variance of error: {variance}")
    plot_results(data, theta)


if __name__ == "__main__":
    N = 100     # number of data
    execute(N)
