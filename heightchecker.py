def checkheight(heights):
    n = len(heights)
    sum1 = 0
    h1 = sorted(heights)
    for i in range(n):
        if h1[i]!=heights[i]:
            sum1+=1
    return sum1
print(checkheight([1,2,4,3,5,9,7]))