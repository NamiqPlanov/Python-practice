def prefix(word,s):
    ans = 0
    for i in word:
        if s.startswith(i):
            ans+=1
    return ans
print(prefix(["a","b","c"],'abc'))