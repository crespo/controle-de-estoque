from Produto import Produto
from Estoque import Estoque, EstoqueLista
from PedidoDeCompra import PedidoDeCompra
from Venda import Vendas

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
vendas = Vendas()

while True:
    userInput = input(menuPrincipal())
    
    if userInput == "1":
        while True:
            userInput = input(menuProduto())
            
            if userInput == "1": ## criar produto
                while True:
                    nome = input('Digite o nome do produto: ')
                    valor = input('Digite o valor do produto: ')
                    quantidade = input('Digite a quantidade do produto: ')
                    if not valor.isnumeric() or not quantidade.isnumeric():
                        print('Valor e quantidade devem ser um valores numéricos.')
                        continue
                    criarProduto(nome, valor, quantidade)
                    break

            elif userInput == "2": ## remover produto
                nome = input('Digite o nome do produto: ')
                estoque.removerEstoque(nome)
            
            elif userInput == "0": ## voltar
                break
            
            else:
                print('Opção inválida.')
    
    elif userInput == "2":
        while True:
            userInput = input(menuEstoque())
    
            if userInput == "1": ## consultar estoque
                estoque.toString()
        
            elif userInput == "2": ## consultar estoque (produto)
                nome = input('Digite o nome do produto: ')
                retorno = estoque.consultarEstoque(nome)
                
                if isinstance(retorno, str):
                    print(retorno)
                else:
                    print(retorno.quantidade)
    
            elif userInput == "3": ## alterar estoque (produto)
                while True:
                    nome = input('Digite o nome do produto: ')
                    quantidade = input('Digite a nova quantidade: ')
                    if not quantidade.isnumeric():
                        print('Quantidade deve ser um valor numérico.')
                        continue
                    estoque.alterarEstoque(nome, quantidade)
                    break
        
            elif userInput == "0": ## voltar
                break
            
            else:
                print('Opção inválida.')
    
    elif userInput == "3":
        userInput = input(menuPedidoDeCompra())
        
        if userInput == "1": ## novo pedido de compra
            pedidoDeCompraNovo = []
            
            while True:
                nome = input('Digite o nome do produto: ')
                quantidade = input('Digite a quantidade do produto: ')
                
                if quantidade.isnumeric():
                    quantidade = int(quantidade)
                else:
                    print('Quantidade deve ser um valor numérico.')
                    continue
                
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
                    if not pedidoDeCompraNovo:
                        print('Pedido de compra descartado.')
                    else:
                        pedidoDeCompra.add(pedidoDeCompraNovo)
                        
                    break
        
        elif userInput == "2": ## consultar pedidos de compra
            pedidoDeCompra.toString()
            
        elif userInput == "3": ## processar pedido de compra
            if not pedidoDeCompra.proximoPedido():
                print('Nenhum pedido de compra encontrado')
            else:
                userInput = input('1 - Processar pedido de compra\n2 - Descartar pedido de compra\n0 - Voltar')
                if userInput == "1":
                    pedido = pedidoDeCompra.removerPedido()
                    nomesPedido, valoresPedido, quantidadesPedido, estoquesPedido = [], [], [], []
                    estoquesOk = True
                    
                    for produto in pedido:
                        nomesPedido.append(produto[0])
                        quantidadesPedido.append(produto[1])
                        valoresPedido.append(produto[2])
                        estoquesPedido.append(int(estoque.consultarEstoque(produto[0]).quantidade))
                        
                        if int(quantidadesPedido[-1]) > estoquesPedido[-1]:
                            print(f'Estoque do produto "{nomesPedido[-1]}" insuficiente.\nEstoque atual: {estoquesPedido[-1]}\nQuantidade do pedido: {quantidadesPedido[-1]}\n')
                            print('Venda não realizada.')
                            estoquesOk = False
                            break
                                                    
                    if estoquesOk:
                        valorTotal = 0
                        for i in range(0, len(nomesPedido)):
                            nomePedido = nomesPedido[i]
                            quantidadePedido = int(quantidadesPedido[i])
                            estoquePedido = int(estoquesPedido[i])
                            valorTotal += int(valoresPedido[i])
                            
                            estoque.alterarEstoque(nomePedido, str(estoquePedido - quantidadePedido))
                        
                        vendas.addVenda([pedido, str(valorTotal)])
                    else:
                        pedidoDeCompra.add(pedido)
                        print('Pedido recolocado no final da fila.')
                
                elif userInput == "2":
                    pedido = pedidoDeCompra.proximoPedido()
                    
                    while pedido:
                        confirmar = input('\nDeseja excluir o pedido acima? 1 - Sim, 2 - Não')
                        if confirmar == "1":
                            pedidoDeCompra.removerPedido()
                            print('Pedido excluído com sucesso.')
                        elif confirmar == "2":
                            print('Pedido não excluído')
                        else:
                            print('\nDigite 1 para confirmar e 2 para cancelar.')
                
                elif userInput == "0":
                    break
                
                else:
                    print('Opção inválida.')              
        
        elif userInput == "0":
            break
                    
        else:
            print('Opção inválida.')
        
        
    elif userInput == "0":
        break
    
    else:
        print('Opção inválida.')
