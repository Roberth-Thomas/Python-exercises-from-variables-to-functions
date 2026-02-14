'''Exercício 2: Calculadora de Imposto Sobre Serviço - ISS (Setor Fiscal) Crie uma função
chamada calcular_iss que receba o valor de um serviço.
● Se o valor for maior que R$ 5.000,00, a taxa é de 5%.
● Caso contrário, a taxa é de 3%. A função deve retornar o valor do imposto (e não o
valor total). Depois, use essa função para calcular o imposto de uma nota de R$
8.000,00 e outra de R$ 2.000,00, exibindo os resultados.'''

def calcular_iss(valor):

    if valor > 5000:
        taxa5 = valor * 0.05
        valor -= taxa5
    else:
        taxa3 = valor * 0.03
        valor -= taxa3
    return valor

def menu():
    
    print('Menu')
    print('1 - Calcular iss')
    print('2 - Sair')
    return input('Escolha uma opção: ')

while True:
    
    escolha = menu()

    if escolha == '1':
        try:
            valor = float(input('Digite o valor para calcular o iss: '))
            if valor > 0:
                resultado = calcular_iss(valor)
                print(f'Retirando o imposto o valor fica: {resultado}')
            else:
                print('Valor não pode ser 0 ou menor')
        
        except ValueError:
            print('Digite apenas números')
    
    elif escolha == '2':
        print('Programa encerrado.')
        break

    else:
        print('Pedimos que verifique o menu')
