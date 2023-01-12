from time import perf_counter_ns
from module.algorithmen import binäre_suche, linearesuche, fibonacci_zahl


# ergebniss ist in sekunden
def zeit(zu_bestimmen: callable, **argumente: dict) -> int:
    if zu_bestimmen == binäre_suche:
        liste: list = argumente["liste"]
        zu_suchen: int = argumente["zu_suchen"]
        anfang: int = argumente["anfang"]
        länge: int = argumente["länge"]
        zeit_bevor: int = perf_counter_ns()
        zu_bestimmen(liste=liste, zu_suchen=zu_suchen,
                     anfang=anfang, länge=länge)
        zeit_danach: int = perf_counter_ns()

    elif zu_bestimmen == linearesuche:
        liste: list = argumente["liste"]
        länge: int = argumente["länge"]
        zu_suchen: int = argumente["zu_suchen"]
        zeit_bevor: int = perf_counter_ns()
        zu_bestimmen(liste=liste, länge=länge, zu_suchen=zu_suchen)
        zeit_danach: int = perf_counter_ns()

    elif zu_bestimmen == fibonacci_zahl:
        zahl = argumente["zahl"]
        zeit_bevor: int = perf_counter_ns()
        zu_bestimmen(zahl)
        zeit_danach: int = perf_counter_ns()

    else:
        liste: list = argumente["liste"]
        zeit_bevor: int = perf_counter_ns()
        zu_bestimmen(liste=liste)
        zeit_danach: int = perf_counter_ns()

    return (zeit_danach-zeit_bevor) / 1000000000
