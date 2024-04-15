import math


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

def main():
    a, b = -1, 0
    eps = 0.001
    print("Корень уравнения:")
    print(f"Метод простой итерации: {simple_iteration_method(b, eps)}")
    print(f"Метод Ньютона: {newton_method(b, eps)}")

if __name__ == "__main__":
    main()