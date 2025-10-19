'''
Escreva um programa em Python que leia um número e represente o número antecessor e sucessor 
desse número que foi lido, utilizando operadores de atribuição.
'''

#Recebendo um valor do tipo inteiro
num = int(input("Digite um número:"))

#Calculando antecessor e sucessor
antecessor = num - 1
sucessor = num + 1

#Imprimindo o resultado
print(f"O antecessor de {num} é {antecessor} e o sucessor é {sucessor}")
