import math
import random
import itertools

def validate(udt, ordering):
    parsed = []
    i = 0
    while (i < len(udt)):
        valid = True
        req = udt[i]
        udt[len(udt) - 1] = str(int(udt[len(udt) - 1]))
        key = str(int(req))
        if (key in ordering.keys()):
            nec = ordering[key]
            for p in nec:
                if ((p not in parsed) and (str(p) in udt)):
                    valid = False
        if valid:
            i = i + 1
            parsed.append(int(req))
        else: 
            end = udt.pop()
            udt.insert(i, end)
        
    return udt

out = 0
fixed = 0
ordering = {}

#with open('testcase.txt', 'r') as file:
with open('5input.txt', 'r') as file:
    
    for line in file:
        valid = True
        ln = line.strip()
        if ("|" in line):
            vals = line.split("|")
            v = str(int(vals[1]))
            if (v in ordering.keys()):
                ordering[v].append(int(vals[0]))
            else:
                ordering[v] = [int(vals[0])]
        else:
            if ("," in line):
                udt = line.split(",")
                parsed = []
                for req in udt:
                    udt[len(udt) - 1] = str(int(udt[len(udt) - 1]))
                    key = str(int(req))
                    if (key in ordering.keys()):
                        nec = ordering[key]
                        for p in nec:
                            if ((p not in parsed) and (str(p) in udt)):
                                valid = False
                    parsed.append(int(req))
                if (valid):
                    out = out + int(parsed[math.ceil(len(parsed)/2) - 1])
                else: 
                    reordered = validate(udt, ordering)
                    fixed = fixed + int(reordered[math.ceil(len(reordered)/2) - 1])
        
        
print(f"Editor dumbass, what's the answer?: {out}") #Part 1
print(f"Editor dumbass, what's the second answer?: {fixed}") #Part 2