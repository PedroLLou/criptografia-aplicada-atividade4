"""
Números primos, função φ de Euler e lista de coprimos.

O φ é o que liga esta parte ao resto: é ele que dá o expoente que satisfaz
a ≡ 1 (mod n) para todo a coprimo com n, e é sobre isso que o RSA se apoia.
"""

from .euclides import algoritmo_euclides


def eprimo(numero: int) -> bool:
    """
    Diz se 'numero' é primo.

    Basta testar divisores até a raiz quadrada: se n = p*q com ambos maiores
    que sqrt(n), o produto passaria de n. Então um dos fatores é sempre menor
    ou igual à raiz, e é onde se procura.
    """
    if numero < 2:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True


def euler(numero: int) -> int:
    """
    Função totiente de Euler: quantos inteiros em [1, n] são coprimos com n.

    Usa a fórmula por fatoração, φ(n) = n * Π (1 - 1/p) para cada primo p que
    divide n, escrita como subtrações inteiras para não passar por float. Cada
    primo entra uma vez só, por isso o laço interno esvazia todas as
    repetições dele antes de seguir.
    """
    resultado = numero
    p = 2
    while p * p <= numero:
        if numero % p == 0:
            while numero % p == 0:
                numero //= p
            resultado -= resultado // p
        p += 1

    # Sobrou um fator primo maior que a raiz do número original.
    if numero > 1:
        resultado -= resultado // numero

    return resultado


def coprimos(numero: int) -> list[int]:
    """
    Lista os inteiros de 1 até 'numero' que são coprimos com ele.

    É o conjunto Z*n do material. O tamanho desta lista é exatamente φ(n),
    o que serve de conferência para a função acima.
    """
    return [i for i in range(1, numero + 1) if algoritmo_euclides(numero, i) == 1]
