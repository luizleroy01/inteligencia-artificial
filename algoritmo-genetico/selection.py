#torneio

def torneio_selecao(populacao, tamanho_torneio=3):
    selecionados = random.sample(populacao, tamanho_torneio)
    selecionado = max(selecionados, key=lambda ind: ind['fitness'])
    return selecionado


#roleta

def roleta_selecao(populacao):
    total_fitness = sum(ind['fitness'] for ind in populacao)
    escolha = random.uniform(0, total_fitness)
    fitness_acumulado = 0

    for ind in populacao:
        fitness_acumulado += ind['fitness']
        if fitness_acumulado >= escolha:
            return ind
