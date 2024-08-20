# Derivative

Here we are discussing derivatives and their generalization to multiple dimensions. 

Derivatives are used in many algorithms to inform the choice of direction of the search for an optimum. 

Often derivatives are not known analytically, and so we discuss how to estimate them numerically and using automatic differentiation techniques.

The derivative $f'(x)$ of a function f of a single variable $x$ is the rate at which the value of $f$ changes at $x$.

<div style="text-align: center;">
    <img src="..\assets\FIG1.jpg" alt="Derivative" width="300">
</div>

# Understanding the Gradient
We can use the derivative to provide a linear approximation (tangent line approximation) of the fucntion near $x$: $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$

The derivative is the ratio between the changes in $f$ and the change in $x$ at the point $x$:
$f'(x) = \frac{\Delta f(x)}{\Delta x}$

which is the change in $f(x)$ divided by the change in $x$ as the step $h$ becomes infinitely small:
<div style="text-align: center;">
    <img src="..\assets\FIG2.png" alt="Derivative" width="1000">
</div>

## Single Variable vs. Multiple Variables

- **Single Variable**:
  - In single-variable calculus, the derivative of a function $f(x)$ tells us the slope of the tangent line to the function at a point. It indicates how the function value changes as $x$ changes.
- **Multiple Variables**:
  - In multiple variables, the gradient is a generalization of the derivative. It tells us how the function value changes as any of the input variables change.

### Gradient: A Vector of Slopes

- **Definition**: For a function $f(x_1, x_2, \ldots, x_n)$, the gradient is a vector that contains all the partial derivatives (slopes) of the function with respect to each variable. If $\mathbf{x} = (x_1, x_2, \ldots, x_n)$, then the gradient is:
  $\nabla f(\mathbf{x}) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n} \right)$

### What Does the Gradient Tell Us?

1. **Direction of Steepest Ascent**:
   - The gradient vector points in the direction where the function increases the fastest.
   - If you want to increase the function value quickly, move in the direction of the gradient.

2. **Magnitude (Length) of the Gradient**:
   - The length of the gradient vector indicates how steep the slope is in that direction. A longer gradient vector means a steeper slope.

### Simple Example

Consider a function $f(x, y) = x^2 + y^2$.

1. **Calculate the Gradient**:
   - The partial derivative with respect to $x$ is $\frac{\partial f}{\partial x} = 2x$.
   - The partial derivative with respect to $y$ is $\frac{\partial f}{\partial y} = 2y$.
   - So, the gradient is $\nabla f(x, y) = (2x, 2y)$.

2. **Interpret the Gradient**:
   - At the point $(1, 1)$, the gradient is $\nabla f(1, 1) = (2, 2)$.
   - This means that if you move in the direction of $(2, 2)$ from the point $(1, 1)$, the function $f(x, y)$ will increase most rapidly.

### Using the Gradient

- **Predicting Small Changes**: If you take a small step $\Delta \mathbf{x}$ from a point $\mathbf{x}$, the change in the function $f$ can be approximated as:
  $f(\mathbf{x} + \Delta \mathbf{x}) \approx f(\mathbf{x}) + \nabla f(\mathbf{x}) \cdot \Delta \mathbf{x}$
  - Here, $\nabla f(\mathbf{x}) \cdot \Delta \mathbf{x}$ is the dot product, telling you how much the function will change in the direction of $\Delta \mathbf{x}$.

## Notes

- The gradient is like a compass that points in the direction where the function increases the fastest.
- It is a vector of partial derivatives, showing how the function changes with each variable.
- The length of the gradient vector indicates how steep the slope is.
- Use the gradient to predict changes in the function for small steps in any direction.

In essence, the gradient helps you understand the "slope" of a function in multiple dimensions, guiding you in the direction of the steepest ascent.

## Derivatives in Multiple Dimensions

The Hessian of a multivariate function is a matrix containing all of the second
derivatives with respect to the input. 

The second derivatives capture information about the local curvature of the function.

In optimization, the goal is often to find the minimum or maximum of a function $f(x)$. For functions of multiple variables, the behavior near critical points (where the gradient $\nabla f(x)=0$) is crucial. The Hessian matrix, which contains all the second-order partial derivatives of $f$, provides information about the curvature of the function around these critical points.

The Hessian matrix $H(\mathbf{x})$ of a function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is defined as:

$H(\mathbf{x})$ = $\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}$

# Compute the Derivative

Computing derivatives is a fundamental concept in calculus, and there are several methods used to compute them, depending on the context and the function in question. 

## 1. Analytical Differentiation (Symbolic Differentiation)
Analytical differentiation involves applying calculus rules to obtain an exact expression for the derivative. This method is suitable for functions that can be expressed explicitly and manipulated algebraically.

- **Power Rule**: $\frac{d}{dx}x^n = nx^{n-1}$
- **Product Rule**: $\frac{d}{dx}[u(x) \cdot v(x)] = u'(x) \cdot v(x) + u(x) \cdot v'(x)$
- **Quotient Rule**: $\frac{d}{dx}\left[\frac{u(x)}{v(x)}\right] = \frac{u'(x) \cdot v(x) - u(x) \cdot v'(x)}{v(x)^2}$
- **Chain Rule**: $\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$

Analytical differentiation provides exact results, but it can become complex when dealing with higher-order derivatives or intricate functions.

### Use Cases:

- Mathematical Analysis: When an explicit expression of the function is known, and exact derivatives are required.

- Theoretical Work: In fields like physics, engineering, and economics, where precise analytical expressions are necessary for further theoretical development.

- Computer Algebra Systems: Used in software like Mathematica, Maple, or SymPy for symbolic computation.

### Advantages:
- Exact Results: Provides precise and exact derivatives, which are essential for rigorous mathematical proofs and theoretical work.

- No Approximation Errors: Unlike numerical methods, there are no errors due to approximation.

### Disadvantages:
- Complexity: For complex functions, especially those involving many variables or higher-order derivatives, the expressions can become extremely complicated.

- Not Always Feasible: Some functions cannot be differentiated analytically (e.g., those involving special functions or implicit definitions).

## 2. Numerical Differentiation
The process of estimating derivatives numerically is referred to as numerical differentiation. Estimates can be derived in different ways from function evaluations.

Numerical differentiation is used when an analytical solution is difficult to obtain or when the function is known only at discrete points. It approximates the derivative using finite differences.

- **Finite Difference Method**: Approximates the derivative using discrete data points.
  - **Forward Difference**: $\frac{f(x+h) - f(x)}{h}$
  - **Backward Difference**: $\frac{f(x) - f(x-h)}{h}$
  - **Central Difference**: $\frac{f(x+h) - f(x-h)}{2h}$
- **Higher-order Approximations**: Involve more terms for better accuracy.

### Finite Difference Method
As the name implies, finite difference methods compute the difference between two values that differ by a finite step size. They approximate the derivative definitions using small differences:
<div style="text-align: center;">
    <img src="..\assets\EQ1.png" alt="Mathematically, the smaller the step size h, the better the derivative estimate" width="1000">
</div>


### Use Cases:
- Scientific Computing: Where functions are known only at discrete points (e.g., experimental data) or are too complex for analytical differentiation.

- Engineering Applications: Common in simulations where only sampled data is available, such as in finite element analysis.

- Real-time Systems: Used when quick approximations are needed, and exact derivatives are not crucial.

### Advantages:
- Simplicity: Easy to implement, especially when dealing with discrete data or when the function is not known analytically.

- Applicability: Can be used for any function, regardless of complexity, as long as data points are available.

- Flexibility: Useful for functions that are piecewise or defined by a set of discrete data.

### Disadvantages:

- Approximation Errors: Numerical methods introduce truncation and round-off errors, which can accumulate, especially for higher-order derivatives.

- Accuracy Depends on Step Size: Smaller step sizes improve accuracy but can also increase computational cost and the risk of numerical instability.

- Limited Precision: May not be suitable for problems requiring very high precision.

### Complex step
Which is a powerful technique to compute derivatives with high accuracy while avoiding the issue of subtractive cancellation that plagues traditional finite difference methods.

#### How the Complex Step Method Works

The key idea behind the complex step method is to use a complex step instead of a real step to compute the derivative. This method takes advantage of the fact that in complex arithmetic, the imaginary part can be isolated without the subtraction that causes cancellation errors.

For a given function $f(x)$, the derivative at a point $x$ can be approximated using the complex step method as:
<div style="text-align: center;">
    <img src="..\assets\EQ2.png" alt="EQ2" width="300">
</div>

### 3. Automatic Differentiation (Autodiff)

Automatic differentiation is a computational technique used in machine learning and scientific computing. It computes derivatives efficiently and accurately by breaking down complex functions into a sequence of elementary operations.

- **Forward Mode**: Computes derivatives alongside function evaluation by propagating the derivative information through each operation. It's efficient when the number of inputs is small compared to the number of outputs. for example, it's useful in evaluating gradients for optimization problems with fewer variables.

- How it Works
  - Initialization: Start with the input variable for which you want the derivative. Initialize the derivative of this variable to 1 and all others to 0.

  - Propagation: As you evaluate the function step by step, propagate the derivative information using the chain rule.

  - Final Derivative: The final value gives the derivative of the output with respect to the chosen input variable.

- **Reverse Mode**: Computes derivatives by first evaluating the function and then propagating the derivatives backward from the output to the inputs. This is the basis for backpropagation in neural networks it's ideal for scenarios where there are many inputs and a single output, such as in training deep learning models.

- How it Works
  - Initialization: Start by evaluating the function, keeping track of all intermediate results.

  - Backward Propagation: After the forward pass, initialize the derivative of the output with respect to itself to 1. Then propagate this derivative information backward to all input variables using the chain rule.

  - Final Derivatives: The final values give the derivatives of the output with respect to each input variable.

Autodiff provides exact derivatives up to machine precision and is automated, requiring no manual derivative calculations.

### Use Cases:
- Machine Learning: Essential in training neural networks where gradients are required for optimization (backpropagation).

- Scientific Computing: Used in optimization problems where gradients need to be computed repeatedly.

- Robotics and Control Systems: For real-time applications where derivatives of functions governing the system dynamics are needed.

### Advantages:
- Efficiency: Combines the accuracy of analytical differentiation with the flexibility of numerical differentiation, offering precise derivatives with minimal computational overhead.

- Automation: Automatically handles complex functions, including those with loops and conditionals, without needing manual intervention.

- Scalability: Scales well for large, complex functions, making it ideal for high-dimensional problems.

### Disadvantages:
- Complex Implementation: While automatic differentiation is highly efficient, it can be complex to implement from scratch. However, many libraries like TensorFlow, PyTorch, and JAX offer built-in support.

- Memory Consumption: Reverse mode autodiff, in particular, can consume a lot of memory, especially for large computational graphs.