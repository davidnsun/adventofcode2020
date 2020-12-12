import numpy as np
from copy import deepcopy

input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

L = [(line[0],int(line[1:])) for line in lines]
# keep an x, y. a negative x means west, a negative y means north
dic = {"N":["N","E","S","W"],"E":["E","S","W","N"],"S":["S","W","N","E"],"W":["W","N","E","S"]}
face = "E"
x,y = 0,0
for d,n in L:
    if d == "N":
        y -= n
        continue
    if d == "S":
        y += n
        continue
    if d == "E":
        x += n
        continue
    if d == "W":
        x -= n
        continue
    if d == "L":
        face = dic[face][4 - n//90]
        continue
    if d == "R":
        face = dic[face][n//90]
        continue
    if d == "F":
        if face == "E":
            x += n
        if face == "W":
            x -= n
        if face == "S":
            y += n
        if face == "N":
            y -= n
print(abs(x)+abs(y))
