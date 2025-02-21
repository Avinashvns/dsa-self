
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 1, 0], [2, 4, 3]]

rows_M=len(m1)
cols_M=len(m1[0])

result=[[0]*cols_M for _ in range(rows_M)]
print(result)

for i in range(rows_M):
    for j in range(cols_M):
        result[i][j]=m1[i][j] + m2[i][j]

for i in result:
    print(i)