import numpy as np
from copy import deepcopy

input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

L = np.array([list(s) for s in lines])
n = len(L)
m = len(L[0])
#If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
#If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
#Otherwise, the seat's state does not change.
while True:
    new = deepcopy(L)
    changed = 0
    for i in range(n):
        for j in range(m):
            result = 0
            current = L[i][j]
            if current == ".":
                continue
            if i > 0 and j > 0 and L[i-1][j-1] == "#":
                result += 1
            if i > 0 and L[i-1][j] == "#":
                result += 1
            if i > 0 and j < m-1 and L[i-1][j+1] == "#":
                result += 1
            if i < n-1 and j > 0 and L[i+1][j-1] == "#":
                result += 1
            if i < n-1 and L[i+1][j] == "#":
                result += 1
            if i < n-1 and j < m-1 and L[i+1][j+1] == "#":
                result += 1
            if j > 0 and L[i][j-1] == "#":
                result += 1
            if j < m-1 and L[i][j+1] == "#":
                result += 1
            if current == "L" and result == 0:
                new[i][j] = "#"
                changed += 1
                continue
            if current == "#" and result >= 4:
                new[i][j] = "L"
                changed += 1
                continue
    L = new
    if changed == 0:
        break
print(sum([sum([c == "#" for c in l]) for l in L]))
