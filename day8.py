def verify(a, b, x, y, locs, once):
    xdif = a[0] - b[0]
    ydif = a[1] - b[1]
    
    m = int(once)
    s = False
    while not s:
        if (a[0] + m*xdif >= 0 and a[0] + m*xdif < x):
            if (a[1] + m*ydif >= 0 and a[1] + m*ydif < y):
                if (not [a[0] + m*xdif, a[1] + m*ydif] in locs):
                    locs.append([a[0] + m*xdif, a[1] + m*ydif])
            else:
                s = True
        else:
            s = True
        if once:
            s = True
        m += 1
            
    m = int(once)
    s = False 
    while not s:
        if (b[0] - m*xdif >= 0 and b[0] - m*xdif < x):
            if (b[1] - m*ydif >= 0 and b[1] - m*ydif < y):
                if (not [b[0] - m*xdif, b[1] - m*ydif] in locs):
                    locs.append([b[0] - m*xdif, b[1] - m*ydif])
            else:
                s = True
        else:
            s = True
        if once:
            s = True
        m += 1
    
    return locs
    

ants = {}

#with open('testcase.txt', 'r') as file:
with open('8input.txt', 'r') as file:
    i = 0    
    for line in file:
        j = 0
        ln = line.strip()
        ln = list(ln)
        for s in ln:
            if s != ".":
                if (s in ants.keys()):
                    ants[s].append([i, j])
                else:
                    ants[s] = [[i, j]]
            j += 1
        i += 1
    x = j
    y = i
        
locs = []        

for k in ants.keys():
    if len(ants[k]) > 1:
        for i in range(len(ants[k]) - 1):
            for j in range(i + 1, len(ants[k])):
                locs = verify(ants[k][i], ants[k][j], x, y, locs, False) #True for p1, False for p2 

count = len(locs)
print(locs)                            
print(f"Antinodes: {count}")