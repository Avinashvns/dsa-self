import dimension as d

ncols = 5
cols = [0 for x in range(ncols)]  # List comprehension
# print(cols)
nrows=4
a=[cols.copy() for x in range(nrows)]
d.print_Matrix(a)
a[0][0]=9
print()
d.print_Matrix(a)