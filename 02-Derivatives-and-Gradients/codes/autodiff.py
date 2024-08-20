# class Tensor:
#     def __init__(self, data, requires_grad=False):
#         self.data = data
#         self.requires_grad = requires_grad
#         self.grad = 0.0
#         self._backward = lambda: None
#         self._prev = set()

#     def backward(self):
#         topo = []
#         visited = set()

#         def build_topo(v):
#             if v not in visited:
#                 visited.add(v)
#                 for child in v._prev:
#                     build_topo(child)
#                 topo.append(v)

#         build_topo(self)
        
#         self.grad = 1.0
#         for v in reversed(topo):
#             v._backward()

#     def __repr__(self):
#         return f"Tensor(data={self.data}, requires_grad={self.requires_grad})"

#     def __add__(self, other):
#         other = other if isinstance(other, Tensor) else Tensor(other)
#         out = Tensor(self.data + other.data, requires_grad=self.requires_grad or other.requires_grad)

#         def _backward():
#             if self.requires_grad:
#                 self.grad += out.grad  # Accumulate gradient for self
#             if other.requires_grad:
#                 other.grad += out.grad  # Accumulate gradient for other

#         out._backward = _backward
#         out._prev = {self, other}
#         return out

#     def __mul__(self, other):
#         other = other if isinstance(other, Tensor) else Tensor(other)
#         out = Tensor(self.data * other.data, requires_grad=self.requires_grad or other.requires_grad)

#         def _backward():
#             if self.requires_grad:
#                 self.grad += other.data * out.grad  # Accumulate grad from multiplication
#             if other.requires_grad:
#                 other.grad += self.data * out.grad  # Accumulate grad from multiplication

#         out._backward = _backward
#         out._prev = {self, other}
#         return out

# # Example to test
# x = Tensor(2.0, requires_grad=True)
# y = Tensor(3.0, requires_grad=True)

# # Perform operations
# z = x * y + y

# # Trigger the backward pass
# z.backward()

# # Retrieve gradients
# print(f"x.grad: {x.grad}")  # Expected: 3.0
# print(f"y.grad: {y.grad}")  # Expected: 5.0
class Node:
    def __init__(self, value, children=None, operation=None):
        self.value = value
        self.grad = 0.0
        self.children = children or []
        self.operation = operation
        self.backward_fn = lambda: None

    def backward(self):
        self.backward_fn()

    def __repr__(self):
        return f"Node(value={self.value}, grad={self.grad})"
    
class ComputationGraph:
    def __init__(self):
        self.nodes = []

    def create_node(self, value, children=None, operation=None):
        node = Node(value, children, operation)
        self.nodes.append(node)
        return node

    def forward(self):
        for node in self.nodes:
            if node.operation:
                node.value = node.operation(*[child.value for child in node.children])

    def backward(self):
        self.nodes[-1].grad = 1.0
        for node in reversed(self.nodes):
            node.backward()

class ForwardAccumulationAD:
    def __init__(self, graph):
        self.graph = graph

    def differentiate(self, wrt_node):
        # Reset gradients
        for node in self.graph.nodes:
            node.grad = 0.0

        # Set the gradient of wrt_node to 1
        wrt_node.grad = 1.0

        # Forward pass
        for node in self.graph.nodes:
            if node.operation:
                node.value, node.grad = self._forward_diff(node)

        return self.graph.nodes[-1].grad

    def _forward_diff(self, node):
        if node.operation == add:
            return (
                node.children[0].value + node.children[1].value,
                node.children[0].grad + node.children[1].grad
            )
        elif node.operation == multiply:
            return (
                node.children[0].value * node.children[1].value,
                node.children[0].grad * node.children[1].value + node.children[0].value * node.children[1].grad
            )
        # Add more operations as needed

class ReverseAccumulationAD:
    def __init__(self, graph):
        self.graph = graph

    def differentiate(self):
        # Reset gradients
        for node in self.graph.nodes:
            node.grad = 0.0

        # Set up backward functions
        for node in self.graph.nodes:
            if node.operation == add:
                self._setup_add_backward(node)
            elif node.operation == multiply:
                self._setup_multiply_backward(node)
            # Add more operations as needed

        # Backward pass
        self.graph.backward()

    def _setup_add_backward(self, node):
        def _backward():
            node.children[0].grad += node.grad
            node.children[1].grad += node.grad
        node.backward_fn = _backward

    def _setup_multiply_backward(self, node):
        def _backward():
            node.children[0].grad += node.grad * node.children[1].value
            node.children[1].grad += node.grad * node.children[0].value
        node.backward_fn = _backward

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Create a computation graph
graph = ComputationGraph()

# Create nodes
x = graph.create_node(2.0)
y = graph.create_node(3.0)
z = graph.create_node(0.0, [x, y], add)
w = graph.create_node(0.0, [z, x], multiply)

# Forward pass
graph.forward()

# Perform forward accumulation differentiation
forward_ad = ForwardAccumulationAD(graph)
dx_forward = forward_ad.differentiate(x)
print(f"Forward AD - dw/dx: {dx_forward}")

# Perform reverse accumulation differentiation
reverse_ad = ReverseAccumulationAD(graph)
reverse_ad.differentiate()
print(f"Reverse AD - dw/dx: {x.grad}")
print(f"Reverse AD - dw/dy: {y.grad}")