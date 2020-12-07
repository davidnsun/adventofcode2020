input_file = open("input.txt")
lines = input_file.read().split("\n")
input_file.close()
lines = lines[:-1] # get rid of last ['']

# create dict mapping bag string to list of (n,bag) for every n bags within
target = "shiny gold"
end = "no other bags."
d = dict()
for line in lines:
    temp = list()
    L = line.split(" bags contain ")
    if L[1] == end: # L = ['shiny gold', '3 bright turquoise bags, 1 blahblah...']
        d[L[0]] = [(0,"")]
        continue
    l = L[1].split(", ")
    for phrase in l: # l = ['3 bright turquoise bags', ...]
        frags = phrase.split(" bag") # phrase = '3 bright turquoise bags'
        relevant = frags[0] # frags = ['3 bright turquoise', 's']
        num = int(relevant[0:2]) # relevant = '3 bright turquoise'
        bag = relevant[2:]
        temp.append((num,bag))
    d[L[0]] = temp

result = 0
def compute(target):
    result = 0
    for (n,bag) in d[target]:
        if n == 0:
            return result
        result += n + n*compute(bag)
    return result
print(compute(target))
