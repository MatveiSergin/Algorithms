#https://pro-prof.com/forums/topic/sweep-method-for-solving-systems-of-linear-algebraic-equations

import numpy as np

def get_diagonales(A): #Разделим матрицу A на верхнюю (с), главную (b) и нижнюю диагональ (a)
    a = np.zeros((len(A[0])))
    b = np.zeros((len(A[0])))
    c = np.zeros((len(A[0])))
    ind = 0
    for string in A:
        if 0 <= (ind-1) <= len(string) - 1:
            a[ind] = string[ind-1]
        b[ind] = string[ind]
        if 0 <= (ind+1) <= len(string) - 1:
            c[ind] = string[ind+1]
        ind += 1
    return a, b, c

def thomas_algorithm(A, B): #метод прогонки
    a, b, c = get_diagonales(A)
    d = B
    n = len(d)

    alpha = np.zeros(n - 1)
    betta = np.zeros(n)
    y = b[0]
    alpha[0] = -c[0] / y
    betta[0] = d[0] / y

    for i in range(1, n - 1):
        y = (b[i] + a[i] * alpha[i - 1])
        alpha[i] = -c[i] / y

    for i in range(1, n):
        y = (b[i] + a[i] * alpha[i - 1])
        betta[i] = (d[i] - a[i] * betta[i - 1]) / y

    x = np.zeros(n)  # Обратный ход
    x[-1] = betta[-1]

    for i in range(n - 2, -1, -1):
        x[i] = betta[i] + alpha[i] * x[i + 1]

    return x


def main():
    A = np.array([
        [18, -9, 0, 0, 0],
        [2, -9, -4, 0, 0],
        [0, -9, 21, -8, 0],
        [0, 0, -4, -10, 5],
        [0, 0, 0, 7, 12]
    ])

    B = np.array([-81, 71, -39, 64, 3])
    x = thomas_algorithm(A, B)
    print(x)

if __name__ == '__main__':
    main()

