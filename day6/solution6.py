from __future__ import print_function
import numpy as np

def manhattan((x1, y1), (x2, y2)):
    return np.abs(x1 - x2) + np.abs(y1 - y2)

def closest(x, y, points, threshold):
    distances = [(manhattan((x, y), points[i]), i) for i in range(len(points))]
    distances.sort()
    score = np.sum(np.asarray(distances), axis=0)[0]
    if distances[0][0] < distances[1][0] and score < threshold:
        return (distances[0][1] + 1, 1) if score < threshold else (distances[0][1] + 1, 0)
    else:
        return (0, 1) if score < threshold else (0, 0)

def solution(points):
    matrix = np.zeros(np.max(points, axis=0))
    region = 0
    for i, j in [[x, y] for x in range(matrix.shape[0]) for y in range(matrix.shape[1])]:
        matrix[i][j], included = closest(i, j, points, 10000)
        region += included
    inf_areas = np.unique(np.concatenate([matrix[0], matrix[-1], matrix.T[0], matrix.T[-1]]))
    return np.max([matrix[matrix==k].sum()/k for k in range(1, points.shape[0]+1) if k not in inf_areas]), region

#READ THE INPUT
points = np.asarray([(int(x[:-1]), int(y)) for x, y in [z.split(' ') for z in open('./input.txt').read().splitlines()]])

#SOLUTION TO PARTS 1 AND 2
print(solution(points))
