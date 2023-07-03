def gsd(arr):
    max1 = max(arr)
    min1 = min(arr)
    i = 1
    ans = []
    while max1>=i:
        if max1%2==0 and min1%2==0:
            ans.append(i)
        i+=1
    return max(ans)
print(gsd([2,5,6,8,9,10]))