matrix = []
rowsInput = int(input("Enter the amount of rows: "))
columnInput = int(input("Enter the amount of columns: "))

for i in range(rowsInput):
    tempList = []
    for j in range(columnInput):
        x = int(input("Enter your values: "))
        tempList.append(x)
    matrix.append(tempList)

for a in range(rowsInput):
    for b in range(columnInput):
        print(matrix[a][b], end="   ")
    
    print("\n")    