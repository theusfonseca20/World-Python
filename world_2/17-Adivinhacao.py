"""
Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:
Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção para sair do programa.
Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.
"""

import random
numero_sistema = random.randint(1,10)
done = False

while not done:
    numero_usuario = int(input("Digite um número: "))
    if numero_sistema == numero_usuario:
        print("Parabens, você acertou o número :) ")
        done = True
    else:
        print("Infelizmente você errou, vamos tentar novamente...")
print("Programa Finalizado....")