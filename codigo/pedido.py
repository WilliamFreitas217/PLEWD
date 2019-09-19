class Pedido():
    def __init__(self):
        self.valor = 0
        self.itens = []

    def addItem(self, item):
        self.itens.append(item)
        self.valor += item.valor

    def __repr__(self):
        return "<Itens: {}, Valor: {}>".format(self.itens, self.valor)