"""
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
"""

import time
numero = 10
print("===Lançamento do Foguete===")
while numero > 0:
    print(numero)
    numero -= 1
    time.sleep(3)
print("Foguete lançado!")
