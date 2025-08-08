def step(mp, xpos):
    turns = []
    while True:
        i = xpos[0]
        j = xpos[1]
        c = mp[i][j]
        if c in ["v", "^", ">", "<"]:
            if c == "v":
                if i == (len(mp) - 1):
                    mp[i][j] = "X"
                    return False
                else:
                    if (mp[i + 1][j] == "#"):
                        if ([i, j, 0] in turns):
                            return True
                        mp[i][j] = "<"
                        turns.append([i, j, 0])
                    else:
                        mp[i][j] = "X"
                        mp[i + 1][j] = "v"
                        xpos = [i + 1, j]
            elif c == "^":
                if i == 0:
                    mp[i][j] = "X"
                    return False
                else:
                    if (mp[i - 1][j] == "#"):
                        if ([i, j, 1] in turns):
                            return True
                        mp[i][j] = ">"
                        turns.append([i, j, 1])
                    else:
                        mp[i][j] = "X"
                        mp[i - 1][j] = "^"
                        xpos = [i - 1, j]
            elif c == ">":
                if j == (len(r) - 1):
                    mp[i][j] = "X"
                    return False
                else:
                    if (mp[i][j + 1] == "#"):
                        if ([i, j, 2] in turns):
                            return True
                        mp[i][j] = "v"
                        turns.append([i, j, 2])
                    else:
                        mp[i][j] = "X"
                        mp[i][j + 1] = ">"
                        xpos = [i, j + 1]
            elif c == "<":
                if j == 0:
                    mp[i][j] = "X"
                    return False
                else:
                    if (mp[i][j - 1] == "#"):
                        if ([i, j, 3] in turns):
                            return True
                        mp[i][j] = "^"
                        turns.append([i, j, 3])
                    else:
                        mp[i][j] = "X"
                        mp[i][j - 1] = "<"
                        xpos = [i, j - 1]    

out = 0
loops = 0
mp = []

#with open('testcase.txt', 'r') as file:
with open('6input.txt', 'r') as file:    
    for line in file:
        ln = line.strip()
        ln = list(ln)
        mp.append(ln)
        
i = 0
for r in mp:
    j = 0
    for c in r:
        if c == "^":
            xpos = [i, j]
            reset = [i, j]
        j = j + 1
    i = i + 1
    
# Part 1
step(mp, xpos)
    
for r in mp:
    for c in r:
        if c == "X":
            out = out + 1

#Part 2
    
print("This is NOT optimal, will take about a minute to run.")
i = 0
for r in mp:
    j = 0
    for c in r:
        if c != "^" and c != "#":
            xpos = [reset[0], reset[1]]
            mp[i][j] = "#"
            mp[reset[0]][reset[1]] = "^"
            if(step(mp, xpos)):
                loops = loops + 1
            mp[i][j] = "."
        j = j + 1
    i = i + 1
        
print(f"Tiles covered: {out}") #Part 1
print(f"Infinite loops: {loops}") #Part 2