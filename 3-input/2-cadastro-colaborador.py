'''Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH) Ao cadastrar um novo
funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o
e-mail. Crie um programa que:
1. Peça o nome completo do colaborador.
2. Peça o e-mail pessoal do colaborador.
3. Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).
4. Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).
5. Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail
padronizado]".'''


nome_colaborador = input('Insira o nome do(a) colaborador(a): ').strip()
email_colaborador = input('Insira o e-mail do(a) colaborador(a): ').strip().lower()

posicao_primeiro_nome = nome_colaborador.find(' ', 0)
primeiro_nome = nome_colaborador[:posicao_primeiro_nome].title()

print(f'Cadastro concluído. Nome: {primeiro_nome} | E-mail: {email_colaborador}')
