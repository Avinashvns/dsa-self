A = [ [1, 2, 1], [2, 2, 7], [3, 5, 3], [4, 1, 9] ]
B = [ [1, 1, 6], [8, 4, 2], [6, 3, 2], [2, 4, 4] ]

# Get Dimension of Arr 1
rowsA=len(A)
colsA=len(A[0])

# Get Dimension of Arr 2
rowsB=len(B)
colsB=len(B[0])

if rowsA ==rowsB and colsA==colsB:
    print("Matrices A and B have the same dimensions.")
else:
    print("Matrices A and B do NOT have the same dimensions.")

# result matrix like as [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
result=[[0]*colsA for _ in range(rowsA)]

for i in range(rowsA):
    for j in range(colsB):
        result[i][j]=A[i][j] + B[i][j]

for addMatrix in result:
    print(addMatrix)

