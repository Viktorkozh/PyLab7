#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(float, input().split()))
    a_modified = a
    # Если список пуст, завершить программу.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    count = 0
    # Определить индексы минимального и максимального элементов.
    for i, item in enumerate(a):
        if item == 0:
            i_zero = i
        if item > 0:
            count += 1
        if int(item) <= 1:
            poped = a_modified.pop(i)
            a_modified.insert(0, poped)

    a_cut = a[i_zero + 1:]
    S = 0
    for item in a_cut:
        S += item

    print("Kоличество положительных элементов списка: ", count)
    print("Cуммa элементов списка, расположенных после"
          " последнего элемента, равного нулю: ", 
          S
    )
    print(
        "Преобразованный список, где сначала располагаются все элементы, "
        "целая часть которых не превышает 1, а потом - все остальные: ",
        a_modified
    )
