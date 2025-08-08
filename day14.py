import math
robots = []

# with open('testcase.txt', 'r') as file:
with open('14input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        ln = ln[2:].split(" v=")
        p = [int(x) for x in ln[0].split(",")]
        v = [int(x) for x in ln[1].split(",")]
        robots.append([p, v])
        
w = 101 #Test case: 11
h = 103 #Test case: 7

qs = [[], [], [], []]
chrm = True

n = 1
c = 0
while (chrm):
    poss = []
    c += 1
    for r in robots:
        r[0][0] = (r[0][0] + r[1][0]*n)%w
        r[0][1] = (r[0][1] + r[1][1]*n)%h
        if c == 100:
            if (r[0][0] < (w-1)/2):
                if (r[0][1] < (h-1)/2):
                    qs[0].append(r)
                elif (r[0][1] > (h-1)/2):
                    qs[2].append(r)
            elif (r[0][0] > (w-1)/2):
                if (r[0][1] < (h-1)/2):
                    qs[1].append(r)
                elif (r[0][1] > (h-1)/2):
                    qs[3].append(r)
        if ([r[0][0], r[0][1]] not in poss):
            poss.append([r[0][0], r[0][1]])
    if (len(poss) == len(robots)):
        chrm = False
    
            
sf = len(qs[0]) * len(qs[1]) * len(qs[2]) * len(qs[3])
 
print(f"Security factor: {sf}") #Part 1
print(f"Fewest seconds: {c}") #Part 2

# Make a graph to show how *incredibly dumb* the question for part 2 was.
# import matplotlib.pyplot as plt
# import numpy as np

# X = np.array(poss)

# print(X[:, 0])
# plt.scatter(X[:, 0], X[:, 1])
# plt.show()