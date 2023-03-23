def smallernunmbers(arr):
   temp = sorted(arr)
   result = []
   mapping = {}
   a = len(temp)
   b = len(arr)
   for i in range(a):
    if temp[i] not in mapping:
        mapping[temp[i]] = i
    for i in range(b):
        result.append(mapping[arr[i]])
    return result
print(smallernunmbers([1,2,3,4,5,6]))
