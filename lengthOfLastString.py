def length(s):
    i = len(s)-1
    n = 0
    while s[i]==' ':
        i-=1
    while i>=0 and s[i]!=' ':
        n+=1
        i-=1
    return n
print(length('hello AYKHAN'))