import numpy as np
#http://elibrary.sgu.ru/uch_lit/1719.pdf
def func_Newton(x, y):
    return np.array([
        x**2/4 + y**2/9 - 1,
        y - x**(1/3)
    ])

def func_simple_iteration(x, y):
    return np.array([
        (1 - y ** 2 / 9) ** (1 / 2) * 2,
        x ** (1 / 3)
    ])

def J(x, y):
    return np.array([
        [x/2, 2*y/9],
        [-1/3*x**(-2/3), 1]
    ])


def newton_method(F, J, init_value, esp):
    x_prev = np.array(init_value)
    iterations = 0

    while True:
        delta_x = np.linalg.solve(J(*x_prev), F(*x_prev))
        x_next = x_prev - delta_x

        if np.linalg.norm(delta_x) < esp:
            break

        x_prev = x_next
        iterations += 1

    return x_next, iterations


def simple_iteration_method(init_value, esp):
    x_prev = np.array(init_value)
    iterations = 0
    x_next = func_simple_iteration(*x_prev)

    while np.linalg.norm(x_next - x_prev) >= esp:
        x_prev = x_next
        x_next = func_simple_iteration(*x_prev)
        iterations += 1

    return x_next, iterations


def main():
    init_value  = [1, 1]
    esp = 0.0001
    true_answer = np.array([1.826449209846151, 1.22236957941035])

    result_newton, iterations_newton = newton_method(func_Newton, J, init_value, esp)
    print("Метод Ньютона:")
    print("Решение:", result_newton)
    print("Количество итераций:", iterations_newton)
    print()
    result_simple_iteration, iterations_simple_iteration = simple_iteration_method(init_value, esp)
    print("Метод простых итераций:")
    print("Решение:", result_simple_iteration)
    print("Количество итераций:", iterations_simple_iteration)
    print()

    if iterations_newton > iterations_simple_iteration:
        print("Метод Ньютона совершил больше итераций, чем метод простых итераций")
    elif iterations_newton == iterations_simple_iteration:
        print("Метод Ньютона совершил столько же итераций, чем метод простых итераций")
    else:
        print("Метод простых итераций совершил больше итераций, чем метод Ньютона")

    calc_error_simple_iter = true_answer - result_simple_iteration
    calc_error_newton = true_answer - result_newton
    if abs(calc_error_simple_iter[0]) + abs(calc_error_simple_iter[1]) < abs(calc_error_newton[0]) + abs(calc_error_newton[1]):
        print("Метод Ньютона точнее")
    else:
        print("Метод простых итераций точнее")
if __name__ == "__main__":
    main()