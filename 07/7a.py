input_file = open("input.txt")
lines = input_file.read().split("\n")
input_file.close()
lines = lines[:-1] # get rid of last ['']

# starting point incl all that mention shiny gold but isn't shiny gold itself
target = "shiny gold"
result = set()
def containers(target,result):
    for line in lines:
        L = line.split(" bags contain ")
        if L[0] == target:
            continue
        if target in L[1]:
            result.add(L[0])
    return result
result = containers(target,result)

# look for all of those in the latter half of each line too and add the bags
# containing them
# you know when to stop once there's nothing more to add (len before = len after)
unvis = result
while True: # BRRRRRRRRR
    new = set()
    for target in unvis:
        new = containers(target,new)
    result = result.union(new)
    unvis = new
    if len(unvis) == 0:
        break
print(len(result))
