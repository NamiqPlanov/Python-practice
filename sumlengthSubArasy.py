def SubArray(arr):
    answer = 0
    n = len(arr)
    for i in range(n):
        j = i+1
        while j<=n:
            answer+=sum(arr[i:j])
    return answer
print(SubArray([1,2,2,3]))