"""
Menu de demonstração da criptolib.

Antes cada módulo tinha o próprio bloco de `input()`, o que obrigava a abrir um
arquivo diferente para cada algoritmo. Agora a parte interativa está toda aqui,
e a biblioteca ficou só com as funções.

    python main.py
"""

import sys

# O terminal do Windows usa cp1252 por padrao, que nao tem os simbolos "≡" e
# "φ" usados nas mensagens. Sem isto o programa quebra com UnicodeEncodeError.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from criptolib import (
    algoritmo_euclides,
    algoritmo_euclides_estendido,
    coprimos,
    eprimo,
    euler,
    exponenciacao_modular,
    inverso_multiplicativo,
    multiplicacao_modular,
    soma_modular,
    subtracao_modular,
    teorema_chines_resto,
    verificar,
)


def ler_int(rotulo: str) -> int:
    """Pede um inteiro e insiste até receber um."""
    while True:
        try:
            return int(input(rotulo))
        except ValueError:
            print("  valor inválido, digite um número inteiro.")


def demo_euclides() -> None:
    print("\n--- Algoritmo de Euclides ---")
    a = ler_int("a: ")
    b = ler_int("b: ")
    print(f"MDC({a}, {b}) = {algoritmo_euclides(a, b)}")

    g, x, y = algoritmo_euclides_estendido(a, b)
    print(f"\nEstendido: MDC = {g}, coeficientes de Bézout x = {x}, y = {y}")
    print(f"Verificação: {a}*({x}) + {b}*({y}) = {a * x + b * y}")


def demo_inverso() -> None:
    print("\n--- Inverso multiplicativo ---")
    a = ler_int("a: ")
    m = ler_int("módulo m: ")
    try:
        print(f"{a}^-1 mod {m} = {inverso_multiplicativo(a, m)}")
    except ValueError as erro:
        print(f"Não existe: {erro}")


def demo_primos() -> None:
    print("\n--- Primos e função φ de Euler ---")
    n = ler_int("n: ")
    print(f"{n} é primo? {'sim' if eprimo(n) else 'não'}")
    print(f"φ({n}) = {euler(n)}")
    lista = coprimos(n)
    print(f"coprimos de {n} ({len(lista)} deles): {lista}")


def demo_aritmetica() -> None:
    print("\n--- Aritmética modular ---")
    a = ler_int("a: ")
    b = ler_int("b: ")
    m = ler_int("módulo m: ")
    print(f"({a} + {b}) mod {m} = {soma_modular(a, b, m)}")
    print(f"({a} - {b}) mod {m} = {subtracao_modular(a, b, m)}")
    print(f"({a} * {b}) mod {m} = {multiplicacao_modular(a, b, m)}")


def demo_exponenciacao() -> None:
    print("\n--- Exponenciação modular ---")
    a = ler_int("base a: ")
    b = ler_int("expoente b: ")
    m = ler_int("módulo m: ")
    print(f"{a}^{b} mod {m} = {exponenciacao_modular(a, b, m)}")


def demo_teorema_chines() -> None:
    print("\n--- Teorema Chinês do Resto ---")
    print("Resolve x ≡ a (mod n) para módulos coprimos dois a dois.")

    quantidade = ler_int("\nQuantas congruências? ")

    congruencias: list[tuple[int, int]] = []
    for i in range(quantidade):
        print(f"\nCongruência {i + 1}:")
        a = ler_int(f"  a{i + 1} (o resto): ")
        n = ler_int(f"  n{i + 1} (o módulo): ")
        congruencias.append((a, n))

    print("\nSistema:")
    for a, n in congruencias:
        print(f"  x ≡ {a} (mod {n})")

    try:
        x, n_total = teorema_chines_resto(congruencias)
    except ValueError as erro:
        print(f"\nNão dá para resolver: {erro}")
        return

    print(f"\nSolução: x ≡ {x} (mod {n_total})")
    print(f"Ou seja, as soluções são {x} + {n_total}k, para k inteiro.")

    print("\nVerificação:")
    for a, n in congruencias:
        print(f"  {x} mod {n} = {x % n}, esperado {a % n}")
    print("Confere!" if verificar(x, congruencias) else "NÃO CONFERE, algo está errado")


OPCOES = {
    "1": ("Algoritmo de Euclides (clássico e estendido)", demo_euclides),
    "2": ("Inverso multiplicativo", demo_inverso),
    "3": ("Primos, φ de Euler e coprimos", demo_primos),
    "4": ("Aritmética modular", demo_aritmetica),
    "5": ("Exponenciação modular", demo_exponenciacao),
    "6": ("Teorema Chinês do Resto", demo_teorema_chines),
}


def main() -> None:
    print("=" * 52)
    print("  criptolib - SecureDocs, Missão 1")
    print("=" * 52)

    while True:
        print("\nEscolha um algoritmo:")
        for chave, (rotulo, _) in OPCOES.items():
            print(f"  {chave}. {rotulo}")
        print("  0. Sair")

        escolha = input("\nOpção: ").strip()

        if escolha == "0":
            print("Até mais.")
            return

        if escolha in OPCOES:
            OPCOES[escolha][1]()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
