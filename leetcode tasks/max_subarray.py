def max_subarray(arr):
    res = 0
    maxsub = arr[0]
    for i in arr:
        if res<0:
            res = 0
        res+=i
        maxsub = max(maxsub,res)
    return maxsub
print(max_subarray([1,2,3,4,4,-1,-2]))