#with open('testcase.txt', 'r') as file:
with open('3input.txt', 'r') as file:
    enabled = True
    sum = 0
    for line in file:
        ln = line.strip()
        ln = ln.split("mul(")
        for i in range(len(ln)):
            sp1 = ln[i].split(",")
            if(sp1[0].__contains__("do()")):
                enabled = True
            if(sp1[0].__contains__("don't()")):
                enabled = False
            if (len(sp1) >= 2):
                sp2 = sp1[1].split(")")
                if (sp2[0] != sp1[1] and enabled): #Remove the and to simulate part 1
                    try:
                        mul = int(sp1[0]) * int(sp2[0])
                        sum = sum + mul
                    except:
                        sum = sum + 0
                for i in range(1, len(sp1)):
                    if(sp1[i].__contains__("do()")):
                        enabled = True
                    if(sp1[i].__contains__("don't()")):
                        enabled = False
            #I don't like this solution for the do() and don't() because it doesn't take into account the test case where don't()do() occurs in a pattern like that, in one segment.                
        
        
print(f"Sum: {sum}")