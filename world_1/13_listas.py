#Lista é uma forma de armazenar múltiplos valores em uma única variável.
#Listas são mutáveis, ou seja, seus valores podem ser alterados após a criação da lista.
#Listas são definidas por colchetes [] e os valores são separados por vírgulas.

gameFifa = ["Fifa 23", 2022, 90.65, True] #criando uma lista com diferentes tipos de dados
print(gameFifa)

#Criando uma lista de jogos
gamesLista = ["Resident Evil 4", "Star Wars Jedi: Survivor", "Hogwarts Legacy",
            "The Last of Us Part I", "The Legende of Zelda: Tears of the Kingdom"]
print(gamesLista)

print(gamesLista[0]) #Acessando o primeiro elemento da lista
print(gamesLista[2]) #Acessando o terceiro elemento da lista)
print(gamesLista[0:2]) #Fatiamento de lista (slice) - do índice 0 ao índice 1
print(gamesLista[-1]) #Acessando o último elemento da lista
print(gamesLista[1:4]) #Fatiamento de lista (slice) - do índice 1 ao índice 3