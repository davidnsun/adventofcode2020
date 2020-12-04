with open("input.txt") as input_file:
    lines = input_file.read().split("\n\n")
result = 0
valid_hair = set("1234567890abcdef")
valid_eyecolors = set("amb blu brn gry grn hzl oth".split())
for line in lines:
    L = line.split()
    d = dict()
    for s in L:
        [key,val] = s.split(":")
        if key == "byr" or key == "iyr" or key == "eyr":
            val = int(val)
        d[key] = val
    num_keys = len(d.keys())
    if (num_keys == 8 or (num_keys == 7 and ("cid" not in d.keys()))):
        byr = d["byr"]
        iyr = d["iyr"]
        eyr = d["eyr"]
        hgt = d["hgt"]
        # some hgt only have 2 char, so computing ht might fail. thus, we skip
        if len(hgt) <= 2:
            continue
        units = hgt[-2:]
        ht = int(hgt[:-2])
        hcl = d["hcl"]
        ecl = d["ecl"]
        pid = d["pid"]
        if 1920 <= byr <= 2002 and \
           2010 <= iyr <= 2020 and \
           2020 <= eyr <= 2030 and \
           ((units == "in" and 59 <= ht <= 76) or
            (units == "cm" and 150 <= ht <= 193)) and \
           hcl[0] == "#" and len(hcl[1:]) == 6 and \
            set(hcl[1:]).issubset(valid_hair) and \
           ecl in valid_eyecolors and \
           len(pid) == 9:
               result += 1
print(result)
