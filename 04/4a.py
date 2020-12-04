with open("input.txt") as input_file:
    lines = input_file.read().split("\n\n")
    result = 0
    for line in lines:
        L = line.split()
        d = dict()
        for s in L:
            [key,val] = s.split(":")
            d[key] = val
        num_keys = len(d.keys())
        if (num_keys == 8 or (num_keys == 7 and ("cid" not in d.keys()))):
            result += 1
print(result)
