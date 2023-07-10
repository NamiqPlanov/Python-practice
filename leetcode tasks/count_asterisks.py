def asterisks(s):
    arr = s.split('|')[::2]
    ans = 0
    for i in arr:
        ans+=i.count('*')
    return ans
print(asterisks('helg**s*a'))