import os

from scipy.stats import norm
from csv import writer


def generate_Wr(points, locx, scalex, locy, scaley, locz, scalez):
    distribution_x = norm(locx, scalex)
    distribution_y = norm(locy, scaley)
    distribution_z = norm(locz, scalez)

    x = distribution_x.rvs(size=points)
    y = distribution_y.rvs(size=points)
    z = distribution_z.rvs(size=points)

    points = zip(x, y, z)
    return points


def wr_file(name, cl_point):
    with open(name, 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in cl_point:
            csvwriter.writerow(p)


def gen_wr(name='data.xyz', points=2000, locx=0, scalex=20, locy=0, scaley=20, lockz=0, scalez=20):
    # generowanie ścieżki pliku
    full_name = os.path.join('pliki', name)
    wr_file(full_name, generate_Wr(points, locx, scalex, locy, scaley, lockz, scalez))


if __name__ == '__main__':
    gen_wr(name='body_a.xyz', points=5000, locx=0, scalex=100, locy=0, scaley=1, lockz=0, scalez=100)
    gen_wr(name='body_b.xyz', points=5000, locx=0, scalex=1, locy=0, scaley=100, lockz=0, scalez=100)
