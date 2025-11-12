#Criando nossa primeira classe
class Filme:
    nome = "Telefone Preto 2"
    ano_lancamento = 0
    incluso_plano = False
    nota = 0
    duracao_minutos = 0
    
#Criando a instÂncia da minha classe (objetos da mina classe)
#Primeiro filme

filme = Filme()
print(filme)
#O retorno vai ser <__main__.Filme object at 0x7f46302bf1c0>, o objeto foi criado na nossa classe Filme

#inserindo os valores
filme.nome = "Telefone Preto 2"
filme.ano_lancamento = 2025
filme.incluso_plano = False
filme.nota = 7.2
filme.duracao_minutos = 114

print("*****Dados do filme*****")
print(f"Nome do filme: {filme.nome} \n Ano de lançamento: {filme.ano_lancamento}")
