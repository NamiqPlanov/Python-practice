def BinarySearch(arr,target):
    n = len(arr)
    left =0
    right = n-1
    while left <=right:
        middle = (left+right)//2
        if arr[middle]==target:
            return middle
        elif arr[middle]>target:
            right = middle-1
        else:
            left = middle+1
    return -1

print(BinarySearch([1,2,3,4,5,6,7,8,9], 5))