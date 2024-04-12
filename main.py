from Produto import Produto
from Estoque import Estoque, EstoqueLista
from PedidoDeCompra import PedidoDeCompra

def criarProduto(nome, valor, quantidade):
    produtoNovo = Produto(nome, valor)
    retorno = estoque.add(Estoque(produtoNovo, quantidade))
    print(retorno)


def menuPrincipal():
    return """
            1 - Produtos
            2 - Estoque
            3 - Pedidos de Compra
            4 - Vendas
            0 - Sair"""
           
            
def menuProduto():
    return """
            1 - Criar Produto
            2 - Remover Produto
            0 - Voltar"""
            
            
def menuEstoque():
    return """
            1 - Consultar Estoque
            2 - Consultar Estoque (Produto)
            3 - Alterar Estoque (Produto)
            0 - Voltar"""
            
def menuPedidoDeCompra():
    return """
            1 - Novo Pedido de Compra
            2 - Consultar Pedidos de Compra
            3 - Processar Pedido de Compra
            0 - Voltar"""

def menuVenda():
    return """
            1 - Consultar Vendas
            2 - Desfazer Última Venda
            0 - Voltar"""

estoque = EstoqueLista()
pedidoDeCompra = PedidoDeCompra()

while True:
    userInput = input(menuPrincipal())
    
    if userInput == "1":
        while True:
            userInput = input(menuProduto())
            
            if userInput == "1":
                nome = input('Digite o nome do produto: ')
                valor = input('Digite o valor do produto: ')
                quantidade = input('Digite a quantidade do produto: ')
                criarProduto(nome, valor, quantidade)

            elif userInput == "2":
                nome = input('Digite o nome do produto: ')
                estoque.removerEstoque(nome)
            
            elif userInput == "0":
                break
            
            else:
                print('Opção inválida.')
    
    elif userInput == "2":
        while True:
            userInput = input(menuEstoque())
    
            if userInput == "1":
                estoque.toString()
        
            elif userInput == "2":
                nome = input('Digite o nome do produto: ')
                retorno = estoque.consultarEstoque(nome)
                
                if isinstance(retorno, str):
                    print(retorno)
                else:
                    print(retorno.quantidade)
    
            elif userInput == "3":
                nome = input('Digite o nome do produto: ')
                quantidade = input('Digite a nova quantidade: ')
                estoque.alterarEstoque(nome, quantidade)
        
            elif userInput == "0":
                break
            
            else:
                print('Opção inválida.')
    
    elif userInput == "3":
        userInput = input(menuPedidoDeCompra())
        
        if userInput == "1":
            pedidoDeCompraNovo = []
            
            while True:
                nome = input('Digite o nome do produto: ')
                quantidade = int(input('Digite a quantidade do produto: '))
                
                retorno = estoque.consultarEstoque(nome)
                
                if isinstance(retorno, str):
                    print(retorno)
                else: 
                    if int(retorno.quantidade) < quantidade:
                        print(f'qtd: {retorno.quantidade}')
                        print('Quantidade não disponível.')
                    else:
                        podeIncluir = True
                        for pedido in pedidoDeCompraNovo:
                            if nome in pedido:
                                podeIncluir = False
                        
                        if podeIncluir:
                            valor = int(estoque.consultarValor(nome)) * quantidade
                            pedidoDeCompraNovo.append([nome, str(quantidade), str(valor)])
                        else: 
                            print('Produto já incluído.')   
            
                continuar = input("""
                                  Pressione ENTER para continuar...
                                  0 - Finalizar Pedido""")
                
                if continuar == "0":
                    pedidoDeCompra.add(pedidoDeCompraNovo)
                    break
        
        elif userInput == "2":
            pedidoDeCompra.toString()
            
        
        
    elif userInput == "0":
        break
    
    else:
        print('Opção inválida.')
    
        
        
        
        

