def SumArraysLinear(arr, numofConselem ,target):
    sum = 0
    for i in range(0,len(arr)-numofConselem):
        s+=arr[i]
        if i>= numofConselem:
            s-=arr[i-numofConselem]
        if i+1 >= numofConselem -1:
            if s<target:
                return True
    return False


print ( SumArraysLinear([1, 2, 3, 4, 5], 10, 3))
