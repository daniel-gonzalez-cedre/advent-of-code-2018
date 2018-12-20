from __future__ import print_function
import numpy as np

with open('./input.txt') as f:
    points = [[x[:-1], y] for x, y in [z.split(' ') for z in f.read().splitlines()]]

print(points)
