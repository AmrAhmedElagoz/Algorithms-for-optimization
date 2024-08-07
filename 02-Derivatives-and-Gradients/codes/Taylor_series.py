import numpy as np
import matplotlib.pyplot as plt

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to compute the Taylor series expansion of e^x around a=0
def taylor_expansion_exponential(x, terms):
    series_sum = 0
    for n in range(terms):
        series_sum += (x**n) / factorial(n)
    return series_sum

# Define the range of x values for plotting
x_values = np.linspace(-2, 2, 400)
y_exact = np.exp(x_values)  # Exact exponential function

# Number of terms in the Taylor series
num_terms = 5

# Compute Taylor series approximations
y_taylor = taylor_expansion_exponential(x_values, num_terms)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_exact, label='Exact $e^x$', color='blue', linewidth=2)
plt.plot(x_values, y_taylor, label=f'Taylor Series ({num_terms} terms)', linestyle='--', color='red', linewidth=2)
plt.title(f'Taylor Series Expansion of $e^x$ around $a=0$ with {num_terms} terms')
plt.xlabel('x')
plt.ylabel('$e^x$')
plt.legend()
plt.grid(True)
plt.show()
