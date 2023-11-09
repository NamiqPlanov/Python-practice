#brute force

def brute_force(height):
    res = 0
    for l in range(len(height)):
        for r in range(l+1,len(height)):
            area = (r-l)*min(height[l],height[r])
            res = max(res,area)
    return res

print(brute_force[1,8,6,2,5,4,8,3,7])

#linear
def linear(height):
    res = 0
    l = 0
    s = len(height)
    r = s-1
    while l<r:
        area = (r-l)*min(height[l],height[r])
        res = max(res,area)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return res
print(linear([1,2,3,4,5,6,7]))
