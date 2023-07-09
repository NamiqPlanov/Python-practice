def LeftRightDif(arr):
    left,right = 0,sum(arr)
    for i,number in enumerate(arr):
        left += number
        arr[i] = abs(right-left)
        right -=number

    return arr

print(LeftRightDif([1,2,3,4,5,6,7]))
