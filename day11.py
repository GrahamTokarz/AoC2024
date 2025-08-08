import math

lst = []
#with open('testcase.txt', 'r') as file:
with open('11input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        lst = ln.split(" ")
        
col = {}

for val in lst:
    if (val in col.keys()):
        col[val] += 1
    else:
        col[val] = 1

print(col)

i = 0
n = 1000 #P1: 25, P2: 75
for i in range(n):
    ncol = {}
    for v in col.keys():
        if (v == "0"):
            if ("1" in ncol.keys()):
                ncol["1"] += col[v]
            else:
                ncol["1"] = col[v]
        elif (len(v)%2 == 0):
            y = v[0:math.floor(len(v)/2)]
            x = str(int(v[math.ceil(len(v)/2):]))
            if (y in ncol.keys()):
                ncol[y] += col[v]
            else:
                ncol[y] = col[v]
            if (x in ncol.keys()):
                ncol[x] += col[v]
            else:
                ncol[x] = col[v]
        else:
            x = str(int(v)*2024)
            if (x in ncol.keys()):
                ncol[x] += col[v]
            else:
                ncol[x] = col[v]
    col = ncol
       
num = 0
for v in col.keys():
    num += col[v]

print(f"Num stones: {num}")