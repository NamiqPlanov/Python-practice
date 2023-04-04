def duplicate(arr):
    a = set()
    n = len(arr)
    for i in range(n):
        if arr[i] not in a:
            a.add(arr[i])
        else:
            return True
    return False
print(duplicate([1,1,2,3,4,5]))