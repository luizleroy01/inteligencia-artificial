'''
Primeiro, você define as cidades com suas coordenadas no plano 2D e calcula a matriz de distâncias entre todas as cidades. A função `euclidean_distance` é usada para calcular a distância entre duas cidades com base nas suas coordenadas (x,y)(x, y)(x,y).
'''

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [ ... ]  # Coordenadas das cidades
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))

# Preenchendo a matriz de distâncias
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

'''
2. Inicialização dos Feromônios
O ACO utiliza uma matriz de feromônios para guiar as formigas na construção de rotas. Inicialmente, todos os valores são iguais e baixos.
'''
pheromone_matrix = np.ones((n_cities, n_cities)) / n_cities

'''
3. Parâmetros do Algoritmo
Você define os parâmetros do ACO:

n_ants: Número de formigas que irão construir soluções.
n_iterations: Número de iterações do algoritmo.
evaporation_rate: Taxa de evaporação dos feromônios.
alpha: Peso dos feromônios na decisão da formiga.
beta: Peso da heurística (distância) na decisão da formiga.
'''

def construct_solution():
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


#iterações
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


#Resultado e visualização
print("Best route:", best_route)
print("Best length:", best_length)

x = [cities[i][0] for i in best_route] + [cities[best_route[0]][0]]
y = [cities[i][1] for i in best_route] + [cities[best_route[0]][1]]
plt.figure(figsize=(10, 10))
plt.scatter([city[0] for city in cities], [city[1] for city in cities], color='red')
plt.plot(x, y, 'b-')
plt.title('Best Route Found by ACO')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

