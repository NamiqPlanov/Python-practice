def delete(arr,val):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i]!=val:
            arr[count]=arr[i]
            count +=1
    return count

print(delete([1,2,3,4,5], 2))



def removeelem(arr2,target):
    newarr= []
    n = len(arr2)
    for i in range(n):
         if arr2[i]!=target:
            newarr.append(arr2[i])
    return newarr

print(removeelem([1,2,3,4,5], 3))
