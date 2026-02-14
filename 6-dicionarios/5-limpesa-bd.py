'''Exercício 5: Limpeza de Banco de Dados (Setor de TI) O sistema de e-commerce
descontinuou alguns produtos. Você tem o dicionário: produtos = {"celular": 1500,
"camera": 800, "radio": 200, "fone": 100}. O item "radio" deve ser removido
por estar obsoleto. Crie um código que:
1. Remova o item "radio" do dicionário usando o método .pop().
2. Imprima o valor do produto que foi removido para fins de log.
3. Verifique se o produto "celular" ainda existe no dicionário e imprima True ou False.'''

produtos = {"celular": 1500,"camera": 800, "radio": 200, "fone": 100}

item_a_ser_removido = input('Digite um item que deseja excluir: ').strip().lower()

valor_item_removido = produtos[item_a_ser_removido]

produtos.pop(item_a_ser_removido)

print(produtos)

verifica_item = input('Digite o nome do produto que deseja verificar se está na tabela: ').strip().lower()

if verifica_item in produtos:
    print(f'Ainda há {verifica_item} no estoque como o valor de {produtos[verifica_item]}')