gamesLista = ["Resident Evil 4", "Star Wars Jedi: Survivor", "Hogwarts Legacy",
            "The Last of Us Part I", "The Legende of Zelda: Tears of the Kingdom"]

print(len(gamesLista)) #retorna o tamanho da lista
print(gamesLista.index("Hogwarts Legacy")) #retorna o índice do elemento especificado

gamesLista.append("Cyberpunk 2077") #adiciona um elemento ao final da lista
print(gamesLista)

gamesLista.sort() #ordena a lista em ordem alfabética
print(gamesLista)

gamesReset = gamesLista.copy() #cria uma cópia da lista
gamesReset.remove("Star Wars Jedi: Survivor") #remove o elemento especificado da lista
print(gamesReset)

gamesReset.clear() #remove todos os elementos da lista
print(gamesReset)

gamesLista.pop() #remove o último elemento da lista
print(gamesReset)