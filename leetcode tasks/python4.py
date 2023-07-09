def sum(arr,numsofconselem,target):
    for i in range(len(arr)-numsofconselem):
        s = arr[i]
        for j in range(i+1,i+numsofconselem):
            s+=arr[i]
        if s<target:
            return True
    return False

print(sum([1,2,3,4,5,6], 3, 7))
        













