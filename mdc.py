def mdc(a: int, b: int) -> int:
    """
    Calcula o Maior Divisor Comum entre 'a' e 'b'.
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a