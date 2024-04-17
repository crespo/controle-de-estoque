class Vendas:
    def __init__(self):
        self.vendas = []
        
    def addVenda(self, venda):
        self.vendas.append(venda) # estrutura venda: [pedido, valorTotal]
        
    def excluirVenda(self):
        return self.vendas.pop()
    
    def consultarVenda(self):
        if self.vendas:
            venda = self.vendas[-1]
            pedido = venda[0]
            valorTotal = venda[1]
            print('Vendas:\n')
            for produto in pedido:
                print(f"Nome: {produto[0]}\nQuantidade: {produto[1]}\nValor: {produto[2]}")
                print("+----------------------+")
            
            print(f'Valor total: R$ {valorTotal}')
            return True
        else:
            print('Nenhuma venda encontrada.')
            return False