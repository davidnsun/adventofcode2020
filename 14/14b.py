with open("input.txt") as input_file:
    lines = input_file.read().split("\n")
lines = lines[:-1]

WIDTH = 36
mem = dict()
mask = "0"*WIDTH
for line in lines:
    L = line.split(" = ")
    if L[0] == "mask":
        mask = L[1]
    else:
        value = int(L[1])
        raw = bin(int(L[0][4:][:-1]))[2:]
        pads = "0" * (WIDTH - len(raw))
        before = pads + raw
        after = ""
        for i in range(WIDTH):
            if mask[i] == "X":
                after += "X"
                continue
            if mask[i] == "0":
                after += before[i]
                continue
            if mask[i] == "1":
                after += "1"
                continue
        A = [""]
        for i in range(WIDTH):
            if after[i] == "X":
                temp = list()
                for partial in A:
                    temp.append(partial + "0")
                    temp.append(partial + "1")
                A = temp
            else:
                for j in range(len(A)):
                    A[j] += after[i]
        for addr in A:
            mem[addr] = value
print(sum(mem.values()))
