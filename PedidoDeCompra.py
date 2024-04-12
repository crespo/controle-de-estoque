## must be a queue
from Estoque import Estoque

id = 0
  
class PedidoDeCompra:
    def __init__(self):
        self.pedidoDeCompra = []
        
    def add(self, pedidoDeCompra):
        self.pedidoDeCompra.append(pedidoDeCompra)     
        return 'Pedido de compra criado.'
    
    
    def removerPedido(self):
        return self.pedidoDeCompra.pop(0)
    
    
    def toString(self):
        for pedido in self.pedidoDeCompra:
            for produto in pedido:
                print(f"""
                    nome: {produto[0]}
                    quantidade: {produto[1]}
                    valor: {produto[2]}""")
            