"""
Bateria de testes da criptolib.

Cobre o item 6 da missão, "atacar/testar algumas das soluções desenvolvidas".

A estratégia não é conferir alguns valores escolhidos a dedo, que é o tipo de
teste que passa mesmo quando o algoritmo está errado. Cada função é comparada
com uma referência independente:

  - exponenciação modular  ->  contra o `pow(a, b, m)` embutido
  - φ de Euler             ->  contra a contagem direta dos coprimos
  - Teorema Chinês do Resto->  contra o valor que gerou o sistema
  - inverso multiplicativo ->  conferindo que a * a^-1 ≡ 1

    python testes.py
"""

import sys

# O terminal do Windows usa cp1252 por padrao, que nao tem os simbolos "≡" e
# "φ" usados nas mensagens. Sem isto o programa quebra com UnicodeEncodeError.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math
import random

from criptolib import (
    algoritmo_euclides,
    algoritmo_euclides_estendido,
    coprimos,
    eprimo,
    euler,
    exponenciacao_modular,
    inverso_multiplicativo,
    mdc,
    multiplicacao_modular,
    soma_modular,
    subtracao_modular,
    teorema_chines_resto,
    verificar,
)

falhas: list[str] = []


def checar(descricao, obtido, esperado) -> None:
    if obtido == esperado:
        print(f"  ok    {descricao} -> {obtido}")
    else:
        falhas.append(f"{descricao}: obtido {obtido}, esperado {esperado}")
        print(f"  FALHA {descricao} -> obtido {obtido}, esperado {esperado}")


def checar_erro(descricao, funcao, *args) -> None:
    try:
        funcao(*args)
    except ValueError:
        print(f"  ok    {descricao} -> recusado com ValueError")
    else:
        falhas.append(f"{descricao}: deveria ter levantado ValueError")
        print(f"  FALHA {descricao} -> não levantou erro")


def testar_euclides() -> None:
    print("\nEuclides, MDC e inverso multiplicativo")
    checar("mdc(437, 292)", algoritmo_euclides(437, 292), 1)
    checar("mdc(-60, 24) com negativo", algoritmo_euclides(-60, 24), 12)
    checar("mdc(0, 5)", algoritmo_euclides(0, 5), 5)
    checar("apelido mdc é a mesma função", mdc is algoritmo_euclides, True)

    g, x, y = algoritmo_euclides_estendido(240, 46)
    checar("Bézout 240x + 46y = MDC", (g, 240 * x + 46 * y), (2, 2))

    checar("7^-1 mod 26", inverso_multiplicativo(7, 26), 15)
    checar("1234^-1 mod 4321", inverso_multiplicativo(1234, 4321), 3239)
    checar_erro("inverso de 4 mod 8 não existe", inverso_multiplicativo, 4, 8)

    ruins = 0
    for _ in range(2000):
        m = random.randint(2, 10**5)
        a = random.randint(1, m - 1)
        if algoritmo_euclides(a, m) != 1:
            continue
        if a * inverso_multiplicativo(a, m) % m != 1:
            ruins += 1
    checar("2000 inversos aleatórios com a*a^-1 ≡ 1", ruins, 0)


def testar_modular() -> None:
    print("\nAritmética e exponenciação modular")
    checar("(7 + 9) mod 5", soma_modular(7, 9, 5), 1)
    checar("(2 - 9) mod 5, resultado não negativo", subtracao_modular(2, 9, 5), 3)
    checar("(11 * 15) mod 26", multiplicacao_modular(11, 15, 26), 9)

    checar("84^250 mod 263, exemplo do material", exponenciacao_modular(84, 250, 263), 52)
    checar("3^302 mod 11", exponenciacao_modular(3, 302, 11), 9)
    checar("13^28 mod 29, Fermat", exponenciacao_modular(13, 28, 29), 1)
    checar("expoente zero", exponenciacao_modular(5, 0, 7), 1)

    checar("módulo 1, tudo é zero", exponenciacao_modular(5, 0, 1), 0)

    ruins = 0
    for _ in range(3000):
        a = random.randint(-50, 10**6)
        b = random.randint(0, 3000)
        m = random.choice([1, 2, random.randint(1, 10**5)])
        if exponenciacao_modular(a, b, m) != pow(a, b, m):
            ruins += 1
    checar("3000 casos aleatórios contra pow() embutido", ruins, 0)


def testar_primos() -> None:
    print("\nPrimos e função φ de Euler")
    checar("179 é primo", eprimo(179), True)
    checar("1 não é primo", eprimo(1), False)
    checar("2 é primo", eprimo(2), True)
    checar("φ(26)", euler(26), 12)
    checar("φ(180)", euler(180), 48)
    checar("φ(1)", euler(1), 1)

    ruins = sum(1 for n in range(1, 3000) if euler(n) != len(coprimos(n)))
    checar("φ(n) == quantidade de coprimos, n de 1 a 2999", ruins, 0)

    ruins = sum(1 for n in range(2, 5000) if eprimo(n) != (euler(n) == n - 1))
    checar("n é primo <=> φ(n) = n-1, n de 2 a 4999", ruins, 0)


def testar_teorema_chines() -> None:
    print("\nTeorema Chinês do Resto")
    checar("Sun Tzu, século III", teorema_chines_resto([(2, 3), (3, 5), (2, 7)]), (23, 105))
    checar("satélites sobre o Rio", teorema_chines_resto([(2, 13), (5, 15), (8, 19)]), (3200, 3705))
    checar("general chinês", teorema_chines_resto([(5, 7), (4, 9), (1, 10)]), (481, 630))
    checar("partilha de senha, k=2", teorema_chines_resto([(6, 7), (3, 11)]), (69, 77))
    checar("partilha de senha, k=3", teorema_chines_resto([(3, 7), (2, 11), (3, 13)]), (640, 1001))

    checar("uma só congruência", teorema_chines_resto([(7, 10)]), (7, 10))
    checar("módulo 1", teorema_chines_resto([(0, 1), (3, 5)]), (3, 5))
    checar("resto negativo", teorema_chines_resto([(-1, 5), (-1, 7)]), (34, 35))
    checar("resto maior que o módulo", teorema_chines_resto([(12, 5), (9, 7)]), (2, 35))

    checar_erro("lista vazia", teorema_chines_resto, [])
    checar_erro("módulo zero", teorema_chines_resto, [(1, 0)])
    checar_erro("módulo negativo", teorema_chines_resto, [(1, -5)])
    # 6, 10 e 15 têm MDC 1 no conjunto todo, mas MDC(6, 10) = 2.
    checar_erro("coprimos no conjunto mas não dois a dois",
                teorema_chines_resto, [(1, 6), (2, 10), (3, 15)])

    ruins = 0
    for _ in range(500):
        modulos: list[int] = []
        while len(modulos) < random.randint(2, 5):
            candidato = random.randint(2, 60)
            if all(math.gcd(candidato, m) == 1 for m in modulos):
                modulos.append(candidato)

        alvo = random.randint(0, 10**6)
        sistema = [(alvo % m, m) for m in modulos]

        x, n_total = teorema_chines_resto(sistema)
        if x != alvo % n_total or not verificar(x, sistema):
            ruins += 1
    checar("500 sistemas aleatórios contra o valor que os gerou", ruins, 0)


def main() -> None:
    random.seed(7)   # semente fixa: uma falha é sempre reproduzível

    print("=" * 60)
    print("  Testes da criptolib")
    print("=" * 60)

    testar_euclides()
    testar_modular()
    testar_primos()
    testar_teorema_chines()

    print("\n" + "=" * 60)
    if falhas:
        print(f"  {len(falhas)} FALHA(S):")
        for falha in falhas:
            print(f"    - {falha}")
    else:
        print("  Tudo passou.")
    print("=" * 60)

    raise SystemExit(1 if falhas else 0)


if __name__ == "__main__":
    main()
