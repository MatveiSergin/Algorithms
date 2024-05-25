import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def linear_func(x, k, b):
    return k * x + b

def quadratic_func(x, a2, a1, a0):
    return a2 * x**2 + a1 * x + a0

def regression(func, x, y):
    params, array = curve_fit(func, x, y)
    return params

def create_basic_polynomial(x_values, i):
    def basic_polynomial(x):
        divider = 1
        result = 1
        for j in range(len(x_values)):
            if j != i:
                result *= (x-x_values[j])
                divider *= (x_values[i]-x_values[j])
        return result/divider
    return basic_polynomial

#https://www.youtube.com/watch?v=hE2Nz0PgV_o
#https://www.youtube.com/watch?v=nj2RBZ6xFeY
def create_Lagrange_polynomial(x_values, y_values):
    basic_polynomials = []
    for i in range(len(x_values)):
        basic_polynomials.append(create_basic_polynomial(x_values, i))

    def Lagrange_polynomial(x):
        result = 0
        for i in range(len(y_values)):
            result += y_values[i]*basic_polynomials[i](x)
        return result
    return Lagrange_polynomial

def create_divided_difference(x_values, y_values, k):
    result = 0
    for j in range(k + 1):
        mul = 1
        for i in range(k + 1):
            if i != j:
                mul *= x_values[j] - x_values[i]
        result += y_values[j]/mul
    return result

#https://www.youtube.com/watch?v=Bi4KzPGtdQU
def create_Newton_polynomial(x_values, y_values):
    divided_differences = []
    for i in range(1, len(x_values)):
        divided_differences.append(create_divided_difference(x_values, y_values, i))

    def Newton_polynomial(x):
        result = y_values[0]
        for k in range(1, len(y_values)):
            mul = 1
            for j in range(k):
                mul *= (x-x_values[j])
            result += divided_differences[k-1]*mul
        return result
    return Newton_polynomial

def plot_functions_graph(func1, func2, x_values, y_values, params1, params2):
    plt.figure(figsize=(10, 10))
    plt.scatter(x_values, y_values, color='red', label='Исходные точки')

    discrete_x_values = np.linspace(min(x_values), max(x_values), 100)
    discrete_func1_values = [func1(x) for x in discrete_x_values]
    discrete_func2_values = [func2(x) for x in discrete_x_values]
    plt.plot(discrete_x_values, discrete_func1_values, color='blue', label="Полином Лагранжа")
    plt.plot(discrete_x_values, discrete_func2_values, color='green', label="Полином Ньютона")
    draw_regression(params1, params2, x_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Полиномы Лагранжа и Ньютона')
    plt.legend()
    plt.grid(True)
    plt.show()

def draw_regression(params1, params2, X):
    x_values = np.linspace(min(X), max(X), 1000)
    y_values1 = [linear_func(x, *params1) for x in x_values]
    y_values2 = [quadratic_func(x, *params2) for x in x_values]

    plt.plot(x_values, y_values1, color='orange', label="Линейная регрессия")
    plt.plot(x_values, y_values2, color='pink', label="Квадратичная регрессия")


def main():
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [0.1, 0.15, 0.3, 0.4, 0.45, 0.55, 0.65, 0.75, 0.9, 1]

    linal_regression = regression(linear_func, X, Y)
    quadratic_regression = regression(quadratic_func, X, Y)
    print("Линейная регрессия: ", linal_regression)
    print("Квадратичная регрессия:", quadratic_regression)

    Lagrange_polynomial = create_Lagrange_polynomial(X, Y)
    Newton_polynomial = create_Newton_polynomial(X, Y)

    plot_functions_graph(Lagrange_polynomial, Newton_polynomial, X, Y, linal_regression, quadratic_regression)

if __name__ == "__main__":
    main()
