from typing import Tuple


def gcdex(a: int, b: int) -> Tuple[int, int, int]:
    """
    Расширенный Алгоритм Евклида.
    :param a: число
    :param b: число
    :return: три числа (d, x, y) таких что где d = НОД(a, b), a*x+b*y = d
    """
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = gcdex(b, a % b)  # d = НОД(b, a % b), b*x1 + (a%b)*y1 = d
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y


def gcdex_print(a, b):
    d, x, y = gcdex(a, b)
    print(str(a) + " * " + str(x) + " + " + str(b) + " * " + str(y) + " = " + str(d))
