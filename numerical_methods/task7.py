import math

#https://www.articleshub.net/2023/05/metod-pryamougolnikov-python.html
def rectangle_method(f, a, b, eps):
    n = int(1 / eps)
    h = (b - a) / n
    s = 0
    x = a
    for i in range(n):
        s += f(x)
        x += h
    result = s * h
    degree_of_rounding = abs(int(math.log(eps, 10)))
    result = round(result, degree_of_rounding)
    return result

#https://zaochnik.com/spravochnik/matematika/integraly-integrirovanie/metod-simpsona-parabol/
#https://www.articleshub.net/2023/05/metod-simpsona-python.html
def simpson_method(f, a, b, eps):
    n = int(1 / eps)
    h = (b - a) / n
    result = f(a)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)

    result += f(b)
    result *= h / 3
    degree_of_rounding = abs(int(math.log(eps, 10)))
    result = round(result, degree_of_rounding)
    return result

#https://zaochnik.com/spravochnik/matematika/integraly-integrirovanie/metod-trapetsij/
#https://www.articleshub.net/2023/05/metod-trapetsii-python_1.html
def trapezoid_method(f, a, b, eps):
    n = int(1 / eps)
    h = (b - a) / n
    result = f(a)

    for i in range(1, n):
        result += 2 * f(a + i * h)

    result += f(b)
    result *= h / 2
    degree_of_rounding = abs(int(math.log(eps, 10)))
    result = round(result, degree_of_rounding)
    return result

def f(x):
    return (math.tan(x) ** 2) / (x ** 2 + 1)

def main():
    a = 0.2
    b = 1
    eps = 0.0001
    res1 = rectangle_method(f, a, b, eps)
    res2 = trapezoid_method(f, a, b, eps)
    res3 = simpson_method(f, a, b, eps)
    print(f"Метод треугольника: {res1}")
    print(f"Метод трацпеции: {res2}")
    print(f"Метод Симпсона: {res3}")


if __name__ == '__main__':
    main()