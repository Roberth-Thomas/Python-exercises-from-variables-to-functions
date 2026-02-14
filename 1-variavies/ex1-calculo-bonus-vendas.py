'''Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento final da empresa
após subtrair esse bônus.
● Faturamento inicial: 50.000
● Percentual de bônus: 0.10'''

#comentário teste

# Funções:
def calcular_faturamento_bonus(faturamento, percentual_bonus):
    percentual = faturamento * percentual_bonus
    return faturamento + percentual

def menu():

    print('\n-----------Menu-----------\n')
    print('|1 - Calcular bonus de venda.')
    print('|2 - Encerrar programa.')
        
    return input('\nEscolha uma opção: ')

def calculo():

    try:
        digite_faturamento = float(input('Digite o faturamento: '))
        digite_percentual = float(input('Digite o percentual: '))
        porcentagem = digite_percentual / 100

        resultado = calcular_faturamento_bonus(digite_faturamento, porcentagem)

        print('-' * 100)
        print(f'O faturamento inicial foi de {digite_faturamento:,.2f} e com o percentual de {digite_percentual}% o faturamento final foi para: {resultado:,.2f}')
        print('-' * 100)

    except ValueError:
        print('\n! Digite apenas números !')

# Loop:
while True:

    escolha = menu()

    if escolha == '2':
        print('Programa encerrado')
        break

    elif escolha == '1':
        calculo()
    
    else:
        print('\n! Verifique o a opção escolhida !')
    
