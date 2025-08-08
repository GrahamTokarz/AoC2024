
intrs = []
#with open('testcase.txt', 'r') as file:
with open('2016_2input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        ln = list(ln)
        intrs.append(ln)
     
start = 5    
out = ""
order = ["X", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"]

#Part 1 (6:35.30)
# for ins in intrs:
#     for n in ins:
#         if n == "U":
#             start -= 3
#             if start < 1:
#                 start += 3
#         if n == "L":
#             start -= 1
#             if start%3 == 0:
#                 start += 1
#         if n == "R":
#             start += 1
#             if start%3 == 1:
#                 start -= 1
#         if n == "D":
#             start += 3
#             if start > 9:
#                 start -= 3
#     out = out + order[start]

#Part 2 (6:23.14)
for ins in intrs:
    for n in ins:
        if n == "U":
            if (start in [6, 7, 8, 10, 11, 12]):
                start -= 4
            elif (start in [3, 13]):
                start -= 2
        if n == "L":
            if (start in [3, 4, 6, 7, 8, 9, 11, 12]):
                start -= 1
        if n == "R":
            if (start in [2, 3, 5, 6, 7, 8, 10, 11]):
                start += 1
        if n == "D":
            if (start in [2, 3, 4, 6, 7, 8]):
                start += 4
            elif (start in [1, 11]):
                start += 2
    out = out + order[start]
    
print(out)