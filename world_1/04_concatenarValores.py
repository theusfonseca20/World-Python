#O objetivo de concatenar é juntar os valores de variáveis diferentes em uma única string para exibição ou processamento.

#Abaixo está o código do arquivo 03_input.py, que coleta dados do usuário e os armazena em variáveis, concatenando-os em mensagens formatadas para exibição.")
name = input("Digite qual é o nome do jogo: ")
yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
gamePrice = float(input("Digite o preço do jogo: "))
planInclude = input("Qual o plano de assinatura? (true/false): ").lower()

print(f"O nome do jogo é {name}")
print(f"O ano de lançamento do jogo é {yearLaunch}")
print(f"O preço do jogo é {gamePrice}")
print(f"O plano de assintaura é {planInclude}")

# Também podemos concatenar utilizando o operaodr + ou usando a vírgula , dentro do print. Mas o mais recomendado é usar f""
