import random


class Population:

    @classmethod
    def criar_rota(cls, cidades):
        rota = random.sample(cidades, len(cidades))
        return rota

    @classmethod
    def pop_inicial(cls, n_pop, cidades):
        pop = list()

        for i in range(0, n_pop):
            pop.append(cls.criar_rota(cidades))
        return pop
