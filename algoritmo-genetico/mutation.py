# por troca

def mutacao_troca(individuo):
    idx1, idx2 = random.sample(range(len(individuo)), 2)
    individuo[idx1], individuo[idx2] = individuo[idx2], individuo[idx1]
    return individuo


#por inversao

def mutacao_inversao(individuo):
    idx1, idx2 = random.sample(range(len(individuo)), 2)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    individuo[idx1:idx2+1] = reversed(individuo[idx1:idx2+1])
    return individuo
