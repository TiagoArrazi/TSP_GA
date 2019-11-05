from .fitness import Fitness
import operator
import pandas as pd
import random
import numpy as np


class Evolution:

    @classmethod
    def rank_de_rotas(cls, pop):
        resultados_aptidao = dict()
        for i in range(0, len(pop)):
            resultados_aptidao[i] = Fitness(pop[i]).aptd_rota()
        return sorted(resultados_aptidao.items(), key=operator.itemgetter(1), reverse=True)

    @classmethod
    def selecao(cls, rank_pop, n_elite):
        resultados_selecao = list()
        df = pd.DataFrame(np.array(rank_pop), columns=["Index", "Fitness"])
        df['soma_acumulada'] = df.Fitness.cumsum()
        df['perc_acumulado'] = 100 * df.soma_acumulada / df.Fitness.sum()

        for i in range(n_elite):
            resultados_selecao.append(rank_pop[i][0])
        for i in range(len(rank_pop) - n_elite):
            pick = 100 * random.random()
            for i in range(len(rank_pop)):
                if pick <= df.iat[i, 3]:
                    resultados_selecao.append(rank_pop[i][0])
                    break
        return resultados_selecao

    @classmethod
    def mating_pool(cls, pop, resultados_selecao):
        matingpool = list()
        for i in range(0, len(resultados_selecao)):
            index = resultados_selecao[i]
            matingpool.append(pop[index])
        return matingpool

    @classmethod
    def procriar(cls, parent1, parent2):
        descendente_p1 = list()

        gene_a = int(random.random() * len(parent1))
        gene_b = int(random.random() * len(parent1))

        gene_ini = min(gene_a, gene_b)
        gene_final = max(gene_a, gene_b)

        for i in range(gene_ini, gene_final):
            descendente_p1.append(parent1[i])

        descendente_p2 = [item for item in parent2 if item not in descendente_p1]

        child = descendente_p1 + descendente_p2
        return child

    @classmethod
    def procriar_pop(cls, matingpool, n_elite):
        descendentes = list()
        _len = len(matingpool) - n_elite
        pool = random.sample(matingpool, len(matingpool))

        for i in range(0, n_elite):
            descendentes.append(matingpool[i])

        for i in range(0, _len):
            child = cls.procriar(pool[i], pool[len(matingpool) - i - 1])
            descendentes.append(child)
        return descendentes

    @classmethod
    def mutar(cls, individuo, taxa_mutacao):
        for swapped in range(len(individuo)):
            if random.random() < taxa_mutacao:
                swap_with = int(random.random() * len(individuo))

                cidade_1 = individuo[swapped]
                cidade_2 = individuo[swap_with]

                individuo[swapped] = cidade_2
                individuo[swap_with] = cidade_1
        return individuo

    @classmethod
    def mutar_pop(cls, pop, taxa_mutacao):
        pop_mutada = list()

        for ind in range(len(pop)):
            ind_mut = cls.mutar(pop[ind], taxa_mutacao)
            pop_mutada.append(ind_mut)
        return pop_mutada

    @classmethod
    def nxt_gen(cls, gen_atual, n_elite, taxa_mutacao):
        rank_pop = cls.rank_de_rotas(gen_atual)
        resultados_selecao = cls.selecao(rank_pop, n_elite)
        matingpool = cls.mating_pool(gen_atual, resultados_selecao)
        descendentes = cls.procriar_pop(matingpool, n_elite)
        nxt = cls.mutar_pop(descendentes, taxa_mutacao)
        return nxt
