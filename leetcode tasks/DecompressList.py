def DecompressList(arr):
    answer = []
    n = len(arr)
    for i in range(0,n,2):
        answer = [arr[i+1]]*arr[i]
    return answer

print(DecompressList([1,2]))

