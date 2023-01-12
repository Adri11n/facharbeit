from math import log2

# O(1)


def O(liste: list) -> int:
    return 1

# O(log n)


def binärer_logorythmuen_von_n(liste: list) -> list:
    ergebnisse: list = []
    for i in liste:
        ergebnisse.append(log2(i))
    return ergebnisse

# O(n)


def linar(liste: list) -> list:
    a = int()
    for _, i in enumerate(liste):
        a = liste[_]
    return liste

# O(n log n)


def linear_mal_log_von_n(liste: list) -> list:
    ergebnisse: list = []
    for i in liste:
        ergebnisse.append(i*log2(i))
    return ergebnisse

# O(n^²)


def quadieren(liste: list) -> list:
    ergebnisse: list = []
    for i in liste:
        ergebnisse.append(i**2)
    return ergebnisse

# O(2^n)


def duplizieren(liste: list) -> list:
    ergebnisse: list = []
    for i in liste:
        ergebnisse.append(2**i)
    return ergebnisse
