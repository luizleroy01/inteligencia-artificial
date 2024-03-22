import heapq

class No:
    def __init__(self, estado, pai=None, custo_g=0, custo_h=0):
        self.estado = estado
        self.pai = pai
        self.custo_g = custo_g  # Custo acumulado do início ao nó atual
        self.custo_h = custo_h  # Heurística (estimativa do custo do nó até o objetivo)

    def __lt__(self, outro):
        return (self.custo_g + self.custo_h) < (outro.custo_g + outro.custo_h)

def a_estrela(grafo, estado_inicial, estado_final, heuristicas):
    abertos = []
    fechados = set()
    no_inicial = No(estado_inicial)
    heapq.heappush(abertos, no_inicial)
    
    while abertos:
        no_atual = heapq.heappop(abertos)
        
        if no_atual.estado == estado_final:
            caminho = []
            while no_atual:
                caminho.append(no_atual.estado)
                no_atual = no_atual.pai
            return caminho[::-1]  # Retorna o caminho do início ao fim
        
        fechados.add(no_atual.estado)
        estado = no_atual.estado
        valida = grafo.get(estado)

        if valida is not None:
            vizinhos = grafo[estado]
            for vizinho in vizinhos:
                vizinho_nome = vizinho['destino']
                custo = vizinho['distancia']
                
                if vizinho_nome in fechados:
                    continue
                
                custo_g = no_atual.custo_g + custo
                custo_h = heuristicas[vizinho_nome]
                novo_no = No(vizinho_nome, no_atual, custo_g, custo_h)
                heapq.heappush(abertos, novo_no)
    
    return None  # Se não houver caminho encontrado

# Grafo
grafo = {
    'Oradea': [{'destino': 'Zerind', 'distancia': 71}, {'destino': 'Sibiu', 'distancia': 151}],
    'Arad': [{'destino': 'Zerind', 'distancia': 75}, {'destino': 'Sibiu', 'distancia': 140}, {'destino': 'Timisoara', 'distancia': 118}],
    'Timisoara': [{'destino': 'Lugoj', 'distancia': 111}],
    'Lugoj': [{'destino': 'Mehadia', 'distancia': 70}],
    'Mehadia': [{'destino': 'Drobeta', 'distancia': 75}],
    'Drobeta': [{'destino': 'Craiova', 'distancia': 120}],
    'Craiova': [{'destino': 'Rimnicu Vilcea', 'distancia': 146}, {'destino': 'Pitesti', 'distancia': 138}],
    'Rimnicu Vilcea': [{'destino': 'Pitesti', 'distancia': 97}, {'destino': 'Sibiu', 'distancia': 80}],
    'Sibiu': [{'destino': 'Fagaras', 'distancia': 99}],
    'Fagaras': [{'destino': 'Bucareste', 'distancia': 211}],
    'Pitesti': [{'destino': 'Bucareste', 'distancia': 101}],
    'Bucareste': [{'destino': 'Giurgiu', 'distancia': 90}, {'destino': 'Urziceni', 'distancia': 85}],
    'Urziceni': [{'destino': 'Hirsova', 'distancia': 98}, {'destino': 'Vaslui', 'distancia': 142}],
    'Hirsova': [{'destino': 'Eforie', 'distancia': 86}],
    'Vaslui': [{'destino': 'Iasi', 'distancia': 92}],
    'Iasi': [{'destino': 'Neamt', 'distancia': 87}],
    'Giurgiu': [],
    'Eforie': [],
    'Neamt': []
}

# Heurística
heuristica = {
    'Arad': 366, 'Bucareste': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161, 'Fagaras': 176,
    'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
    'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

# Exemplo de uso
estado_inicial = 'Arad'
estado_final = 'Bucareste'

caminho = a_estrela(grafo, estado_inicial, estado_final, heuristica)
print("Caminho encontrado:", caminho)
