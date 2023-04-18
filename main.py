import Sheep
import time
import os
import Sheepard
import Bush


def renewposition(axisx, axisy, map):
    map[axisx][axisy] = ' '


def printmap(map):
    for fila in map:
        for pos in fila:
            print(pos, end=" ")
        print()


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def inicializer(map, caracters=None):
    if caracters is None:
        caracters = []
    else:
        for entity in caracters:
            entity.existinmap(map)


if __name__ == '__main__':

    FINAL = True

    mapGranja = [
#   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
        ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ], #0
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #1
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #2
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #3
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #4
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #5
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #6
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #7
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #8
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #9
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #10
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #11
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #12
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #13
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #14
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', ], #15
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ], #16
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ], #17
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ], #18
        ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ]  #19
    ]
    ovj = Sheep.Oveja(7, 8, mapGranja)
    bush = Bush.Arbusto()
    bush.spawn(mapGranja)

    shepheards = [Sheepard.Pastor(7, 7, mapGranja), Sheepard.Pastor(18, 1, mapGranja), Sheepard.Pastor(18, 2, mapGranja)]

    entitys = [ovj, bush, shepheards[0], shepheards[1], shepheards[2]]
    inicializer(mapGranja, entitys)

    while FINAL:

        clear()

        # Posicionarse en el mapa - Todas las entidades - En sus conocimientos
        ovj.existinmap(ovj.knwlg)

        for shepard in shepheards:
            shepard.existinmap(shepheards[0].knwlg)
            shepard.existinmap(shepheards[1].knwlg)
            shepard.existinmap(shepheards[2].knwlg)

        # Imprimir Mapa o mapas
        printmap(mapGranja)

        # Moverse

        gotoHelpX = 0
        gotoHelpY = 0

        if shepheards[0].sheepFounded or shepheards[1].sheepFounded or shepheards[2].sheepFounded:
            ovj.canMove = False
            ovj.axisX = 0
            ovj.axisY = 0

            for shepard in shepheards:
                if shepard.requestAssistance:
                    gotoHelpX = shepard.axisX
                    gotoHelpY = shepard.axisY

            # for shepard in shepheards:
            #     if shepard.requestAssistance is False:
            #         shepard.help(gotoHelpX, gotoHelpY)

        else:
            # ovj.move()

            for shepard in shepheards:
                shepard.move()


        # Limpiar posiciones en el Mapa General de todas las entidades

        renewposition(ovj.pastPostX, ovj.pastPostY, mapGranja)
        renewposition(ovj.pastPostX, ovj.pastPostY, ovj.knwlg)

        # Limpiar pocisiones en el Mapa del granjero 1 Para todas las entidades (incluyendose)

        for shepard in shepheards:
            renewposition(shepard.pastPostX, shepard.pastPostY, mapGranja)
            renewposition(shepard.pastPostX, shepard.pastPostY, shepheards[0].knwlg)
            renewposition(shepard.pastPostX, shepard.pastPostY, shepheards[1].knwlg)
            renewposition(shepard.pastPostX, shepard.pastPostY, shepheards[2].knwlg)

        # Posicionarse en el mapa - Todas las entidades - En el mapa general

        if shepheards[0].sheepFounded or shepheards[1].sheepFounded or shepheards[2].sheepFounded:
            pass
        elif shepheards[0].sheepFounded or shepheards[1].sheepFounded or shepheards[2].sheepFounded:
            ovj.existinmap(mapGranja)

        ovj.existinmap(mapGranja)

        for shepard in shepheards:
            shepard.existinmap(mapGranja)

        time.sleep(1)

        if ovj.freedom:
            FINAL = False
        for shepard in shepheards:
            if shepard.jobDone:
                FINAL = False

    ovj.existinmap(ovj.knwlg)  # Posicionarse en el Mapa del agente - Oveja

    renewposition(ovj.pastPostX, ovj.pastPostY, mapGranja)
    renewposition(ovj.pastPostX, ovj.pastPostY, ovj.knwlg)

    clear()
    print("\n\n\n\n\n\n")
    if ovj.freedom:
        print("Eres libre amiga. Save the world - Oveja wins")

    for shepard in shepheards:
        if shepard.jobDone:
            print("Se acabo para mi UnU - Oveja loses")
            FINAL = False

    print("\n")

    printmap(mapGranja)

    print("\n")

    printmap(ovj.knwlg)

    print("\n\n")
