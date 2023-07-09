def mintime(points):
    ans = 0
    n = len(points)
    p1 = points[0]
    for i in range(1,n):
        p2 = points[i]
        dx = p2[0]-p1[0]
        dy = p2[1]-p1[1]
        ans += max(abs(dx), abs(dy))
        p1=p2
    return ans

print(mintime([[1,1],[3,4],[-1,0]]))