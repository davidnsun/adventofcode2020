input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

lines = lines[:572]
target = 133015568
# find contiguous set of numbers summing to the target
L = [int(lines[j]) for j in range(0,25)]
for i in range(25,len(lines)):
    print(sum(L))
    new = int(lines[i])
    L.append(new)
    while sum(L) > target:
        L.pop(0)
    if sum(L) == target:
        print("success")
        break
L = sorted(L)
print(L[0] + L[-1])
