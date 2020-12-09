input_file = open("input.txt")
lines = input_file.read().split("\n")
lines = lines[:-1]
input_file.close()

# keep track of the prev 25 numbers
# loop through them to see if the next is valid
for i in range(25,len(lines)):
    L = [int(lines[j]) for j in range(i-25,i)]
    a = int(lines[i])
    print(a)
    flag = False
    for c in L:
        for d in L:
            if c == d:
                continue
            if c + d == a:
                flag = True
    if not flag:
        print(a)
        break
