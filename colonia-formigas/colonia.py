import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a distância entre duas cidades
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Inicialização das coordenadas das cidades
cities = [
    (4, 8), (8, 8), (12, 8), (0, 7), (2, 7), (6, 7), (9, 7),
    (4, 6), (6, 6), (8, 6), (11, 6), (1, 5), (3, 5), (4, 5),
    (7, 5), (9, 5), (4, 4), (9, 4), (12, 4), (0, 3), (2, 3),
    (7, 3), (11, 3), (4, 2), (6, 2), (10, 2), (1, 1), (5, 1),
    (8, 1), (11, 1), (3, 0), (9, 0)
]

n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))

# Preenchendo a matriz de distâncias
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Parâmetros do ACO
n_ants = 20
n_iterations = 100
evaporation_rate = 0.5
alpha = 1  # Influência dos feromônios
beta = 2   # Influência da heurística

# Inicialização dos feromônios
pheromone_matrix = np.ones((n_cities, n_cities)) / n_cities

def construct_solution():
    # Construção de uma solução por uma formiga
    route = []
    visited = [False] * n_cities
    current_city = np.random.randint(n_cities)
    route.append(current_city)
    visited[current_city] = True
    for _ in range(n_cities - 1):
        probabilities = []
        for next_city in range(n_cities):
            if not visited[next_city]:
                prob = (pheromone_matrix[current_city][next_city] ** alpha) * \
                       ((1 / distance_matrix[current_city][next_city]) ** beta)
                probabilities.append(prob)
            else:
                probabilities.append(0)
        probabilities = np.array(probabilities)
        probabilities = probabilities / probabilities.sum()
        next_city = np.random.choice(range(n_cities), p=probabilities)
        route.append(next_city)
        visited[next_city] = True
        current_city = next_city
    return route

def update_pheromones(best_route, best_length):
    global pheromone_matrix
    pheromone_matrix *= (1 - evaporation_rate)
    for i in range(len(best_route) - 1):
        pheromone_matrix[best_route[i]][best_route[i + 1]] += 1 / best_length
    pheromone_matrix[best_route[-1]][best_route[0]] += 1 / best_length

# Algoritmo ACO
best_route = None
best_length = float('inf')

for iteration in range(n_iterations):
    all_routes = []
    for _ in range(n_ants):
        route = construct_solution()
        route_length = sum(distance_matrix[route[i]][route[i + 1]] for i in range(n_cities - 1)) + distance_matrix[route[-1]][route[0]]
        all_routes.append((route, route_length))
        if route_length < best_length:
            best_route = route
            best_length = route_length
    update_pheromones(best_route, best_length)
    print(f"Iteration {iteration + 1}/{n_iterations}, Best Length: {best_length}")

# Exibição da melhor rota
print("Best route:", best_route)
print("Best length:", best_length)

# Plotando a solução
x = [cities[i][0] for i in best_route] + [cities[best_route[0]][0]]
y = [cities[i][1] for i in best_route] + [cities[best_route[0]][1]]
plt.figure(figsize=(10, 10))
plt.scatter([city[0] for city in cities], [city[1] for city in cities], color='red')
plt.plot(x, y, 'b-')
plt.title('Best Route Found by ACO')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
