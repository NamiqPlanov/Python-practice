def MissingNumber(arr):
    arrset = set(arr)
    n = len(arr)+1
    for number in range(n):
        if number not in arrset:
            return number
print(MissingNumber([0,1,3]))

