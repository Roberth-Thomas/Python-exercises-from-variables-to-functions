'''Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as
vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um
programa que exiba um pequeno relatório contendo:
1. O total de vendas na semana.
2. A média de vendas diária.
3. O valor da melhor venda e da pior venda do período.'''

vendas = [1500, 2000, 800, 3500, 1200]
print(vendas)

soma_de_vendas = sum(vendas)
qtd_dias = len(vendas)
media_vendas = soma_de_vendas/qtd_dias

maior_venda = max(vendas)
menor_venda = min(vendas)

print(f'''

Valor total de vendas: {soma_de_vendas}
Média de vendas: {media_vendas}
Maior valor vendido: {maior_venda}
Menos valor vendido: {menor_venda}

''')

