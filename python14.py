def SearchInsert(arr,target):
    left = 0
    n = len(arr)
    right = n-1
    while left<=right:
        middle = (left+right)//2
        if arr[middle] ==target:
            return middle
        elif target >arr[middle]:
            left = middle +1
        else:
            right = middle-1
    return left

print(SearchInsert([1,3,4,5,6,7],2))