import matplotlib.pyplot as plt


def vergleiche_visualisiere(graphen: tuple, überschrift: str) -> None:
    """zweites plot muss eine funktion der vergleichsfunktionen sein also((),(vergleichsfunktion)), 
    tupel = ((xachse, yachse,titel)), 
    zip funktion nutzen"""

    plt.subplot(1, 2, 1)
    plt.plot(graphen[0][0], graphen[0][1])
    plt.title(graphen[0][2])
    plt.xlabel("Input Größe")
    plt.ylabel("Zeit in Sekunden")
    plt.subplot(1, 2, 2)
    plt.plot(graphen[1][0], graphen[1][1])
    plt.title(graphen[1][2])
    plt.xlabel("Input Größe")
    plt.ylabel("Iterationen")
    plt.suptitle(überschrift)
    plt.show()


def vergleiche_visualisieren(graphen_links: tuple, graphen_rechts: tuple, titel: tuple, überschrift: str) -> None:
    """zweites plot muss eine funktion der vergleichsfunktionen sein also((),(vergleichsfunktion)), genauso bei den titeln, 
    tupel = ((xachse, yachse, slabel)), 
    zip funktion nutzen"""

    plt.subplot(1, 2, 1)
    for i in graphen_links:
        plt.plot(i[0], i[1], label=i[2])
        plt.title(titel[0])
    plt.xlabel("Input Größe")
    plt.ylabel("Zeit in Sekunden")
    plt.legend()
    plt.subplot(1, 2, 2)
    for i in graphen_rechts:
        plt.plot(i[0], i[1], label=i[2])
        plt.title(titel[1])
    plt.xlabel("Input Größe")
    plt.ylabel("Iterationen")
    plt.legend()
    plt.suptitle(überschrift)
    plt.show()


def visualisiere(xachse: list, yachse: list, titel: str, vergleich=False) -> None:
    plt.plot(xachse, yachse)
    plt.xlabel("Input Größe")
    if not vergleich:
        plt.ylabel("Zeit in Sekunden")
    else:
        plt.ylabel("Iterationen")
    plt.title(titel)
    plt.show()


def visualisieren(graphen: tuple, titel: str, vergleich=False) -> None:
    """tupel = ((xachse, yachse,label)), 
    zip funktion nutzen"""

    for i in graphen:
        plt.plot(i[0], i[1], label=i[2])
    plt.xlabel("Input Größe")
    if not vergleich:
        plt.ylabel("Zeit in Sekunden")
    else:
        plt.ylabel("Iterationen")
    plt.title(titel)
    plt.legend()
    plt.show()
