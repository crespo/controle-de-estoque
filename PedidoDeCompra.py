class PedidoDeCompra:
    def __init__(self):
        self.pedidoDeCompra = []
        
    def add(self, pedidoDeCompra):
        self.pedidoDeCompra.append(pedidoDeCompra)     
        return 'Pedido de compra criado.'
    
    
    def removerPedido(self):
        return self.pedidoDeCompra.pop(0)
    
    
    def proximoPedido(self):
        if self.pedidoDeCompra:
            for produto in self.pedidoDeCompra[0]:
                print(f"nome: {produto[0]}\nquantidade: {produto[1]}\nvalor: {produto[2]}\n")
            return True
        else:
            print("Nenhum pedido de compra encontrado.")
            return False
    
    
    def toString(self):
        numeroPedido = 0
        if self.pedidoDeCompra:
            for pedido in self.pedidoDeCompra:
                numeroPedido += 1
                print(f"Pedido {numeroPedido}:")
                for produto in pedido:
                    print(f"Nome: {produto[0]}\nQuantidade: {produto[1]}\nValor: {produto[2]}")
                print("+----------------------+")
        else:
            print("Nenhum pedido de compra encontrado.")
            