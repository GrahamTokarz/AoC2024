avail = []
patterns = []

# with open('testcase.txt', 'r') as file:
with open('19input.txt', 'r') as file:
    for line in file:
        ln = line.strip().split(", ")
        if (len(ln) > 1):
            avail = ln
        elif (ln[0] != ""):
            patterns.append(ln[0])
            
maxAvail = 0

for a in avail:
    if (len(a) > maxAvail):
        maxAvail = len(a)
            

def verify(p):
    o = ["NOT"]
    for j in range(1, maxAvail + 1):
        x = p[0:j]
        if (x in avail and o[0] != "DONE"):
            if (p[j:] == ""):
                o[0] = "DONE"
            else:
                o.append(p[j:])
    return o

def verCount(p):
    dp = [0] * (len(p) + 1)
    dp[0] = 1

    for i in range(1, len(p) + 1):
        for comb in avail:
            if i >= len(comb) and p[i - len(comb):i] == comb:
                dp[i] += dp[i - len(comb)]

    return dp[len(p)]

c = 0
counter = 0
number = 0
for p in patterns:
    number += 1
    patts = [p]
    pattVer = False
    while (len(patts) > 0 and not pattVer):
        newPatts = verify(patts[0])
        if (newPatts[0] != "DONE"):
            for i in range (1, len(newPatts)):
                if (newPatts[i] not in patts):
                    patts.append(newPatts[i])
        else:
            c += 1
            pattVer = True
            n = verCount(p)
            if (n != -1):
                counter += n
        patts = patts[1:]
        
print(f"Makable cases: {c}") #Part 1
print(f"Total number of combinations: {counter}") #Part 2
        