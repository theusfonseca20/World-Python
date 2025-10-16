'''
O que é input?
Função que permite a entrada de dados pelo usuário durante a execução do programa.
'''


#Colocando as variáveis para receber dados do usuário
name = input("Digite qual é o nome do jogo: ")
yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
gamePrice = float(input("Digite o preço do jogo: "))
planInclude = input("Qual o plano de assinatura? (true/false): ").lower()
#int é usado para converter a entrada do ano de lançamento em um número inteiro.
#float é usado para converter a entrada do preço do jogo em um número decimal.
#lower() é usado para converter a entrada do plano de assinatura em minúsculas.

#Imprimindo valores das minhas variáveis
print(f"O nome do jogo é {name}")
print(f"O ano de lançamento do jogo é {yearLaunch}")
print(f"O preço do jogo é {gamePrice}")
print(f"O plano de assintaura é {planInclude}")







