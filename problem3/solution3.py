from __future__ import print_function
import numpy as np
import re

n = 0
m = 0
#COMPUTE THE MINIMUM SIZE OF THE FABRIC
with open('./input') as f_input:
    for line in f_input:
        line = line.strip().split(' ')
        x1, y1 = [int(x) for x in re.split(r'[,:]', line[2])[:-1]]
        x2, y2 = [int(x) for x in re.split(r'x', line[3])]
        n = max(n, y1+y2+1)
        m = max(m, x1+x2+1)

#MAP THE CLAIMS ONTO THE FABRIC
#OVERLAPPING CLAIMS RESULT IN A TILE > 1 ON THE FABRIC
fabric = np.zeros([n, m])
with open('./input') as f_input:
    for line in f_input:
        line = line.strip().split(' ')
        x1, y1 = [int(x) for x in re.split(r'[,:]', line[2])[:-1]]
        x2, y2 = [int(x) for x in re.split(r'x', line[3])]
        for i in range(x1, x1+x2):
            for j in range(y1, y1+y2):
                fabric[i][j] += 1

#SOLUTION TO PART 1
print(fabric[fabric > 1].shape[0])

#FIND THE UNIQUE NON-OVERLAPPING CLAIM
with open('./input') as f_input:
    for line in f_input:
        line = line.strip().split(' ')
        x1, y1 = [int(x) for x in re.split(r'[,:]', line[2])[:-1]]
        x2, y2 = [int(x) for x in re.split(r'x', line[3])]
        flag = True
        for i in range(x1, x1+x2):
            for j in range(y1, y1+y2):
                if fabric[i][j] != 1:
                    flag = False
        if flag:
            claim = line[0]
            break

#SOLUTION TO PART 2
print(claim)
