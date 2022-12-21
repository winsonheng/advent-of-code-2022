target_cycles = [20 + 40 * i for i in range(6)]
target_id = 0
cycle = 0
signal = 1

grid = [['.' for i in range(40)] for j in range(6)]
grid_x = 0
grid_y = 0

MAX_GRID_X = 39

with open("10.in") as file:
    for line in file:
        cycle += 1
        line = line.rstrip()

        if grid_x >= signal - 1 and grid_x <= signal + 1:
            grid[grid_y][grid_x] = '#'

        if grid_x == MAX_GRID_X:
            grid_y += 1
            grid_x = 0
        else:
            grid_x += 1

        if line == "noop":
            continue
        else:
            cycle += 1
            if grid_x >= signal - 1 and grid_x <= signal + 1:
                grid[grid_y][grid_x] = '#'

            if grid_x == MAX_GRID_X:
                grid_y += 1
                grid_x = 0
            else:
                grid_x += 1
            signal += int(line.removeprefix("addx "))
        

for row in grid:
    print("".join(row))