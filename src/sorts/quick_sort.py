from typing import List
import random


def quick_sort(data: List[float]) -> List[float]:
    """
    Быстрая Сортировка Хоара.

    Идея: выбираем опорный элемент, раскидываем вокруг него элементы и дальше рекурсивно по левой и правой части

    Сложность: O(n * log(n)).

    Достоинства:

    Недостатки: Рекурсия, требуется 0(n) доп памяти (но можно реализовать без доп памяти)

    :param data: неотсортированный список.
    :return: отсортированный список
    """
    if len(data) <= 1:
        return data
    else:
        q = random.choice(data)  # барьерный элемент
        L = [elem for elem in data if elem < q]
        M = [elem for elem in data if elem == q]
        R = [elem for elem in data if elem > q]
        return quick_sort(L) + M + quick_sort(R)
