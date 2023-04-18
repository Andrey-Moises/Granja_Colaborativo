import random as rm
ENTITYS = ['B', 'S', '=', '0', 'O']


class Oveja:
    def __init__(self, x, y, map):
        self.pastPostX = 0
        self.pastPostY = 0
        self.axisX = x
        self.axisY = y
        self.canMove = True

        self.eatTime = 0
        self.satiate = False
        self.freedom = False

        self.figure = 'O'

        self.map = map
        self.knwlg = [
            #   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
            ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ],  # 0
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 1
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 2
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 3
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 4
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 5
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 6
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 7
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 8
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 9
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 10
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 11
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 12
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 13
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 14
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 15
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 16
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 17
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 18
            ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ]  # 19
        ]
        self.exploredPos = [[x, y]]
        self.returningPos = []

        self.bushFound = False
        self.bushAxisX = None
        self.bushAxisY = None

        self.knwlg[self.axisX][self.axisY] = self.figure

    def revealmap(self):
        self.knwlg[self.axisX - 1][self.axisY] = self.map[self.axisX - 1][self.axisY]  # Norte
        self.knwlg[self.axisX + 1][self.axisY] = self.map[self.axisX + 1][self.axisY]  # Sur
        self.knwlg[self.axisX][self.axisY - 1] = self.map[self.axisX][self.axisY - 1]  # Est
        self.knwlg[self.axisX][self.axisY + 1] = self.map[self.axisX][self.axisY + 1]  # Oest

    def move(self):

        magicnumber = rm.randrange(1, 5)
        self.revealmap()

        # Checar alrededor

        if self.knwlg[self.axisX - 1][self.axisY] == 'B':
            self.bushAxisX = self.axisX - 1
            self.bushAxisY = self.axisY
            self.bushFound = True
            if self.satiate:
                self.canMove = True
            else:
                self.canMove = False

        elif self.knwlg[self.axisX + 1][self.axisY] == 'B':
            self.bushAxisX = self.axisX + 1
            self.bushAxisY = self.axisY
            self.bushFound = True
            if self.satiate:
                self.canMove = True
            else:
                self.canMove = False

        elif self.knwlg[self.axisX][self.axisY - 1] == 'B':
            self.bushAxisX = self.axisX
            self.bushAxisY = self.axisY - 1
            self.bushFound = True
            if self.satiate:
                self.canMove = True
            else:
                self.canMove = False

        elif self.knwlg[self.axisX][self.axisY + 1] == 'B':
            self.bushAxisX = self.axisX
            self.bushAxisY = self.axisY + 1
            self.bushFound = True
            if self.satiate:
                self.canMove = True
            else:
                self.canMove = False

        if self.bushFound:

            if self.satiate:

                if self.canMove:

                    cleanplan = self.createpath()

                    self.pastPostX = self.axisX
                    self.pastPostY = self.axisY

                    self.axisX = cleanplan[0]
                    self.axisY = cleanplan[1]

                    if self.exploredPos:
                        pass
                    else:
                        self.freedom = True
            else:
                self.eat()

        elif self.canMove:

            if self.knwlg[self.axisX - 1][self.axisY] and self.knwlg[self.axisX][self.axisY - 1] != ' ' or \
                    self.knwlg[self.axisX - 1][self.axisY] and self.knwlg[self.axisX][self.axisY + 1] != ' ' or \
                    self.knwlg[self.axisX + 1][self.axisY] and self.knwlg[self.axisX][self.axisY - 1] != ' ' or \
                    self.knwlg[self.axisX + 1][self.axisY] and self.knwlg[self.axisX][self.axisY + 1] != ' ':
                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX - 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX -= 1
                    else:
                        self.move()
                elif magicnumber == 2:
                    if self.knwlg[self.axisX + 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX + 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX += 1
                    else:
                        self.move()
                elif magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY - 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY -= 1
                    else:
                        self.move()
                elif magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY + 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY += 1
                    else:
                        self.move()

            elif [self.axisX - 1, self.axisY] and \
                    [self.axisX + 1, self.axisY] and \
                    [self.axisX, self.axisY - 1] and [self.axisX, self.axisY + 1] in self.exploredPos:

                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX - 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX -= 1
                    else:
                        self.move()
                elif magicnumber == 2:
                    if self.knwlg[self.axisX + 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX + 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX += 1
                    else:
                        self.move()
                elif magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY - 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY -= 1
                    else:
                        self.move()
                elif magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY + 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY += 1
                    else:
                        self.move()

            elif [self.axisX - 1, self.axisY] or [self.axisX + 1, self.axisY] or [self.axisX, self.axisY - 1] or \
                    [self.axisX, self.axisY + 1] not in self.exploredPos:

                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] not in ENTITYS \
                            and [self.axisX - 1, self.axisY] not in self.exploredPos:
                        self.exploredPos.append([self.axisX - 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX -= 1
                    else:
                        self.move()
                elif magicnumber == 2:
                    if self.knwlg[self.axisX + 1][self.axisY] not in ENTITYS and \
                            [self.axisX, self.axisY + 1] not in self.exploredPos:
                        self.exploredPos.append([self.axisX + 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX += 1
                    else:
                        self.move()
                elif magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] not in ENTITYS and \
                            [self.axisX, self.axisY - 1] not in self.exploredPos:
                        self.exploredPos.append([self.axisX, self.axisY - 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY -= 1
                    else:
                        self.move()
                elif magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] not in ENTITYS and \
                            [self.axisX, self.axisY + 1] not in self.exploredPos:
                        self.exploredPos.append([self.axisX, self.axisY + 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY += 1
                    else:
                        self.move()

    def existinmap(self, map):
        map[self.axisX][self.axisY] = self.figure

    def eat(self):
        if self.eatTime < 6:
            self.canMove = False
            self.eatTime += 1
            print(f"Turnos para comer {7 - self.eatTime}")
        else:
            self.satiate = True

    def createpath(self):

        coordinate = self.exploredPos.pop()
        return coordinate

