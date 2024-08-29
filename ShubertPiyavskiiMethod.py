import numpy as np
import matplotlib.pyplot as plt

def shubert_piyavskii(f, L, a, b, tol=1e-5, max_iter=100):
    # Initial bounds and points
    x_points = [a, b]
    f_points = [f(a), f(b)]
    
    for _ in range(max_iter):
        # Calculate midpoints and upper bounds
        midpoints = []
        upper_bounds = []
        for i in range(len(x_points) - 1):
            mid_x = (x_points[i] + x_points[i+1]) / 2
            mid_y = (f_points[i] + f_points[i+1]) / 2
            mid_y -= (L / 2) * (x_points[i+1] - x_points[i])
            
            midpoints.append(mid_x)
            upper_bounds.append(mid_y)
        
        # Find the point with the minimum upper bound
        min_upper_bound_index = np.argmin(upper_bounds)
        min_x = midpoints[min_upper_bound_index]
        min_f = f(min_x)
        
        # Insert the new point into the list
        x_points.insert(min_upper_bound_index + 1, min_x)
        f_points.insert(min_upper_bound_index + 1, min_f)
        
        # Check termination criteria
        if np.abs(x_points[-1] - x_points[0]) < tol:
            break
    
    # The minimum is at the point with the lowest function value
    min_index = np.argmin(f_points)
    return x_points[min_index], f_points[min_index]

# Example usage
def example_function(x):
    return np.sin(3*x) + 0.5*np.sin(5*x)

# Lipschitz constant (estimated)
L = 10

# Search interval [a, b]
a, b = 0, 2*np.pi

# Find minimum
min_x, min_f = shubert_piyavskii(example_function, L, a, b)

# Plotting
x = np.linspace(a, b, 500)
y = example_function(x)

plt.plot(x, y, label='f(x)')
plt.plot(min_x, min_f, 'ro', label='Minimum')
plt.legend()
plt.show()

print(f"Minimum found at x = {min_x}, f(x) = {min_f}")
