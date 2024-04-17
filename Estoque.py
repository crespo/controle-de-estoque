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
                return estoque
        
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
        if self.estoque:
            print("Estoque atual:\n")
            for estoque in self.estoque:
                print(f"nome: {estoque.produto.nome}\nvalor: {estoque.produto.valor}\nquantidade: {estoque.quantidade}")
                print("+----------------------+")
        else:
            print('Estoque vazio.')
            
    
    def consultarValor(self, nome):
        for estoque in self.estoque:
            if estoque.produto.nome == nome:
                return estoque.produto.valor
        
        return 'Produto não encontrado.'
    
    def recolocarEstoque(self, venda):
        pedido = venda[0]
        for produto in pedido:
            nome, quantidade = produto[0], produto[1]
            estoqueAtual = self.consultarEstoque(nome).quantidade
            self.alterarEstoque(nome, estoqueAtual + quantidade)