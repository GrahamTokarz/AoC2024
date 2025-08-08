import math
mp = []

# with open('testcase.txt', 'r') as file:
with open('16input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp.append(list(ln))

rpos = []
ndot = 0
for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] == "S":
            rpos = [i, j]
        elif mp[i][j] == ".":
            ndot += 1
            
def evaluate(x, y, facing, score, prevs):
    prevs.append([x, y])
    ps = prevs.copy()
    ops = []
    if facing == ">":
        if mp[x][y + 1] != "#":
            ops.append([x, y + 1, ">", score + 1, ps.copy()])
        if mp[x + 1][y] != "#":
            ops.append([x + 1, y, "v", score + 1001, ps.copy()])
        if mp[x - 1][y] != "#":
            ops.append([x - 1, y, "^", score + 1001, ps.copy()])
    elif facing == "<":
        if mp[x][y - 1] != "#":
            ops.append([x, y - 1, "<", score + 1, ps.copy()])
        if mp[x + 1][y] != "#":
            ops.append([x + 1, y, "v", score + 1001, ps.copy()])
        if mp[x - 1][y] != "#":
            ops.append([x - 1, y, "^", score + 1001, ps.copy()])
    elif facing == "v":
        if mp[x + 1][y] != "#":
            ops.append([x + 1, y, "v", score + 1, ps.copy()])
        if mp[x][y + 1] != "#":
            ops.append([x, y + 1, ">", score + 1001, ps.copy()])
        if mp[x][y - 1] != "#":
            ops.append([x, y - 1, "<", score + 1001, ps.copy()])
    elif facing == "^":
        if mp[x - 1][y] != "#":
            ops.append([x - 1, y, "^", score + 1, ps.copy()])
        if mp[x][y + 1] != "#":
            ops.append([x, y + 1, ">", score + 1001, ps.copy()])
        if mp[x][y - 1] != "#":
            ops.append([x, y - 1, "<", score + 1001, ps.copy()])
    return ops

x = rpos[0]
y = rpos[1]
best = math.inf
options = evaluate(x, y, ">", 0, [])
evaled = {}
while len(options) > 0:
    x = options[0][0]
    y = options[0][1]
    fc = options[0][2]
    tot = options[0][3]
    ps = options[0][4]
    
    if (tot <= best):
        if mp[x][y] == "E":
            ps.append([x, y])
            if (tot == best):
                paths.append(ps)
            else:
                paths = [ps]
            best = tot
        else:
            coord = f"{x},{y}"
            if (coord not in evaled.keys() or evaled[coord] >= tot):
                evaled[coord] = tot
                ops = evaluate(x, y, fc, tot, ps)
                for o in ops:
                    options.append(o)
    options = options[1:]
    
print(f"Lowest score: {best}") #Part 1

x = rpos[0]
y = rpos[1]
paths = []
options = evaluate(x, y, ">", 0, [])

while len(options) > 0:
    x = options[0][0]
    y = options[0][1]
    fc = options[0][2]
    tot = options[0][3]
    ps = options[0][4]
    
    if (tot <= best):
        if mp[x][y] == "E":
            ps.append([x, y])
            paths.append(ps)
        else:
            coord = f"{x},{y}"
            if (coord not in evaled.keys() or evaled[coord] >= (tot - 1000)):
                evaled[coord] = tot
                ops = evaluate(x, y, fc, tot, ps)
                for o in ops:
                    options.append(o)
    options = options[1:]

coords = []
for p in paths:
    for c in p:
        if c not in coords:
            coords.append(c)
print(f"Valid tiles: {len(coords)}") #Part 2