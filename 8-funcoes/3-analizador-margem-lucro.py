'''Exercício 3: Analisador de Margem de Lucro (Setor Financeiro) Crie uma função
chamada analisar_margem que receba o faturamento e o custo. A função deve calcular a
margem (lucro / faturamento).
● Se a margem for maior ou igual a 30%, retorne "Margem Saudável".
● Se for menor que 30%, retorne "Margem Baixa". Exiba o resultado da função para
um produto que faturou R$ 10.000,00 com custo de R$ 6.000,00.'''

def menu():

    print('Bem-vindo(a) ao calculador de margem de lucro =)')

    try:
        f = float(input('Digite o faturamento: '))
        c = float(input('Digite o custo: '))

        if f <= 0:
            print("Erro: O faturamento deve ser maior que zero.")
            return None, None

        return f, c

    except ValueError:
        print('Pedimos que insira apenas números.')
        return None, None

def analisar_margem(faturamento, custo):
    lucro = faturamento - custo
    margem = lucro / faturamento

    if margem >= 0.3:
        return 'Margem Saudável'
    else: 
        return 'Margem Baixa'

fat, cust = menu()

if fat is not None:
    resultado = analisar_margem(fat, cust)
    print(resultado)

else:
    print('Operação cancelada devido a entrada inválida')

