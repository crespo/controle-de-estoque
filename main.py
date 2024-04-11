from Produto import Produto
from Estoque import Estoque, EstoqueLista

def criarProduto(nome, valor, quantidade):
    produtoNovo = Produto(nome, valor)
    estoque.add(Estoque(produtoNovo, quantidade))
    
    ## debug prints
    print('Produto criado:')
    print(produtoNovo.toString())


estoque = EstoqueLista()

while True:
    userInput = input("""
                    1 - Criar Produto
                    2 - Consultar Estoque do Produto
                    S - Sair
                    """)

    if userInput == "1":
        nome = input('Digite o nome do produto: ')
        valor = input('Digite o valor do produto: ')
        quantidade = input('Digite a quantidade do produto: ')
        criarProduto(nome, valor, quantidade)
        
    elif userInput == "2":
        nome = input('Digite o nome do produto: ')
        print(estoque.consultarEstoque(nome))
        
    elif userInput.lower() == "s":
        break
        

