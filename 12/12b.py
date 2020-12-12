import numpy as np
from copy import deepcopy

input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

L = [(line[0],int(line[1:])) for line in lines]
# keep an x, y. a negative x means west, a negative y means north
x,y = 0,0
wx,wy = 10,-1
for d,n in L:
    if d == "N":
        wy -= n
    if d == "S":
        wy += n
    if d == "E":
        wx += n
    if d == "W":
        wx -= n
    if d == "L":
        if n == 90:
            temp = wy
            wy = -1*wx
            wx = temp
        if n == 180:
            wx *= -1
            wy *= -1
        if n == 270:
            temp = wx
            wx = -1*wy
            wy = temp
    if d == "R":
        if n == 90:
            temp = wx
            wx = -1*wy
            wy = temp
        if n == 180:
            wx *= -1
            wy *= -1
        if n == 270:
            temp = wy
            wy = -1*wx
            wx = temp
    if d == "F":
        x += n*wx
        y += n*wy
print(abs(x)+abs(y))
