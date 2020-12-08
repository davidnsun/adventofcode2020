input_file = open("input.txt")
lines = input_file.read().split("\n")
input_file.close()
lines = lines[:-1] # get rid of last ['']

# have a dict or set of already executed. if ip is in, break
ip = 0
acc = 0
E = set()
while ip not in E:
    E.add(ip)
    word,n = lines[ip].split()
    n = int(n)
    if word == "jmp":
        ip += n
        continue
    elif word == "acc":
        acc += n
    ip += 1
print(acc)
