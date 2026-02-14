'''Exercício 3: Análise de Faturamento por Região (Setor Financeiro) Dada a lista de
faturamento por região: vendas_regiao = {"Norte": 15000, "Sul": 22000,
"Leste": 18000, "Oeste": 25000}. Seu programa deve:
1. Extrair todos os valores (faturamentos) para uma lista.
2. Calcular e exibir o faturamento total da empresa (soma de todas as regiões).
3. Calcular e exibir o faturamento médio das regiões.'''

vendas_regiao = {"Norte": 15000, "Sul": 22000,"Leste": 18000, "Oeste": 25000}

print('Região | Faturamento')
for regiao, faturamento  in vendas_regiao.items():
    print(f'{regiao} - {faturamento:,.2f}')

faturamento_total = (sum(vendas_regiao.values()))
print(f'Total faturado: {faturamento_total:,.2f}')

numero_regioes = len(vendas_regiao.values())
print(f'Quantidade de regiões: {numero_regioes}')

media_faturamento = faturamento_total / numero_regioes
print(f'A média de faturento é: {media_faturamento:,.2f}')



