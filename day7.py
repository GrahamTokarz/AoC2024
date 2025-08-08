out = 0

#with open('testcase.txt', 'r') as file:
with open('7input.txt', 'r') as file:    
    for line in file:
        ln = line.strip()
        ln = ln.split(": ")
        
        total = int(ln[0])        
        nums = ln[1].split(" ")
        possibilities = [int(nums[0])]
        
        for i in range(1, len(nums)):
            newP = []
            for p in possibilities:
                newP.append(p + int(nums[i]))
                newP.append(p * int(nums[i]))
                newP.append(int(str(p) + nums[i])) #Comment out this line for p1
            possibilities = newP.copy()
        if (total in possibilities):
            out += total
            
print(f"Sum of acceptable equations: {out}")