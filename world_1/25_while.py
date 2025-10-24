#Laço While

gameName = input("Digite o nome do jogo: ")
contador = 0 #Contador para controlar o número de avaliações
nota = 0 #Variável para armazenar a nota digitada pelo usuário
totalNotas = 0 #Variável para armazenar a soma das notas

while nota != -1:
    nota = float(input("Digite a nota para o jogo: "))
    if nota != -1:
        totalNotas += nota
        contador += 1 

# Verifica se houve pelo menos uma nota antes de calcular a média
if contador == 0:
    print("Nenhuma nota informada. Não é possível calcular a média.")
else:
    media = totalNotas / contador
    print("A média das notas do jogo", gameName, "é de:", media)