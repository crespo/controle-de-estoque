class Vendas:
    def __init__(self):
        self.vendas = []
        
    def addVenda(self, venda):
        self.vendas.append(venda)
        
    def excluirVenda(self):
        return self.vendas.pop()