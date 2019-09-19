from usuario import Usuario
from pedido import Pedido

class Comprador(Usuario):
    
    def __init__(self, carteiraComprador):
        self.carrinho = Pedido()
        self.carteiraComprador = carteiraComprador

    def getCarteiraComprador(self):
        return self.carteira

    def getCarrinho(self):
        return self.carrinho

    def setCarteira(self, valor, op):
        if op == "+":
            self.carteira += valor
        else:
            self.carteira -= valor 

    def addCarrinho(self, item):
        self.carrinho.addItem(item)
        return self.carrinho

    def finalizarCompra(self):
        for item in self.carrinho.itens:
            item.qtd -= 1
        return "COMPRA REALIZADA COM SUCESSO"
            


        

    