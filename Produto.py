from Estoque import Estoque


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
    def toString(self):
        return f'''
                nome: {self.nome}
                valor: {self.valor}
                '''