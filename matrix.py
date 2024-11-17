matrix1=[[1,2,3],[2,3,4],[4,3,2]]
matrix2=[[11,12,13],[21,31,14],[41,31,12]]
# no of rows
print(len(matrix1))
# no of col
print(len(matrix1[0]))
# print(matrix1+matrix2)
result=[]
rows=len(matrix1)
col=len(matrix1[0])
for i in range(rows):
  temp=[]
  for j in range(col):
    temp.append(matrix1[i][j]+matrix2[i][j])
    # print(matrix1[i][j],"  ",i,j)
  result.append(temp)
  
print(result)

newList=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(rows):
    for j in range(col):
        for k in range(2):
            newList[i][j] = newList[i][j] + (matrix1[i][k]*matrix2[k][j])
print(newList)            