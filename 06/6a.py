input_file = open("input.txt")
lines = input_file.read().split("\n\n")
input_file.close()
result = 0
L = [len(set("".join(line.split()))) for line in lines]
print(sum(L))
