with open("input.txt") as input_file:
    lines = input_file.read().split("\n")
lines = lines[:-1]

d = dict()
s = set()
for i in range(20):
    s1 = lines[i].split(": ") # ["field name","29-917 or 943-952"]
    field = s1[0]
    s.add(field)
    s2 = s1[1].split(" or ") # ["29-917","943-952"]
    L = list()
    for j in range(len(s2)):
        sj = s2[j].split("-") # ["29","917"] or ["943","952"]
        L.append([int(elem) for elem in sj]) # L = [[29,917],[943,952]]
    intervals = ((L[0][0],L[0][1]),(L[1][0],L[1][1]))
    d[field] = intervals

# first comma sep line of stuff starts on 26th line (index 25)
# 28-974 valid range for all

valid = list()
for i in range(25,len(lines)):
    line = lines[i]
    L = [int(elem) for elem in line.split(",")]
    if sum([27 <= elem <= 973 for elem in L]) == 20:
        valid.append(L)

S = list() # list of sets (of candidate fields)
for j in range(len(valid[0])):
    cand = s.copy()
    for i in range(len(valid)):
        L = valid[i]
        value = L[j] # 917
        invalid = set()
        for field in cand:
            (l1,u1),(l2,u2) = d[field]
            if not (l1 <= value <= u1 or l2 <= value <= u2): # if not valid
                invalid.add(field)
        cand = cand.difference(invalid)
    S.append(cand)

myticket = [int(s) for s in lines[22].split(",")]

# if len(S[i]) == 1 then name = list(S[i])[0]
# fti[name] = i
# setminus from all the other sets
# update collection S via a temp list
fti = dict()
result = 1
for k in range(len(S)): # do the following, 20 times
    for i in range(len(S)): # find the one with length 1
        if len(S[i]) == 1:
            fti[list(S[i])[0]] = i
            S = [S[j].difference(S[i]) for j in range(len(S))] # x setminus S[i] for all x \in S
            break

# fti mapping from field name to index in comma sep list, complete
for field in fti.keys():
    L = field.split(" ")
    if len(L) == 2 and L[0] == "departure":
        result *= myticket[fti[field]]
print(result)
