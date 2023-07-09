def dividearr(arr):
    ans = set()
    for num in arr:
        if num in ans:
            ans.remove(num)
        else:
            ans.add(num)
    return len(ans)==0
print(dividearr([1,2,1,1,2,2]))
