def arrpartition(arr):
    n = len(arr)
    arr.sort()
    sum1 = 0
    for i in range(0,n,2):
        sum1+=arr[i]
    return sum1
print(arrpartition([1,2,3,6]))






