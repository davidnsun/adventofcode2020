import numpy as np

with open("input.txt") as input_file:
    lines = np.genfromtxt(input_file, delimiter='\n', dtype=str)

    result = 0
    for line in lines:
        L = line.split() # e.g. ['4-5', 't:', 'ftttttrvts']
        limits = L[0].split('-')
        lo = int(limits[0])
        hi = int(limits[1])
        target = L[1][0]
        s = L[2]
        n = s.count(target)
        if lo <= n and n <= hi:
            result += 1

print(result)
