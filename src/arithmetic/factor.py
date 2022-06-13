from typing import List


def factor(n: int) -> List[int]:
    """
    Разложение на множители.
    :param n: число.
    :return: лист множителей
    """
    ans = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            ans.append(d)
        d += 1
    if n != 1:
        ans.append(n)
    return ans
