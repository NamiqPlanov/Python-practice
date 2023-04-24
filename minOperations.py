def minOperations(arr):
    ans = 0
    n = len(arr)
    for i in range(n-1):
        if arr[i]>=arr[i+1]:
            diff = abs(arr[i+1]-arr[i])
            ans += diff+1
            arr[i+1] +=diff+1
    return ans

print(minOperations([1,2,2,3]))