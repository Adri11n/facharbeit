from random import randint


def zufälligeliste(länge: int) -> list:
    liste: list = []
    for i in range(0, länge):
        liste.append(randint(0, länge * 1000))
    return liste


def geordneteliste(länge: int) -> list:
    liste: list = []
    for i in range(1, länge + 1):
        liste.append(i)
    return liste
