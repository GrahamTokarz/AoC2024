def decreasing(line):
    for i in range(len(line) - 1):
        if int(line[i]) <= int(line[i + 1]):
            return 0
    return 1
    
def increasing(line):
    for i in range(len(line) - 1):
        if int(line[i]) >= int(line[i + 1]):
            return 0
    return 1

def validate(line):
    for i in range(len(line) - 1):
        if abs(int(line[i]) - int(line[i + 1])) > 3:
            return 0
    
    if int(line[0]) > int(line[1]):
        return decreasing(line)
    else:
        return increasing(line)

def removal(line):
    for i in range (len(line)):
        ln = line.copy()
        del ln[i]
        valid = validate(ln)
        if (valid == 1):
            return 1
        
#with open('testcase.txt', 'r') as file:
with open('2input.txt', 'r') as file:
    safe = 0
    for line in file:
        ln = line.strip()
        ln = ln.split(" ")
        valid = validate(ln)
        if (valid == 1):
            safe = safe + 1
        else: #Comment out this else block for part 1 data
            newlyValid = removal(ln)
            if (newlyValid == 1):
                safe = safe + 1
        
print(f"Safe reports: {safe}")