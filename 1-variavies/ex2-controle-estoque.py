'''Exercício 2: Controle de Estoque de E-commerce (Logística)
Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no
estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um
fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final.'''

'''stock_smartphone_initial = 250
sales = 78
product_arived = 100

smartphones_in_stock = stock_smartphone_initial - sales + product_arived

print(f'The value of smartphones in stock is: {smartphones_in_stock}')'''

'''

dicionario = {nome_produto:quantidade_inicial}

print(dicionario)
'''
dicionario = {}

# Funções
def menu():

    print('MENU')
    print('1 - Verificar estoque')
    print('2 - Adiconar produto e estoque: ')
    print('3 - Fazer uma venda de um produto')
    print('4 - Encerrar')
    return input('Escolha uma opção: ')

def verifica_estoque():

    if not dicionario:
        print('Não há itens no estoque.')
    else:
        print(dicionario)

def adiciona_item_no_estoque():

    nome_produto = input('Digite o nome do produto: ').strip().title()
    quantidade_inicial = int(input('Digite a quantidade inicial em estoque: '))
    dicionario[nome_produto] =  quantidade_inicial
    print(dicionario)

def venda_produto():

    produto_no_dicionario = input('Digite o nome do produto que deseja fazer uma venda: ').strip().title()
    
    if produto_no_dicionario in dicionario:
        quantidade_de_vendas = int(input('Digite a quantidade vendida: '))
        if quantidade_de_vendas <= dicionario[produto_no_dicionario]:
            dicionario[produto_no_dicionario] -= quantidade_de_vendas
            print(dicionario)
        else:
            print(f'Erro ! Estoque insuficiente. Há somente {dicionario[produto_no_dicionario]} unidade(s)')
    
    else:
        print('Produto não encontrado.')

# Loop principal

while True:

    escolha = menu()

    if escolha == '1':
        verifica_estoque()

    elif escolha == '2':
        adiciona_item_no_estoque()
    
    elif escolha == '3':
        venda_produto()

    elif escolha == '4':
        print('Programa encerrado.')
        break
    
    else:
        print('Verifique o valor informado')
    
