def deleteunsortedcol(strs):
    m = len(strs)
    n = len(strs[0])
    ans = 0
    for col in range(n):
        for row in range(m-1):
            if strs[row][col]>strs[row+1][col]:
                ans+=1
                break
    return ans
print(deleteunsortedcol(['abc','def,ghi']))


