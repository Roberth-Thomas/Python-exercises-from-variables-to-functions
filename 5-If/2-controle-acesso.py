'''Exercício 2: Controle de Acesso ao Sistema (Setor de Segurança) Você tem uma lista
de e-mails de administradores: admins = ["ana@empresa.com",
"guilherme@empresa.com", "felipe@empresa.com"]. Crie um programa que peça
o e-mail do usuário. O programa deve:
1. Padronizar o e-mail (letras minúsculas e sem espaços).
2. Verificar se o e-mail está na lista de admins.
3. Se estiver, exibir: "Acesso liberado! Bem-vindo ao painel de controle".
4. Caso contrário, exibir: "Acesso negado. Você não tem permissões de administrador".'''

admins = ["ana@empresa.com","guilherme@empresa.com", "felipe@empresa.com"]

inserir_email = input('Insira o e-mail: ').lower().strip()

if inserir_email in admins:
    print('Acesso permitido')
else:
    print('Acesso negado')

