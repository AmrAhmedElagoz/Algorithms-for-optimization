1. **Exact Line Search**
   - Theory: For a quadratic function f(x) = x², the exact minimum along any direction can be found analytically by solving f'(x + αd) = 0 for α.
   - Implementation: In our code, we directly calculate α = -x₀/d.
   - Pros: Finds the exact minimum in one step.
   - Cons: Only possible for simple functions; computationally infeasible for most real-world problems.

2. **Backtracking Line Search**
   - Theory: Starts with a large step size and reduces it geometrically until the Armijo condition is satisfied:
     f(x + αd) ≤ f(x) + c₁α∇f(x)ᵀd
   - Implementation: We start with α = 1 and multiply by β (< 1) until the condition is met.
   - Pros: Simple, fast, and often effective in practice.
   - Cons: May not find the best step size; can be slow if the initial guess is far off.

3. **Wolfe Conditions**
   - Theory: Adds a curvature condition to ensure the gradient is sufficiently reduced:
     ∇f(x + αd)ᵀd ≥ c₂∇f(x)ᵀd
   - Implementation: Checks both Armijo and curvature conditions, adjusting step size up or down as needed.
   - Pros: Better convergence properties than backtracking alone.
   - Cons: More complex implementation; more function evaluations per iteration.

4. **Strong Wolfe Conditions**
   - Theory: Modifies the curvature condition to:
     |∇f(x + αd)ᵀd| ≤ c₂|∇f(x)ᵀd|
   - Implementation: Similar to regular Wolfe conditions but with stricter curvature check.
   - Pros: Ensures the gradient doesn't oscillate; better for certain optimization algorithms.
   - Cons: Most complex implementation; may require more iterations.

Key Differences in Practice:
1. **Number of Function Evaluations**
   - Exact: Always 1 (for our simple quadratic)
   - Backtracking: Usually fewer than Wolfe conditions
   - Wolfe and Strong Wolfe: Often require more evaluations but may lead to better steps

2. **Step Size Selection**
   - Exact: Perfect step size
   - Backtracking: May be conservative
   - Wolfe and Strong Wolfe: Usually better than backtracking, closer to exact

3. **Convergence Properties**
   - Exact: Immediate convergence for quadratic functions
   - Backtracking: May require more iterations in the overall optimization
   - Wolfe and Strong Wolfe: Generally better convergence properties

When to Use Each Method:
- Exact: When analytically possible and computationally feasible
- Backtracking: When simplicity and speed are priorities
- Wolfe: When better convergence properties are needed
- Strong Wolfe: When using methods like conjugate gradient that require more precise line searches