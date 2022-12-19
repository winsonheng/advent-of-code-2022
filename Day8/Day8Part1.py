grid = []

with open("8.in") as file:
    for line in file:
        line = line.rstrip()
        grid.append(list(map(lambda x: int(x), line)))


tallest_tree_grid = [[[-1 for c in grid[0]] for r in grid] for i in range(4)] # L, U, R, D

# Compute the tallest tree for each tree from the left and right directions
for r in range(len(grid)):
    tallest = 0
    row = grid[r]
    tallest_row = tallest_tree_grid[0][r]
    for c in range(1, len(row)):
        tallest = max(tallest, row[c - 1])
        tallest_row[c] = tallest
    
    tallest = 0
    tallest_row = tallest_tree_grid[2][r]
    for c in range(len(row) - 2, -1, -1):
        tallest = max(tallest, row[c + 1])
        tallest_row[c] = tallest

# Compute the tallest tree for each tree from the left and right directions
for c in range(len(grid[0])):
    tallest = 0
    for r in range(1, len(grid)):
        tallest = max(tallest, grid[r - 1][c])
        tallest_tree_grid[1][r][c] = tallest
    
    tallest = 0
    for r in range(len(grid) - 2, -1 , -1):
        tallest = max(tallest, grid[r + 1][c])
        tallest_tree_grid[3][r][c] = tallest

count = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        for i in range(4):
            if grid[r][c] > tallest_tree_grid[i][r][c]:
                count += 1
                break

print(count)