# Biblioteca de Criptografia Aplicada, Atividade 4

Biblioteca em Python com as funções de aritmética modular e teoria dos números
que sustentam os algoritmos de chave pública.

Sem dependência nenhuma além da biblioteca padrão. Testado no Python 3.13.

## O que tem aqui

| Módulo | O que faz |
| --- | --- |
| `mdc.py` | Máximo divisor comum, pelo algoritmo de Euclides |
| `alg_euclides.py` | Euclides clássico e estendido, com os coeficientes de Bézout |
| `invMult.py` | Inverso multiplicativo módulo m |
| `primo_euler.py` | Teste de primalidade, totiente de Euler e lista de coprimos |
| `aritmetica_modular.py` | Soma, subtração e multiplicação módulo m |
| `exponenciacao_modular.py` | Exponenciação rápida, o square-and-multiply |
| `teorema_chines.py` | Teorema Chinês do Resto, para módulos coprimos |

## Como usar

Cada arquivo funciona das duas formas: importado como biblioteca, ou executado
direto, e aí ele pede os valores e mostra o resultado.

```bash
python teorema_chines.py
```

```python
from teorema_chines import teorema_chines_resto, verificar

x, n = teorema_chines_resto([(2, 3), (3, 5), (2, 7)])
print(x, n)              # 23 105
print(verificar(x, [(2, 3), (3, 5), (2, 7)]))   # True
```

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

## Sobre a organização dos arquivos

Dois arquivos tinham as chamadas de `input()` soltas no corpo do módulo, o que
fazia qualquer `import` travar pedindo número no terminal. Elas foram movidas
para dentro de `if __name__ == "__main__":`, sem mudar o algoritmo nem o
comportamento de quem roda o arquivo direto. É o que permite os módulos se
usarem uns aos outros: o Teorema Chinês do Resto importa o `mdc` e o
`inverso_multiplicativo` em vez de reescrevê-los.
