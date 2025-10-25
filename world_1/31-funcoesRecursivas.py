"""
Fatorial de um numero
3 -> 3 *2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""

# Fatorial de um numero
def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num-1))
numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é: {fatorial(numero)}")