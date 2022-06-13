from typing import List


def selection_sort(data: List[float]) -> List[float]:
    """
    Сортировка Выбором (in place - сортирует список, который дали).

    Сложность: O(n^2).

    Инвариантный алгоритм: элементы с одинаковым значением не меняются местами.

    :param data: неотсортированный список.
    :return: отсортированный список
    """
    for i in range(len(data) - 1):
        m = i
        for j in range(i + 1, len(data)):
            if data[j] < data[m]:
                m = j
        data[i], data[m] = data[m], data[i]
    return data
