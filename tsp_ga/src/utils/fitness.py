class Fitness:
    def __init__(self, rota):
        self.rota = rota
        self.dist = 0
        self.aptidao = 0.0

    def dist_rota(self):
        if self.dist == 0:
            dist_caminho = 0
            for i in range(0, len(self.rota)):
                origem = self.rota[i]
                destino = None
                if i + 1 < len(self.rota):
                    destino = self.rota[i + 1]
                else:
                    destino = self.rota[0]
                dist_caminho += origem.distancia(destino)
            self.dist = dist_caminho
        return self.dist

    def aptd_rota(self):
        if self.aptidao == 0:
            self.aptidao = 1 / float(self.dist_rota())
        return self.aptidao
