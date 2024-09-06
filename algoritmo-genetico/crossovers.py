#ponto único
def crossover_ponto_unico(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

#dois pontos
def crossover_dois_pontos(pai1, pai2):
    ponto1 = random.randint(1, len(pai1) - 2)
    ponto2 = random.randint(ponto1 + 1, len(pai1) - 1)
    filho1 = pai1[:ponto1] + pai2[ponto1:ponto2] + pai1[ponto2:]
    filho2 = pai2[:ponto1] + pai1[ponto1:ponto2] + pai2[ponto2:]
    return filho1, filho2

#aritmético

def crossover_aritmetico(pai1, pai2, alpha=0.5):
    filho1 = alpha * np.array(pai1) + (1 - alpha) * np.array(pai2)
    filho2 = (1 - alpha) * np.array(pai1) + alpha * np.array(pai2)
    return filho1.tolist(), filho2.tolist()



#uniforme
def crossover_uniforme(pai1, pai2):
    filho1 = [random.choice([p1, p2]) for p1, p2 in zip(pai1, pai2)]
    filho2 = [p2 if p1 != f1 else p1 for p1, p2, f1 in zip(pai1, pai2, filho1)]
    return filho1, filho2

#media
def crossover_media(pai1, pai2):
    filho = (np.array(pai1) + np.array(pai2)) / 2
    return filho.tolist()