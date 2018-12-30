from __future__ import print_function
import numpy as np

def no_parent(v, E):
    return True if len({x for (x, y) in E if v == y}) == 0 else False

def top_sort(S, E):
    e = E
    T = []
    while len(S) != 0:
        E = e
        v = S.pop(0)
        T.append(v)
        e = [(x, y) for (x, y) in E if x != v]
        S.extend([x for (x, y) in e if no_parent(x, e)])
        S = sorted(set(S))
    T.extend(sorted([y for (x, y) in E]))
    return T

instr = [(line[5], line[36]) for line in open('./input.txt')]
start = sorted({x for (x, y) in instr if no_parent(x, instr)})

#SOLUTION TO PART 1
order = top_sort(start, instr)
print(''.join(order))
