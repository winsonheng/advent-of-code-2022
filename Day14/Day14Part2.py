with open("14.in") as file:
    lines = [list(map(lambda x: list(map(lambda y: int(y), x.split(","))), line.rstrip().split(" -> "))) for line in file]

xIndices = [inner[0] for outer in lines for inner in outer]
yIndices = [inner[1] for outer in lines for inner in outer]

yMax = max(yIndices) + 2
ySize = yMax + 1
xMin = min(xIndices)
xMax = max(xIndices)
xSize = xMax - xMin + 1 + 2 * ySize # Added 2 * ySize to allow trickling of sand on both sides

grid = [[False for i in range(ySize - 1)] + [True] for i in range(xSize)]

for row in lines:
    for i in range(len(row) - 1):
        xStart, yStart = row[i]
        xEnd, yEnd = row[i + 1]
        if xStart == xEnd:
            step = 1 if yEnd >= yStart else -1
            for y in range(yStart, yEnd + step, step):
                grid[xStart - xMin + ySize][y] = True
        elif yStart == yEnd:
            step = 1 if xEnd >= xStart else -1
            for x in range(xStart, xEnd + step, step):
                grid[x - xMin + ySize][yStart] = True

continueFlag = True
count = 0
xSandInit = 500 - xMin + ySize
ySandInit = 0
while continueFlag:
    xSand = xSandInit
    ySand = ySandInit
    while True:
        if not grid[xSand][ySand + 1]: # Straight down
            ySand += 1
        elif not grid[xSand - 1][ySand + 1]: # Diagonal left
            xSand -= 1
            ySand += 1
        elif not grid[xSand + 1][ySand + 1]:
            xSand += 1
            ySand += 1
        else: # Sand settles as no where to go
            count += 1
            grid[xSand][ySand] = True
            if xSand == xSandInit and ySand == ySandInit:
                continueFlag = False
            break

print(count)
