mp = []
regions = []
ex = []

#with open('testcase.txt', 'r') as file:
with open('12input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp.append(list(ln))
        
for i in range(len(mp)):
    for j in range(len(mp[0])):
        reg = []
        ver = [[i, j]]
        while len(ver) > 0:
            v = ver[0]
            x = v[0]
            y = v[1]
            if (v not in ex):
                reg.append(v)
                ex.append(v)
                if (x > 0):
                    if (mp[x - 1][y] == mp[x][y]):
                        ver.append([x - 1, y])
                if (x < len(mp) - 1):
                    if (mp[x + 1][y] == mp[x][y]):
                        ver.append([x + 1, y])
                if (y > 0):
                    if (mp[x][y - 1] == mp[x][y]):
                        ver.append([x, y - 1])
                if (y < len(mp[0]) - 1):
                    if (mp[x][y + 1] == mp[x][y]):
                        ver.append([x, y + 1])
                
            ver = ver[1:]
        if (len(reg) > 0):
            regions.append(reg)
            
                
areas = [len(x) for x in regions]

def perim(area):
    p = 0
    for b in area:
        x = b[0]
        y = b[1]
        if x == 0 or x == len(mp) - 1:
            p += 1
        if (x > 0):
            if [x-1, y] not in area:
                p += 1
        if (x < len(mp) - 1):
            if [x+1, y] not in area:
                p += 1
        if y == 0 or y == len(mp[0]) - 1:
            p += 1
        if (y > 0):
            if [x, y - 1] not in area:
                p += 1
        if (y < len(mp[0]) - 1):
           if [x, y + 1] not in area:
                p += 1
    return p

def sides(area):
    area = sorted(area)
    sides = []
    for b in area:
        x = b[0]
        y = b[1]
        if (x == 0):
            if "h0-" not in sides:
                sides.append("h0-")
            elif (y > 0):
                if ([x, y-1] not in area):
                    sides.append("h0-")
        if (x == len(mp) - 1):
            if "h+" not in sides:
                sides.append("h+")
            elif (y > 0):
                if ([x, y-1] not in area):
                    sides.append("h+")
        if (x > 0):
            txt =  f"h{x}-"
            if [x-1, y] not in area:
                if txt not in sides:
                    sides.append(txt)
                elif (y > 0):
                    if ([x-1, y-1] in area or [x, y-1] not in area):
                        sides.append(txt)
        if (x < len(mp) - 1):
            txt =  f"h{x}+"
            if [x+1, y] not in area:
                if txt not in sides:
                    sides.append(txt)
                elif (y > 0):
                    if ([x+1, y-1] in area or [x, y-1] not in area):
                        sides.append(txt)      
        if y == 0:
            if "l0-" not in sides:
                sides.append("l0-")
            elif (x > 0):
                if ([x - 1, y] not in area):
                    sides.append("l0-")
        if y == len(mp[0]) - 1:
            if "l+" not in sides:
                sides.append("l+")
            elif (x > 0):
                if ([x - 1, y] not in area):
                    sides.append("l0-")
        if (y > 0):
            txt =  f"l{y}-"
            if [x, y - 1] not in area:
                if txt not in sides:
                    sides.append(txt)
                elif (x > 0):
                    if ([x - 1, y - 1] in area or [x-1, y] not in area):
                        sides.append(txt)
        if (y < len(mp[0]) - 1):
            txt =  f"l{y}+"
            if [x, y + 1] not in area:
                if txt not in sides:
                    sides.append(txt)
                elif (x > 0):
                    if ([x - 1, y + 1] in area or [x-1, y] not in area):
                        sides.append(txt)
    return len(sides)

perims = []
pPrice = 0
sPrice = 0
for reg in regions:
    area = len(reg)
    pm = perim(reg)
    sds = sides(reg)
    pPrice += (pm*area)
    sPrice += sds*area

print(f"Price by perimeter: {pPrice}") #Part 1
print(f"Price by sides: {sPrice}") #Part 2