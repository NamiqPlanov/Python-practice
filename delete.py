
def deleteelem(arr,target):
    newarr = []
    n = len(arr)
    for i in range(n):
        if arr[i]!=target:
            newarr.append(arr[i])
    return newarr
print(deleteelem([10,20,30,40,50],30))

