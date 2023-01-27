###Pascal triangle
a = 1
b = 1
prevRow = []
prevRow.append([1,1])###second row
rows = int(input("Enter the number of rows: "))
print("1")
for k in range(1,rows):
    for m in range(k):
        r = prevRow[m] + prevRow[m+1]
        
