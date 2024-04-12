import Produto

class Estoque:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        
        
class EstoqueLista:
    def __init__(self):
        self.estoque = []
       
        
    def add(self, estoqueNovo):
        for estoque in self.estoque:
            if estoque.produto.nome == estoqueNovo.produto.nome:
               return 'Produto de mesmo nome já existe.'
                
        self.estoque.append(estoqueNovo)
        return 'Produto criado.'
        
        
    def consultarEstoque(self, nome):
        for estoque in self.estoque:
            if estoque.produto.nome == nome:
                return f'Quantidade: {estoque.quantidade}'
        
        return 'Produto não encontrado.'
            
        
    def removerEstoque(self, nome):
        for estoque in self.estoque:
            if estoque.produto.nome == nome:
                self.estoque.remove(estoque)
                return 'Produto removido.'
        
        return 'Produto não encontrado.'
        
    
    def alterarEstoque(self, nome, quantidade):
        for estoque in self.estoque:
            if estoque.produto.nome == nome:
                index = self.estoque.index(estoque)
                self.estoque[index].quantidade = quantidade
    
    
    def toString(self):
        for estoque in self.estoque:
            print(f"""
                  nome: {estoque.produto.nome}
                  valor: {estoque.produto.valor}
                  quantidade: {estoque.quantidade}
                  """)