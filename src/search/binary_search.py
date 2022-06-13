from typing import List


def binary_search(data: List[float], key: float) -> bool:
    """
    Бинарный поиск, находит крайнее правое значение если несколько одинаковых элементов.
    """
    left = -1
    right = len(data)
    while right - left > 1:
        m = (left + right) // 2
        if data[m] > key:  # если напишем data[m] >= key, то будет искать среди равных крайнее левое 1, 2!, 2, 3,
            right = m
        else:
            left = m
    return left >= 0 and data[left] == key
