tot = 0
#with open('testcase.txt', 'r') as file:
with open('9input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        ln = list(ln)
        
drive = []
freeBlocks = []
ticker = 0
on = True
j = 0
for v in ln:
    for i in range(int(v)):
        j += 1
        if on:
            drive.append([ticker, int(v)])
        else:
            drive.append([".", int(v)])
    if on:
        ticker += 1
    else:
        freeBlocks.append([int(v), j - int(v)])
    on = not on

s = 0
e = len(drive) - 1

#Part 1
# while s < e:
#     while(drive[s][0] != "."):
#         s += 1
#     while(drive[e][0] == "."):
#         e -= 1
#     if (s < e):
#         drive[s] = drive[e]
#         drive[e] = [".", 1]

#Part 2
while e > 0:
    while(drive[e][0] == "."):
        e -= 1
    comp = False
    for block in freeBlocks:
        if (not comp):
            if (block[0] >= drive[e][1]) and (block[1] < e):
                comp = True
                s = block[1]
                for i in range(block[0]):
                    if (i < drive[e][1]):
                        drive[s + i] = drive[e]
                block[0] = block[0] - drive[e][1]
                block[1] = block[1] + drive[e][1]
                for i in range(drive[e][1]):
                    drive[e - i] = [".", 1]
    e -= 1

i = 0
for v in drive:
    if (v[0] != "."):
        tot += i * v[0]
    i += 1
        
print(f"Checksum: {tot}")