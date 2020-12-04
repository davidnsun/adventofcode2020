import numpy as np

with open("input.txt") as input_file:
    lines = np.genfromtxt(input_file, delimiter='\n', dtype=None)

    found = False
    for e1 in lines:
        for e2 in lines:
            if e1 == e2:
                continue
            for e3 in lines:
                if e1 + e2 + e3 == 2020:
                    print("%d * %d * %d = %d" % (e1, e2, e3, e1*e2*e3))
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        print("Not found :(")

