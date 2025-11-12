# Criar um molde (uma planta baixa) para um novo tipo de 'coisa' no meu programa. O nome desse molde é Filme
class Filme:
    """
    __init__ é o construtor. Ele é uma função que roda automaticamente toda vez que você cria um novo objeto a partir do molde Filme
    self é a palavra-chave mais confusa, mas mais importante, é uma referência ao próprio objeto que está sendo criado.
    def __str__(self): Este é outro método mágico. Ele define o que o Python deve fazer quando você tenta "imprimir" o objeto diretamente
    """
    def __init__ (self, nome, ano_lancamento, incluso_plano, nota, duracao_minutos):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.incluso_plano = incluso_plano
        self.nota = nota
        self.duracao_minutos = duracao_minutos
    def __str__(self):
        return f"Filme: {self.nome}"

#instanciando/criando um objeto
filme = Filme("Telefone Preto 2", 2025, False, 7.3, 113)
filme2 = Filme("Invocação do Mal - O Último Ritual", 2025, False, 7.0, 130)
print(filme)
print(filme.nome)
print(f"O filme {filme.nome} lançado em {filme.ano_lancamento} é muito bom")
print(f"O filme {filme2.nome} lançado em {filme2.ano_lancamento} é mais ou menos")