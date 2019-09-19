from usuario import Usuario
from produto import Produto 

class Vendedor(Usuario):

    def __init__(self):
        self.carteira = 0
        self.estoque = []

    def getCarteira(self):
        return self.carteira

    def getEstoque(self):
        produtoList = []
        for item in self.estoque:
            produtoList.append([item.qtd,item.valor,item.nomeProduto])
        return produtoList

    def setCarteira(self, valor):
        self.carteira += valor
    
    def setEstoque(self, produto):
        self.estoque.append(produto)

