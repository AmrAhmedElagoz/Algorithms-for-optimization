import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Example quadratic function: f(x) = (x - 2)^2 + 1
    return (x - 2)**2 + 1

def quadratic_fit_search(f, a, b, c, n):
    ya, yb, yc = f(a), f(b), f(c)
    plots = []

    for i in range(n):
        # Calculate the minimum of the quadratic fit
        x = 0.5 * ((ya*(b**2 - c**2) + yb*(c**2 - a**2) + yc*(a**2 - b**2)) /
                   (ya*(b - c) + yb*(c - a) + yc*(a - b)))
        
        yx = f(x)
        plots.append((a, b, c, x, ya, yb, yc, yx))
        
        if x > b:
            if yx > yb:
                c, yc = x, yx
            else:
                a, ya, b, yb = b, yb, x, yx
        elif x < b:
            if yx > yb:
                a, ya = x, yx
            else:
                c, yc, b, yb = b, yb, x, yx

    return a, b, c, plots

def plot_quadratic_search(plots, f):
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    for i, (a, b, c, x, ya, yb, yc, yx) in enumerate(plots[:4]):  # Plot first 4 iterations
        ax = axs[i]
        X = np.linspace(min(a, x) - 0.5, max(c, x) + 0.5, 100)
        Y = f(X)
        ax.plot(X, Y, 'b-')
        
        # Plot the points a, b, c
        ax.plot([a, b, c], [ya, yb, yc], 'ko')
        ax.plot(x, yx, 'ro')
        
        ax.set_title(f"Iteration {i+1}")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        
    plt.tight_layout()
    plt.show()

# Initial bracketing points
a, b, c = 0, 3, 4

# Number of iterations
n = 4

# Run the quadratic fit search
a, b, c, plots = quadratic_fit_search(f, a, b, c, n)

# Plot the results
plot_quadratic_search(plots, f)

print(f"Final bracketing interval: a={a:.4f}, b={b:.4f}, c={c:.4f}")
print(f"Best solution found: x = {b:.4f}, f(x) = {f(b):.4f}")