"""
Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
"""



print("===Tabuada de Multiplicação===")
numero = int(input("Digite o número para a operação: "))
for i in range(1, 11): #contando de 1 a 10
    resultado = numero * i 
    print(f"{numero} * {i} = {resultado}")