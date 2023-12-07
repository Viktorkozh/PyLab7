#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # ввести список одной строкой.
    A = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) < 2:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    S = [item for item in A if item % 2 == 0]
    cnt = len(S)
    ans = sum(S)

    print("Сумма элементов кратных 2:", ans,
          "\nКоличество элементов кратных 2:", cnt)
