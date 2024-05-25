import math

import numpy as np
from matplotlib import pyplot as plt


def func(x):
    return 3 * math.exp(x) + 5*x + 1

def equivalent_func(x):
    return -1/5 - 3/5 * math.exp(x)

def derivative_function(x):
    return 3 * math.exp(x) + 5


def simple_iteration_method(x0, eps):
    x1 = equivalent_func(x0)

    while abs(x1 - x0) >= eps:
        x0 = x1
        x1 = equivalent_func(x0)
    return x1


def newton_method(x0, eps):
    x1 = x0 - func(x0) / derivative_function(x0)

    while abs(x1 - x0) >= eps:
        x0 = x1
        x1 = x0 - func(x0) / derivative_function(x0)

    return x1
def draw_graph(a, b, root1, root2):
    x_values = np.linspace(a, b, 1000)
    y_values = [func(x) for x in x_values]

    plt.plot(x_values, y_values, label='f(x)')

    plt.scatter(root1, func(root1), color='red', label='Решение методом простой итерации')
    plt.scatter(root2, func(root2), color='blue', label='Решение методом Ньютона')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Решение уравнения')
    plt.legend()
    plt.grid(True)
    plt.show()
def main():
    a, b = -2, 0
    eps = 0.001
    root1 = simple_iteration_method(b, eps)
    root2 = newton_method(b, eps)
    print("Корень уравнения:")
    print(f"Метод простой итерации: {root1}")
    print(f"Метод Ньютона: {root2}")
    draw_graph(a, b, root1, root2)
if __name__ == "__main__":
    main()