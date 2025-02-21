def add_matrix(A,B):
    row=len(A)
    col=len(A[0])

    result=[[0] * col for _ in range(row)]

    # Matrix Addition
    for i in range(row):
        for j in range(col):
            result[i][j]=A[i][j] + B[i][j]
    return result

A = [ [1, 2, 1], [2, 2, 7], [3, 5, 3], [4, 1, 9] ]
B = [ [1, 1, 6], [8, 4, 2], [6, 3, 2], [2, 4, 1] ]

result=add_matrix(A,B)
print("Result Matrix is :" )

for i in result:
    print(" ".join(map(str,i)))
    # print(i)

