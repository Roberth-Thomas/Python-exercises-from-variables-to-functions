'''Calculadora de Imposto sobre Vendas (Setor Fiscal) Uma empresa de
serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o
valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
1. Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
2. Limpar o texto removendo o "R$" e trocando a vírgula por ponto. - REMOVIDO DO EXERCICIO
3. Converter para número decimal (float).
4. Calcular o valor do imposto (15% do valor bruto).
5. Exibir uma mensagem formatada com f-string mostrando o valor do imposto com
duas casas decimais.'''

while True:

    escolha_usuario = float(input('Digite o valor bruto ou 0 para encerrar o programa: '))

    if escolha_usuario == '0':
        break

    elif escolha_usuario is str:
        print('Digite apenas valores: ')
    
    else:
        imposto = escolha_usuario * 0.15
        valor_final = escolha_usuario - imposto
        print(f'Valor bruto: {escolha_usuario:,.2f}')
        print(f'O imposto corresponde a: {imposto:,.2f}')
        print(f'O valor final corresponde a: {valor_final:,.2f}')
