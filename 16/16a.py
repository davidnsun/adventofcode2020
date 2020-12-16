with open("input.txt") as input_file:
    lines = input_file.read().split("\n")
lines = lines[:-1]

for i in range(20):
    s1 = lines[i].split(": ")
    s2 = s1[1].split(" or ")
    #print(s2[0],s2[1])
# 26th line, index 25 is first comma sep line of stuff
# 28-974
#print(lines[25])
result = 0
for i in range(25,len(lines)):
    line = lines[i]
    L = [int(elem) for elem in line.split(",")]
    for elem in L:
        if elem < 28 or elem > 974:
            result += elem
print(result)
