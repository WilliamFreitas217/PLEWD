class Produto():
    def __init__(self, qtd, valor, nomeProduto):
        self.qtd = qtd
        self.valor = valor
        self.nomeProduto = nomeProduto

    def cadastrarItem(self, qtd, valor, nomeProduto):
        self.qtd = qtd
        self.valor = valor
        self.nomeProduto = nomeProduto

    def __repr__(self):
        return "<Quantidade: {}, Valor: {}, Nome: {}>".format(self.qtd, self.valor, self.nomeProduto)