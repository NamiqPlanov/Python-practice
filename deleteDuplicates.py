def removeduplicates(arr):
    k = 1
    n = len(arr)
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            arr[k] = arr[i]
            k+=1
    return k

print(removeduplicates([1,2,2,3,4,5]))


def showunique(arr2):
    arr2 = list(set(arr2))
    return str(arr2)
print(showunique([1,2,3,3,3,4,5]))
