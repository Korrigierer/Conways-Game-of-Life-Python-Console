import time

A = "A" # Alive Cells that will be displayed as a green square
D = "D" # Dead Cells = Red square

# 10 x 10 grid
grid = [
    [D, D, D, D, D, D, D, D, D, D],
    [D, D, D, D, A, A, D, D, D, D],
    [D, D, D, A, D, D, A, D, D, D],
    [D, D, A, D, D, D, D, A, D, D],
    [D, A, D, D, D, D, D, D, A, D],
    [D, A, D, D, D, D, D, D, A, D],
    [D, D, A, D, D, D, D, A, D, D],
    [D, D, D, A, D, D, A, D, D, D],
    [D, D, D, D, A, A, D, D, D, D],
    [D, D, D, D, D, D, D, D, D, D]
]

needChange = []


def printGrid(grid):
    for i, item in enumerate(grid):
        for j, item2 in enumerate(grid[i]):
            print(grid[i][j], end=' ')
        print()
    print()


def formatGrid():
    for i, item in enumerate(grid):
        for j, item2 in enumerate(grid[i]):
            if item2 == D:
                grid[i][j] = "🟥"
            else:
                grid[i][j] = "🟩"


def getAlive(i, j):
    alive_cells = 0
    if grid[i-1][j-1] == "🟩":
        alive_cells += 1
    if grid[i-1][j] == "🟩":
        alive_cells += 1
    if grid[i-1][j+1] == "🟩":
        alive_cells += 1
    if grid[i][j-1] == "🟩":
        alive_cells += 1
    if grid[i][j+1] == "🟩":
        alive_cells += 1
    if grid[i+1][j-1] == "🟩":
        alive_cells += 1
    if grid[i+1][j] == "🟩":
        alive_cells += 1
    if grid[i+1][j+1] == "🟩":
        alive_cells += 1
    return alive_cells


def getChanges():
    needChange.clear()
    for i, item in enumerate(grid):
        for j, item2 in enumerate(grid[i]):
            if i > 0 and j > 0 and i < len(grid) - 1 and j < len(grid[i]) - 1:
                alive_cells = getAlive(i, j)
                if item2 == "🟥":
                    if alive_cells == 3:
                        needChange.append([i, j, "🟩"])
                if item2 == "🟩":
                    if alive_cells < 2 or alive_cells > 3:
                        needChange.append([i, j, "🟥"])


def applyChanges():
    for i, item in enumerate(needChange):
        grid[needChange[i][0]][needChange[i][1]] = needChange[i][2]


formatGrid()
printGrid(grid)
while True:
    getChanges()
    applyChanges()
    printGrid(grid)
    time.sleep(1)
