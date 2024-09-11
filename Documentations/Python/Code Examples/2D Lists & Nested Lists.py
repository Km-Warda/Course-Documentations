number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#print(number_grid[ROW][COLUMN])
print(number_grid[0][1])
print(number_grid[2][2])
print("----------")

for row in number_grid:
    print(row)
print("----------")

for row in number_grid:
    for col in row:
        print(col)