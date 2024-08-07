import numpy as np
import matplotlib.pyplot as plt

# Parameters
y0 = 1  # Initial condition
t0 = 0  # Initial time
T = 1   # Final time
h_explicit_small = 0.01  # Small step size for explicit Euler
h_explicit_large = 0.1   # Large step size for explicit Euler (demonstrates instability)
h_implicit = 0.1         # Step size for implicit Euler (larger step size)

# Time grids
t_explicit_small = np.arange(t0, T + h_explicit_small, h_explicit_small)
t_explicit_large = np.arange(t0, T + h_explicit_large, h_explicit_large)
t_implicit = np.arange(t0, T + h_implicit, h_implicit)

# Explicit Euler method with small step size
y_explicit_small = np.zeros_like(t_explicit_small)
y_explicit_small[0] = y0
for i in range(1, len(t_explicit_small)):
    y_explicit_small[i] = y_explicit_small[i-1] * (1 - 15 * h_explicit_small)

# Explicit Euler method with large step size
y_explicit_large = np.zeros_like(t_explicit_large)
y_explicit_large[0] = y0
for i in range(1, len(t_explicit_large)):
    y_explicit_large[i] = y_explicit_large[i-1] * (1 - 15 * h_explicit_large)

# Implicit Euler method
y_implicit = np.zeros_like(t_implicit)
y_implicit[0] = y0
for i in range(1, len(t_implicit)):
    y_implicit[i] = y_implicit[i-1] / (1 + 15 * h_implicit)

# Exact solution
t_exact = np.linspace(t0, T, 1000)
y_exact = y0 * np.exp(-15 * t_exact)

# Plotting the results
plt.plot(t_exact, y_exact, label='Exact Solution')
plt.plot(t_explicit_small, y_explicit_small, 'o-', label='Explicit Euler (small step size)')
plt.plot(t_explicit_large, y_explicit_large, 'x-', label='Explicit Euler (large step size, unstable)')
plt.plot(t_implicit, y_implicit, 's-', label='Implicit Euler')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.legend()
plt.title('Comparison of Explicit and Implicit Euler Methods')
plt.show()
