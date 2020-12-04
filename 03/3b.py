with open("input.txt") as input_file:
    lines = input_file.readlines()
    lines = [line[:-1] for line in lines]
    rows = len(lines)
    cols = len(lines[0])
    pairs = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    result = 1
    for (right,down) in pairs:
        i,j = 0,0
        trees = 0
        while i < rows:
            if lines[i][j] == "#":
                trees += 1
            j = (j + right) % cols
            i += down
        result *= trees
print(result)
