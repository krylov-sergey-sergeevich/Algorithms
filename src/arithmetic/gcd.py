def gcd(a: int, b: int) -> int:
    """
    НОД - Алгоритм Евклида
    return: наименьший общий делитель
    """
    # a, b >= 1
    while b > 0:
        a, b = b, a % b
    return a


def gcd_recursion(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd_recursion(b, a % b)
