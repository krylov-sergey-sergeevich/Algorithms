"""
Наибольшая общая подпоследовательность.
Сложность: O(n * m)
A = b, a, c, c, b, c, a
B = a, b, c, a, b, a, a, c
result = b, c, b, c

Функция: пусть data[i,j] = Длина НОП для A[:i] и B[:j]
Результат: data(n, m) - ?
Ответ тривиален когда у нас длина одной из последовательностей равна 0 или 1.
data[0, j] = data[i, 0] = 0
"""
from typing import Tuple


def gcs(a: str, b: str) -> Tuple[int, str]:
    n = len(a)  # кол-во строк
    m = len(b)  # кол-во столбцов
    print(n, m)
    data = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # вычисляем data[i,j]
            if a[i - 1] == b[j - 1]:
                data[i][j] = data[i - 1][j - 1] + 1
            else:
                data[i][j] = max(data[i - 1][j], data[i][j - 1])

    # восстановление ответа
    i = n
    j = m
    ans = ""
    while data[i][j] > 0:
        if data[i][j] == data[i - 1][j]:
            i -= 1
        elif data[i][j] == data[i - 1][j]:
            j -= 1
        else:
            i -= 1
            j -= 1
            ans = a[i - 1] + ans
    return data[n][m], ans
