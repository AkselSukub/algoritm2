#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import numpy as np
import matplotlib.pyplot as plt

def fibonachi(n):
    if n <= 1:
        return n
    else:
        return fibonachi(n-1) + fibonachi(n-2)

def fibonachifast(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

def create_graph(a, b, c):            
    y_ticks = np.linspace(0, max(b+c), num=5)
    plt.plot(a, b)
    plt.plot(a, c)
    plt.xticks(a)
    plt.yticks(y_ticks)
    plt.title("Фибоначчи")
    plt.xlabel("Номер числа Фибоначчи")
    plt.ylabel("Время работы алгоритма")
    plt.show()

if __name__ == '__main__':  
    N = 15
    a = []; b = []; c = []

    print("fibonachi:")
    for i in range(1, N):
        a.append(i)
        time = sum(timeit.timeit(lambda: fibonachi(i), number=1) for j in range(10000))
        s = time/10000
        b.append(s)
        print("при i =", i, "число =", fibonachi(i), "время =", s)

    print("fibonachifast:")
    for i in range(1, N):
        time = sum(timeit.timeit(lambda: fibonachifast(i), number=1) for j in range(10000))
        l = time/10000
        c.append(l)
        print("при i =", i, "число =", fibonachifast(i), "время =", l)

    create_graph(a, b, c)