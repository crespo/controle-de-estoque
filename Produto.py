from Estoque import Estoque

id = 0

class Produto:
    def __init__(self, nome, valor, quantidade):
        global id
        id += 1
        self.id = id
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        
    def toString(self):
        return f'''
                id: {self.id}
                nome: {self.nome}
                valor: {self.valor}
                quantidade: {self.quantidade}
                '''