def longest(s):
    res = ""
    reslen = 0
    n = len(s)
    for i in range(n):
        l,r = i,i
        while l>=0 and r<n and s[l]==s[r]:
            if (r-l+1)>reslen:
                res = s[r:l+1]
                reslen = r-l+1
            l-=1
            r+=1
        l,r = i,i+1
        while l>=0 and r<n and s[l]==s[r]:

            if (r-l+1)>reslen:
                res = s[r:l+1]
                reslen  = r-l+1
            l-=1
            r+=1
    return res

print(longest("hello"))
        