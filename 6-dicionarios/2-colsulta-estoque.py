'''A empresa possui o
seguinte estoque: estoque = {"teclado": 50, "mouse": 120, "monitor": 30}.
Crie um programa que peça para o usuário digitar o nome de um produto.
1. Se o produto existir no estoque, exiba a quantidade disponível.
2. Se o produto não existir, exiba a mensagem: "Produto não encontrado no sistema".
Dica: Lembre-se de tratar o input para evitar erros de letras maiúsculas ou espaços.'''

estoque = {"teclado": 50, "mouse": 120, "monitor": 30}

tem_no_estoque = input('Digite o produto que desaja verificar no estoque: ').lower().strip()

if tem_no_estoque in estoque:
    estoque[tem_no_estoque]
    print(f'Produto: {tem_no_estoque.title()} | Estoque: {estoque[tem_no_estoque]}')

else:
    print("Produto não encontrado no sistema")