def TargetArray(arr,index):
    n = len(arr)
    answer = []
    for i in range(n):
        answer.insert(index[i], arr[i])
    return answer
print(TargetArray([1,2,3,4,5],[0,1,2,3,1]))