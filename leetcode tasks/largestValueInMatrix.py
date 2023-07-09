def LargestValue(grid):
    n = len(grid)
    answer = [[0]*(n-2) for _ in range(n-2)]
    for i in range(n-2):
        for j in range(n-2):
            for x in range(i,i+3):
                for y in range(j,j+3):
                    answer[i][j] = max(answer[i][j], grid[x][y])
    return answer

print()