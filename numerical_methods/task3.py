def zero_approximation(a, b):
    x = [0] * len(b)
    for i in range(len(b)):
        x[i] = b[i] / a[i][i]
    return x

def find_other_indexes(ind, n): #Возращает массив индексов, которые подставляются в формулу
    return [i for i in range(n) if i != ind]

def reduction_of_equation(a, b): #приведение уравнений к виду x = B * x + g
    length = len(b)
    a1 = [ [] for i in range(length)]
    b1 = [0] * length
    for i in range(length):
        for j in find_other_indexes(i, length):
            a1[i].append(-a[i][j])
        a1[i].append(b[i])
        b1[i] = a[i][i]
    return a1, b1

#https://www.youtube.com/watch?v=4s9GxRY_DNM&t=494s
def method_simple_iteration(a, b, eps):
    length = len(b)
    x0 = zero_approximation(a, b)
    a1, b1 = reduction_of_equation(a, b)

    x1 = [0] * length
    for i in range(length):
        x1[i] = 0
        for ind, val in enumerate(find_other_indexes(i, length)):
            x1[i] += a1[i][ind] * x0[val]
        x1[i] += a1[i][-1] #добавляю свободный член
        x1[i] = x1[i]/b1[i] #делю на коэф данного x

    while any((abs(x1[i] - x0[i]) / abs(x1[i])) >= eps for i in range(length)):
        x0 = x1.copy()
        for i in range(length):
            x1[i] = 0
            for ind, val in enumerate(find_other_indexes(i, length)):
                x1[i] += a1[i][ind] * x0[val]
            x1[i] += a1[i][-1]
            x1[i] = x1[i] / b1[i]

    return x1

#https://www.youtube.com/watch?v=NAUT7IdvjXI&t=104s
def method_zeidel(a, b, eps):
    length = len(b)
    x0 = zero_approximation(a, b)
    a1, b1 = reduction_of_equation(a, b)

    x1 = [0] * length
    for i in range(length):
        x1[i] = 0
        for ind, val in enumerate(find_other_indexes(i, length)):
            if i < val:
                x1[i] += a1[i][ind] * x0[val]
            else:
                x1[i] += a1[i][ind] * x1[val]
        x1[i] += a1[i][-1]
        x1[i] = x1[i]/b1[i]

    while any((abs(x1[i] - x0[i]) / abs(x1[i])) >= eps for i in range(length)):
        x0 = x1.copy()
        for i in range(length):
            x1[i] = 0
            for ind, val in enumerate(find_other_indexes(i, length)):
                x1[i] += a1[i][ind] * x0[val]
            x1[i] += a1[i][-1]
            x1[i] = x1[i] / b1[i]

    return x1

def main():
    a = [ #матрица приведена к диагональному преобладанию
        [5, -3, -2],
        [1.5, -5, 2],
        [1, 1, -4]
    ]
    b = [3, 2, -5]
    print(method_simple_iteration(a, b, eps=0.001))
    print(method_zeidel(a, b, eps=0.001))


if __name__ == '__main__':
    main()