def euclEst(a: int, b: int) -> tuple[int, int, int]:
    """
    Retorna uma tupla (g, x, y) tal que:
    a*x + b*y = g = MDC(a, b)
    """
    if a == 0:
        return b, 0, 1

    g, x1, y1 = euclEst(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return g, x, y


def inverso_multiplicativo(a: int, m: int) -> int:
    """
    Calcula o Inverso Multiplicativo de 'a' módulo 'm'.
    Lança ValueError se o inverso não existir (quando MDC != 1).
    """
    g, x, _ = euclEst(a, m)

    if g != 1:
        raise ValueError(
            f"O inverso multiplicativo de {a} mod {m} não existe pois MDC({a}, {m}) = {g} != 1"
        )

    return (x % m + m) % m