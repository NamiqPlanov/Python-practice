def min_max_val(arr):
    n = len(arr)
    if n<-3:
        return -1
    min_val = min(arr)
    max_val = max(arr)
    for num in arr:
        if num !=min_val and num !=max_val:
            return num
    return -1
print(min_max_val([1,3,4]))