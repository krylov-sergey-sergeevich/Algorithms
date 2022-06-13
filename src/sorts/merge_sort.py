from typing import List


def merge_sort(data: List[float]) -> List[float]:
    """
    Сортировка Слиянием (in place - сортирует список, который дали).

    Идея: рекурсивно делим пополам и сортируем части

    Сложность: O(n * log(n)).

    Достоинства: Устойчивость(Stable Sort)

    Недостатки: Рекурсия, требуется 0(n) доп памяти

    :param data: неотсортированный список.
    :return: отсортированный список
    """

    def merge(a: List[float], b: List[float]) -> List[float]:
        """
        Сложность: O(len(a)+len(b))

        :param a: отсортированный упорядоченно массив.
        :param b: отсортированный упорядоченно массив.
        :return: объединенный отсортированный массив
        """
        result = []
        first = 0
        second = 0
        while first < len(a) and second < len(b):
            if a[first] <= b[second]:
                result.append(a[first])
                first += 1
            else:
                result.append(b[second])
                second += 1
        result += a[first:] + b[second:]
        return result

    if len(data) <= 1:
        return data
    else:
        m = len(data) // 2
        return merge(merge_sort(data[:m]), merge_sort(data[m:]))
