arr = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
]

rows = len(arr)
print("length of Array :" ,rows)

cols= len(arr[0])
print("Columns Length of Array :" , cols)

# create a function for Searching an Element
def searching_number(arr,num):
    rows,cols= len(arr),len(arr[0])

    # Traverse each row and columns
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==num:
                return True
    return False

if searching_number(arr,8):
    print("Yes Available Number")
else:
    print("Not Available Number")
