def replace(s):
    n = len(s)
    ans = ""
    for i in range(n):
        if i%2==0:
            ans+=s[i]
        else:
            offset = int(s[i])
            ans+=chr(ord(s[i-1])+offset)
    return ans
print(replace('a1b1c1'))