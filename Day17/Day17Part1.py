jet_pattern = []

with open("17.in") as file:
    for line in file:
        jet_pattern = list(map(lambda x: -1 if x == '<' else 1 , line.rstrip()))

# Stored as boolean in rocks[rock_num][row][col]
rocks = []
# Stored as int in rocks
rocks_lowest = []
rocks_ptr = []

with open("17-Rocks.in") as file:
    index = 0
    for line in file:
        if line.isspace():
            index += 1
            continue
        if len(rocks) == index:
            rocks.append([])
            rocks_lowest.append([])
            rocks_ptr = rocks[index]
        
        rocks_ptr.append([])
        line = line.rstrip()

        for c in line:
            rocks_ptr[-1].append(True if c == "#" else False)


grid = [[True for i in range(7)]]
jet_index = 0
rock_index = 0

for count in range(2022):
    rock_curr = rocks[rock_index]
    rock_height = len(rock_curr)
    rock_width = len(rock_curr[0])

    for row_idx in range(len(grid) - 1, -1, -1): # Check where the highest rock is
        if True in grid[row_idx]: # Check which row contains the highest rock
            add_times = 4 + rock_height - len(grid) + row_idx
            if add_times >= 0: # Add additional rows
                for i in range(add_times):
                    grid.append([False for i in range(7)])
                break
            else: # Remove extra rows
                for i in range(-add_times):
                    grid.pop()
                break
    
    rock_x = 2
    rock_y = len(grid) - 1

    while True:
        # Rock pushed by jet
        rock_x_jet = rock_x + jet_pattern[jet_index]
        if rock_x_jet >= 0 and rock_x_jet + rock_width <= 7:
            for x in range(rock_width):
                for y in range(rock_height):
                    # Collision between moving and settled rock
                    if rock_curr[y][x] and grid[rock_y - y][rock_x_jet + x]:
                        rock_x_jet = rock_x
                        break
            rock_x = rock_x_jet

        jet_index = (jet_index + 1) % len(jet_pattern)
        
        # Rock falling 1 unit
        rock_y_fall = rock_y - 1
        to_settle = False
        for x in range(rock_width):
            for y in range(rock_height):
                if rock_curr[y][x] and grid[rock_y_fall - y][rock_x + x]:
                    to_settle = True
                    break
        
        if to_settle:
            for x in range(rock_width):
                for y in range(rock_height):
                    grid[rock_y - y][rock_x + x] = rock_curr[y][x] or grid[rock_y - y][rock_x + x]
            break
        else:
            rock_y = rock_y_fall
    
    rock_index = (rock_index + 1) % len(rocks)

 
for i in range(len(grid) - 1, -1, -1):
    if True in grid[i]:
        print(i)
        break