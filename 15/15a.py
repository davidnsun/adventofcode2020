L = [9,12,1,4,17,0,18]
# Plan: add to dict
# d[0] = turn number i
# d maps a number to the last turn it was spoken
# prev maps a number to the most recent turn it was spoken before that
# last is the last number spoken
d = {L[i]:i+1 for i in range(len(L))}
prev = dict()
last = L[-1]
for i in range(len(L)+1,2020+1):
    if last in prev.keys():
        spoken = d[last] - prev[last]
    else:
        spoken = 0
    if spoken in d.keys():
        prev[spoken] = d[spoken]
    d[spoken] = i
    last = spoken
print(last)
