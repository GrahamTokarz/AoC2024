def horiz(r, col):
    if (r[col] == "X"
        and r[j + 1] == "M"
        and r[col + 2] == "A"
        and r[col + 3] == "S"):
        return 1
    return 0

def bhoriz(r, col):
    if (r[col] == "X"
        and r[j - 1] == "M"
        and r[col - 2] == "A"
        and r[col - 3] == "S"):
        return 1
    return 0

def vert(r, row, col):
    if (r[row][col] == "X" 
        and r[i + 1][col] == "M"
        and r[row + 2][col] == "A"
        and r[row + 3][col] == "S"):
        return 1
    return 0

def bvert(r, row, col):
    if (r[row][col] == "X" 
        and r[i - 1][col] == "M"
        and r[row - 2][col] == "A"
        and r[row - 3][col] == "S"):
        return 1
    return 0

def ul(r, row, col):
    if (r[row][col] == "X" 
        and r[i - 1][j - 1] == "M"
        and r[row - 2][col - 2] == "A"
        and r[row - 3][col - 3] == "S"):
        return 1
    return 0

def ur(r, row, col):
    if (r[row][col] == "X" 
        and r[i - 1][j + 1] == "M"
        and r[row - 2][col + 2] == "A"
        and r[row - 3][col + 3] == "S"):
        return 1
    return 0

def dl(r, row, col):
    if (r[row][col] == "X" 
        and r[i + 1][j - 1] == "M"
        and r[row + 2][col - 2] == "A"
        and r[row + 3][col - 3] == "S"):
        return 1
    return 0

def dr(r, row, col):
    if (r[row][col] == "X" 
        and r[i + 1][j + 1] == "M"
        and r[row + 2][col + 2] == "A"
        and r[row + 3][col + 3] == "S"):
        return 1
    return 0

#with open('testcase.txt', 'r') as file:
with open('4input.txt', 'r') as file:
    count = 0
    
    r = []
    for line in file:
        ln = line.strip()
        r.append(list(ln))
            
    i = 0
    j = 0
    
    for row in r:
        j = 0
        for col in row:
            #Part 1
            # if (col == "X"):
                # if (j < (len(row) - 3)):
                #     count = count + horiz(row, j)
                #     if (i < (len(r) - 3)):
                #         count = count + dr(r, i, j)
                #     if (i > 2):
                #         count = count + ur(r, i, j)
                # if (j > 2):
                #     count = count + bhoriz(row, j)
                #     if (i < (len(r) - 3)):
                #         count = count + dl(r, i, j)
                #     if (i > 2):
                #         count = count + ul(r, i, j)
                # if (i < (len(r) - 3)):
                #     count = count + vert(r, i, j)
                # if (i > 2):
                #     count = count + bvert(r, i, j)
            
            #Part 2
            if (col == "A" and i > 0 and i < len(r) - 1 and j > 0 and j < len(row) - 1):
                if ((r[i - 1][j - 1] == "M" and r[i + 1][j + 1] == "S") or
                    (r[i - 1][j - 1] == "S" and r[i + 1][j + 1] == "M")):
                    if ((r[i + 1][j - 1] == "M" and r[i - 1][j + 1] == "S") or
                        (r[i + 1][j - 1] == "S" and r[i - 1][j + 1] == "M")):
                        count = count + 1
            
            j = j + 1
        i = i + 1
                
        
          
        
print(f"Count: {count}")