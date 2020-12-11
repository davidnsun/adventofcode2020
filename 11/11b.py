import numpy as np
from copy import deepcopy

input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

L = np.array([list(s) for s in lines])
n = len(L)
m = len(L[0])

while True:
    new = deepcopy(L)
    changed = 0
    for i in range(n):
        for j in range(m):
            result = 0
            current = L[i][j]
            if current == ".":
                continue
            # NW
            if i > 0 and j > 0:
                lo = min(i,j)+1
                for k in range(1,lo):
                    if L[i-k][j-k] == "#":
                        result += 1
                        break
                    if L[i-k][j-k] == "L":
                        break
            # N
            if i > 0:
                lo = i+1
                for k in range(1,lo):
                    if L[i-k][j] == "#":
                        result += 1
                        break
                    if L[i-k][j] == "L":
                        break
            # NE
            if i > 0 and j < m-1:
                lo = min(i,(m-1)-j)+1
                for k in range(1,lo):
                    if L[i-k][j+k] == "#":
                        result += 1
                        break
                    if L[i-k][j+k] == "L":
                        break
            # E
            if j < m-1:
                lo = ((m-1)-j)+1
                for k in range(1,lo):
                    if L[i][j+k] == "#":
                        result += 1
                        break
                    if L[i][j+k] == "L":
                        break
            # SE
            # to understand the logic, it helps to switch the input to small.txt and run 11a.py then look back at this
            if i < n-1 and j < m-1:
                lo = min((n-1)-i,(m-1)-j)+1
                for k in range(1,lo):
                    if L[i+k][j+k] == "#":
                        result += 1
                        break
                    if L[i+k][j+k] == "L":
                        break
            # S
            if i < n-1:
                lo = (n-1)-i+1
                for k in range(1,lo):
                    if L[i+k][j] == "#":
                        result += 1
                        break
                    if L[i+k][j] == "L":
                        break
            # SW
            if i < n-1 and j > 0:
                lo = min((n-1)-i,j)+1
                for k in range(1,lo):
                    if L[i+k][j-k] == "#":
                        result += 1
                        break
                    if L[i+k][j-k] == "L":
                        break
            # W
            if j > 0:
                lo = j+1
                for k in range(1,lo):
                    if L[i][j-k] == "#":
                        result += 1
                        break
                    if L[i][j-k] == "L":
                        break
            if current == "L" and result == 0:
                new[i][j] = "#"
                changed += 1
                continue
            if current == "#" and result >= 5:
                new[i][j] = "L"
                changed += 1
                continue
    L = new
    if changed == 0:
        break
print(sum([sum([c == "#" for c in l]) for l in L]))
