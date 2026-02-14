'''Exercício 3: Divisão de Cargas (Logística/Transporte)
Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
última viagem menor? (Use %)'''

'''boxes = 1250
volume_truck = 12

boxes % 2

max_volume_truck = boxes // volume_truck

remainder_box = boxes % volume_truck

print(f'{max_volume_truck} trucks at full capacity will be necessary and 1 truck with {remainder_box} boxes, because the remainder of boxes is {remainder_box}.')
'''

def menu():

    print('Menu')
    print('1 - Verificar estoque atual e caminhões disponíveis')
    print('2 - Despachar cargas')
    return input ('Escolha uma opção: ')

estoque_atual_caixas = 1250
quantidade_caminhao = 12

dicionario = {estoque_atual_caixas: quantidade_caminhao}

def mensagem():
    return print(f'Nº de Caminhões: {quantidade_caminhao} | Qauntidade de Cargas: {estoque_atual_caixas}')

def despachar():

    selecao = int(input('Selecione a quantidade de cargas a serem enviadas: '))
    dicionario[estoque_atual_caixas] =- selecao
    print(dicionario)

while True:

    escolha = menu()

    if escolha == '1':
        mensagem()

    if escolha == '2':
        despachar()
    
