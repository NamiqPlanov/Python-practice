
def binarysearch(arr,target):
    n =len(arr)
    left = 0
    right = n-1
    while left<=right:
        middle = (right+left)//2
        if arr[middle]==target:
            return middle
        elif arr[middle]<target:
            left = middle+1
        else:
            right = middle-1
    return 'this number does not exist in this array'
print(binary([102,134,23,12,14,56], 34))