def permutation(arr):
    n = len(arr)
    answer = []
    for i in range(n):
        value = arr[arr[i]]
        answer.append(value)

    return answer

print(permutation([1,2,3,4]))