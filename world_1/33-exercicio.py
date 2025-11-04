"""
Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
"""

def check_numbers(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        elif numero % 2 == 1:
            impares.append(numero)
    return pares, impares
print(check_numbers([1,2,3,4,5,6,7,8,9,10]))

