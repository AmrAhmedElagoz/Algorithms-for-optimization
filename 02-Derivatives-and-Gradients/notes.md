# Derivative

Here we are discussing derivatives and their generalization to multiple dimensions. 

Derivatives are used in many algorithms to inform the choice of direction of the search for an optimum. 

Often derivatives are not known analytically, and so we discuss how to estimate them numerically and using automatic differentiation techniques.

The derivative $f'(x)$ of a function f of a single variable $x$ is the rate at which the value of $f$ changes at $x$.

<div style="text-align: center;">
    <img src="..\assets\FIG1.jpg" alt="Derivative" width="300">
</div>

# Understanding the Gradient
We can use the derivative to provide a linear approximation of the fucntion near $x$: $f(x + \Delta x) \approx f(x) + f'(x) \Delta x$

The derivative is the ratio between the changes in $f$ and the change in $x$ at the point $x$:
$f'(x) = \frac{\Delta f(x)}{\Delta x}$

which is the change in $f(x)$ divided by the change in $x$ as the step $h$ becomes infinitely small:
![derivative](..\assets\FIG2.png)

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

The Hessian matrix $H(\mathbf{x})$ of a function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is defined as:

$H(\mathbf{x})$ = $\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}$

#  Numerical Differentiation
The process of estimating derivatives numerically is referred to as numerical differentiation. Estimates can be derived in different ways from function evaluations.

## Finite difference method
As the name implies, finite difference methods compute the difference between two values that differ by a finite step size. They approximate the derivative definitions using small differences:
![Mathematically, the smaller the step size h, the better the derivative estimate.](..\assets\EQ1.png)

## Complex step
Which is a powerful technique to compute derivatives with high accuracy while avoiding the issue of subtractive cancellation that plagues traditional finite difference methods.

### How the Complex Step Method Works

The key idea behind the complex step method is to use a complex step instead of a real step to compute the derivative. This method takes advantage of the fact that in complex arithmetic, the imaginary part can be isolated without the subtraction that causes cancellation errors.

For a given function $f(x)$, the derivative at a point $x$ can be approximated using the complex step method as:
![EQ](..\assets\EQ2.png)
