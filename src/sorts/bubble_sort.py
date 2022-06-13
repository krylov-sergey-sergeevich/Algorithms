from typing import List


def bubble_sort(data: List[float]) -> List[float]:
    """
    Сортировка Пузырьком (in place - сортирует список, который дали).

    Идея: сравниваются соседние элементы, наибольшие элементы всплывают

    Сложность: в лучшем случае O(n), в среднем O((n^2)/4), в худшем O(n^2).

    Инвариантный алгоритм: правая часть всегда упорядочена. Неплохо работает на почти упорядоченных массивах.

    :param data: неотсортированный список.
    :return: отсортированный список
    """
    j = len(data)
    unordered = True  # флаг неупорядоченного массива, позволит когда перестановки закончатся узнать об этом
    while unordered:
        j -= 1
        unordered = False
        for i in range(j):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                unordered = True
    return data
