#Brute force method
def area_most(height):
    n = len(height)
    res = 0
    for l in range(n):
        for r in range(l+1,n):
            area = (r-l)*(min(height[l],height[r]))
            res = max(res,area)
    return res

print(area_most([1,2,3,4,5,6,7]))
#linear method
def are2(height2):
    res = 0
    l,r = 0,len(height2)-1
    while l<r:
        area = (r-l)*(min(height2[l],height2[r]))
        res = max(res,area)
        if height2[l]<height2[r]:
            l+=1
        else:
            r-=1
    return res
    
