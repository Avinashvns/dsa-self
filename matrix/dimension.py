def MatSizes(a):
    nrows,ncols=len(a),len(a[0])
    return nrows,ncols

def print_Matrix(a):
    print()
    nrows,ncols=MatSizes(a)
    
    for i in range(nrows):
        for j in range(ncols):
            print(a[i][j], end="\t")
        print()
    print()

def create_matrix(nrows,ncols):
    cols=[0 for x in range(ncols)]
    a=[cols.copy() for c in range(nrows)]
    return a


def add_matrix(a,b):
    nrows,ncols=MatSizes(a)
    result=create_matrix(nrows,ncols)
    # print(result)
    for i in range(nrows):
        for j in range(ncols):
            result[i][j]=a[i][j] + b[i][j]
    return result

def sub_matrix(a,b):
    nrows,ncols=MatSizes(b)
    result=create_matrix(nrows,ncols)

    for i in range(nrows):
        for j in range(ncols):
            result[i][j]=a[i][j] - b[i][j]
    return result


a=[[1,2,3],[4,5,6]]
# nrows=len(a)           
# ncols=len(a[0])  

b=[[1,2,3],[4,6,2]]
# print_Matrix(b)

x=add_matrix(a,a)
print_Matrix(a)
print_Matrix(b)
print_Matrix(x)

print("Subtraction")
z=sub_matrix(a,a)
print_Matrix(a)
print_Matrix(b)
print_Matrix(z)

