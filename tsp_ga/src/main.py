from src.utils.genetic_algorithm import GeneticAlgorithm
from src.utils.city import Cidade


with open('mapa250.txt') as f:

    coordenadas_raw = [d.replace('\n', '').split(' ') for d in f.readlines()]
    tsp_map_x = [float(d[0]) for d in coordenadas_raw]
    tsp_map_y = [float(d[1]) for d in coordenadas_raw]

    cidades = list()

    for (x, y), i in zip(zip(tsp_map_x, tsp_map_y), range(len(coordenadas_raw))):
        cidades.append(Cidade(x=x, y=y, label=i))

    print(GeneticAlgorithm.algoritmo_genetico(pop=cidades,
                                              n_pop=100,
                                              n_elite=20,
                                              taxa_mutacao=0.001,
                                              n_geracoes=10000))
