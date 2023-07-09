def kthmissing(arr,k):
    set1 = set(arr)
    i = 1
    while True:
        if i not in set1:
            k-=1
        if k==0:
            return i
        i+=1
    return i
print(kthmissing([1,3,4,5,6], 1))