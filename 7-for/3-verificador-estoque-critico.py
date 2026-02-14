'''Exercício 3: Verificação de Estoque Crítico (Setor de Logística) Dada a lista de produtos
estoque_produtos = ["monitor", "teclado", "mouse", "headset",
"gabinete"] e a lista correspondente de quantidades estoque_quantidades = [5,
12, 2, 8, 15]. O estoque mínimo para qualquer item é 8 unidades. Crie um programa
que percorra as listas e, para cada item que esteja abaixo do mínimo, imprima: "ALERTA: O
produto [nome] está com apenas [quantidade] unidades no estoque!".'''

estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]

estoque_quantidades = [5, 12, 2, 8, 15]

def une_listas(estoque_produtos, estoque_quantidades):
    return dict(zip(estoque_produtos, estoque_quantidades))

lista_produtos_e_estoque = une_listas(estoque_produtos, estoque_quantidades)

print(f'Estoque atual: {lista_produtos_e_estoque}')

for produto, quantidade in lista_produtos_e_estoque.items():
    
    if quantidade < 8:
        print(f'ALERTA: O produto {produto.title()} está com apenas {quantidade} unidade(s) no estoque!')
