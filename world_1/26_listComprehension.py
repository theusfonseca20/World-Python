# List Comprehension -> Comprimir uma expressão de laço de repetição em uma única linha de código

for numero in range(10):
    if numero <= 4:
        print(numero)

# Usando List Comprehension para fazer a mesma coisa em uma linha
listNumbers = [numero for numero in range(10) if numero <= 4] # Cria uma lista com os números de 0 a 9 que são menores ou iguais a 4
print(listNumbers)

gameList = ["Mario", "Sonic", "Pokemon", "Zelda"]
newList = [jogo for jogo in gameList if "a" in jogo] # Cria uma nova lista com os jogos que contém a letra "a"
print(newList)
