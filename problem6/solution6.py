from __future__ import print_function
import numpy as np

def cartesian(a, b):
    return [[x, y] for x in a for y in b]

def manhattan(x, y, points):
    dist = np.infty
    for i in range(0, len(points)):
        px, py = points[i]
        d = np.abs(px - x) + np.abs(py - y)
        if d < dist:
            dist = d
            index = i
            flag = False
        elif d == dist:
            flag = True
    if flag:
        return 0
    else:
        return index+1

with open('./input.txt') as f:
    points = np.asarray([[int(x[:-1]), int(y)] for x, y in [z.split(' ') for z in f.read().splitlines()]])

matrix = np.zeros(np.max(points, axis=0))

for i, j in cartesian(range(0, matrix.shape[0]), range(0, matrix.shape[1])):
    matrix[i][j] = manhattan(i, j, points)
print(matrix)

infinities = np.unique(np.concatenate([matrix[0][:], matrix[:][0], matrix[-1][:], matrix[:][-1]]))
print(infinities)

area = np.max([matrix[matrix==k].sum()/k for k in range(1, len(points)+1) if k not in infinities])
print(area)
