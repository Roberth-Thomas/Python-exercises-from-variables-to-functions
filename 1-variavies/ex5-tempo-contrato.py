'''Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente
quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de
divisão inteira e resto da divisão para converter os 40 meses.'''

duracao_projeto_meses = 40
meses_do_ano = 12

anos = duracao_projeto_meses // meses_do_ano
meses = duracao_projeto_meses % meses_do_ano

print(f'O projeto levará {anos} anos e {meses} meses')