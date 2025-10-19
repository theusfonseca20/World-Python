gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports.
Ele é conhecido por seus gráficos realistas, jogabilidade envolvente e
uma ampla variedade de modos de jogo, incluindo carreira, torneios e multiplayer online.
"""

#Métodos de string
print(gameName.upper()) #Retorna a string em maiúsculas
print(gameName.lower()) #Retorna a string em minúsculas
print(gameName.capitalize()) #Retorna a string com a primeira letra em maiúscula
print(gameName.find("a")) #Retorna o índice da primeira ocorrência do caractere "a"
print(gameDescription.count("a")) #Conta quantas vezes o caractere "a" aparece na string
print(gameDescription.replace("Fifa", "PES")) #Substitui "Fifa" por "PES" na string
print(gameDescription.split(",")) #Divide a string em uma lista, usando a vírgula como separador ou outro caractere especificado