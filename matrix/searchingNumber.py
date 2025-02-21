arr = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
]

# create a function for Searching an Element
def searching_number(arr,num):
    rows,cols= len(arr),len(arr[0])

    # Traverse each row and columns
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==num:
                return (i,j)
    return None

number=500
position = searching_number(arr,number)

if position:
    print(f"Yes , number {number} is available at Position {position}")
else:
    print(f"Number {number} is not available")