def prefix(words,pref):
    n = len(words)
    ans = 0
    for i in range(n):
        if words[i].startswith(pref):
            ans += 1
    return ans

print(prefix(['hello','hey hi','racecar','good boy'],'he'))