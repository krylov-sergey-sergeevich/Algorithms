from typing import List


def count_sort(data: List[int]) -> List[int]:
    """
    Сортировка Подсчетом.

    Идея: считаем сколько раз встречается каждый элемент

    Особенность: данная реализация работает только с положительными элементами

    Сложность: O(N + M).

    :param data: неотсортированный список.
    :return: отсортированный список
    """
    M = max(data)
    count = [0] * (M + 1)
    for elem in data:
        count[elem] += 1
    result = []
    for elem in range(M + 1):
        result += [elem] * count[elem]
    return result
