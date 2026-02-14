'''Exercício 5: Atualização de Preços Interativa (Input + Lista) Você tem uma lista de
preços de produtos: precos = [100.0, 250.0, 500.0] e uma com o nome: vinhos
= ["Branco", "Tinto","Champagne"]. Crie um programa interativo que:
1. Peça para o usuário digitar qual o nome do produto.
2. Peça para o usuário digitar o novo preço.
3. Atualize o preço na lista e exiba as listas completas com os nomes e os preços'''

# Listas:
vinhos = ["Branco", "Tinto","Champagne"]
precos = [100.0, 250.0, 500.0]

# Funções:
def mostra_vinho():
    for v in vinhos:
        print(v)
    return

def mostra_preco():
    for p in precos:
        print(p)
    return

def printer():
    print('-' * 50 )
    print('Lista de vinhos: \n')
    mostra_vinho()
    print('\nLista de preços: \n')
    mostra_preco()
    print('-' * 50 )

def atualiza_preco():

    escolha_do_vinho = input('Digite o nome do vinho: ')

    if escolha_do_vinho in vinhos:
        posicao_vinho = vinhos.index(escolha_do_vinho)
        novo_preco = float(input('Digite o novo valor: '))
        precos[posicao_vinho] = novo_preco

        print('\nSegue Lista atualizada:')
        printer()

    else:
        print('\n! Nome do vinho está errado ou não há na lista !')
        

# Programa:
while True:

    try:

        print('''
        
        1 - Verificar lista de vinhos seus preços
        2 - Atualizar preço de um vinho
        3 - Sair
        ''')

        escolha_usuario = int(input('\nEscolha uma opção: '))

        if escolha_usuario == 3:
            print('Programa encerrado')
            break

        elif escolha_usuario == 1:
            printer()
        
        elif escolha_usuario == 2:
            atualiza_preco()
            
        else:
            print('\n! Digite um valor correspondente ao menu !')
            
    except ValueError:
        print('-' * 30)
        print('Digite apenas números.')
        print('-' * 30)


