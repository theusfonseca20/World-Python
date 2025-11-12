#Criando uma classe:
class Filme:
    def __init__(self, nome, ano_lancamento, incluso_plano, duraco_minutos):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.incluso_plano = incluso_plano
        self.total_notas = 0
        self.duracao_minutos = duraco_minutos
        self.total_avaliadores = 0
        
    def __str__(self):
        return f"O nome do filme é {self.nome}"
    
    def ficha_filme(self):
        print(f"Nome do filme: {self.nome}")
        print(f"Ano de lançamento: {self.ano_lancamento}")
        print(f"Avaliação do Filme: {self.total_notas}")
        print(f"Total de Avaliadores: {self.total_avaliadores}")
              
    
    def avaliacao(self, nota):
        self.total_notas += nota
        self.total_avaliadores += 1
    
    def media(self):
        print(f"A média do filme {self.nome} é {self.total_notas/self.total_avaliadores}")

mario = Filme("Super Mario", 2023, False, 135)
avatar = Filme("Avatar", 2023, False, 180)

mario.avaliacao(9.5)
mario.avaliacao(10.0)
mario.ficha_filme()
mario.media()