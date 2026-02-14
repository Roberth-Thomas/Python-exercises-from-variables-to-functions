'''Um gerente quer comparar o
desempenho de duas filiais. O programa deve:
1. Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar
números decimais).
2. Calcular o faturamento total das duas lojas.
3. Calcular a média de faturamento entre elas.
4. Exibir uma única mensagem formatada informando o total e a média, utilizando o
separador de milhar e duas casas decimais.'''

while True:

    try:

        escolha_usuario = int(input('''
        Escolha uma opção:

        1 - Começar
        2 - Encerrar
        
        '''))

        if escolha_usuario == int('2'):
            print('Programa encerrado.')
            break

        else:
            try:

                fat_loja_a = float(input('Digite o faturamento da loja A: '))
                fat_loja_b = float(input('Digite o faturamento da loja B: '))

                total_fat = fat_loja_a + fat_loja_b
                media_tat_lojas = (total_fat / 2)

                print('-' * 30)
                print(f'Total faturado na loja A: {fat_loja_a:,.2f} | na loja B: {fat_loja_b:,.2f}')
                print(f'O total faturado nas lojas A e B é {total_fat:,.2f} | A média entra elas é de: {media_tat_lojas:,.2f}')
                print('-' * 30)

            except ValueError:
                print('Digite apenas valores.')
    
    except ValueError:
        print('-' * 30)
        print('Ecolha entre as opções do menu.')
        print('-' * 30)
