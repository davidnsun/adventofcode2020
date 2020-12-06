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
