L = [9,12,1,4,17,0,18]
# Plan: add to dict
# d[0] = turn number i
# d maps a number to the last turn it was spoken
# prev maps a number to the most recent turn it was spoken before that
# last is the last number spoken
d = {L[i]:i+1 for i in range(len(L))}
prev = dict()
last = L[-1]
for i in range(len(L)+1,30000000+1):
    try:
        spoken = d[last] - prev[last]
    except KeyError:
        spoken = 0
    try:
        prev[spoken] = d[spoken]
    except KeyError:
        pass
    d[spoken] = i
    last = spoken
print(last)
