input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

L = [int(line) for line in lines]
L = sorted(L)
L = [0] + L + [L[-1]+3]
result = 0
total = [1]
for i in range(1,len(L)):
    result = 0
    for j in range(i):
        if L[i] <= L[j]+3:
            result += total[j]
    total.append(result)
print(total[-1])

# orig
# 5
# 6
# 5 6
# 11
# 5 11
# 6 11
# 5 6 11
# 1 + 3 + 3 + 1 = 8
# 13
# 5 13
# 6 13
# 11 13
# 5 6 13
# 5 11 13
# 6 11 13
# 5 6 11 13
# 1 + 4 + 6 + 4 + 1 = 16
