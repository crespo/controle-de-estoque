import Produto

class Estoque:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        
        
class EstoqueLista:
    def __init__(self):
        self.estoque = []
        
    def add(self, Produto):
        self.estoque.append(Produto)
        
    def consultarEstoque(self, nome):
        for estoque in self.estoque:
            if estoque.produto.nome == nome:
                return estoque.quantidade
        
    # def alterarEstoque(self, nome, quantidadeNova)
        
    def print(self):
        for item in self.estoque:
            print(item.id)
            print(item.nome)
            print(item.valor)
            print(item.quantidade)