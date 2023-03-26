def RunningSum(arr):
    answer = []
    temp = 0
    for i in arr:
        temp+=i
        answer.append(temp)

    return answer
print(RunningSum([1,2,3,4,5]))