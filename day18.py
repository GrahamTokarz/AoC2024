numBlocks = 120000 # Arbitrary high value
startBlocks = 2800 # Tested value that reducing computation time drastically, gets near the answer.
val = 1024 #Test case: 12, input: 1024
x = 71 #Test case: 7, input: 71
y = 71

i = 0
numSteps = 0
mp = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(".")
    mp.append(row)

# with open('testcase.txt', 'r') as file:
with open('18input.txt', 'r') as file:
    for line in file:
        if (i < numBlocks):
            ln = line.strip().split(",")
            mp[int(ln[1])][int(ln[0])] = "#"
            i += 1
            visited = [[0, 0]]
            steps = [[0, 0, 0]]
            found = False

        while ((i >= startBlocks or i == val) and len(steps) > 0 and not found):
            stp = steps[0]
            if (stp[0] == x - 1 and stp[1] == y - 1):
                found = True
                if val == i:
                    numSteps = stp[2]
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
        
        if (i == startBlocks and not found):
            print("REDUCE THE STARTING VALUE!")
            i += 1

                
        if (i >= startBlocks and found == False):
            numBlocks = 0
            startBlocks = 10000000
        
print(f"Takes {numSteps} steps after {val} fallen blocks.")
print(f"First block that causes failure at {ln[0]},{ln[1]}. Block number: {i}")


# Map visualization at first blocked case:
# for v in visited:
#     if (mp[v[0]][v[1]] != "#"):
#         mp[v[0]][v[1]] = "O"
        
# for r in mp:
#     out = ""
#     for x in r:
#         out += (x)
#     print(out)