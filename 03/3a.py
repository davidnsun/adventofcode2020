with open("input.txt") as input_file:
    lines = input_file.readlines()
    lines = [line[:-1] for line in lines]
    rows = len(lines)
    cols = len(lines[0])
    i,j = 0,0
    result = 0
    while i < rows:
        if lines[i][j] == "#":
            result += 1
        j = (j + 3) % cols
        i += 1
print(result)
