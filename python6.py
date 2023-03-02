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


def linear(arr2,nums2,target2):
    s = 0
    for i in range(len(arr2)-nums2):
        s+=arr2[i]
        if i>=nums2:
            s-arr2[i-nums2]
        if i+1>=nums2-1:
            if s<target2:
                return arr2[i],i
print(linear([1,2,3,4,5,6], 3, 10))
