'''A empresa "LogTrack" tem uma
rota de entregas: rota = ["Sao Paulo", "Campinas", "Jundiai",
"Sorocaba"]. Novas cidades foram adicionadas por uma empresa parceira:
novas_cidades = ["Itu", "Valinhos"]. Seu script deve:
1. Unir as duas listas em uma só (usando extend).
2. Identificar em qual posição (índice) está a cidade de "Sorocaba".
3. Exibir a lista completa e a posição encontrada.
4. Exibir uma mensagem final: “Sorocaba é a Xa cidade da rota”'''


rota = ["Sao Paulo", "Campinas", "Jundiai","Sorocaba"]

novas_cidades = ["Itu", "Valinhos"]

rota.extend(novas_cidades)

localiza_sorocaba_index = rota.index('Sorocaba')
n_posicao_sorocaba = localiza_sorocaba_index + 1
sorocaba = rota[localiza_sorocaba_index]

print(f'Lista de todas as rotas: {rota}')
print(f'{sorocaba} é a {n_posicao_sorocaba}ª cidade da rota')
