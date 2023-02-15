from helfer import json_schreiben, main_aufrufen

# O(1)


def O(liste: list) -> int:
    return liste[0]

# O(log n)


def binärer_logorythmuen_von_n(liste: list) -> list:
    json_schreiben(function="Binärer_logorythmuen_von_n", liste=liste)
    return main_aufrufen()

# O(n)


def linar(liste: list) -> list:
    json_schreiben(function="Linar", liste=liste)
    return main_aufrufen()

# O(n log n)


def linear_mal_log_von_n(liste: list) -> list:
    json_schreiben(function="Linear_mal_log_von_n", liste=liste)
    return main_aufrufen()

# O(n^²)


def quadieren(liste: list) -> list:
    json_schreiben(function="Quadieren", liste=liste)
    return main_aufrufen()

# O(2^n)


def duplizieren(liste: list) -> list:
    json_schreiben(function="Duplizieren", liste=liste)
    return main_aufrufen()