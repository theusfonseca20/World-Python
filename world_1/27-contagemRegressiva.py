"""
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
"""

import time #Importei uma biblioteca time no python para usar o sleep
numero = 10
print("===Lançamento do Foguete===")
while numero > 0: #Enquanto o numero for maior que 0 o programa vai rodar
    print(numero)
    numero -= 1 #diminui -1
    time.sleep(3) #tempo de 3 segundos
print("Foguete lançado!")
