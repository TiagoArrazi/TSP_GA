from .evolution import Evolution
from .population import Population
import matplotlib.pyplot as plt


class GeneticAlgorithm:

    @classmethod
    def plot_progresso(cls, progresso):
        plt.plot(progresso)
        plt.ylabel('Distancia')
        plt.xlabel('Geracao')
        plt.show()

    @classmethod
    def plot_caminho_10(cls, caminho):
        x_coord = list()
        y_coord = list()
        labels = list()
        for i, c in enumerate(caminho[:10]):
            x_coord.append(c.x)
            y_coord.append(c.y)
            labels.append('{}'.format(c.label))

        plt.plot(x_coord, y_coord, '-ro', lw=0.5, label=labels)
        [plt.text(x, y, label) for x, y, label in zip(x_coord, y_coord, labels)]
        plt.show()

    @classmethod
    def plot_caminho_all(cls, caminho):
        x_coord = list()
        y_coord = list()
        for c in caminho:
            x_coord.append(c.x)
            y_coord.append(c.y)

        plt.plot(x_coord, y_coord, '-ro', lw=0.5)
        plt.show()

    @classmethod
    def algoritmo_genetico(cls, pop, n_pop, n_elite, taxa_mutacao, n_geracoes):
        pop = Population.pop_inicial(n_pop, pop)
        progresso = list()
        progresso.append(1 / Evolution.rank_de_rotas(pop)[0][1])
        print("Distancia inicial " + str(1 / Evolution.rank_de_rotas(pop)[0][1]))

        for i in range(0, n_geracoes):
            pop = Evolution.nxt_gen(pop, n_elite, taxa_mutacao)
            progresso.append(1 / Evolution.rank_de_rotas(pop)[0][1])

        print("Distancia final: " + str(1 / Evolution.rank_de_rotas(pop)[0][1]))
        index_melhor_rota = Evolution.rank_de_rotas(pop)[0][0]
        melhor_rota = pop[index_melhor_rota]

        cls.plot_progresso(progresso)
        cls.plot_caminho_10(melhor_rota)

        return melhor_rota
