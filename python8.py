def sumindices(arr,target):
    cache = {}
    for i in range(len(arr)):
        a = arr[i]
        b = target - a
        if b in cache:
            return i,cache[b]
        cache[a]=i

sumindices([1,2,3,4],5 )