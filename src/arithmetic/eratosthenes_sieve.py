from typing import List


def eratosthenes_sieve(n: int) -> List[bool]:
    """
    Получение списка простых чисел с 0 до n.
    :param n: число.
    :return: список из n+1 значений True or False
    """
    is_prime = [True] * (n + 1)  # делаем так для удобства

    d = 2
    while d * d <= n:
        if is_prime[d]:
            for i in range(d * d, n + 1, d):
                is_prime[i] = False
        d += 1
    # начинаем с 0
    return is_prime
