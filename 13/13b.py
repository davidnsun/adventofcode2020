with open("input.txt") as input_file:
    lines = input_file.read().split("\n")
lines = lines[:-1]

L = lines[1].split(",")
rems,mods = list(),list()
for i in range(len(L)):
    if L[i] == "x":
        continue
    mod = int(L[i])
    rems.append(mod - i)
    mods.append(mod)

# Solution 1:
# https://reference.wolfram.com/language/ref/ChineseRemainder.html
# Print this out:
print("r's = ",rems)
print("m's = ",mods)
# Go here:
# https://www.wolframalpha.com/input/?i=ChineseRemainder%5B%7B%7D%2C+%7B%7D%2C100000000000000%5D
# Copy pasta, hit button, done.
# Answer: 554865447501099

