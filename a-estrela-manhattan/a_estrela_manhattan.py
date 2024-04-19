import heapq
"""
Nomes: Luiz Eduardo Leroy Souza (20213002126) e Sulamita Ester Costa(20213001568)
Data: 19/04/2024

Decisões de implementação:
Utilização da fila de prioridades pois é possível garantir uma ordem interna a estrutura de dados e garante que o item de maior
prioridade é o item de menor custo. Dessa forma foi possível criar uma classe com todas as funções necessárias para a resolução
do quebra cabeça como a função da distancia manhattan e o calculo da distancia considerando a heuristica a partir da distancia
manhatan
"""

def print_puzzle(puzzle):
    for line in puzzle:
        for piece in line:
            print(piece,end=" ")
        print()

class Puzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def manhattan_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def is_goal_state(self, state):
        return state[0][0] == 0 and state[0][1:] == [1, 2] and state[1] == [3, 4, 5] and state[2] == [6, 7, 8]

    def possible_moves(self, state):
        moves = []
        zero_pos = None
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    zero_pos = (i, j)
                    break

        x, y = zero_pos
        if x > 0:
            moves.append((x - 1, y))
        if x < 2:
            moves.append((x + 1, y))
        if y > 0:
            moves.append((x, y - 1))
        if y < 2:
            moves.append((x, y + 1))

        return moves

    def apply_move(self, state, move):
        new_state = [row[:] for row in state]
        x1, y1 = move
        x2, y2 = None, None
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x2, y2 = i, j
                    break
        new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
        return new_state

    def manhattan_heuristic(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    target_x = int((state[i][j] - 1) / 3)
                    target_y = (state[i][j] - 1) % 3
                    distance += self.manhattan_distance(i, j, target_x, target_y)
        return distance

    def solve(self):
        open_set = [(self.manhattan_heuristic(self.initial_state), 0, self.initial_state, [])]
        closed_set = set()

        while open_set:
            _, cost, current_state, path = heapq.heappop(open_set)

            if self.is_goal_state(current_state):
                return cost, path

            closed_set.add(tuple(map(tuple, current_state)))

            for move in self.possible_moves(current_state):
                new_state = self.apply_move(current_state, move)
                if tuple(map(tuple, new_state)) not in closed_set:
                    new_cost = cost + 1
                    new_path = path + [move]
                    heapq.heappush(
                        open_set,
                        (
                            new_cost + self.manhattan_heuristic(new_state),
                            new_cost,
                            new_state,
                            new_path,
                        ),
                    )

        return -1, []



# Estado inicial do quebra-cabeça
start_state = [[7, 2, 4],
               [5, 0, 6],
               [8, 3, 1]]



solver = Puzzle(start_state)

#chamada da função de resolução do quebra-cabeça cosniderando a heuristica
cost, path = solver.solve()

print("Resultados")
print("Custo total:", cost)
print("Caminho completo:")
print("Estado inicial:")
print_puzzle(start_state)
for move in path:
    print(f"Movimento: Peça {move[1]} na linha {move[0]+1}")
    start_state = solver.apply_move(start_state, move)
    print_puzzle(start_state)

