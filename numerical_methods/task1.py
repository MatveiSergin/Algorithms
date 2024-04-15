import math


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

def main():
    a = 1
    b = 2
    epsilon = 0.001
    x = bisection_method(a, b, epsilon)

    if x is not None:
        print(x)
    else:
        print("Решений нет")


if '__main__' == __name__:
    main()