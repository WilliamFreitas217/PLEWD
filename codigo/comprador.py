from usuario import Usuario
from pedido import Pedido

class Comprador(Usuario):
    
    def __init__(self, carrinho, carteiraComprador):
        self.carrinho = carrinho
        self.carteiraComprador = carteiraComprador

    def getCarteiraComprador(self):
        return self.carteira

    def getCarrinho(self):
        car = []
        for item in self.carrinho:
            car.append([[item.qtd,item.valor,item.nomeProduto]])
        return car

    def setCarteira(self, valor, op):
        if op == "+":
            self.carteira += valor
        else:
            self.carteira -= valor 

    def addCarrinho(self, item):
        self.carrinho.addItem(item)
        return self.carrinho

    def finalizarCompra(self,item):
        pedido = Pedido()
        for item in carrinho:
            pedido.addItem(item)
        
        return pedido