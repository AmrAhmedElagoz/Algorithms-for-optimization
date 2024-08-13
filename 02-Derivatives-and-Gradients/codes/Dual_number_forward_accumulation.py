import torch
import torch.nn as nn

# DualNumber class to track value and derivative
class DualNumber:
    def __init__(self, value, derivative):
        self.value = value
        self.derivative = derivative

    def __mul__(self, other):
        return DualNumber(self.value * other.value,
                          self.value * other.derivative + self.derivative * other.value)

    def __add__(self, other):
        return DualNumber(self.value + other.value,
                          self.derivative + other.derivative)

    def __sub__(self, other):
        return DualNumber(self.value - other.value,
                          self.derivative - other.derivative)

# Custom optimizer using forward accumulation
class ForwardAccumulationSGD:
    def __init__(self, parameters, lr=0.01):
        self.parameters = list(parameters)
        self.lr = lr

    def step(self):
        for param in self.parameters:
            param.data -= self.lr * param.grad

    def zero_grad(self):
        for param in self.parameters:
            if param.grad is not None:
                param.grad.zero_()

# Simple linear model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.w = nn.Parameter(torch.tensor(1.0))
        self.b = nn.Parameter(torch.tensor(0.0))

    def forward(self, x):
        # Use dual numbers to compute value and gradient simultaneously
        dual_x = DualNumber(x, 1.0)  # x as DualNumber with derivative 1
        dual_w = DualNumber(self.w, 0.0)  # w as DualNumber with derivative 0
        dual_b = DualNumber(self.b, 0.0)  # b as DualNumber with derivative 0

        dual_output = dual_w * dual_x + dual_b
        return dual_output

    def compute_loss(self, output, target):
        # Mean Squared Error (MSE) loss
        loss = (output.value - target)**2
        loss_grad = 2 * (output.value - target) * output.derivative
        return loss, loss_grad

# Training loop
def train():
    model = SimpleModel()
    optimizer = ForwardAccumulationSGD(model.parameters(), lr=0.01)

    inputs = torch.tensor(2.0)
    target = torch.tensor(4.0)

    for epoch in range(1000):
        optimizer.zero_grad()

        # Forward pass
        output = model(inputs)

        # Compute loss and gradients
        loss, grad = model.compute_loss(output, target)

        # Manually set gradients
        model.w.grad = torch.tensor(grad)
        model.b.grad = torch.tensor(grad)

        # Update weights
        optimizer.step()

        if epoch % 100 == 0:
            print(f'Epoch [{epoch}/1000], Loss: {loss:.4f}, w: {model.w.item():.4f}, b: {model.b.item():.4f}')

    # Test the model
    with torch.no_grad():
        test_input = torch.tensor(3.0)
        test_output = model(test_input)
        print(f'Prediction for input {test_input.item()}: {test_output.value:.4f}')

train()
