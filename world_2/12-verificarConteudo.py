"""
Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).
"""

import re
def checar_caracter(string):
    regra = re.compile(r"[^a-zA-Z0-9]") #REGRA -> Isso cria uma expressão regular que procura qualquer caractere que NÃO seja A ATE Z, a ate z ou de 0 a 9
    string = regra.search(string) # Aqui ele procura o primeiro caractere inválido na string.Se encontrar vira um objeto match, se nao none
    return not bool(string)
checar_caracter("ADAOSKSAOJDSIJDSIS5648952")