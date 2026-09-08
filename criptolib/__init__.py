"""
criptolib, a biblioteca da Missão 1 do SecureDocs.

Reúne as ferramentas matemáticas que sustentam os algoritmos de chave pública:
Euclides e MDC, inverso multiplicativo, primos e função φ de Euler, aritmética
e exponenciação modular, e o Teorema Chinês do Resto.

Tudo é importável direto do pacote:

    from criptolib import teorema_chines_resto, exponenciacao_modular

    x, n = teorema_chines_resto([(2, 3), (3, 5), (2, 7)])   # (23, 105)

Sem dependências além da biblioteca padrão.
"""

from .euclides import (
    algoritmo_euclides,
    algoritmo_euclides_estendido,
    euclEst,
    inverso_multiplicativo,
    mdc,
)
from .modular import (
    exponenciacao_modular,
    multiplicacao_modular,
    soma_modular,
    subtracao_modular,
)
from .primos import coprimos, eprimo, euler
from .teorema_chines import (
    teorema_chines_resto,
    validar_congruencias,
    verificar,
)

__all__ = [
    # Euclides e MDC
    "algoritmo_euclides",
    "mdc",
    "algoritmo_euclides_estendido",
    "euclEst",
    "inverso_multiplicativo",
    # Aritmética modular
    "soma_modular",
    "subtracao_modular",
    "multiplicacao_modular",
    "exponenciacao_modular",
    # Primos e Euler
    "eprimo",
    "euler",
    "coprimos",
    # Teorema Chinês do Resto
    "teorema_chines_resto",
    "validar_congruencias",
    "verificar",
]
