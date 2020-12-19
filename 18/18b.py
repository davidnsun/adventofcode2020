with open("input.txt") as input_file:
    lines = input_file.read().split("\n")
lines = lines[:-1]

debug = False
result = 0
for line in lines:
    L = line.replace("(","( ").replace(")"," )").split(" ")
    if debug:
        print(L)
    n = len(L)
    while n >= 3:
        flag = False
        # Perform all free additions first
        for i in range(1,n-1):
            if L[i] == "+" and L[i-1].isnumeric() and L[i+1].isnumeric():
                L[i-1:i+2] = [str(int(L[i-1])+int(L[i+1]))]
                flag = True
                break
        if flag:
            if debug:
                print(L)
            n = len(L)
            continue
        # Remove parenthesis
        for i in range(1,n-1):
            if L[i].isnumeric() and L[i-1] == "(" and L[i+1] == ")":
                L[i-1:i+2] = [L[i]]
                flag = True
                break
        if flag:
            if debug:
                print(L)
            n = len(L)
            continue
        # Perform multiplications last
        temp = list()
        ps = list()
        for i in range(len(L)):
            if L[i] == "(":
                temp.append(i)
                continue
            if L[i] == ")":
                ps.append((temp.pop(),i))
                continue
        for start,end in ps:
            for i in range(start+2,end-1):
                if L[i] == "*" and L[i-1].isnumeric() and L[i+1].isnumeric():
                    L[i-1:i+2] = [str(int(L[i-1])*int(L[i+1]))]
                    flag = True
                    break
            if flag:
                break
        if flag:
            if debug:
                print(L)
            n = len(L)
            continue
        for i in range(1,n-1):
            if L[i] == "*" and L[i-1].isnumeric() and L[i+1].isnumeric():
                L[i-1:i+2] = [str(int(L[i-1])*int(L[i+1]))]
                flag = True
                break
        if flag:
            if debug:
                print(L)
            n = len(L)
            continue
    result += int(L[0])
print(result)
