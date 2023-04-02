def BalancedSplit(s):
    count = result = 0
    for c in s:
        count+=1 if c=='L' else -1
        if count==0:
            result+=1
    return result
print(BalancedSplit(''))