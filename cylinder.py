import random as rnd
from csv import writer
import numpy as np
import os


def cylinder(points: int = 100000, r=200, h=500):
    xx = []
    yy = []
    zz = []
    while (len(xx) < points):
        x = rnd.uniform(-1, 1) * r
        y = rnd.uniform(-1, 1) * np.sqrt(r ** 2 - x ** 2)
        z = rnd.uniform(-1, 1) * h

        xx.append(x)
        yy.append(y)
        zz.append(z)

        return zip(xx, yy, zz)


def cylinder2(points: int = 100000, r=200, h=500):
    xx = []
    yy = []
    zz = []
    for i in range(points):
        x = rnd.uniform(-1, 1) * r
        y = rnd.uniform(-1, 1) * np.sqrt(r ** 2 - x ** 2)
        z = rnd.uniform(-1, 1) * h

        xx.append(x)
        yy.append(y)
        zz.append(z)

    return zip(xx, yy, zz)


if __name__ == '__main__':
    points = cylinder2()
    sciezka = os.path.join('pliki', 'cyl.xyz')
    with open(sciezka, 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in points:
            csvwriter.writerow(p)
