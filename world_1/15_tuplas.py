#Usamos parênteses para definir uma tupla
#Possui algumas semelhanças com listas, mas são imutáveis
#Ou seja, uma vez criada, seus valores não podem ser alterados

gamesTuples = ("Fifa 23", "Resident Evil 4", "Star Wars Jedi: Survivor", "Hogwarts Legacy",
            "The Last of Us Part I", "The Legende of Zelda: Tears of the Kingdom")
print(gamesTuples)
print(type(gamesTuples))

print(gamesTuples[0]) #Acessando o primeiro elemento da tupla
print(gamesTuples[0:2]) #Pegando do índice 0 ao índice 1
print(gamesTuples[-1]) #Acessando o último elemento da tupla
print(gamesTuples[2:])  #Pegando do índice 2 até o final da tupla
print(gamesTuples.index("Hogwarts Legacy")) #Retorna o índice do elemento especificado

