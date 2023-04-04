def first(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i]+arr[j]==target:
                return arr[i],arr[j]
print(first([1,2,3,4,5], 5))
        






