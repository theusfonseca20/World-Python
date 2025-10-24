# Laço de repetição for
lista = ["Fifa", "God of War", "Minecraft", "The Last of Us", "Cyber Punk", "Mario Bros"]
# O jogo vai receber cada um dos valores da lista, um por vez (iterando = passando por cada um)
for jogo in lista:
    print("O jogo é:", jogo) #Vai imprimir cada jogo da lista
print("Fim da lista de jogos")

# Quando a condição for atendida, o laço for para de executar
for jogo in lista:
    if jogo == "Minecraft":
        print("Achei o jogo que você queria", jogo) #Vai imprimir quando achar minecraft
        break #Interrompe o laço for
    print("O jogo é:", jogo)# Vai imprimir cada jogo da lista até achar minecraft
print("Fim da busca pelo jogo")

#Quando a condição for atendida, o laço for vai para a próxima iteração
for jogo in lista:
    if jogo == "The Last of Us":
        continue # Vai pular essa iteração e vai para a próxima
    print(jogo)

# Avaliação do jogo
gameName = input("Digite o nome do jogo: ")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo: "))
soma = 0 #Recebe o valor inicial da soma das notas
for i in range(gameRating): # Vai repetir o bloco de código a quantidade de vezes que o usuário digitou
    nota = float(input("Digite a sua nota para o jogo: "))
    soma += nota
print("A media das notas do jogo", gameName, "é de:", soma/gameRating)

