'''def island(grid):
    answer = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c]==1:
                answer+=1
                stack = [(r,c)]
                grid[r][c] =0
                while stack:
                    r1,c1 = stack.pop()
                    if r1+1<len(grid) and grid[r1+1][c1]==1  :
                        stack.append(r1+1,c1)
                        grid[r1+1][c1]=0
                    if r1-1>=0 and grid[r1-1][c1]==1  :
                        stack.append(r1-1,c1)
                        grid[r1-1][c1]=0
                    if c1+1<len(grid[0]) and grid[r1][c1+1]==1  :
                        stack.append(r1,c1+1)
                        grid[r1][c1+1]=0
                    if c1-1>=0 and grid[r1][c1-1]==1   :
                        stack.append(r1,c1-1)
                        grid[r1][c1-1]=0
    return answer1
    '''
print('neftchi is bad club in Azerbaijan')


