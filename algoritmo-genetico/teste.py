import numpy as np
import matplotlib.pyplot as plt

# Definindo a função Alpine 2 para n=2
def alpine2(x):
    return np.prod(np.sqrt(x) * np.sin(x))

# Parâmetros do algoritmo genético
pop_size = 50           # Tamanho da população
num_generations = 100   # Número de gerações
mutation_rate = 0.1     # Taxa de mutação
crossover_rate = 0.8    # Taxa de crossover
n_dimensions = 2        # Dimensionalidade do problema (n=2)
lower_bound = 0         # Limite inferior para cada variável
upper_bound = 10        # Limite superior para cada variável

# Máximo Global da função
global_max = 2.808 ** n_dimensions
optimal_x = np.array([7.917] * n_dimensions)

# Inicializando a população
population = np.random.uniform(lower_bound, upper_bound, (pop_size, n_dimensions))

# Função de avaliação
def evaluate_population(pop):
    return np.array([alpine2(ind) for ind in pop])

# Função de seleção por torneio
def tournament_selection(pop, fitness, k=3):
    selected_indices = []
    for _ in range(len(pop)):
        participants = np.random.choice(np.arange(len(pop)), k, replace=False)
        best_idx = participants[np.argmax(fitness[participants])]
        selected_indices.append(best_idx)
    return pop[selected_indices]

# Função de crossover
def crossover(parent1, parent2):
    if np.random.rand() < crossover_rate:
        a = np.random.rand()

        child1 = a * parent1 + (1 - a) * parent2
        child2 = a * parent2 + (1 - a) * parent1

        child1 = np.clip(child1, lower_bound, upper_bound)
        child2 = np.clip(child2, lower_bound, upper_bound)
        return child1, child2
    return parent1, parent2

# Função de mutação
def mutate(individual):
    if np.random.rand() < mutation_rate:
        mutation_idx = np.random.randint(n_dimensions)
        individual[mutation_idx] += np.random.uniform(-1, 1)
        # Garantir que os valores estejam dentro dos limites
        individual = np.clip(individual, lower_bound, upper_bound)
    return individual

# Guardando os melhores fitnesses e valores da função objetivo ao longo das gerações
best_fitness_history = []
worst_fitness_history = []
best_individual_history = []
average_fitness_history = []

# Algoritmo genético
for generation in range(num_generations):
    # Avaliação da população
    fitness = evaluate_population(population)
    average_fitness = np.mean(fitness)
    average_fitness_history.append(average_fitness)
    
    # Seleção
    population = tournament_selection(population, fitness)
    
    # Crossover e Mutação
    new_population = []
    for i in range(0, pop_size, 2):
        parent1 = population[i]
        parent2 = population[i+1 if i+1 < pop_size else 0]
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])
    
    # Atualizar a população
    population = np.array(new_population)
    
    # Melhor indivíduo da geração
    best_fitness = np.max(fitness)
    worst_fitness = np.min(fitness)
    best_individual = population[np.argmax(fitness)]
    
    best_fitness_history.append(best_fitness)
    worst_fitness_history.append(worst_fitness)
    best_individual_history.append(best_individual)
    
    print(f"Geração {generation + 1}: Melhor Fitness = {best_fitness}, Melhor Indivíduo = {best_individual}")

    # Verifica se o máximo global foi alcançado
    if np.isclose(best_fitness, global_max, atol=1e-2):
        print(f"Máximo global encontrado na geração {generation + 1} com o valor {best_fitness} e o indivíduo {best_individual}")
        break

# Preencher os valores faltantes nas listas
num_executed_generations = len(best_fitness_history)

if num_executed_generations < num_generations:
    best_fitness_history.extend([best_fitness_history[-1]] * (num_generations - num_executed_generations))
    best_individual_history.extend([best_individual_history[-1]] * (num_generations - num_executed_generations))

# Resultados finais
best_fitness = np.max(evaluate_population(population))
best_individual = population[np.argmax(evaluate_population(population))]
print(f"\nMelhor solução encontrada: {best_individual}, Fitness: {best_fitness}")

# Exibir informações adicionais
print("\n--- Informações do Algoritmo Genético ---")
print(f"Tamanho da População: {pop_size}")
print("Forma de Seleção: Seleção por Torneio")
print("Tipo de Crossover: Crossover aritmético")
print(f"Taxa de Crossover: {crossover_rate}")
print(f"Taxa de Mutação: {mutation_rate}")


# Gráficos
# 1. Gráfico da função de fitness ao longo das gerações
plt.figure(figsize=(14, 6))
plt.ylim(0, None)
plt.subplot(1, 2, 1)
# Plotando o histórico do melhor fitness
plt.plot(range(1, num_generations + 1), best_fitness_history, label='Melhor Fitness', color='blue')

# Plotando o histórico do pior fitness
plt.plot(range(1, num_generations+ 1), worst_fitness_history, label='Pior Fitness', color='red')
plt.plot(range(1, num_generations + 1), average_fitness_history, label='Fitness Médio', color='green')
plt.title('Evolução da Fitness')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
plt.grid(True)

# 2. Gráfico da melhor função objetivo (f(x)) ao longo das gerações
plt.subplot(1, 2, 2)
objective_values = [alpine2(ind) for ind in best_individual_history]
plt.plot(range(1, num_generations + 1), objective_values, label='Função Objetivo')
plt.title('Evolução da Função Objetivo')
plt.xlabel('Gerações')
plt.ylabel('f(x)')
plt.grid(True)

plt.show()
