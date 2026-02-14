'''Exercício 4: Verificador de Meta de Vendedores (Setor Comercial) Crie uma função
chamada quem_bateu_meta que receba dois parâmetros: um dicionário de vendedores
(onde a chave é o nome e o valor é o faturamento) e o valor da meta. A função deve
percorrer o dicionário e imprimir: "Vendedor [Nome] bateu a meta!" apenas para aqueles
que atingiram ou superaram o valor da meta. Dica: Use um loop for dentro da função.
equipe_vendas = { "João": 12000, "Maria": 9500, "Ricardo": 10000, "Fernanda": 15200,
"Paulo": 5000 }; meta_objetivo = 10000'''

equipe_vendas = { "João": 12000, "Maria": 9500, "Ricardo": 10000, "Fernanda": 15200,
"Paulo": 5000 }

meta_objetivo = 10000

def quem_bateu_meta(vendas_dos_vendedores: dict, meta: float):
    for vendedor in vendas_dos_vendedores:
        if vendas_dos_vendedores[vendedor] >= meta:
            print(f'Vendedor(a) {vendedor} bateu a meta ! Vendeu: {vendas_dos_vendedores[vendedor]}')

quem_bateu_meta(equipe_vendas, meta_objetivo)

