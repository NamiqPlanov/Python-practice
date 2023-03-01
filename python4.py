def SumArrays(arr, numofConselem ,target):
    for i in range(len(arr)-numofConselem):
        s = arr[i]
        for j in range(i+1, i+numofConselem):
            s += arr[j]
        if s < target:
            return True
    return False

print ( SumArrays([1, 2, 3, 4, 5], 10, 3))








