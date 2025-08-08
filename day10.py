out = 0
mp = []

#with open('testcase.txt', 'r') as file:
with open('10input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp.append(list(ln))
        
heads = []
for i in range(len(mp)):
    for j in range(len(mp[i])):
        mp[i][j] = int(mp[i][j])
        if mp[i][j] == 0:
            heads.append([i, j, 0])

for hd in heads:
    steps = [hd]
    peaks = []    
    
    while (len(steps) != 0):
        peaks = [] #Comment this line out for p1
        s = steps[0]
        x = s[0]
        y = s[1]
        v = s[2]
        
        if (x > 0):
            if (mp[x-1][y] == (v + 1)):
                if (v + 1) == 9:
                    if (not [x - 1, y] in peaks):
                        peaks.append([x-1, y])
                        out += 1
                else:
                    steps.append([x-1, y, v + 1])
        if (x < len(mp) - 1):
            if (mp[x+1][y] == (v + 1)):
                if (v + 1) == 9:
                    if (not [x + 1, y] in peaks):
                        peaks.append([x+1, y])
                        out += 1
                else:
                    steps.append([x+1, y, v + 1])
        if (y > 0):
            if (mp[x][y-1] == (v + 1)):
                if (v + 1) == 9:
                    if (not [x, y-1] in peaks):
                        peaks.append([x, y-1])
                        out += 1
                else:
                    steps.append([x, y-1, v + 1])
        if (y < len(mp[0]) - 1):
            if (mp[x][y+1] == (v + 1)):
                if (v + 1) == 9:
                    if (not [x, y+1] in peaks):
                        peaks.append([x, y+1])
                        out += 1
                else:
                    steps.append([x, y+1, v + 1])
        
        steps = steps[1:]
        
print(f"Trail ratings: {out}")