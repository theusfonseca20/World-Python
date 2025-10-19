gameDescription = """
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports.
Ele é conhecido por seus gráficos realistas, jogabilidade envolvente e
uma ampla variedade de modos de jogo, incluindo carreira, torneios e multiplayer online.
"""
gameName = "Fifa"
gameVersion = "23"

#1 - Operação de concatenção de strings
gameFullName = gameName + " " + gameVersion #Concatenação de strings
print(gameFullName)

#2- Operação de multiplicação de strings
line = "-" * 30
print(line)

#3 - Procurar uma plavra dentro de um texto
print("Futebol" in gameDescription) #Vai retornar True ou False
print("futebol" in gameDescription) #Vai retornar True ou False