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
        addr = int(L[0][4:][:-1])
        raw = bin(int(L[1]))[2:]
        pads = "0" * (WIDTH - len(raw))
        before = pads + raw
        after = ""
        for i in range(WIDTH):
            if mask[i] == "X":
                after += before[i]
                continue
            if mask[i] == "0":
                after += "0"
                continue
            if mask[i] == "1":
                after += "1"
                continue
        value = int(after,2)
        mem[addr] = value
print(sum(mem.values()))
