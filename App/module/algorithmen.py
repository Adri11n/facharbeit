
# sortierte liste
# O(1)
def zugriff_element(liste: list) -> int:
    return liste[0]

# sortierte liste
# quelle https://www.programiz.com/dsa/binary-search
# O(log n)


def binäre_suche(liste: list, zu_suchen: int, anfang: int, länge: int) -> int:
    while anfang <= länge:
        mid = anfang + (länge - anfang)//2
        if liste[mid] == zu_suchen:
            return mid
        elif liste[mid] < zu_suchen:
            anfang = mid + 1
        else:
            länge = mid - 1
    return -1

# unsortierte liste
# quelle https://www.programiz.com/dsa/linear-search
# O(n)


def linearesuche(liste: list, länge: int, zu_suchen: int) -> int:
    for i in range(0, länge):
        if (liste[i] == zu_suchen):
            return i
    return -1

# unsortierte liste
# quelle https://www.programiz.com/dsa/merge-sort
# O(n log n)


def mergesort(liste: list) -> list:
    if len(liste) > 1:
        r = len(liste)//2
        L = liste[:r]
        M = liste[r:]
        mergesort(L)
        mergesort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                liste[k] = L[i]
                i += 1
            else:
                liste[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            liste[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            liste[k] = M[j]
            j += 1
            k += 1
    return liste

# unsortierte liste
# quelle https://www.programiz.com/dsa/bubble-sort
# O(n^²)


def bubbleSort(liste: list):
    for i in range(len(liste)):
        swapped = False
        for j in range(0, len(liste) - i - 1):
            if liste[j] > liste[j + 1]:
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
                swapped = True
        if not swapped:
            break

# quelle https://realpython.com/fibonacci-sequence-python/#generating-the-fibonacci-sequence-recursively-in-python
# O(2^n)


def fibonacci_zahl(zahl: int) -> int:
    if zahl in [0, 1]:
        return zahl
    return fibonacci_zahl(zahl - 1) + fibonacci_zahl(zahl - 2)
