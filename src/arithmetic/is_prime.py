def is_prime(n: int) -> bool:
    """
    Проверка на простоту
    return: true если простое
    """
    if n % 2 == 0:
        return n == 2
    d = 3
    while n % 2 != 0 and d * d < n:
        d += 2
    return d * d > n
