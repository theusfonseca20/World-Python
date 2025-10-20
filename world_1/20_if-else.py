#Definindo variáveis (str, int e float)
name = input("Digite o nome do jogo: ")
yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
classification = float(input("Digite a classificação do jogo: "))

#Condicional se a classificação for maior ou igual a 8.0 execute o codigo no bloco if
if classification >= 8.0 or yearLaunch >= 2020: #posso usar o or para adicionar mais uma condição ou and para exigir que ambas as condições sejam verdadeiras
    print(f"O jogo {name} lançado no ano de {yearLaunch} é muito bom!!!!")
else: #SE NÃO, execute o codigo no bloco else
    print("O jogo é ruim, não recomendo!!!")