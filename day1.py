x = []
y = []

with open('1input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        ln = ln.split("   ")
        x.append(int(ln[0]))
        y.append(int(ln[1]))
        
x.sort()
y.sort()

sum = 0
similarity = 0

for i in range(len(x)):
    diff = abs(y[i] - x[i])
    sum = sum + diff
    count = y.count(x[i])
    similarity = similarity + count*x[i]
    
print(f"Sum: {sum}") #Part 1
print(f"Similarity: {similarity}") #Part 2