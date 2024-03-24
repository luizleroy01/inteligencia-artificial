#-------------------------------------------------------------------------------------
# Nomes : Luiz Eduardo Leroy Souza (20213002126) e Sulamita Ester Costa (20213001568) 
# Data : 24/03/2024
#-------------------------------------------------------------------------------------

import heapq

grafo = {}
heuristica = {}

def addToHeuristic(city, distance):
    heuristica[city] = distance

def readHeuristic(filename):
     with open(filename, 'r') as arquivo:
        for linha in arquivo:
            data = linha.split(';')
            distancia = data[1].replace('\n','')
            addToHeuristic(data[0],int(distancia))


def readArq(name):
    # Abre o arquivo no modo de leitura ('r')
    with open(name, 'r') as arquivo:
        for linha in arquivo:
            data = linha.split(';')
            aux = data[2]
            distance = aux.replace('\n','')
            addToGraph(data[0], data[1], int(distance))


def addToGraph(key,value,distance):
    if grafo.get(key):
        cidade = {'destino':value,'distancia':distance}
        grafo[key].append(cidade)
        if grafo.get(value):
            cidade2 = {'destino':key,'distancia':distance}
            grafo[value].append(cidade2)
        else:
            grafo[value] = []
            cidade2 = {'destino':key,'distancia':distance}
            grafo[value].append(cidade2)
     
    else:
        grafo[key] = []
        cidade = {'destino':value,'distancia':distance}
        grafo[key].append(cidade)

        if grafo.get(value):
            cidade2 = {'destino':key,'distancia':distance}
            grafo[value].append(cidade2)
        else:
            grafo[value] = []
            cidade2 = {'destino':key,'distancia':distance}
            grafo[value].append(cidade2)

class No:
    def __init__(self, estado, pai=None, custo_g=0, custo_h=0):
        self.estado = estado
        self.pai = pai
        self.custo_g = custo_g  # Custo acumulado do início ao nó atual
        self.custo_h = custo_h  # Heurística (estimativa do custo do nó até o objetivo)

    def __lt__(self, outro):
        return (self.custo_g + self.custo_h) < (outro.custo_g + outro.custo_h)

def mostra_informacoes(nos_abertos,iteration,no_atual,fechados):
    print(f"\nLoop: {iteration} No atual: {no_atual.estado} Custo: {no_atual.custo_g + no_atual.custo_h}")
    print("Abertos:")
    if len(nos_abertos) > 0:
        for no in nos_abertos:
            print(f"No :{no.estado} custo: {no.custo_g + no.custo_h}")
    else:
        print("Ainda não há nos abertos")
    
    print("\nFechados:")
    if len(fechados) > 0:
        for no in fechados:
            print(f"No :{no} ")
    else:
        print("Ainda não há nos fechados")

def mostra_caminho(caminho):
    print()
    print("Caminho: ",end="")
    for i in range(len(caminho)):
        if i < len(caminho)-1:
             print(f"{caminho[i]}->",end="")
        else:
            print(f"{caminho[i]}",end="")
       

def a_estrela(grafo, estado_inicial, estado_final, heuristicas):
    abertos = []
    fechados = set()
    no_inicial = No(estado_inicial)

    #armazena os nos abertos em uma estrutura heap
    heapq.heappush(abertos, no_inicial)
    loop = 0

    while abertos:
        no_atual = heapq.heappop(abertos)

        mostra_informacoes(abertos,loop,no_atual,fechados)

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
                vizinho_nome = vizinho["destino"]
                custo = vizinho["distancia"]

                if vizinho_nome in fechados:
                    continue

                custo_g = no_atual.custo_g + custo
                custo_h = heuristicas[vizinho_nome]
                novo_no = No(vizinho_nome, no_atual, custo_g, custo_h)
                heapq.heappush(abertos, novo_no)
        
        loop = loop + 1


    return None  # Se não houver caminho encontrado


# Grafo

readArq('Grafo.txt')
readHeuristic('Heuristica.txt')

# Exemplo de uso
estado_inicial = "Arad"
estado_final = "Bucareste"

caminho = a_estrela(grafo, estado_inicial, estado_final, heuristica)
mostra_caminho(caminho)
