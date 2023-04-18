import random as rm
ENTITYS = ['B', 'S', '=', '0', 'O']


class Arbusto:
    def __init__(self):
        self.axisY = None
        self.axisX = None
        self.figure = 'B'

    def existinmap(self, map):
        map[self.axisX][self.axisY] = self.figure

    def spawn(self, map):
        axisx = rm.randrange(1, 19)
        axisy = rm.randrange(1, 19)
        if map[axisx][axisy] == ' ':
            self.axisX = 17
            self.axisY = 17
        else:
            self.spawn()