def prefix_suffix(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        prefix1 = len(set(arr[:i+1]))
        suffix1 = len(set(arr[i+1:]))
        ans.append(prefix1-suffix1)
    return ans
print(prefix_suffix([1,2,3,4,5,6]))
