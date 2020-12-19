with open("input.txt") as input_file:
    lines = input_file.read().split("\n")
lines = lines[:-1]

result = 0
# https://stackoverflow.com/questions/10623302/how-assignment-works-with-python-list-slice
for line in lines:
    L = line.replace("(","( ").replace(")"," )").split(" ")
    #print(L)
    n = len(L)
    while n >= 3:
        for i in range(1,n-1):
            if L[i] == "+" and L[i-1].isnumeric() and L[i+1].isnumeric():
                L[i-1:i+2] = [str(int(L[i-1])+int(L[i+1]))]
                break
            if L[i] == "*" and L[i-1].isnumeric() and L[i+1].isnumeric():
                L[i-1:i+2] = [str(int(L[i-1])*int(L[i+1]))]
                break
            if L[i].isnumeric() and L[i-1] == "(" and L[i+1] == ")":
                L[i-1:i+2] = [L[i]]
                break
        #print(L)
        n = len(L)
    result += int(L[0])
print(result)
