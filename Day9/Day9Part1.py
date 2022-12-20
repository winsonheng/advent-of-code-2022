grid = [[False for i in range(1000)] for j in range(1000)]
direction = {"L": [0, -1], "R": [0, 1], "U": [1, 0], "D": [-1, 0]}

head = [0, 0]
tail = [0, 0]
visited = 0

with open("9.in") as file:
    for line in file:
        dir, moves = line.rstrip().split(" ")
        moves = int(moves)
        dir = direction[dir]

        for i in range(moves):
            head[0] += dir[0]
            head[1] += dir[1]
            
            if abs(head[0] - tail[0]) == 2:
                tail[1] = head[1]
                if head[0] > tail[0]:
                    tail[0] = head[0] - 1
                else:
                    tail[0] = head[0] + 1
            elif abs(head[1] - tail[1]) == 2:
                tail[0] = head[0]
                if head[1] > tail[1]:
                    tail[1] = head[1] - 1
                else:
                    tail[1] = head[1] + 1
                    
            if not grid[tail[0]][tail[1]]:
                visited += 1
                grid[tail[0]][tail[1]] = True


print(visited)