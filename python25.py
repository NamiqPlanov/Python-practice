def shufflearray (arr,n):
    answer = []
    for i in range(n):
        answer.append(arr[i])
        answer.append(arr[i+1])

    return answer

print(shufflearray([1,2,3,4], 3))


