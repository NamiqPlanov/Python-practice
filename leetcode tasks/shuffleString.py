def ShuffleString(s,indices):
    list1,list2 = zip(*sorted(zip(indices,s)))
    n = len(s)
    answer = ''
    for i in range(n):
        answer += list2[i]
    return answer
print(ShuffleString('hello', [4,3,2,1,0]))