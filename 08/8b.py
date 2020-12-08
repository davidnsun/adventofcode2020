input_file = open("input.txt")
lines = input_file.read().split("\n")
input_file.close()
lines = lines[:-1] # get rid of last ['']

def f():
    ip = 0
    acc = 0
    E = set()
    while ip not in E:
        if ip >= len(lines):
            break
        E.add(ip)
        word,n = lines[ip].split()
        n = int(n)
        if word == "jmp":
            ip += n
            continue
        elif word == "acc":
            acc += n
        ip += 1
    if ip == len(lines):
        return (True,acc)
    else:
        return (False,None)

# 1. fix the instruction
# 2. run the modified lines as before
for i in range(len(lines)):
    word,n = lines[i].split()
    if word == "jmp":
        lines[i] = lines[i].replace("jmp","nop")
        (b,result) = f()
        lines[i] = lines[i].replace("nop","jmp")
        if b:
            print(result)
    elif word == "nop":
        lines[i] = lines[i].replace("nop","jmp")
        (b,result) = f()
        lines[i] = lines[i].replace("jmp","nop")
        if b:
            print(result)
