
import numpy as np
from copy import deepcopy

input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

#L = [7,13,59,31,19]
#l = [n - (939 % n) for n in L]

L = [19,41,37,821,13,17,29,463,23]
l = [n - (1001612 % n) for n in L]
print(L[l.index(min(l))]*min(l))
