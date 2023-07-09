def unique_integers(n):
    ans = []
    if n%2:
        ans.append(0)
    for i in range(1,n//2+1):
        ans.append(i)
        ans.append(i+1)
    return ans
print(unique_integers(3))