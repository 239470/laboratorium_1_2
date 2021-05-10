from csv import reader
import cc3d
import numpy as np
import matplotlib.pyplot as plot
import os


def readcsv(name, nl="\n", dl=","):
    cloud = []
    with open(name, newline=nl) as csvfile:
        csvreader = reader(csvfile, delimiter=dl)
        for xx, yy, zz in csvreader:
            cloud.append([int(np.float64(xx)), int(np.float64(yy)), int(np.float64(zz))])
    return cloud


sciezka = os.path.join('pliki', "lidar_point.xyz")
labels_in = np.array(readcsv(sciezka))
labels_out = cc3d.connected_components(labels_in)
N = np.max(labels_out)

fig = plot.figure()
ax = fig.add_subplot(111, projection='3d')
for segid in range(1, N + 1):
    extracted_image = labels_out * (labels_out == segid)
    ax.scatter(extracted_image[0], extracted_image[1], extracted_image[2], c='b')
plot.show()
