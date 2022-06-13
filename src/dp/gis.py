from typing import List


def gis(A: List[int]) -> list[int]:
    """
    Наибольшая возрастающая последовательность.

    Сложность: O(n^2)

    Хотим выбрать подпоследовательность чтобы СТРОГО возрастали.

    A[i] 2 7 1 4 3 5 4 6 2 5 8 3
    F[i] - длина НВП заканчивающаяся A[i]
    """
    n = len(A)
    F = [0] * n
    Prev = [-1] * n  # будем отслеживать предков
    for i in range(n):
        # Найдем F[i]
        m = 0  # max F[j], j < i, A[j] < A[i]
        for j in range(i):
            if A[j] < A[i] and F[j] > m:
                m = F[j]
                Prev[i] = j
        F[i] = m + 1

    # Восстановление ответа
    ans = []
    i = F.index(max(F))  # берем индекс максимального значения
    ans.append(A[i])
    while Prev[i] != -1:
        i = Prev[i]
        ans.append(A[i])
    return ans[::-1]


def gis_fast(A: List[int]) -> list[int]:
    """
    Наибольшая возрастающая последовательность.

    Сложность: O(n * log(n))

    Хотим выбрать подпоследовательность чтобы СТРОГО возрастали.

    A[i] 2 7 1 4 3 5 4 6 2 5 8 3
    L[i] - наименьшее значение последнего элемента в возрастающей последовательности содержащей i элементов
    для удобства двоичного поиска добавим в список L элементы -inf и +inf

    Найдем max j, L[j] < A[i] тогда L[j+1] = A[i] (тут мы можем использовать двоичный поиск)
    """
    n = len(A)
    INF = max([abs(elem) for elem in A]) + 1
    L = [-INF] + [INF] * (n + 1)
    for i in range(n):
        # Куда вставить L[i]?
        left = 0
        right = n + 1
        # L[left] < A[i], L[right] >= A[i]
        while left + 1 < right:
            middle = (left + right) // 2
            if L[middle] < A[i]:
                left = middle
            else:
                right = middle
        L[left + 1] = A[i]

    # ищем максимальное не равное INF
    i = n + 1
    while L[i] == INF:
        i -= 1
    return i
