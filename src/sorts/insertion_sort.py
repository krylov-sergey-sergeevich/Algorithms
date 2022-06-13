from typing import List


def insertion_sort(data: List[float]) -> List[float]:
    """
    Сортировка Вставками (in place - сортирует список, который дали).

    Идея: элементы просматриваются по одному, и каждый новый поступивший элемент размещается в подходящее место среди ранее упорядоченных элементов

    Сложность: в лучшем случае O(n), в среднем O((n^2)/4), в худшем O(n^2).

    Инвариантный алгоритм: левая часть всегда упорядочена. Неплохо работает на почти упорядоченных массивах.

    :param data: неотсортированный список.
    :return: отсортированный список
    """
    for i in range(1, len(data)):
        save = data[i]
        j = i - 1
        while j >= 0 and data[j] > save:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = save
    return data
