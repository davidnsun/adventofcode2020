input_file = open("input.txt")
lines = input_file.read().split("\n\n")
input_file.close()
result = 0
a = set("abcdefghijklmnopqrstuvwxyz")
for line in lines:
    L = line.split()
    fst = set(L[0])
    for i in range(1,len(L)):
        fst = fst.intersection(set(L[i]))
    result += len(fst)
print(result)
