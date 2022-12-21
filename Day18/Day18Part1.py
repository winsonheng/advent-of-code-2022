grid_x = {}
grid_y = {}
grid_z = {}

with open("18.in") as file:
    for line in file:
        coord = list(map(lambda x: int(x), line.rstrip().split(",")))
        
        x, y, z = coord

        # Add into grid_x
        if y not in grid_x:
            grid_x[y] = {}
        if z not in grid_x[y]:
            grid_x[y][z] = []

        target_list = grid_x[y][z]
        new_int = [x, x]
        to_remove = []
        add_flag = True # Boolean to add new_int
        for interval in target_list:
            if new_int[0] >= interval[0]:
                if new_int[1] <= interval[1]: # Coordinate already contained
                    add_flag = False
                    break
                elif new_int[0] <= interval[1] + 1:
                    new_int[0] = interval[0]
                    to_remove.append(interval)
            elif new_int[1] >= interval[0] - 1:
                new_int[1] = max(new_int[1], interval[1])
                to_remove.append(interval)
        
        for interval in to_remove:
            target_list.remove(interval)
        if add_flag:
            target_list.append(new_int)
        

        # Add into grid_y
        if x not in grid_y:
            grid_y[x] = {}
        if z not in grid_y[x]:
            grid_y[x][z] = []

        target_list = grid_y[x][z]
        new_int = [y, y]
        to_remove = []
        add_flag = True # Boolean to add new_int
        for interval in target_list:
            if new_int[0] >= interval[0]:
                if new_int[1] <= interval[1]: # Coordinate already contained
                    add_flag = False
                    break
                elif new_int[0] <= interval[1] + 1:
                    new_int[0] = interval[0]
                    to_remove.append(interval)
            elif new_int[1] >= interval[0] - 1:
                new_int[1] = max(new_int[1], interval[1])
                to_remove.append(interval)
        
        for interval in to_remove:
            target_list.remove(interval)
        if add_flag:
            target_list.append(new_int)


        # Add into grid_z
        if x not in grid_z:
            grid_z[x] = {}
        if y not in grid_z[x]:
            grid_z[x][y] = []

        target_list = grid_z[x][y]
        new_int = [z, z]
        to_remove = []
        add_flag = True # Boolean to add new_int
        for interval in target_list:
            if new_int[0] >= interval[0]:
                if new_int[1] <= interval[1]: # Coordinate already contained
                    add_flag = False
                    break
                elif new_int[0] <= interval[1] + 1:
                    new_int[0] = interval[0]
                    to_remove.append(interval)
            elif new_int[1] >= interval[0] - 1:
                new_int[1] = max(new_int[1], interval[1])
                to_remove.append(interval)
        
        for interval in to_remove:
            target_list.remove(interval)
        if add_flag:
            target_list.append(new_int)


area = 0

for i in grid_x:
    for j in grid_x[i]:
        area += 2 * len(grid_x[i][j])

for i in grid_y:
    for j in grid_y[i]:
        area += 2 * len(grid_y[i][j])

for i in grid_z:
    for j in grid_z[i]:
        area += 2 * len(grid_z[i][j])
    
print(area)