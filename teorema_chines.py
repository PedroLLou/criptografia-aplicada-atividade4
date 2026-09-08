"""
Teorema Chinês do Resto, para módulos coprimos dois a dois.

O PROBLEMA QUE ELE RESOLVE

Um sistema de congruências simultâneas:

    x ≡ a1 (mod n1)
    x ≡ a2 (mod n2)
    ...
    x ≡ ak (mod nk)

Quando os módulos n1, n2, ..., nk são coprimos DOIS A DOIS, o teorema garante
duas coisas: existe solução, e ela é ÚNICA módulo N = n1 * n2 * ... * nk.

A COPRIMALIDADE É DOIS A DOIS, e não do conjunto todo. É uma exigência mais
forte do que parece: 6, 10 e 15 têm MDC 1 quando olhados juntos, e mesmo assim
não servem, porque MDC(6, 10) = 2. Por isso a validação aqui compara cada par.

COMO A CONSTRUÇÃO FUNCIONA

Para cada congruência i, monta-se Ni = N / ni, que é o produto de todos os
outros módulos. Como os módulos são coprimos dois a dois, Ni não compartilha
fator nenhum com ni, então MDC(Ni, ni) = 1 e o inverso multiplicativo de Ni
módulo ni existe. Chamando esse inverso de yi:

    x = soma de (ai * Ni * yi), tudo módulo N

Cada parcela foi construída para valer ai módulo ni e ZERO módulo todos os
outros: Ni é múltiplo de nj para todo j diferente de i. É isso que faz as
parcelas não interferirem umas nas outras.

Escrito por Pedro Lourençoni para a Atividade 4 de Criptografia Aplicada.
Reaproveita `mdc` e `inverso_multiplicativo`, que são as partes do grupo.
"""

from mdc import mdc
from invMult import inverso_multiplicativo


def validar_congruencias(congruencias: list[tuple[int, int]]) -> None:
    """
    Confere as duas exigências do teorema antes de tentar resolver.

    Falhar cedo e com mensagem clara importa aqui: sem a coprimalidade dois a
    dois o inverso multiplicativo simplesmente não existe, e o erro apareceria
    lá dentro, num ponto que não explica a causa.
    """
    if not congruencias:
        raise ValueError("é preciso pelo menos uma congruência")

    for a, n in congruencias:
        if n < 1:
            raise ValueError(f"módulo inválido: {n}. Todo módulo precisa ser >= 1")

    for i in range(len(congruencias)):
        for j in range(i + 1, len(congruencias)):
            ni = congruencias[i][1]
            nj = congruencias[j][1]
            g = mdc(ni, nj)
            if g != 1:
                raise ValueError(
                    f"os módulos {ni} e {nj} não são coprimos: MDC({ni}, {nj}) = {g}. "
                    "O teorema, nesta forma, exige coprimalidade dois a dois"
                )


def teorema_chines_resto(congruencias: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Resolve o sistema e devolve (x, N).

    `congruencias` é uma lista de pares (a, n), lidos como x ≡ a (mod n).

    `x` é a MENOR solução não negativa, sempre no intervalo [0, N), e `N` é o
    produto dos módulos. Toda solução do sistema tem a forma x + k*N.

    Exemplo clássico, o problema de Sun Tzu:

        >>> teorema_chines_resto([(2, 3), (3, 5), (2, 7)])
        (23, 105)
    """
    validar_congruencias(congruencias)

    n_total = 1
    for _, n in congruencias:
        n_total *= n

    x = 0
    for a, n in congruencias:
        # Produto de todos os outros módulos. Ele é múltiplo de cada nj com
        # j != i, então esta parcela vale zero módulo todos os outros.
        n_parcial = n_total // n

        # Existe porque MDC(n_parcial, n) = 1, que é o que a validação garantiu.
        inverso = inverso_multiplicativo(n_parcial % n, n)

        x += a * n_parcial * inverso

    return x % n_total, n_total


def verificar(x: int, congruencias: list[tuple[int, int]]) -> bool:
    """
    Confere que o x encontrado satisfaz TODAS as congruências.

    Existe porque conferir é barato e a conta acima é fácil de errar em
    silêncio: um resultado errado continua sendo um número plausível.
    """
    return all(x % n == a % n for a, n in congruencias)


if __name__ == "__main__":
    print("--- Teorema Chinês do Resto ---")
    print("Resolve x ≡ a (mod n) para várias congruências de módulos coprimos.\n")

    quantidade = int(input("Quantas congruências? "))

    congruencias: list[tuple[int, int]] = []
    for i in range(quantidade):
        print(f"\nCongruência {i + 1}:")
        a = int(input(f"  a{i + 1} (o resto): "))
        n = int(input(f"  n{i + 1} (o módulo): "))
        congruencias.append((a, n))

    print("\nSistema:")
    for a, n in congruencias:
        print(f"  x ≡ {a} (mod {n})")

    try:
        x, n_total = teorema_chines_resto(congruencias)
    except ValueError as erro:
        print(f"\nNão dá para resolver: {erro}")
    else:
        print(f"\nSolução: x ≡ {x} (mod {n_total})")
        print(f"Ou seja, as soluções são {x} + {n_total}k, para k inteiro.")

        print("\nVerificação:")
        for a, n in congruencias:
            print(f"  {x} mod {n} = {x % n}, esperado {a % n}")
        print("Confere!" if verificar(x, congruencias) else "NÃO CONFERE, algo está errado")
