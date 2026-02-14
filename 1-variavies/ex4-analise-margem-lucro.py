'''Exercício 4: Análise de Margem de Lucro (Financeiro)
Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).'''

faturamento = 15000.00
custos_fixos = 5000.00
percentual_imposto = 0.15

imposto_do_faturamento = faturamento * percentual_imposto
print(f'O imposto foi de 15% sobre o faturamento. Imposto = {imposto_do_faturamento}')

lucro = faturamento - custos_fixos - imposto_do_faturamento
print(f'Com o faturamento de {faturamento} menos os custos fixos de {custos_fixos} e menos o imposto de {imposto_do_faturamento}, o lucro foi de {lucro}')

margem = lucro / faturamento

print(margem)

margem_atingida = margem > 0.3

print(margem_atingida)