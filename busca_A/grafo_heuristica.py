#lê o arquivo Grafo.txt e retorna uma estrutura dicionário referente ao grafo
grafo = {}
heuristica = {}

def addToGraph(key,value,distance):
    if grafo.get(key):
        cidade = {'destino':value,'distancia':distance}
        grafo[key].append(cidade)
        if grafo.get(value) is None:
            grafo[value].append({})
    else:
        grafo[key] = []
        cidade = {'destino':value,'distancia':distance}
        grafo[key].append(cidade)

def addToHeuristic(city, distance):
    heuristica[city] = distance

def readArq(name):
    # Abre o arquivo no modo de leitura ('r')
    with open(name, 'r') as arquivo:
        for linha in arquivo:
            data = linha.split(';')
            aux = data[2]
            distance = aux.replace('\n','')
            addToGraph(data[0], data[1], int(distance))

def readHeuristic(filename):
     with open(filename, 'r') as arquivo:
        for linha in arquivo:
            data = linha.split(';')
            distancia = data[1].replace('\n','')
            addToHeuristic(data[0],int(distancia))
            

def get_graph():
    return grafo

def get_heuristic():
    return heuristica

