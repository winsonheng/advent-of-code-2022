grid = [[False for i in range(2000)] for j in range(2000)]
direction = {"L": [0, -1], "R": [0, 1], "U": [1, 0], "D": [-1, 0]}

rope = [[1000, 1000] for i in range(10)]
visited = 0

with open("9.in") as file:
    for line in file:
        dir, moves = line.rstrip().split(" ")
        moves = int(moves)
        dir = direction[dir]

        for i in range(moves):
            rope[0][0] += dir[0]
            rope[0][1] += dir[1]

            for idx in range(1, 10):
                if abs(rope[idx - 1][0] - rope[idx][0]) == 2 or abs(rope[idx - 1][1] - rope[idx][1]) == 2:
                    if rope[idx - 1][0] > rope[idx][0]:
                        rope[idx][0] += 1
                    elif rope[idx - 1][0] < rope[idx][0]:
                        rope[idx][0] -= 1
                    if rope[idx - 1][1] > rope[idx][1]:
                        rope[idx][1] += 1
                    elif rope[idx - 1][1] < rope[idx][1]:
                        rope[idx][1] -= 1
        
                        
            if not grid[rope[9][0]][rope[9][1]]:
                visited += 1
                grid[rope[9][0]][rope[9][1]] = True


print(visited)