class Filme:
    def __init__(self, nome, ano_lancamento, plano_incluso, nota, duracao_minutos):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.plano_incluso = plano_incluso
        self.nota = nota
        self.duracao_minutos = duracao_minutos
    
    def __str__(self):
        return f"Filme: {self.nome}"
    
    def ficha_tecnica(self):
        print("\n------Dados dos filmes------")
        print(f"Nome do filme:{self.nome}")
        print(f"Ano de lançamento: {self.ano_lancamento}")
        print(f"Está no plano? {self.plano_incluso}")
        print(f"Nota: {self.nota}")
        print(f"Duração em minutos: {self.duracao_minutos}")

telefone_preto2 = Filme("Telefone Preto 2", 2025, False, 7.3, 113)
invocaco_mal4 = Filme("Invocação do Mal - O Último Ritual", 2025, False, 7.0, 130)

telefone_preto2.ficha_tecnica()
invocaco_mal4.ficha_tecnica()