
#If given an empty map to put things in
x = 71 
y = 71
mp = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(".")
    mp.append(row)


#Puts blocks in x,y coord form from input
with open('testcase.txt', 'r') as file:
    for line in file:
        ln = [int(x) for x in line.strip().split(",")]
        mp[ln[1]][ln[0]] = "#"
        
#Puts rows from input into an array
mp = []
with open('testcase.txt', 'r') as file:
    for line in file:
        ln = list(line.strip())
        mp.append(ln)       

#BFS
visited = []
steps = []
while (len(steps) > 0):
    stp = steps[0]
    
    #Insert found condition here?
    
    if (mp[stp[0]][stp[1]] != "#"):
        
        if ([stp[0] + 1, stp[1]] not in visited and stp[0] + 1 < x):
            steps.append([stp[0] + 1, stp[1], stp[2] + 1])
            visited.append([stp[0] + 1, stp[1]])
            
        if ([stp[0] - 1, stp[1]] not in visited and stp[0] > 0):   
            steps.append([stp[0] - 1, stp[1], stp[2] + 1])
            visited.append([stp[0] - 1, stp[1]])
            
        if ([stp[0], stp[1] + 1] not in visited and stp[1] + 1 < y):      
            steps.append([stp[0], stp[1] + 1, stp[2] + 1])
            visited.append([stp[0], stp[1] + 1])
            
        if ([stp[0], stp[1] - 1] not in visited and stp[1] > 0):               
            steps.append([stp[0], stp[1] - 1, stp[2] + 1])
            visited.append([stp[0], stp[1] - 1])
            
    steps = steps[1:]




# Visualization of map
for v in visited:
    if (mp[v[0]][v[1]] != "#"):
        mp[v[0]][v[1]] = "O"
        
for r in mp:
    out = ""
    for x in r:
        out += (x)
    print(out)
