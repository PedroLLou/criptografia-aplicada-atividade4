def algoritmo_euclides(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def algoritmo_euclides_estendido(a: int, b: int):
    if a == 0:
        return b, 0, 1
    
    mdc, x1, y1 = algoritmo_euclides_estendido(b % a, a)
    
    # Atualiza x e y usando os resultados do passo recursivo
    x = y1 - (b // a) * x1
    y = x1
    
    return mdc, x, y


#Main
# O `if __name__ == "__main__"` faz este bloco rodar SÓ quando o arquivo é
# executado direto. Sem ele, qualquer `import alg_euclides` dispara os input()
# e trava quem estiver usando isto como biblioteca.
if __name__ == "__main__":
    # 1. Teste do Algoritmo de Euclides Clássico
    print("--- Algoritmo de Euclides Clássico ---")
    a = int(input("Digite o valor de 'a': "))
    b = int(input("Digite o valor de 'b': "))
    print(f"MDC({a}, {b}) = {algoritmo_euclides(a, b)}\n")

    # 2. Teste do Algoritmo Estendido
    print("--- Algoritmo Estendido de Euclides ---")
    a_est = int(input("Digite o valor de 'a': "))
    b_est = int(input("Digite o valor de 'b': "))
    mdc, x, y = algoritmo_euclides_estendido(a_est, b_est)
    print(f"MDC({a_est}, {b_est}) = {mdc}")
    print(f"Coeficientes de Bézout: x = {x}, y = {y}")
    print(f"Verificação: {a_est} * ({x}) + {b_est} * ({y}) = {a_est * x + b_est * y}")