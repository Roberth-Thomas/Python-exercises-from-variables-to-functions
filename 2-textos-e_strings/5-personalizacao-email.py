'''Exercício 5: Personalização de E-mail de Marketing (Setor de Marketing) O marketing
quer enviar um e-mail de boas-vindas. O cliente forneceu o nome completo: lucas
ferreira souza. Você deve extrair apenas o primeiro nome para usar na saudação (ex:
"Olá, Lucas!"). O código deve:
1. Encontrar a posição do primeiro espaço.
2. Fatiar o texto para pegar apenas o primeiro nome.
3. Formatar o nome com a primeira letra maiúscula.
4. Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"'''

nome_completo = 'lucas ferreira souza'


posicao_nome = nome_completo.find(' ', 0)

nome = nome_completo[:posicao_nome].title()

print(f'Olá, {nome}')
