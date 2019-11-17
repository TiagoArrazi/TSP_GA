import numpy as np


class Cidade:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def distancia(self, city):
        dist_x = abs(self.x - city.x)
        dist_y = abs(self.y - city.y)
        distancia = np.sqrt((dist_x ** 2) + (dist_y ** 2))
        return distancia

    def __repr__(self):
        return '<{} - ({}, {})>'.format(self.label, self.x, self.y)
