# import numpy as np
# import matplotlib.pyplot as plt
# from typing import Callable, Tuple

# class LineSearch:
#     def __init__(self, f: Callable[[float], float], df: Callable[[float], float]):
#         """
#         Initialize line search with objective function and its gradient.
        
#         Args:
#             f: Objective function f(x)
#             df: Gradient of objective function f'(x)
#         """
#         self.f = f
#         self.df = df
    
#     def exact(self, x0: float, direction: float) -> Tuple[float, int]:
#         """
#         Perform exact line search for quadratic function.
        
#         Args:
#             x0: Starting point
#             direction: Search direction
        
#         Returns:
#             Tuple of (optimal step size, number of function evaluations)
#         """
#         # For quadratic function, exact minimum is at x = 0
#         alpha = -x0 / direction
#         return alpha, 1
    
#     def backtracking(self, x0: float, direction: float, 
#                      alpha: float = 0.5, beta: float = 0.8,
#                      max_iter: int = 100) -> Tuple[float, int]:
#         """
#         Perform backtracking line search.
        
#         Args:
#             x0: Starting point
#             direction: Search direction
#             alpha: Sufficient decrease parameter
#             beta: Backtracking factor
#             max_iter: Maximum number of iterations
        
#         Returns:
#             Tuple of (step size, number of function evaluations)
#         """
#         t = 1.0
#         n_evals = 0
        
#         for _ in range(max_iter):
#             n_evals += 2  # One for f and one for df
#             if self.f(x0 + t * direction) <= self.f(x0) + alpha * t * self.df(x0) * direction:
#                 break
#             t *= beta
        
#         return t, n_evals
    
#     def wolfe(self, x0: float, direction: float,
#               c1: float = 1e-4, c2: float = 0.9,
#               max_iter: int = 100) -> Tuple[float, int]:
#         """
#         Perform line search with Wolfe conditions.
        
#         Args:
#             x0: Starting point
#             direction: Search direction
#             c1: Sufficient decrease parameter
#             c2: Curvature condition parameter
#             max_iter: Maximum number of iterations
        
#         Returns:
#             Tuple of (step size, number of function evaluations)
#         """
#         t = 1.0
#         n_evals = 0
        
#         for _ in range(max_iter):
#             n_evals += 2
#             x_new = x0 + t * direction
            
#             # Armijo condition (sufficient decrease)
#             if self.f(x_new) > self.f(x0) + c1 * t * self.df(x0) * direction:
#                 t *= 0.5
#                 continue
            
#             # Curvature condition
#             if self.df(x_new) * direction < c2 * self.df(x0) * direction:
#                 t *= 2.0
#                 continue
                
#             break
        
#         return t, n_evals
    
#     def strong_wolfe(self, x0: float, direction: float,
#                      c1: float = 1e-4, c2: float = 0.9,
#                      max_iter: int = 100) -> Tuple[float, int]:
#         """
#         Perform line search with strong Wolfe conditions.
        
#         Args:
#             x0: Starting point
#             direction: Search direction
#             c1: Sufficient decrease parameter
#             c2: Curvature condition parameter
#             max_iter: Maximum number of iterations
        
#         Returns:
#             Tuple of (step size, number of function evaluations)
#         """
#         t = 1.0
#         n_evals = 0
        
#         for _ in range(max_iter):
#             n_evals += 2
#             x_new = x0 + t * direction
            
#             # Armijo condition (sufficient decrease)
#             if self.f(x_new) > self.f(x0) + c1 * t * self.df(x0) * direction:
#                 t *= 0.5
#                 continue
            
#             # Strong curvature condition
#             if abs(self.df(x_new) * direction) > c2 * abs(self.df(x0) * direction):
#                 t *= 0.5
#                 continue
                
#             break
        
#         return t, n_evals

# def compare_line_searches():
#     # Define objective function and its gradient
#     f = lambda x: x**2  # f(x) = x^2
#     df = lambda x: 2*x   # f'(x) = 2x
    
#     # Initialize line search
#     ls = LineSearch(f, df)
    
#     # Starting point and direction
#     x0 = 1.5
#     direction = -1.0
    
#     # Compare methods
#     methods = {
#         'Exact': ls.exact,
#         'Backtracking': ls.backtracking,
#         'Wolfe': ls.wolfe,
#         'Strong Wolfe': ls.strong_wolfe
#     }
    
#     results = {}
#     for name, method in methods.items():
#         alpha, n_evals = method(x0, direction)
#         x_final = x0 + alpha * direction
#         results[name] = {
#             'step_size': alpha,
#             'final_x': x_final,
#             'final_f': f(x_final),
#             'n_evals': n_evals
#         }
    
#     # Plotting
#     x = np.linspace(-2, 2, 1000)
#     y = f(x)
    
#     plt.figure(figsize=(12, 8))
#     plt.plot(x, y, 'b-', label='f(x)')
#     plt.plot(x0, f(x0), 'ko', label='Starting point')
    
#     colors = ['r', 'g', 'm', 'c']
#     for (name, result), color in zip(results.items(), colors):
#         plt.plot(result['final_x'], result['final_f'], f'{color}o', label=f'{name} ({result["n_evals"]} evals)')
    
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.title('Comparison of Line Search Methods')
#     plt.legend()
#     plt.grid(True)
#     plt.show()
    
#     # Print detailed results
#     print("\nDetailed Results:")
#     print(f"{'Method':<15} {'Step Size':<12} {'Final x':<10} {'Final f(x)':<12} {'Evaluations'}")
#     print("-" * 60)
#     for name, result in results.items():
#         print(f"{name:<15} {result['step_size']:<12.6f} {result['final_x']:<10.6f} {result['final_f']:<12.6f} {result['n_evals']}")

# if __name__ == "__main__":
#     compare_line_searches()

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple

class LineSearch:
    def __init__(self, f: Callable[[float], float], df: Callable[[float], float]):
        self.f = f
        self.df = df
    
    def exact(self, x0: float, direction: float) -> Tuple[float, int]:
        """
        Perform "exact" line search for sine wave.
        Note: This is actually an approximation since true exact solution
        would require solving a transcendental equation.
        """
        # Find local minimum close to x0 using numerical optimization
        from scipy.optimize import minimize_scalar
        
        def f_along_line(alpha):
            return self.f(x0 + alpha * direction)
        
        result = minimize_scalar(f_along_line, bracket=[-np.pi, np.pi])
        return result.x, result.nfev
    
    def backtracking(self, x0: float, direction: float, 
                     alpha: float = 0.5, beta: float = 0.8,
                     max_iter: int = 100) -> Tuple[float, int]:
        t = 1.0
        n_evals = 0
        
        for _ in range(max_iter):
            n_evals += 2
            if self.f(x0 + t * direction) <= self.f(x0) + alpha * t * self.df(x0) * direction:
                break
            t *= beta
        
        return t, n_evals
    
    def wolfe(self, x0: float, direction: float,
              c1: float = 1e-4, c2: float = 0.9,
              max_iter: int = 100) -> Tuple[float, int]:
        t = 1.0
        n_evals = 0
        
        for _ in range(max_iter):
            n_evals += 2
            x_new = x0 + t * direction
            
            if self.f(x_new) > self.f(x0) + c1 * t * self.df(x0) * direction:
                t *= 0.5
                continue
            
            if self.df(x_new) * direction < c2 * self.df(x0) * direction:
                t *= 2.0
                continue
                
            break
        
        return t, n_evals
    
    def strong_wolfe(self, x0: float, direction: float,
                     c1: float = 1e-4, c2: float = 0.9,
                     max_iter: int = 100) -> Tuple[float, int]:
        t = 1.0
        n_evals = 0
        
        for _ in range(max_iter):
            n_evals += 2
            x_new = x0 + t * direction
            
            if self.f(x_new) > self.f(x0) + c1 * t * self.df(x0) * direction:
                t *= 0.5
                continue
            
            if abs(self.df(x_new) * direction) > c2 * abs(self.df(x0) * direction):
                t *= 0.5
                continue
                
            break
        
        return t, n_evals

def compare_line_searches():
    # Define sine wave objective function and its gradient
    f = lambda x: np.sin(x)        # f(x) = sin(x)
    df = lambda x: np.cos(x)       # f'(x) = cos(x)
    
    ls = LineSearch(f, df)
    
    # Starting point and direction
    x0 = 1.0  # Starting at x = 1
    direction = -1.0  # Moving in negative direction
    
    methods = {
        'Exact': ls.exact,
        'Backtracking': ls.backtracking,
        'Wolfe': ls.wolfe,
        'Strong Wolfe': ls.strong_wolfe
    }
    
    results = {}
    for name, method in methods.items():
        alpha, n_evals = method(x0, direction)
        x_final = x0 + alpha * direction
        results[name] = {
            'step_size': alpha,
            'final_x': x_final,
            'final_f': f(x_final),
            'n_evals': n_evals
        }
    
    # Plotting
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    y = f(x)
    
    plt.figure(figsize=(15, 10))
    plt.plot(x, y, 'b-', label='f(x) = sin(x)')
    plt.plot(x0, f(x0), 'ko', markersize=10, label='Starting point')
    
    colors = ['r', 'g', 'm', 'c']
    markers = ['o', 's', '^', 'D']
    for (name, result), color, marker in zip(results.items(), colors, markers):
        plt.plot(result['final_x'], result['final_f'], color=color, marker=marker, 
                 markersize=10, label=f'{name} ({result["n_evals"]} evals)')
    
    # Plot vertical lines to show movement
    for name, result in results.items():
        plt.vlines(result['final_x'], f(x0), result['final_f'], 
                   colors='gray', linestyles='dashed', alpha=0.3)
    
    plt.xlabel('x')
    plt.ylabel('f(x) = sin(x)')
    plt.title('Comparison of Line Search Methods on Sine Wave')
    plt.legend()
    plt.grid(True)
    
    # Add text annotations for each point
    for name, result in results.items():
        plt.annotate(f'x = {result["final_x"]:.3f}',
                     (result['final_x'], result['final_f']),
                     xytext=(10, 10), textcoords='offset points')
    
    plt.show()
    
    # Print detailed results
    print("\nDetailed Results:")
    print(f"{'Method':<15} {'Step Size':<12} {'Final x':<10} {'Final f(x)':<12} {'Evaluations'}")
    print("-" * 60)
    for name, result in results.items():
        print(f"{name:<15} {result['step_size']:<12.6f} {result['final_x']:<10.6f} {result['final_f']:<12.6f} {result['n_evals']}")

if __name__ == "__main__":
    compare_line_searches()