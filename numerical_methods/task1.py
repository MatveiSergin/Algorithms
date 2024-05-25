import math

import numpy as np
from matplotlib import pyplot as plt


def func(x):
    return 4*x - math.cos(x) - 1


def bisection_method(a, b, epsilon):
    if func(a) * func(b) >= 0:
        return None

    while (b - a) >= epsilon:
        c = (a + b) / 2

        if func(c) == 0:
            break

        elif func(c) * func(a) > 0:
            a = c
        else:
            b = c


    x = (a + b) / 2

    return x

def draw_graph(a, b, eps):
    x_values = np.linspace(a, b, 1000)
    y_values = [func(x) for x in x_values]

    plt.plot(x_values, y_values, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    root = bisection_method(a, b, eps)
    if root is not None:
        plt.scatter(root, func(root), color='red', label='корень')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Решение уравнения')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    a = -10
    b = 10
    epsilon = 0.001
    x = bisection_method(a, b, epsilon)

    if x is not None:
        print(x)
        draw_graph(a, b, epsilon)
    else:
        print("Решений нет")


if '__main__' == __name__:
    main()