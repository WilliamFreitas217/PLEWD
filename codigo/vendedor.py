from usuario import Usuario
from produto import Produto 

class Vendedor(Usuario):

    def __init__(self):
        self.carteira = 0
        self.estoque = []

    def getCarteira(self):
        return self.carteira

    def getEstoque(self):
        return self.estoque

    def setCarteira(self, valor):
        self.carteira += valor
    
    def setEstoque(self, produto):
        self.estoque.append(produto)

