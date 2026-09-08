"""
Euclides: MDC, algoritmo estendido e inverso multiplicativo.

Este é o único lugar do projeto onde o algoritmo de Euclides está escrito.
Antes ele aparecia duas vezes, em `mdc.py` e em `alg_euclides.py`, e o
estendido também, em `invMult.py` e em `alg_euclides.py`. Duas cópias da
mesma conta é o tipo de coisa que sai de sincronia na primeira correção.

Os nomes antigos continuam valendo como apelidos no fim do arquivo, então
`from criptolib import mdc` e `from criptolib import algoritmo_euclides`
devolvem a mesma função.
"""


def algoritmo_euclides(a: int, b: int) -> int:
    """
    Maior divisor comum de 'a' e 'b'.

    A cada passo troca (a, b) por (b, a mod b). O MDC não muda nessa troca,
    e o segundo valor cai rápido, então o processo termina quando b chega a
    zero: o MDC é o último resto não nulo, que nessa hora está em 'a'.
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def algoritmo_euclides_estendido(a: int, b: int) -> tuple[int, int, int]:
    """
    Devolve (g, x, y) com a*x + b*y = g = MDC(a, b).

    São os coeficientes de Bézout. Eles são o que permite calcular o inverso
    multiplicativo: quando g vale 1, a igualdade a*x + b*y = 1 lida módulo b
    diz que a*x ≡ 1, ou seja, x é o inverso de a.
    """
    if a == 0:
        return b, 0, 1

    g, x1, y1 = algoritmo_euclides_estendido(b % a, a)

    # Desfaz a troca do passo recursivo, propagando os coeficientes de volta.
    x = y1 - (b // a) * x1
    y = x1

    return g, x, y


def inverso_multiplicativo(a: int, m: int) -> int:
    """
    Inverso de 'a' módulo 'm', isto é, o x com a*x ≡ 1 (mod m).

    Levanta ValueError quando não existe, o que acontece exatamente quando
    MDC(a, m) != 1. Falhar aqui, com a causa na mensagem, é melhor do que
    devolver um número qualquer que o chamador usaria sem desconfiar.
    """
    g, x, _ = algoritmo_euclides_estendido(a, m)

    if g != 1:
        raise ValueError(
            f"O inverso multiplicativo de {a} mod {m} não existe pois MDC({a}, {m}) = {g} != 1"
        )

    # O x de Bézout pode vir negativo; traz para o intervalo [0, m).
    return (x % m + m) % m


# Nomes usados antes da unificação, mantidos para não quebrar quem já importa.
mdc = algoritmo_euclides
euclEst = algoritmo_euclides_estendido
