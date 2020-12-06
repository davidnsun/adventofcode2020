input_file = open("input.txt")
lines = input_file.read().split("\n\n")
input_file.close()
result = 0
for line in lines:
    L = line.split()
    inter = set(L[0])
    for i in range(1,len(L)):
        inter = inter.intersection(set(L[i]))
    result += len(inter)
print(result)

# >>> from functools import reduce
# >>> list(map(set,["ab","ac"]))
# [{'b', 'a'}, {'c', 'a'}]
# >>> reduce(lambda x,y : x & y, list(map(set,["ab","ac"])))
# {'a'}

from functools import reduce
input_file = open("input.txt")
lines = input_file.read().split("\n\n")
input_file.close()
result = 0
for line in lines: # line = "ab\nac"
    L = line.split() # L = ["ab","ac"]
    l = list(map(set,L)) # l = [{'a', 'b'}, {'a', 'c'}]
    result += len(reduce(lambda x,y : x & y, l)) # reduce yields {'a'}
print(result)

from functools import reduce
with open("input.txt") as input_file:
    lines = input_file.read().split("\n\n")
print(sum([len(reduce(lambda x,y : x & y, list(map(set,line.split())))) for line in lines]))

from functools import reduce
print(sum([len(reduce(lambda x,y : x & y, list(map(set,line.split())))) for line in open("input.txt").read().split("\n\n")]))
