from __future__ import print_function
import numpy as np

with open("./input") as f_input:
    changes = np.asarray([int(line) for line in f_input])
    #SOLUTION TO PART 1
    print(np.sum(changes))

    i = 0
    freq = 0
    frequencies = np.asarray([])
    while True:
        if i >= len(changes):
            i = 0
        frequencies = np.append(frequencies, [freq])
        freq += changes[i]
        if len(np.where(frequencies == freq)[0]) != 0:
            #SOLUTION TO PART 2
            print(freq)
            break
        i += 1
