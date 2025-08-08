mp = []
mp2 = []
inp = ""
#with open('testcase.txt', 'r') as file:
with open('15input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        if(ln.startswith("#")):
            ml = list(ln)
            ml2 = []
            mp.append(ml)
            for i in ml:
                if (i == "O"):
                    ml2.append("[")
                    ml2.append("]")
                elif (i == "@"):
                    ml2.append("@")
                    ml2.append(".")
                else:
                    ml2.append(i)
                    ml2.append(i)
            mp2.append(ml2)
        elif(len(ln) > 0):
            inp += ln
inp = list(inp)           

rpos = []
for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] == "@":
            rpos = [i, j]
x = rpos[0]
y = rpos[1]            

def moveUpCheck(x, y):
    if mp[x-1][y] == ".":
        return True
    elif(mp[x-1][y] == "O"):
        return moveUpCheck(x - 1, y)
    elif mp[x-1][y] == "[":
        return (moveUpCheck(x - 1, y) and moveUpCheck(x - 1, y + 1))
    elif mp[x-1][y] == "]":
        return (moveUpCheck(x - 1, y) and moveUpCheck(x - 1, y - 1))
    else:
        return False
    
def moveUp(x, y, s):
    if mp[x-1][y] == ".":
        mp[x-1][y] = s
        mp[x][y] = "."
    elif mp[x-1][y] == "O":
        moveUp(x-1, y, "O")
        mp[x-1][y] = s
        mp[x][y] = "."
    elif mp[x-1][y] == "[":
        moveUp(x - 1, y, "[")
        moveUp(x - 1, y + 1, "]")
        mp[x-1][y] = s
        mp[x][y] = "."
    elif mp[x-1][y] == "]":
        moveUp(x -1, y - 1, "[")
        moveUp(x -  1, y, "]")
        mp[x-1][y] = s
        mp[x][y] = "."
        
def moveDownCheck(x, y):
    if mp[x+1][y] == ".":
        return True
    elif(mp[x+1][y] == "O"):
        return moveDownCheck(x + 1, y)
    elif mp[x+1][y] == "[":
        return (moveDownCheck(x + 1, y) and moveDownCheck(x + 1, y + 1))
    elif mp[x+1][y] == "]":
        return (moveDownCheck(x + 1, y) and moveDownCheck(x + 1, y - 1))
    else:
        return False
        
def moveDown(x, y, s):
    if mp[x+1][y] == ".":
        mp[x+1][y] = s
        mp[x][y] = "."
    elif mp[x+1][y] == "O":
        moveDown(x+1, y, "O")
        mp[x+1][y] = s
        mp[x][y] = "."
    elif mp[x+1][y] == "[":
        moveDown(x + 1, y, "[")
        moveDown(x + 1, y + 1, "]")
        mp[x+1][y] = s
        mp[x][y] = "."
    elif mp[x+1][y] == "]":
        moveDown(x + 1, y - 1, "[")
        moveDown(x +  1, y, "]")
        mp[x+1][y] = s
        mp[x][y] = "."

for dir in inp:
    if (dir == "^"):
        if(moveUpCheck(x, y)):
            moveUp(x,y,"@")
            x -= 1
    elif (dir == "v"):
        if(moveDownCheck(x, y)):
            moveDown(x,y,"@")
            x += 1
    elif (dir == "<"):
        if (mp[x][y - 1] == "."):
            mp[x][y - 1] = "@"
            mp[x][y] = "."
            y -= 1
        else:
            n = 1
            while (mp[x][y - n] == "O"):
                n += 1
            if (n != 1):
                if (mp[x][y - n] == "."):
                    for m in range(2, n + 1):
                        mp[x][y - m] = mp[x][y - (m-1)]
                    mp[x][y - 1] = "@"
                    mp[x][y] = "."
                    y -= 1
    elif (dir == ">"):
        if (mp[x][y + 1] == "."):
            mp[x][y + 1] = "@"
            mp[x][y] = "."
            y += 1
        else:
            n = 1
            while (mp[x][y + n] == "O"):
                n += 1
            if (n != 1):
                if (mp[x][y + n] == "."):
                    for m in range(2, n + 1):
                        mp[x][y + m] = mp[x][y + (m-1)]
                    mp[x][y + 1] = "@"
                    mp[x][y] = "."
                    y+= 1
                    
gps = 0
for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] == "O":
            gps += (100*i + j)

mp = mp2
x = rpos[0]
y = rpos[1]*2

for dir in inp:
    if (dir == "^"):
        if(moveUpCheck(x, y)):
            moveUp(x,y,"@")
            x -= 1
    elif (dir == "v"):
        if(moveDownCheck(x, y)):
            moveDown(x,y,"@")
            x += 1   
    elif (dir == "<"):
        if (mp[x][y - 1] == "."):
            mp[x][y - 1] = "@"
            mp[x][y] = "."
            y -= 1
        else:
            n = 1
            while (mp[x][y - n] == "[" or mp[x][y - n] == "]"):
                n += 1
            if (n != 1):
                if (mp[x][y - n] == "."):
                    for m in range(2, n + 1):
                        if (m%2 == 0): v = "]" 
                        else: v = "["
                        mp[x][y-m] = v
                    mp[x][y - 1] = "@"
                    mp[x][y] = "."
                    y -= 1
    elif (dir == ">"):
        if (mp[x][y + 1] == "."):
            mp[x][y + 1] = "@"
            mp[x][y] = "."
            y += 1
        else:
            n = 1
            while (mp[x][y + n] == "[" or mp[x][y + n] == "]"):
                n += 1
            if (n != 1):
                if (mp[x][y + n] == "."):
                    for m in range(2, n + 1):
                        if (m%2 == 0): v = "[" 
                        else: v = "]"
                        mp[x][y+m] = v
                    mp[x][y + 1] = "@"
                    mp[x][y] = "."
                    y += 1
                    
gps2 = 0
for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] == "[":
            gps2 += (100*i + j)
            
print(f"Part 1: {gps}")
print(f"Part 2: {gps2}")
