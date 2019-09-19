from usuario import Usuario
from comprador import Comprador
from pedido import Pedido
from produto import Produto 
from item import ItemProduto
from vendedor import Vendedor

vendedor = Vendedor()
comprador = Comprador(10)

produto1 = Produto(2,1.5,'brigadeiro')
produto2 = Produto(1,2.5,"trufa")

vendedor.setEstoque(produto1)
vendedor.setEstoque(produto2)
print(vendedor.getEstoque())

comprador.addCarrinho(produto1)
comprador.addCarrinho(produto2)

comprador.finalizarCompra()
print(vendedor.getEstoque())


# print(comprador.getCarrinho())
