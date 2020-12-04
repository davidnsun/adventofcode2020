import numpy as np

with open("input.txt") as input_file:
    lines = np.genfromtxt(input_file, delimiter='\n', dtype=str)

    result = 0
    for line in lines:
        L = line.split() # e.g. ['4-5', 't:', 'ftttttrvts']
        positions = L[0].split('-')
        p1 = int(positions[0]) - 1
        p2 = int(positions[1]) - 1
        target = L[1][0]
        s = L[2]
        n = s.count(target)
        if (s[p1] == target) ^ (s[p2] == target):
            result += 1

print(result)
