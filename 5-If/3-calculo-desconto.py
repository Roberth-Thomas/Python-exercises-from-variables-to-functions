'''Um e-commerce
aplica descontos automáticos no carrinho. Crie um programa que receba o valor total da
compra e aplique a seguinte lógica:
● Compras a partir de R$ 500,00: 15% de desconto.
● Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
● Compras abaixo de R$ 200,00: Sem desconto. O programa deve exibir o valor do
desconto e o valor final a pagar, formatados em R$.'''

valor_informado = float(input('Digite o valor da compra: '))

if valor_informado >= 500:
    desconto15 = valor_informado * 0.15
    volor_total = valor_informado - desconto15
    print(f'Valor {valor_informado:,.2f} - Desconto 15%: {desconto15:,.2f} = Valor Total: {volor_total:,.2f}')

elif valor_informado >= 200:
    desconto10 = valor_informado * 0.10
    volor_total = valor_informado - desconto10
    print(f'Valor {valor_informado:,.2f} - Desconto 10%: {desconto10:,.2f} = Valor Total: {volor_total:,.2f}')

else:
    print(f'Valor sem desconto: {valor_informado:,.2f}')
