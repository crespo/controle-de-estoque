import os
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
0 - Sair
"""
           
            
def menuProduto():
    return """
1 - Criar Produto
2 - Remover Produto
0 - Voltar
"""
            
            
def menuEstoque():
    return """
1 - Consultar Estoque
2 - Consultar Estoque (Produto)
0 - Voltar
"""
            
def menuPedidoDeCompra():
    return """
1 - Novo Pedido de Compra
2 - Consultar Pedidos de Compra
3 - Processar Pedido de Compra
0 - Voltar
"""

def menuVenda():
    return """
1 - Consultar Vendas
2 - Desfazer Última Venda
0 - Voltar
"""

estoque = EstoqueLista()
pedidoDeCompra = PedidoDeCompra()
vendas = Vendas()

while True:
    userInput = input(menuPrincipal())
    
    if userInput == "1":
        os.system('cls')
        while True:
            userInput = input(menuProduto())
            
            if userInput == "1": ## criar produto
                os.system('cls')
                while True:
                    nome = input('Digite o nome do produto: ')
                    valor = input('Digite o valor do produto: ')
                    quantidade = input('Digite a quantidade do produto: ')
                    if not valor.isnumeric() or not quantidade.isnumeric():
                        os.system('cls')
                        print('Valor e quantidade devem ser valores numéricos.')
                        continue
                    criarProduto(nome, valor, quantidade)
                    break

            elif userInput == "2": ## remover produto
                os.system('cls')
                nome = input('Digite o nome do produto: ')
                print(estoque.removerEstoque(nome))
            
            elif userInput == "0": ## voltar
                os.system('cls')
                break
            
            else:
                os.system('cls')
                print('Opção inválida.')
    
    elif userInput == "2":
        os.system('cls')
        while True:
            userInput = input(menuEstoque())
    
            if userInput == "1": ## consultar estoque
                os.system('cls')
                estoque.toString()
        
            elif userInput == "2": ## consultar estoque (produto)
                os.system('cls')
                nome = input('Digite o nome do produto: ')
                retorno = estoque.consultarEstoque(nome)
                
                if isinstance(retorno, str):
                    print(retorno)
                else:
                    print(f"Estoque atual de {nome}: {retorno.quantidade}")
    
            # elif userInput == "3": ## alterar estoque (produto)
            #     while True:
            #         nome = input('Digite o nome do produto: ')
            #         quantidade = input('Digite a nova quantidade: ')
            #         if not quantidade.isnumeric():
            #             print('Quantidade deve ser um valor numérico.')
            #             continue
            #         estoque.alterarEstoque(nome, quantidade)
            #         break
        
            elif userInput == "0": ## voltar
                os.system('cls')
                break
            
            else:
                os.system('cls')
                print('Opção inválida.')
    
    elif userInput == "3":
        os.system('cls')
        while True:
            userInput = input(menuPedidoDeCompra())
            
            if userInput == "1": ## novo pedido de compra
                os.system('cls')
                pedidoDeCompraNovo = []
                
                while True:
                    nome = input('Digite o nome do produto: ')
                    quantidade = input('Digite a quantidade do produto: ')
                    
                    if quantidade.isnumeric():
                        quantidade = int(quantidade)
                    else:
                        os.system('cls')
                        print('Quantidade deve ser um valor numérico.')
                        continue
                    
                    retorno = estoque.consultarEstoque(nome)
                    
                    if isinstance(retorno, str):
                        os.system('cls')
                        print(retorno)
                    else: 
                        if int(retorno.quantidade) < quantidade:
                            os.system('cls')
                            print(f'Quantidade não disponível.\nEstoque atual de "{nome}": {retorno.quantidade}')
                        else:
                            podeIncluir = True
                            for pedido in pedidoDeCompraNovo:
                                if nome in pedido:
                                    podeIncluir = False
                            
                            if podeIncluir:
                                valor = int(estoque.consultarValor(nome)) * quantidade
                                pedidoDeCompraNovo.append([nome, str(quantidade), str(valor)])
                            else:
                                os.system('cls')
                                print('Produto já incluído no pedido de compra.')   
                
                    continuar = input("Pressione ENTER para continuar...\n0 - Finalizar Pedido\n")
                    
                    if continuar == "0":
                        if not pedidoDeCompraNovo:
                            os.system('cls')
                            print('Pedido de compra descartado.')
                        else:
                            os.system('cls')
                            print(pedidoDeCompra.add(pedidoDeCompraNovo))
                        break
            
            elif userInput == "2": ## consultar pedidos de compra
                os.system('cls')
                pedidoDeCompra.toString()
                
            elif userInput == "3": ## processar pedido de compra
                os.system('cls')
                if not pedidoDeCompra.proximoPedido():
                    print('Nenhum pedido de compra encontrado.')
                else:
                    while True:
                        userInput = input('1 - Processar pedido de compra\n2 - Descartar pedido de compra\n0 - Voltar')
                        if userInput == "1":
                            os.system('cls')
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
                                print('Venda concluída.')
                            else:
                                pedidoDeCompra.add(pedido)
                                print('Pedido recolocado no final da fila.')
                        
                        elif userInput == "2":
                            os.system('cls')
                            pedido = pedidoDeCompra.proximoPedido()
                            
                            while pedido:
                                confirmar = input('\nDeseja excluir o pedido acima?\n1 - Sim, 2 - Não\n')
                                if confirmar == "1":
                                    pedidoDeCompra.removerPedido()
                                    os.system('cls')
                                    print('Pedido excluído com sucesso.')
                                elif confirmar == "2":
                                    os.system('cls')
                                    print('Pedido não excluído')
                                else:
                                    os.system('cls')
                                    print('Digite 1 para confirmar e 2 para cancelar.\n')
                        
                        elif userInput == "0":
                            break
                        
                        else:
                            os.system('cls')                        
                            print('Opção inválida.')              
            
            elif userInput == "0":
                break
                        
            else:
                os.system('cls')
                print('Opção inválida.')
        
     
     
    elif userInput == "4":
        while True:
            userInput = input(menuVenda())
            
            if userInput == "1":
                vendas.consultarVenda()
                
            elif userInput == "2":
                while True:
                    if vendas.consultarVenda():
                        userInput = input('Deseja excluir a venda acima?\n1 - Sim, 2 - Não\n')
                        
                        if userInput == "1":
                            venda = vendas.excluirVenda()
                            estoque.recolocarEstoque(venda)
                            print('Venda cancelada com sucesso.\nEstoque restituído.')
                            break
                        
                        elif userInput == "2":
                            break
                        
                        else:
                            print('Opção inválida.')
                    else:
                        break
                        
            elif userInput == "0":
                os.system('cls')
                break
            else:
                os.system('cls')
                print('Opção inválida.')
                
    elif userInput == "0":
        os.system('cls')
        break
    
    else:
        os.system('cls')
        print('Opção inválida.')
