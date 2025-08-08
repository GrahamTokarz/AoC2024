import math
regA = 0
oRegA = 0
oRegB = 0
oRegC = 0
prog = []

# with open('testcase.txt', 'r') as file:
with open('17input.txt', 'r') as file:
    i = 0
    for line in file:
        ln = line.strip().split(": ")
        if (i == 0):
            oRegA = int(ln[1])
        elif (i == 1):
            oRegB = int(ln[1])
        elif (i == 2):
            oRegC = int(ln[1])
        elif (i == 4):
            prog = [int(x) for x in ln[1].split(",")]
        i += 1

def evaluate(aVal):
    ip = 0
    out = []
    regA = aVal
    regB = oRegB
    regC = oRegC
    valid = True
    loopA = 0
    
    while (ip < len(prog)):
        op = prog[ip]
        oper = prog[ip + 1]
        coper = oper
        adv = 2
        if (oper == 4):
            coper = regA
        elif (oper == 5):
            coper = regB
        elif (oper == 6):
            coper = regC
        
        if (op == 0):
            regA = int(math.floor(regA / (2**coper)))
        elif (op == 1):
            regB = regB^oper
        elif (op == 2):
            regB = coper%8
        elif (op == 3):
            if (regA != 0):
                ip = oper
                adv = 0
        elif (op == 4):
            regB = regB^regC
        elif (op == 5):
            v = coper%8
            out.append(v)
        elif (op == 6):
            regB = int(math.floor(regA / (2**coper)))
        elif (op == 7):
            regC = int(math.floor(regA / (2**coper)))
                
        ip += adv
    return out

def dfs(v, d):
    d += 1
    if (len(v) == len(prog)):
        return [-1, v]
    
    ops = []
    sum = 0
    for i in range(len(v)):
        sum += v[i] * (8**(i+1)) # This assumes that it's always going to be a/8. Which is not a guarantee. Like op code 0 could be using a value that's not 3.
        
    for i in range (sum, sum+8):
        if (evaluate(i) == prog[len(prog) - len(v) - 1:]):
            ops.append(i-sum)
    
    for o in ops:
        v.insert(0, o)
        out = dfs(v, d)
        if (out[0] != -1):
            v = out[1][1:]
        else:
            return [-1, out[1], d]
        
    return [0, v, d]
        
            
ans = dfs([], 0)[1]
sum = 0
for i in range(len(ans)):
    sum += ans[i] * (8**(i))
    
out = evaluate(oRegA)
outStr = ""
for o in out:
    outStr += str(o) + ","
    
outStr = outStr[0:len(outStr) - 1]
    
print(f"Original output: {outStr}") #Part 1
print(f"Smallest register value: {sum}") #Part 2