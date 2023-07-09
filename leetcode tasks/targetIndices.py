def targetindex(arr,target):
    ans = []
    n = len(arr)
    arr.sort()
    for i in range(n):
        if arr[i]==target:
            ans.append(i)
        
    return ans
print(targetindex([5,3,4,2,7,8], 5))

