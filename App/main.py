from sys import path
path.append("module")
from module import algorithmen, listengenerator, visualisierung
x = []
y = []
for i in range(1,10001):
    lol = listengenerator.zufälligeliste(i)
    x.append(len(lol))
    y.append(algorithmen.mergesort(lol)["zeit"] / 1000000000)
visualisierung.visualisiere(x,y,"lol")