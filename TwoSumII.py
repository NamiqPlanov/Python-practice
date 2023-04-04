def TwoSum(arr,target):
    l = 0
    r = len(arr)-1
    while l<r:
        currentSum = arr[l]+arr[r]
        if currentSum<target:
            l+=1
        elif currentSum >target:
            r-=1
        else:
            return [l+1,r+1]
    return []

print(TwoSum([1,2,3,4,5,6], 6))