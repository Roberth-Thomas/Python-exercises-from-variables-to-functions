'''Exercício 1: Automação de Convites (Setor de Eventos/RH) A empresa terá um
treinamento e você precisa simular o envio de 10 lembretes no console fazendo a contagem
regressiva para aparecer no sistema da empresa. Use a função range() para imprimir 10
vezes a mensagem: "Lembrete: O treinamento de Python começa em X minutos.
'''

tempo = range(10, -1, -1)

for s in tempo:
    print(f'Lembrete ! O treinamento começa em {s} minutos')


