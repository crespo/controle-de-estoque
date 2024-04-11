from Estoque import Estoque

id = 0

class Produto:
    def __init__(self, nome, valor):
        global id
        id += 1
        self.id = id
        self.nome = nome
        self.valor = valor
        
    def toString(self):
        return f'''
                id: {self.id}
                nome: {self.nome}
                valor: {self.valor}
                '''