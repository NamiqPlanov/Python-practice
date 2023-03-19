def elementexists(arr,target):
    start = 0
    end = len(arr)-1

    while start <=end:
        middle = (start+end)//2
        if arr[middle] ==target:
            return True
        elif arr[middle]<target:
            start =middle+1
        elif ar[middle]>target:
            end = middle-1
    


print(elementexists([1,2,3,4],2))