def repeated(arr):
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
        else:
            return i

print(repeated([1,2,3,2]))