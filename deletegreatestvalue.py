def delgreatestvalue(grid:list)->int:
    rows = len(grid)
    cols = len(grid[0])
    result = 0
    for i in range(rows):
        grid[i].sort()
    for j in range(cols):
        result+=max(grid[i][j] for i in range(rows))
    return result
print(delgreatestvalue([[10,6],[6,4]]))