def diStringMatch(s):
    arr =[]
    min1 = 0
    max1 = len(s)
    for i in s:
        if i=='I':
            arr.append(min1)
            min1 += 1
        else:
            arr.append(max1)
            max1 -= 1
    if s[-1]=='I':
        arr.append(min1)
    else:
        arr.append(max1)
    return arr
print(diStringMatch('IDIDDI'))