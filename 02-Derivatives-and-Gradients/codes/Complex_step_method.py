import numpy as np
import matplotlib.pyplot as plt

# Define the function and its true derivative
def f(x):
    return np.sin(x)

def f_prime_true(x):
    return np.cos(x)

# Numerical derivative using central difference
def numerical_derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Point at which we evaluate the derivative
x = np.pi / 4  # 45 degrees

# Range of step sizes to test
h_values = np.logspace(-20, 0, 100)

# Calculate the true derivative
true_value = f_prime_true(x)

# Calculate errors for each step size
errors = []
for h in h_values:
    numerical_value = numerical_derivative(f, x, h)
    error = np.abs(numerical_value - true_value)
    errors.append(error)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.loglog(h_values, errors, label='Numerical Error')
plt.xlabel('Step size h')
plt.ylabel('Absolute Error')
plt.title('Numerical Derivative Error vs. Step Size')
plt.axvline(x=np.sqrt(np.finfo(float).eps), color='red', linestyle='--', label='sqrt(epsilon)')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the function and its true derivative
def f(x):
    return np.sin(x)

def f_prime_true(x):
    return np.cos(x)

# Forward difference method
def forward_difference_derivative(f, x, h):
    return (f(x + h) - f(x)) / h

# Central difference method
def central_difference_derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Complex step method
def complex_step_derivative(f, x, h):
    return np.imag(f(x + h*1j)) / h

# Point at which we evaluate the derivative
x = np.pi / 4  # 45 degrees

# Range of step sizes to test
h_values = np.logspace(-20, 0, 100)

# Calculate the true derivative
true_value = f_prime_true(x)

# Calculate errors for each step size
forward_errors = []
central_errors = []
complex_errors = []

for h in h_values:
    forward_value = forward_difference_derivative(f, x, h)
    central_value = central_difference_derivative(f, x, h)
    complex_value = complex_step_derivative(f, x, h)
    
    forward_errors.append(np.abs(forward_value - true_value))
    central_errors.append(np.abs(central_value - true_value))
    complex_errors.append(np.abs(complex_value - true_value))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.loglog(h_values, forward_errors, label='Forward Difference Error', color='blue')
plt.loglog(h_values, central_errors, label='Central Difference Error', color='orange')
plt.loglog(h_values, complex_errors, label='Complex Step Error', color='green')
plt.axvline(x=np.sqrt(np.finfo(float).eps), color='red', linestyle='--', label='sqrt(epsilon)')
plt.xlabel('Step size h')
plt.ylabel('Absolute Error')
plt.title('Error Comparison: Forward, Central Difference vs. Complex Step Method')
plt.legend()
plt.grid(True)
plt.show()
