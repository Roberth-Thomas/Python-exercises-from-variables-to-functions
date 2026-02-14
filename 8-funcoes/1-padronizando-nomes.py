'''Exercício 1: Padronizador de Nomes de Produtos (Setor de E-commerce) Muitas
vezes, os nomes dos produtos entram no sistema de qualquer jeito (ex: "iPHonE 13", "
macbook air "). Crie uma função chamada padronizar_texto que receba uma string
como parâmetro e retorne esse texto sem espaços extras nas extremidades e com todas as
palavras com a primeira letra maiúscula (formato de título). Teste a função com uma lista de
nomes bagunçados.
produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", "
caixa de som bluetooth " ]'''

produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", "caixa de som bluetooth " ]

def corrige_nome_produto(texto):
    texto = texto.strip()
    texto = texto.title()
    return texto

produtos_arrumados = []

# Opção 1

for produto in produtos_baguncados:
    produto_padronizado = corrige_nome_produto(produto)
    produtos_arrumados.append(produto_padronizado)
print(f'Opção 1: {produtos_arrumados}')


# Opção 2 - for em uma linha é possível quando apenas temos uma única funcção dentro do for

produto_padronizado2 = [corrige_nome_produto(produto) for produto in produtos_baguncados]
print(f'Opção 2: {produto_padronizado2}')


# Opção 3

produto_padronizado3 = list(map(corrige_nome_produto, produtos_baguncados))
print(f'Opção 3: {produto_padronizado3}')
