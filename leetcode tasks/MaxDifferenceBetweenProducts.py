def MaxDifference(arr):
    arr.sort()
    return (arr[-1]*arr[-2])-(arr[0]*arr[1])

print(MaxDifference([10,11,12,5,6]))