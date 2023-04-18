def countpairs(arr,k):
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(1,n):
            if arr[i]==arr[j] and i<j and (i*j)%k==0:
                ans+=1
    return ans
print(countpairs([1,2,3,4,5,9,10], 2))
print(countpairs([3,3,4,2,5,2,3], 2))