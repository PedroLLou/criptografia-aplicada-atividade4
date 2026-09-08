"""
Exponenciação modular pelo método da exponenciação rápida (square-and-multiply).

POR QUE NÃO SE CALCULA `(a ** b) % m` DIRETO: o expoente em criptografia tem
centenas de dígitos, e `a ** b` seria um número que não cabe em memória nenhuma.
Este método reduz módulo m a cada passo, então nenhum valor intermediário passa
do tamanho de m*m.

O expoente é percorrido em binário: a cada bit, a base é elevada ao quadrado, e
quando o bit é 1 ela entra no resultado. São O(log b) multiplicações em vez de b.
"""


def exponenciacao_modular(a: int, b: int, m: int) -> int:
    """
    Calcula (a ** b) mod m.

    Equivale ao `pow(a, b, m)` embutido do Python, que é a versão em C do mesmo
    algoritmo. Aqui ele está escrito à mão porque o objetivo da atividade é o
    método, não o resultado.
    """
    resultado = 1
    a = a % m

    while b > 0:
        if b % 2 == 1:
            resultado = (resultado * a) % m

        a = (a * a) % m
        b = b // 2

    return resultado


if __name__ == "__main__":
    a = int(input("Digite a base: "))
    b = int(input("Digite o expoente: "))
    m = int(input("Digite o módulo: "))

    print("Resultado:", exponenciacao_modular(a, b, m))
