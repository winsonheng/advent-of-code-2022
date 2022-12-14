with open("14.in") as file:
    lines = [list(map(lambda x: list(map(lambda y: int(y), x.split(","))), line.rstrip().split(" -> "))) for line in file]

xIndices = [inner[0] for outer in lines for inner in outer]
yIndices = [inner[1] for outer in lines for inner in outer]

xMin = min(xIndices)
xMax = max(xIndices)
xSize = xMax - xMin + 1
yMax = max(yIndices)
ySize = yMax + 1

grid = [[False for i in range(ySize)] for i in range(xSize)]

for row in lines:
    for i in range(len(row) - 1):
        xStart, yStart = row[i]
        xEnd, yEnd = row[i + 1]
        if xStart == xEnd:
            step = 1 if yEnd >= yStart else -1
            for y in range(yStart, yEnd + step, step):
                grid[xStart - xMin][y] = True
        elif yStart == yEnd:
            step = 1 if xEnd >= xStart else -1
            for x in range(xStart, xEnd + step, step):
                grid[x - xMin][yStart] = True

continueFlag = True
count = 0
while continueFlag:
    xSand = 500 - xMin
    ySand = 0
    while True:
        if ySand == yMax: # Reached bottom of grid
            continueFlag = False
            break
        elif not grid[xSand][ySand + 1]: # Straight down
            ySand += 1
        elif xSand == 0: # Reached leftmost column
            continueFlag = False
            break
        elif not grid[xSand - 1][ySand + 1]: # Diagonal left
            xSand -= 1
            ySand += 1
        elif xSand == xSize - 1: # Reached rightmost column
            continueFlag = False
            break
        elif not grid[xSand + 1][ySand + 1]:
            xSand += 1
            ySand += 1
        else: # Sand settles as no where to go
            count += 1
            grid[xSand][ySand] = True
            break

print(count)
