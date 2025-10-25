"""
Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.
"""

def strings():
    maiuscula = 0
    minuscula = 0
    texto = input("digite um nome: ")
    for letra in texto:
        if letra.isupper():
            maiuscula += 1
        elif letra.islower():
            minuscula += 1        
    print(f"Temos {minuscula} letras minusculas na palavra")
    print(f"Temos {maiuscula} letras maiuscula na palavra")
strings()