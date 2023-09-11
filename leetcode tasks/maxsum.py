def maxsum(arr):
    ans = []
    arr.sort()
    while sum(arr)>sum(ans):
        ans.append(arr.pop())
    if sum(arr)==sum(ans):
        ans.append(arr.pop())
    return ans
print(maxsum([1,2,3,4]))