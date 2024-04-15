import math
import numpy as np
import matplotlib.pyplot as plt
def sec(x):
    return 1 / math.cos(x)
def f(x, y):
    return sec(x) + y * math.tan(x)

def analitic_result_func(x):
    return x / (math.cos(x))

def create_rungeKutta(x0, y0, h):
    def rungeKutta(x):
        n = int((x - x0) / h)
        x1 = x0
        y1 = y0
        for i in range(1, n + 1):
            k1 = h * f(x1, y1)
            k2 = h * f(x1 + 0.5 * h, y1 + 0.5 * k1)
            k3 = h * f(x1 + 0.5 * h, y1 + 0.5 * k2)
            k4 = h * f(x1 + h, y1 + k3)

            y1 += (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            x1 += h
        return y1
    return rungeKutta

#https://masters.donntu.ru/2013/fknt/vodolazskiy/library/nummethod_book_chapter4-1%20Athor%20-%20Alexey%20Skobelev.pdf
def create_Kashi_Euler(x0, y0, h):
    def Kashi_Euler(x):
        x1 = x0
        y1 = y0
        while x1 < x:
            y1 += 0.5 * (h * f(x1, y1) + h * f(x1 + h, y1 + h * f(x1, y1)))
            x1 += h
        return y1

    return Kashi_Euler

def get_graph(x_values, y_values, label="", color="black"):
    plt.plot(x_values, y_values, color=color, label=label)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

def show_graph():
    plt.show()

def get_values_for_graph(func, x_start, x_end):
    x_values = np.linspace(x_start, x_end, 100)
    y_values = []
    for x in x_values:
        y_values.append(func(x))

    return x_values, y_values



def main():
    x0 = 0
    y0 = 0
    x_start = 0
    x_end = 1.5
    h = 0.1

    kashi_euler = create_Kashi_Euler(x0, y0, h)
    result_for_kashi_euler = get_values_for_graph(kashi_euler, x_start, x_end)


    rungeKutta = create_rungeKutta(x0, y0, h)
    result_for_rungeKetta = get_values_for_graph(rungeKutta, x_start, x_end)

    result_for_analitic = get_values_for_graph(analitic_result_func, x_start, x_end)

    plt.figure(figsize=(10, 10))
    get_graph(*result_for_kashi_euler, label="Каши Эйлер", color="red")
    get_graph(*result_for_rungeKetta, label="Рунге-Кутта 4-го порядка", color="green")
    get_graph(*result_for_analitic, label='Аналитическое решение', color="blue")

    show_graph()
if __name__ == '__main__':
    main()