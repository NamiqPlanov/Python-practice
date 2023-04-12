def matrix(matrix,target):
    r = len(matrix)
    c = len(matrix[0])
    top = 0
    bottom = r-1
    while top<=bottom:
        row  = (top+bottom)//2
        if target > matrix[row][-1]:
            top = row+1
        elif target < matrix [row][0]:
            bottom = row-1
        else:
            break
    if not(top<=bottom):
        return False
    row = (top+bottom)//2
    l = 0
    r1 = c-1
    while l<r1:
        m = (l+r1)//2
        if target >matrix[row][m]:
            l = m+1
        elif target <matrix[row][m]:
            r1 = m-1
        else:return True
    return False
