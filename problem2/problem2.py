from __future__ import print_function
import numpy as np

twos = 0
threes = 0
data = np.asarray([])

with open('./input') as f_input:
    for line in f_input:
        line = [ord(x) for x in list(line.strip())]
        data = np.append(data, line)
        unique, freq = np.unique(line, return_counts=True)
        freq = np.unique(freq)
        if 2 in freq:
            twos += 1
        if 3 in freq:
            threes += 1
    data = data.reshape(250, 26)

#SOLUTION TO PART 1
print('checksum: ' + str(twos*threes))

for i in range(0, 26):
    dd = np.delete(data, i, axis=1)
    for j in range(0, 250):
        for k in range(0, 250):
            if j != k and np.array_equal(dd[j], dd[k]):
                box = [chr(int(x)) for x in dd[j]]

print('box: ' + ''.join(box))
