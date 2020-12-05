import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
import itertools

def compute_row(s):
    lo = 0
    hi = 127
    n = len(s)
    result = 0
    for i in range(n):
        c = s[i]
        mid = (hi - lo)//2
        if c == "F":
            hi = lo + mid
        elif c == "B":
            lo = hi - mid
        if i == n-1:
            if c == "F":
                result = lo
            else:
                result = hi
    return result

def compute_col(s):
    lo = 0
    hi = 7
    n = len(s)
    result = 0
    for i in range(n):
        c = s[i]
        mid = (hi - lo)//2
        if c == "L":
            hi = lo + mid
        elif c == "R":
            lo = hi - mid
        if i == n-1:
            if c == "L":
                result = lo
            else:
                result = hi
    return result

with open("input.txt") as input_file:
    lines = input_file.read().split("\n")
L = sorted([compute_row(line[:-3])*8+compute_col(line[-3:]) for line in lines])
n = len(L)
for i in range(n-1):
    if L[i]+2 == L[i+1]:
        print(L[i]+1)
