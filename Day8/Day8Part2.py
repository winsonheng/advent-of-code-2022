grid = []

with open("8.in") as file:
    for line in file:
        line = line.rstrip()
        grid.append(list(map(lambda x: int(x), line)))


tallest_tree_grid = [[[-1 for c in grid[0]] for r in grid] for i in range(4)] # L, U, R, D

# Compute the tallest tree for each tree from the left and right directions
for r in range(len(grid)):
    row = grid[r]
    tallest_row = tallest_tree_grid[0][r]
    nearest_tree = [0 for i in range(10)]
    for c in range(len(row)):
        nearest_index = 0
        for index in nearest_tree[row[c]:]:
            nearest_index = max(nearest_index, index)
        nearest_tree[row[c]] = c
        tallest_row[c] = c - nearest_index
    
    tallest_row = tallest_tree_grid[2][r]
    nearest_tree = [len(row) - 1 for i in range(10)]
    for c in range(len(row) - 1, -1, -1):
        nearest_index = len(row) - 1
        for index in nearest_tree[row[c]:]:
            nearest_index = min(nearest_index, index)
        nearest_tree[row[c]] = c
        tallest_row[c] = nearest_index - c

# Compute the tallest tree for each tree from the left and right directions
for c in range(len(grid[0])):
    nearest_tree = [0 for i in range(10)]
    for r in range(len(grid)):
        nearest_index = 0
        for index in nearest_tree[grid[r][c]:]:
            nearest_index = max(nearest_index, index)
        nearest_tree[grid[r][c]] = r
        tallest_tree_grid[1][r][c] = r - nearest_index
    
    nearest_tree = [len(grid[c]) - 1 for i in range(10)]
    for r in range(len(grid[c]) - 1, -1 , -1):
        nearest_index = len(grid[c]) - 1
        for index in nearest_tree[grid[r][c]:]:
            nearest_index = min(nearest_index, index)
        nearest_tree[grid[r][c]] = r
        tallest_tree_grid[3][r][c] = nearest_index - r

max_score = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        score = 1
        for i in range(4):
            score *= tallest_tree_grid[i][r][c]
        max_score = max(max_score, score)

print(max_score)