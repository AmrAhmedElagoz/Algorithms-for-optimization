import numpy as np
import matplotlib.pyplot as plt

# Define the function and its exact derivative
def f(x):
    return np.exp(x)  # Example function e^x

def exact_derivative(x):
    return np.exp(x)  # Exact derivative of e^x is e^x

# Forward difference approximation
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

# Define the point at which to approximate the derivative and the step size
x = 1.0
h = 0.1

# Compute the exact derivative and the forward difference approximation
exact = exact_derivative(x)
approx = forward_difference(f, x, h)

print(f"Exact derivative at x = {x}: {exact}")
print(f"Forward difference approximation at x = {x} with h = {h}: {approx}")

# Plotting the function and its derivative approximation
x_values = np.linspace(0, 2, 100)
y_values = f(x_values)
y_derivative_exact = exact_derivative(x_values)
y_derivative_approx = forward_difference(f, x_values, h)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='$e^x$', color='blue', linewidth=2)
plt.plot(x_values, y_derivative_exact, label='Exact Derivative $e^x$', linestyle='--', color='green', linewidth=2)
plt.plot(x_values, y_derivative_approx, label='Forward Difference Approximation', linestyle='--', color='red', linewidth=2)
plt.scatter([x], [approx], color='red', zorder=5, label='Approximation at x = 1.0')
plt.title('Forward Difference Approximation of the Derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

####

import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return x**2

# Forward difference method to estimate derivative
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

# Example usage
x = 1
h = 0.1

# Calculate derivative using forward difference method
derivative_estimate = forward_difference(f, x, h)

# Exact derivative for comparison
exact_derivative = 2 * x  # Since f(x) = x^2, f'(x) = 2x

# Print results
print(f"Exact derivative at x = {x}: {exact_derivative}")
print(f"Estimated derivative with h = {h}: {derivative_estimate}")

# Create points for plotting the function and the tangent line
x_values = np.linspace(x - 1, x + 1, 400)
y_values = f(x_values)

# Tangent line at x
tangent_line = exact_derivative * (x_values - x) + f(x)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='$f(x) = x^2$', color='blue')
plt.plot(x_values, tangent_line, '--', label='Tangent line at $x=1$', color='orange')
plt.scatter([x, x + h], [f(x), f(x + h)], color='red')  # Points used in forward difference
plt.plot([x, x + h], [f(x), f(x + h)], label='Forward Difference Approximation', color='green')

# Annotate the points
plt.text(x, f(x), f'($x$, $f(x)$)\n(1, 1)', fontsize=12, ha='right')
plt.text(x + h, f(x + h), f'($x + h$, $f(x + h)$)\n(1.1, 1.21)', fontsize=12, ha='left')

plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('Forward Difference Method for $f(x) = x^2$')
plt.legend()
plt.grid(True)
plt.show()
