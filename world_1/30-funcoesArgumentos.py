# 1 - crie uma função que receba dois argumentos
def full_name(nome, sobrenome):
    print(f"O nome completo é {nome} {sobrenome}")
full_name("Matheus", "Ribeiro")

# 2 - crie uma função que some dois números via parâmetros
def soma(x, y):
    return x + y
print(soma(5,4))

# 3 - Argumentos default em uma função
def endereco(pais="Brasil"):
    print(f"Eu moro no {pais}")
endereco()
endereco("Espanha")

# 4 - Avaliação de um jogo
def media_jogo(qtdAvaliacoes):
    nome = input("Digite o nome do jogo: ")
    soma = 0
    for i in range(qtdAvaliacoes):
        nota = float(input("Digite a nota do jogo: "))
        soma += nota
    print(f"A media do {nome} é {soma/qtdAvaliacoes}")

media_jogo(2)