'''Exercício 4: Análise de Metas Combinadas (Setor Comercial) Uma empresa paga bônus
se a meta individual do vendedor E a meta da loja forem batidas.
1. Peça as vendas do vendedor e a meta individual dele.
2. Peça as vendas totais da loja e a meta da loja.
3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus é de 20% sobre
as vendas do vendedor.
4. Caso contrário, o bônus é zero. Exiba a mensagem: "Seu bônus este mês é de:
R$[valor]".'''

# Vendedor 1
vendas_vendedor1 = input('Digite as vendas do Vendedor 1 separadas por ",": ')
lista_de_vendas1 = [float(venda) for venda in vendas_vendedor1.split(',')]
print(f'Lista de vendas do Vendedor 1: {lista_de_vendas1}')
total_venda_vendedor_1 = sum(lista_de_vendas1)

# Veta vendedor = total de vendas dividodo pela quantidade de vendas
meta_vededor1 = total_venda_vendedor_1 / len(lista_de_vendas1)

# Vendedor 2
vendas_vendedor2 = input('Digite as vendas do Vendedor 2 separadas por ",": ')
lista_de_vendas2 = [float(venda) for venda in vendas_vendedor2.split(',')]
print(f'Lista de vendas do Vendedor 2: {lista_de_vendas2}')
total_venda_vendedor_2 = sum(lista_de_vendas2)

# Veta vendedor = total de vendas dividodo pela quantidade de vendas
meta_vededor2 = total_venda_vendedor_2 / len(lista_de_vendas2)

total_vendas = lista_de_vendas1 + lista_de_vendas2
sum_vendas = sum(total_vendas)
meta_loja = sum(total_vendas) / len(total_vendas)
print(f'A meta da loja é: {meta_loja}')

if total_venda_vendedor_1 > meta_vededor1 and meta_loja < sum_vendas:
    lucro20 = 0.20
    bonus_vendedor1 = total_venda_vendedor_1 * lucro20
    print(f'Como o vendedor1 vendeu a meta de {meta_vededor1} e ganhou um bonus de 20% {bonus_vendedor1}: {meta_loja + bonus_vendedor1}')

elif total_venda_vendedor_2 > meta_vededor2 and meta_loja < sum_vendas:
    lucro20 = 0.20
    bonus_vendedor2 = total_venda_vendedor_2 * lucro20
    print(f'Como o vendedor2 vendeu a meta de {meta_vededor2} e ganhou um bonus de 20% {bonus_vendedor2}: {meta_loja + bonus_vendedor1}')

else: 
    print('A meta não foi atingida')

