"""
Aritmética modular: soma, subtração, multiplicação e exponenciação rápida.
"""


def soma_modular(a: int, b: int, m: int) -> int:
    """(a + b) mod m."""
    return (a + b) % m


def subtracao_modular(a: int, b: int, m: int) -> int:
    """
    (a - b) mod m.

    Não precisa de ajuste para resultado negativo: o `%` do Python já devolve
    resto NÃO NEGATIVO, então `(-1) % 5` é 4, e não -1 como em C ou Java.
    Quatro é justamente o que a aritmética modular espera.
    """
    return (a - b) % m


def multiplicacao_modular(a: int, b: int, m: int) -> int:
    """(a * b) mod m."""
    return (a * b) % m


def exponenciacao_modular(a: int, b: int, m: int) -> int:
    """
    (a ** b) mod m pelo método da exponenciação rápida (square-and-multiply).

    POR QUE NÃO CALCULAR `(a ** b) % m` DIRETO: em criptografia o expoente tem
    centenas de dígitos, e `a ** b` seria um número que não cabe em memória
    nenhuma. Aqui a redução módulo m acontece a cada passo, então nenhum valor
    intermediário passa do tamanho de m*m.

    O expoente é percorrido em binário: a cada bit a base é elevada ao
    quadrado, e quando o bit é 1 ela entra no resultado. Isso dá O(log b)
    multiplicações em vez de b.

    Equivale ao `pow(a, b, m)` embutido, que é a versão em C deste mesmo
    algoritmo. Está escrito à mão porque o objetivo da missão é o método.
    """
    # `1 % m` e não `1`: com m = 1 tudo é congruente a zero, e começar em 1
    # devolveria 1 para expoente zero. É o mesmo que faz o `pow` embutido.
    resultado = 1 % m
    a = a % m

    while b > 0:
        if b % 2 == 1:
            resultado = (resultado * a) % m

        a = (a * a) % m
        b = b // 2

    return resultado
