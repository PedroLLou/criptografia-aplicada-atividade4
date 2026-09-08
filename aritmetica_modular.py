"""
Aritmética modular: soma, subtração e multiplicação módulo m.

O Python já devolve resto NÃO NEGATIVO em `%`, mesmo para operando negativo:
`(-1) % 5` é 4, e não -1 como em C ou Java. Isso é o que a matemática modular
espera, então a subtração aqui não precisa de ajuste.
"""


def soma_modular(a: int, b: int, m: int) -> int:
    return (a + b) % m


def subtracao_modular(a: int, b: int, m: int) -> int:
    return (a - b) % m


def multiplicacao_modular(a: int, b: int, m: int) -> int:
    return (a * b) % m


if __name__ == "__main__":
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    m = int(input("Digite o módulo: "))

    print("\nSoma:", soma_modular(a, b, m))
    print("Subtração:", subtracao_modular(a, b, m))
    print("Multiplicação:", multiplicacao_modular(a, b, m))
