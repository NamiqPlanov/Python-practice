def function(s):
    charSet = set()
    l = 0
    ans = 0
    n = len(s)
    for i in range(n):
        while s[i] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[i])
        ans = max(ans, i-l+1)

    return ans

print(function('abcdabcde'))