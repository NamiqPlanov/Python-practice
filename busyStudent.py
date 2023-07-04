def busystudent(starttime,endtime,querytime):
    ans = 0
    n = len(endtime)
    for i in range(n):
        if starttime[i]<querytime and endtime[i]>querytime:
            ans+=1
    return ans
print(busystudent([3,4,2],[6,7,5],6))