def MaxProduct(arr):
    n = len(arr)
    arr.sort()
    return (arr[-1]-1)*(arr[-2]-1)
print(MaxProduct([1,2,3]))