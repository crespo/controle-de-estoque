import Produto

class Estoque:
    def __init__(self):
        self.estoque = []
        
    def add(self, Produto):
        self.estoque.append(Produto)
        
    def print(self):
        for item in self.estoque:
            print(item.id)
            print(item.nome)
            print(item.valor)
            print(item.quantidade)