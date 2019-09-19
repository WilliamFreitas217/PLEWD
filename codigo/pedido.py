class Pedido():
    def __init__(self, valor):
        self.valor = valor

    def addItem(self, item):
        self.itens.append(item)
        self.valor += item.valor