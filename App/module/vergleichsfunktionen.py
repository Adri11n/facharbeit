from helfer import *

# O(1)


def O(liste: list) -> int:
    return liste[0]

# O(log n)


def binärer_logorythmuen_von_n(liste: list) -> dict:
    return json_lesen(read(json_schreiben(function="Binärer_logorythmuen_von_n", liste=liste)))

# O(n)


def linar(liste: list) -> dict:
    return json_lesen(read(json_schreiben(function="Linar", liste=liste)))

# O(n log n)


def linear_mal_log_von_n(liste: list) -> dict:
    return json_lesen(read(json_schreiben(function="Linear_mal_log_von_n", liste=liste)))

# O(n^²)


def quadieren(liste: list) -> dict:
    return json_lesen(read(json_schreiben(function="Quadieren", liste=liste)))

# O(2^n)


def duplizieren(liste: list) -> dict:
    return json_lesen(read(json_schreiben(function="Duplizieren", liste=liste)))