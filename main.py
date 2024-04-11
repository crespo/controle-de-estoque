from Produto import Produto
from Estoque import Estoque

def criarProduto(nome, valor, quantidade):
    produtoNovo = Produto(nome, valor, quantidade)
    estoque.add(produtoNovo)
    
    ## debug prints
    print('Produto criado:')
    print(produtoNovo.toString())


estoque = Estoque()

while True:
    userInput = input("""
                    1 - Criar Produto
                    S - Sair
                    """)

    if userInput == "1":
        nome = input('Digite o nome do produto: ')
        valor = input('Digite o valor do produto: ')
        quantidade = input('Digite a quantidade do produto: ')
        criarProduto(nome, valor, quantidade)
        
    elif userInput.lower() == "s":
        break
        

