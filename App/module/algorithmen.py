from helfer import *
# O(1)


def zugriff_element(liste: list) -> int:
    return liste[0]

# sortierte liste
# O(log n)


def binäre_suche(liste: list, zu_suchen: int, anfang: int, länge: int) -> dict:
    return json_lesen(read(json_schreiben(function="Binäre_suche", liste=liste,
                                          zu_suchen=zu_suchen, anfang=anfang, länge=länge)))

# unsortierte liste
# O(n)


def linearesuche(liste: list, länge: int, zu_suchen: int) -> dict:
    return json_lesen(read(json_schreiben(function="Lineare_suche", liste=liste,
                                          länge=länge, zu_suchen=zu_suchen)))
# unsortierte liste
# O(n log n)


def mergesort(liste: list) -> dict:
    return json_lesen(read(json_schreiben(function="MergeSort", liste=liste)))

# unsortierte liste
# O(n^²)


def bubblesort(liste: list) -> dict:
    return json_lesen(read(json_schreiben(function="Bubble", liste=liste)))
# O(2^n)


def fibonacci_zahl(zahl: int) -> dict:
    return json_lesen(read(json_schreiben(function="Fibonacci", zahl=zahl)))
