# criptolib — SecureDocs, Missão 1

Biblioteca em Python com as ferramentas matemáticas que sustentam os algoritmos
de chave pública: Euclides e MDC, inverso multiplicativo, primos e função φ de
Euler, aritmética e exponenciação modular, e o Teorema Chinês do Resto.

Entrega da **Missão 1 — Precisamos de matemática**, do problema SecureDocs, da
disciplina CMP2195 A03 — Criptografia Aplicada.

Sem dependências além da biblioteca padrão. Testado no Python 3.13.

## Estrutura

```
criptolib/            a biblioteca
  euclides.py         MDC, algoritmo estendido, inverso multiplicativo
  modular.py          soma, subtração, multiplicação e exponenciação modular
  primos.py           teste de primalidade, φ de Euler, lista de coprimos
  teorema_chines.py   Teorema Chinês do Resto para módulos coprimos
main.py               menu interativo que demonstra todos os algoritmos
testes.py             bateria de testes da biblioteca
```

## Cobertura dos tópicos exigidos

| Tópico da missão | Onde está |
| --- | --- |
| aritmética modular | `criptolib/modular.py` |
| MDC | `criptolib/euclides.py` |
| algoritmo de Euclides | `criptolib/euclides.py` |
| algoritmo estendido de Euclides | `criptolib/euclides.py` |
| inverso multiplicativo | `criptolib/euclides.py` |
| números primos | `criptolib/primos.py` |
| função φ de Euler | `criptolib/primos.py` |
| exponenciação modular | `criptolib/modular.py` |
| teorema Chinês do Resto | `criptolib/teorema_chines.py` |

## Como usar

Menu interativo com todos os algoritmos:

```bash
python main.py
```

Como biblioteca:

```python
from criptolib import teorema_chines_resto, verificar, exponenciacao_modular

x, n = teorema_chines_resto([(2, 3), (3, 5), (2, 7)])
print(x, n)                                      # 23 105
print(verificar(x, [(2, 3), (3, 5), (2, 7)]))    # True

print(exponenciacao_modular(84, 250, 263))       # 52
```

## Testes

```bash
python testes.py
```

São 38 verificações. A estratégia não é conferir alguns valores escolhidos a
dedo, que é o tipo de teste que passa mesmo com o algoritmo errado: cada função
é comparada com uma referência independente.

| Função | Comparada contra |
| --- | --- |
| exponenciação modular | o `pow(a, b, m)` embutido, em 3000 casos aleatórios |
| φ de Euler | a contagem direta dos coprimos, para n de 1 a 2999 |
| inverso multiplicativo | a própria definição, `a * a⁻¹ ≡ 1`, em 2000 casos |
| Teorema Chinês do Resto | o valor que gerou o sistema, em 500 sistemas aleatórios |

Além dos casos de borda: resto negativo, resto maior que o módulo, módulo 1,
uma só congruência, expoente zero, e as entradas que devem ser recusadas.

## Teorema Chinês do Resto

Dado um sistema de congruências simultâneas:

```
x ≡ a1 (mod n1)
x ≡ a2 (mod n2)
...
x ≡ ak (mod nk)
```

com os módulos **coprimos dois a dois**, o teorema garante que existe solução e
que ela é única módulo `N = n1 * n2 * ... * nk`.

A coprimalidade exigida é **dois a dois**, e não do conjunto todo. É uma
exigência mais forte do que parece: 6, 10 e 15 têm MDC 1 quando olhados juntos,
e mesmo assim não servem, porque `MDC(6, 10) = 2`. A função valida cada par
antes de resolver, e recusa dizendo qual par falhou.

Para cada congruência monta-se `Ni = N / ni`, que é múltiplo de todos os outros
módulos e por isso vale zero módulo cada um deles. Como `MDC(Ni, ni) = 1`, o
inverso multiplicativo `yi` de `Ni` módulo `ni` existe, e a solução é a soma de
`ai * Ni * yi`, reduzida módulo `N`. Cada parcela vale `ai` na sua própria
congruência e zero em todas as outras, e é isso que as impede de interferir umas
nas outras.

A função `verificar` existe porque a conta é fácil de errar em silêncio: um
resultado errado continua sendo um número plausível.

O exemplo clássico é o problema de Sun Tzu, do século III: um número que deixa
resto 2 na divisão por 3, resto 3 na divisão por 5 e resto 2 na divisão por 7. A
resposta é 23, e todo número da forma `23 + 105k` também serve.

## Nota sobre a unificação dos arquivos

A primeira versão do repositório era um arquivo por integrante, e o mesmo
algoritmo aparecia mais de uma vez: Euclides estava em `mdc.py` e em
`alg_euclides.py`, e o estendido em `invMult.py` e em `alg_euclides.py`. Duas
cópias da mesma conta saem de sincronia na primeira correção, e o item 8 da
missão pede justamente para *integrar os diferentes mecanismos*.

Os algoritmos foram então reunidos no pacote `criptolib`, cada um com uma única
implementação, e os blocos de `input()` que estavam espalhados pelos módulos
foram para o `main.py`. **Nenhum algoritmo foi reescrito** — o que mudou foi
onde cada um mora. Os nomes antigos `mdc` e `euclEst` continuam funcionando como
apelidos, então código que já importava esses nomes segue valendo.
