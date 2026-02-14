'''Uma importadora listou os
preços de frete em dólar: fretes = [50, 80, 20, 150, 40]. Para apresentar em uma
reunião, você deve:
1. Ordenar a lista do maior para o menor preço.
2. Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova
lista chamada top_fretes.
3. Exibir a lista original ordenada e a lista dos top_fretes.'''

fretes = [50, 80, 20, 150, 40]

# 1. Ordenar a lista do maior para o menor preço.
fretes.sort(reverse=True)
print(f'Lista dos fretes em cordem decrescente: {fretes}')

# 2. Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova lista chamada top_fretes.
top_fretes = fretes[:2]

print(f'Top 2 fretes com maior valor: {top_fretes}')

