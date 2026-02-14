'''Sua empresa mudou de nome
e todos os funcionários que usavam o domínio @empresa.com.br agora devem usar o
domínio @grupocorp.com. O e-mail do funcionário é andre_silva@empresa.com.br.
Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo
endereço de e-mail.'''

lista_de_email = ['andre_silva@empresa.com.br', 'marco_santos@empresa.com.br', 'sonia_alencar@empresa.com.br']

for email in lista_de_email:
    novo_email = email.replace('@empresa.com.br.', '@grupocorp.com')
    print(novo_email)