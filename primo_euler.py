#primo
import math


def eprimo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero**0.5)+1):
        if numero%i==0:
            return False

    return True


#totiente euler
def euler(numero):
    resultado = numero
    p = 2
    while p*p <= numero:
        if numero % p == 0:
            while numero % p==0:
                numero//=p
            resultado-= resultado//p
        p+=1
    if numero>1:
        resultado -= resultado//numero
    return resultado


def coprimos(numero):
    resultado = []
    for i in range(1, numero+1):
        if math.gcd(numero, i) == 1:
            resultado.append(i)
    return resultado


# O `if __name__ == "__main__"` faz este bloco rodar SÓ quando o arquivo é
# executado direto. Sem ele, qualquer `import primo_euler` dispara os input() e
# trava quem estiver usando isto como biblioteca.
if __name__ == "__main__":
    numero = input("Digite um numero:")
    numero = int(numero)

    if eprimo(numero):
        print(f"O numero {numero} é primo.")
    else:
        print(f"O numero {numero} não é primo.")

    numero = int(input("Digite um numero:"))
    resultado = euler(numero)
    lista_c = coprimos(numero)

    print(f"totiente de Euler {numero} = {resultado}")
    print(f"coprimos de {numero}= {lista_c}")
