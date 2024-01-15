#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import numpy as np
import matplotlib.pyplot as plt

def GCD(a, b):
    gcd = 1
    for i in range(2, max(a, b)):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def GCDfast(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return GCDfast(a % b, b)
    else:
        return GCDfast(a, b % a)

def create_graph(b, c, d):
    x_ticks = np.linspace(b[0], b[-1], num=10)
    y_ticks = np.linspace(0, max(c+d), num=5)
    plt.plot(b, c)
    plt.plot(b, d)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.title("НОД")
    plt.xlabel("Второе число функции")
    plt.ylabel("Время работы алгоритма")
    plt.show()

if __name__ == '__main__':
    start = 300
    end = 600
    a = 420
    b = []; c = []; d = []

    print("GCD:")
    for i in range(start, end):
        b.append(i)
        time = sum(timeit.timeit(lambda: GCD(a, i), number=1) for j in range(500))
        s = time/500
        c.append(s)
        print("при i =", i, "число =", GCD(a, i), "время =", s)

    print("GCDfast:")
    for i in range(start, end):
        time = sum(timeit.timeit(lambda: GCDfast(a, i), number=1) for j in range(500))
        l = time/500
        d.append(l)
        print("при i =", i, "число =", GCDfast(a, i), "время =", l)

    create_graph(b, c, d)