input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

L = [int(line) for line in lines]
L = sorted(L)
res1 = res3 = 0
n = len(L)
L = [0] + L
for i in range(n):
    if L[i] + 1 == L[i+1]:
        res1 += 1
    elif L[i] + 3 == L[i+1]:
        res3 += 1
print(res1*(res3+1))
